from classMob import Mob


class BossSlime(Mob):
    def __init__(self, x, y):
        param = {  # voir dans classEntity à quoi servent les valeurs
            'sprite_image_path': 'ressources/BossSlime.png',
            'sprite_image_w': 288,
            'sprite_image_h': 160,
            'sprite_gravity_point': 80,
            'animation_nb_image': 15,
            'animation_num_image_stop': 1,
            'animation_tick_par_image': 4
        }
        super().__init__(x, y, param)
