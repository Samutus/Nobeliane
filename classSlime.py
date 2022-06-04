from classMob import Mob


class Slime(Mob):
    def __init__(self, x, y):
        param = {  # voir dans classEntity à quoi servent les valeurs
            'sprite_image_path': 'ressources/slime.png',
            'sprite_image_w': 16,
            'sprite_image_h': 16,
            'sprite_gravity_point': 8,
            'animation_nb_image': 9,
            'animation_num_image_stop': 1,
            'animation_tick_par_image': 7
        }
        super().__init__(x, y, param)
