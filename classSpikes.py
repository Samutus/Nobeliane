from classTrap import Trap


class Spikes(Trap):
    def __init__(self, x, y):
        param = {  # voir dans classEntity à quoi servent les valeurs
            'sprite_image_path': 'ressources/spikes.png',
            'sprite_image_w': 32,
            'sprite_image_h': 42,
            'sprite_gravity_point': 20,
            'animation_nb_image': 4,
            'animation_num_image_stop': 1,
            'animation_tick_par_image': 20
        }
        super().__init__(x, y, param)
