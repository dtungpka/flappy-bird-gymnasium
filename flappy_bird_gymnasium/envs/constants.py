class GameConstants:
    ############################ Speed and Acceleration ############################
    def __init__(self):
        self.PIPE_VEL_X = -4

        self.PLAYER_MAX_VEL_Y = 10  # max vel along Y, max descend speed
        self.PLAYER_MIN_VEL_Y = -8  # min vel along Y, max ascend speed

        self.PLAYER_ACC_Y = 1  # players downward acceleration
        self.PLAYER_VEL_ROT = 3  # angular speed

        self.PLAYER_FLAP_ACC = -9  # players speed on flapping
        ################################################################################

        ################################## Dimensions ##################################
        self.PLAYER_WIDTH = 34
        self.PLAYER_HEIGHT = 24
        self.PLAYER_PRIVATE_ZONE = (max(self.PLAYER_WIDTH, self.PLAYER_HEIGHT) + 30) / 2

        self.LIDAR_MAX_DISTANCE = int(288 * 0.8) - self.PLAYER_WIDTH

        self.PIPE_WIDTH = 52
        self.PIPE_HEIGHT = 320

        self.BASE_WIDTH = 336
        self.BASE_HEIGHT = 112

        self.BACKGROUND_WIDTH = 288
        self.BACKGROUND_HEIGHT = 512
        ################################################################################

        #: Player's rotation threshold.
        self.PLAYER_ROT_THR = 20

        #: Color to fill the surface's background when no background image was loaded.
        self.FILL_BACKGROUND_COLOR = (200, 200, 200)

    def get(self, name):
        return getattr(self, name, None)

    def set(self, name, value):
        if hasattr(self, name):
            setattr(self, name, value)

    def reset(self):
        self.__init__()
