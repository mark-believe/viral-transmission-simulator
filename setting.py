class Settings():
    # Save all game setting

    def __init__(self):
        # Init game settings

        # Screen setting
        # 屏幕宽度
        self.screen_width = 800
        # 屏幕高度
        self.screen_height = 500  #
        # 每秒刷新频率
        self.screen_fps = 20
        #背景色
        self.bg_color = (230, 230, 230)

        # virus setting
        # 模拟人员颜色
        self.person_color = (0, 250, 154)
        # 被感染人员颜色
        self.infect_person_color = (171, 37, 36)
        # 感染概率 1/50
        self.infect_rate = 50
        # 模拟人员数量
        self.person_count = 3000
        # 人员大小
        self.person_size = 4
        # 人员随机移动步长
        self.person_moving_range = 5
