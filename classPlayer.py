from classEntity import Entity


class Player(Entity):
    def __init__(self, x, y):
        param = {  # voir dans classEntity à quoi servent les valeurs
            'sprite_image_path': 'ressources/player.png',
            'sprite_image_w': 32,
            'sprite_image_h': 32,
            'sprite_gravity_point': 12,
            'animation_nb_image': 3,
            'animation_num_image_stop': 1,
            'animation_tick_par_image': 7
        }
        super().__init__(x, y, param)
