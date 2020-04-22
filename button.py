import pygame.font


class Button():
    # 传入两个参数，一个是主窗口，一个是按钮显示内容
    def __init__(self, screen, msg):
        # 按钮初始化
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮属性
        self.width, self.height = 100, 30
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # 创建一个按钮，并设置位置为左上角
        self.rect = pygame.Rect(15, 5, self.width, self.height)

        # 添加一个消息
        self.prep_msg(msg)

    # 渲染按钮显示的图片
    def prep_msg(self, msg):
        #
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    # 绘制按钮的图片
    def draw_button(self):
        # 先填充按钮颜色，再绘制按钮名称
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
