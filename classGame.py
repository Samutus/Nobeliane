import pygame
import pytmx
import pyscroll

from classPlayer import Player
from classNpcStats import NpcStats
from classSlime import Slime
from classBossSlime import BossSlime
from classFountain import Fountain
from classSpikes import Spikes

pygame.font.init()
# On charge toutes les images
coin = pygame.image.load('./ressources/coin.png', "pièces")
heal = pygame.image.load('./ressources/heal.png', "heal")
sword = pygame.image.load('./ressources/sword.png', "dps")
shield = pygame.image.load('./ressources/shield.png', "shield")
font = pygame.font.Font('./ressources/joystix.ttf', 15)
parchment = pygame.image.load('./ressources/parcho.png', "parchemin ui")
bar = pygame.image.load('./ressources/new_ui.png', "barre ui en haut à gauche")
barre_pv = pygame.image.load('./ressources/barre_vie.png', "barre de vie")
font_niveau = pygame.font.Font('./ressources/DIABLO_H.TTF', 30)
stats = pygame.image.load('./ressources/stats.png', "stats")
cursor = pygame.image.load('./ressources/curseur.png', "cursor")


class Game:
    def __init__(self):
        # fenetre du jeu
        self.screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
        pygame.display.set_caption("Nobeliane")
        program_icon = pygame.image.load('./ressources/rpg.png')
        pygame.display.set_icon(program_icon)

        self.current_map_name = None
        self.current_map_walls = []
        self.current_map_traps = []
        self.current_map_traps_name = []
        self.current_map_group = None
        self.current_map_tmx_data = None
        self.current_map_exits = []

        # initialise le player
        self.player = Player(200, 200)
        self.slime = Slime(200, 200)

        self.boss_slime = BossSlime(250, 20)

        self.fountain = Fountain(740, 325)
        self.fountain2 = Fountain(120, 10)
        self.fountain3 = Fountain(490, 10)

        self.spikes = Spikes(368, 250)
        self.spikes2 = Spikes(402, 250)

        # demarre la 1ère map
        self.create_new_map('cartePlaine', 'player')

        # initialisation des stats du joueur /!\ Aucune stat ne doit dépasser 999 pour l'affichage/!\
        # init de NpcStats : (self, pv, pv_max, po, dps, defense,exp(100 maximum),niveau)
        self.stats_player = NpcStats(800, 800, 123, 500, 800, 100, 20)

    def create_new_map(self, file_map, first_player_spawn):
        self.current_map_name = file_map

        # charger la carte (tmx)
        self.current_map_tmx_data = pytmx.util_pygame.load_pygame('map/' + file_map + '.tmx')
        map_data = pyscroll.data.TiledMapData(self.current_map_tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 3

        for obj in self.current_map_tmx_data.objects:
            if obj.type == "collision":
                self.current_map_walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            if obj.type == "trap":
                self.current_map_traps.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
                self.current_map_traps_name.append(obj.name)

        # dessiner le groupe de calques
        self.current_map_group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=2)
        self.current_map_group.add(self.player)

        # recuperer le point de spawn dans cette nouvelle map
        spawn_point = self.current_map_tmx_data.get_object_by_name(first_player_spawn)
        self.player.position[0] = spawn_point.x
        self.player.position[1] = spawn_point.y - 20

        # definir les rectangles de collision pour sortir (entrer dans la map suivante)
        self.current_map_exits = []

        if self.current_map_name == "cartePlaine":
            self.current_map_exits = [
                "maison1",
                "maison2",
                "carteDonjon"
            ]
            # dessiner le groupe de calques avec les entity
            entity_tab = [self.slime]
            for entity_name in entity_tab:
                self.current_map_group.add(entity_name)

        elif self.current_map_name == "maison1":
            self.current_map_exits = [
                "cartePlaine"
            ]
        elif self.current_map_name == "maison2":
            self.current_map_exits = [
                "cartePlaine"
            ]
        elif self.current_map_name == "carteDonjon":
            self.current_map_exits = [
                "cartePlaine"
            ]

            # dessiner les entitées sur le groupe de calque
            entity_tab = [self.boss_slime, self.fountain, self.fountain2, self.fountain3, self.spikes, self.spikes2]
            for entity_name in entity_tab:
                self.current_map_group.add(entity_name)

    def handle_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation("up")
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation("down")
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation("right")
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation("left")
        else:
            self.player.move_stop()

    def update(self):  # pour changer d'un monde à un autre
        self.current_map_group.update()

        # détecte si le joueur entre un collision un point de sortie, si oui on envoie le joueur sur cette map
        for new_map_name in self.current_map_exits:
            exit_rect = self.current_map_tmx_data.get_object_by_name(self.current_map_name + "_exit_" + new_map_name)
            collision_exit_rect = pygame.Rect(exit_rect.x, exit_rect.y, exit_rect.width, exit_rect.height)
            if self.player.feet.colliderect(collision_exit_rect):
                self.create_new_map(new_map_name, new_map_name + "_spawn_" + self.current_map_name)
                return None

        # verification collision avec les murs et avec les pièges
        for sprite in self.current_map_group.sprites():
            if sprite.feet.collidelist(self.current_map_walls) > -1:
                sprite.move_back()
        for obj in self.current_map_tmx_data.objects:
            if self.player.feet.collidelist(self.current_map_traps) > -1:
                if obj.name == 'spike1':
                    self.stats_player.setPv(-1)

        # actualiser l'animation des entités
        self.player.update_animation()
        entity_tab = [self.slime, self.boss_slime, self.fountain, self.fountain2, self.fountain3, self.spikes,
                      self.spikes2]
        for entity_name in entity_tab:
            entity_name.update_animation()
            entity_name.move()

    # Interface graphique
    def interface(self):
        pressed = pygame.key.get_pressed()

        color_vie = (255, 0, 0)
        x = self.screen.get_size()[0] - 20
        y = self.screen.get_size()[1] - 20

        barre_de_vie_largeur = (NpcStats.get_pv(self.stats_player) * 104 / NpcStats.get_pv_max(self.stats_player))
        color_xp = (0, 255, 0)
        exp_par_niveau = NpcStats.get_niveau(self.stats_player) * 100
        barre_d_xp_largeur = NpcStats.get_exp(self.stats_player) * 104 / exp_par_niveau
        color_text = (0, 0, 0)

        # variables pour le placement des stats
        e = 150
        a = 10

        # texte stats vie joueur
        text_hp = font.render(f"Pv = {NpcStats.get_pv(self.stats_player)}", False, color_text)
        text_place_hp = text_hp.get_rect(bottomright=(x - (50 + a), y - (70 + e)))

        # texte stats max vie joueur
        text_hp_max = font.render(f"Pv max = {NpcStats.get_pv_max(self.stats_player)}", False, color_text)
        text_place_hp_max = text_hp.get_rect(bottomright=(x - (98 + a), y - (45 + e)))

        # texte attaque
        text_dps = font.render(f"Dps = {NpcStats.get_dps(self.stats_player)}", False, color_text)
        text_place_dps = text_dps.get_rect(bottomright=(x - (50 + a), y - (20 + e)))

        # texte PO joueur
        text_po = font.render(f"Po = {NpcStats.get_po(self.stats_player)}", False, color_text)
        text_place = text_po.get_rect(bottomright=(x - (50 + a), y - e))

        # texte defense
        text_shield = font.render(f"shield = {NpcStats.get_defense(self.stats_player)}", False, color_text)
        text_place_shield = text_shield.get_rect(bottomright=(x - (50 + a), y - (e - 20)))

        # texte exp
        text_exp = font.render(f"exp = {NpcStats.get_exp(self.stats_player)}", False, color_text)
        text_place_exp = text_shield.get_rect(bottomright=(x - (14 + a), y - (e - 40)))

        # texte niveau
        text_niveau_s = font.render(f"niveau = {NpcStats.get_niveau(self.stats_player)}", False, color_text)
        text_place_niveau_s = text_niveau_s.get_rect(bottomright=(x - (62 + a), y - (e - 60)))

        size_stats = pygame.transform.scale(stats, (100, 100))

        # curseur personnalisé
        pygame.mouse.set_visible(False)
        cursor_img_rect = cursor.get_rect()

        # parchemin
        parchment_place = text_shield.get_rect(bottomright=(x - 140, y - 270))
        size_parchment = pygame.transform.scale(parchment, (300, 300))

        # barre de vie
        pygame.draw.rect(self.screen, color_vie, pygame.Rect(74, 6, barre_de_vie_largeur, 14), 0, 0)
        pygame.draw.rect(self.screen, color_xp, pygame.Rect(74, 28, barre_d_xp_largeur, 14), 0, 0)

        bar_img_rect = bar.get_rect()
        size_bar = pygame.transform.scale(bar, (103 + 103, 34 + 34))
        self.screen.blit(size_bar, bar_img_rect)

        color_niv = (218, 212, 94)

        if NpcStats.get_niveau(self.stats_player) < 10:
            x1 = 24
        else:
            x1 = 16
        # Affichage du niveau
        text_niveau = font_niveau.render(f"{NpcStats.get_niveau(self.stats_player)}", False, color_niv)
        text_niveau_exp = text_niveau.get_rect(topleft=(x1, 16))
        self.screen.blit(text_niveau, text_niveau_exp)

        if pressed[pygame.K_e]:
            self.screen.blit(size_parchment, parchment_place)

            self.screen.blit(text_po, text_place)

            self.screen.blit(text_hp, text_place_hp)

            self.screen.blit(text_hp_max, text_place_hp_max)

            self.screen.blit(text_po, text_place)

            self.screen.blit(text_dps, text_place_dps)

            self.screen.blit(text_shield, text_place_shield)

            self.screen.blit(text_exp, text_place_exp)

            self.screen.blit(text_niveau_s, text_place_niveau_s)
        else:
            self.screen.blit(size_stats, (x - 80, y - 80))
        cursor_img_rect.center = pygame.mouse.get_pos()
        self.screen.blit(cursor, cursor_img_rect)

    def run(self):
        clock = pygame.time.Clock()
        # boucle du jeu
        running = True
        while running:
            self.player.save_location()
            self.handle_input()
            self.update()
            self.current_map_group.center(self.player.rect.center)
            self.current_map_group.draw(self.screen)
            self.interface()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)
        pygame.quit()
