from classMob import Mob


class Fountain(Mob):
    def __init__(self, x, y):
        param = {  # voir dans classEntity à quoi servent les valeurs
            'sprite_image_path': 'ressources/blood-fountain.png',
            'sprite_image_w': 32,
            'sprite_image_h': 96,
            'sprite_gravity_point': 50,
            'animation_nb_image': 4,
            'animation_num_image_stop': 1,
            'animation_tick_par_image': 10
        }
        super().__init__(x, y, param)
