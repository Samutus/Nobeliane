import math
import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, param):
        super().__init__()
        self.current_image = 0
        self.current_direction = 'down'

        self.sprite_sheet = pygame.image.load(param['sprite_image_path'])
        self.sprite_image_w = param['sprite_image_w']  # largeur de chaque image
        self.sprite_image_h = param['sprite_image_h']  # hauteur
        self.sprite_gravity_point = param['sprite_gravity_point']  # milieu du personnage (gestion de collision)

        self.animation_nb_image = param['animation_nb_image']  # le nombre d'images du sprite
        self.animation_num_image_stop = param[
            'animation_num_image_stop']  # Le num de l'image qu'on affiche quand on est à l'arrêt
        self.animation_tick_par_image = param['animation_tick_par_image']  # influe sur la vitesse d'animation

        # position du joueur
        self.position = [x, y]
        self.old_position = self.position.copy()

        self.speed = 10  # vitesse du joueur

        self.images = {}
        self.__init_sprite_images()

        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, self.sprite_gravity_point)
        self.move_stop()  # remet l'entité à son affichage immobile

    # fait tourner l'animation en boucle dans la direction de l'entité (la ligne de son sprite)
    def __init_sprite_images(self):
        sprite_directions = {'up': 3, 'left': 1, 'right': 2, 'down': 0}
        for direction, num_line in sprite_directions.items():
            for num_col in range(0, self.animation_nb_image):
                self.images[direction + str(num_col)] = self.get_image(num_col * self.sprite_image_w,
                                                                       num_line * self.sprite_image_h)

    def save_location(self):
        self.old_position = self.position.copy()

    def update_animation(self):
        self.image = self.images[
            self.current_direction + str(math.floor(self.current_image / self.animation_tick_par_image))]
        self.image.set_colorkey((0, 0, 0))

    def change_animation(self, name):
        self.current_direction = name

    def move(self):
        self.current_image += 1
        if self.current_image >= self.animation_nb_image * self.animation_tick_par_image:
            self.current_image = 0

    # mouvements du personnage
    def move_right(self):
        self.position[0] += self.speed  # right selon self.position x
        self.move()

    def move_left(self):
        self.position[0] -= self.speed
        self.move()

    def move_up(self):
        self.position[1] -= self.speed  # right selon self.position y
        self.move()

    def move_down(self):
        self.position[1] += self.speed
        self.move()

    def move_stop(self):
        self.current_image = self.animation_num_image_stop * self.animation_tick_par_image

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom
        self.move()

    def get_image(self, x, y):
        image = pygame.Surface([self.sprite_image_w, self.sprite_image_h])
        image.blit(self.sprite_sheet, (0, 0), (x, y, self.sprite_image_w, self.sprite_image_h))
        return image
