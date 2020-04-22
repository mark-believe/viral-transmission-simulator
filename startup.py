import sys
import pygame
from pygame.sprite import Group
from person import Person
from setting import Settings
from button import Button
import random

fcclock = pygame.time.Clock()


# 模拟其主函数
def run_simulator():
    # 构建配置文件对象
    settingInfo = Settings()

    # 需先初始化pygame
    pygame.init()

    # 创建主窗口
    screen = pygame.display.set_mode(
        (settingInfo.screen_width, settingInfo.screen_height))
    # 设置窗口标题
    pygame.display.set_caption("VTS")

    # 初始化模拟人员数组
    persons = Group()

    # 构建模拟人员（下面会给出函数实现）
    create_viruses(settingInfo, screen, persons)

    # 创建启动按钮（名字可自定义……）
    infect_button = Button(screen, "infect+1")

    # 该处是程序的主循环
    while True:
        # 填充背景色
        screen.fill(settingInfo.bg_color)

        # 检测消息（就是为了让我们按钮点了起作用，下面会做实现）
        check_events(settingInfo, screen, persons.sprites(), infect_button)

        # 绘制所有的模拟人员，包括被感染人员
        for person in persons.sprites():
            # 注意，该处会调用每个模拟人员的update函数，我之前自己实现的
            person.update(settingInfo, persons)

        # 绘制按钮
        infect_button.draw_button()

        # 控制刷新频率（FPS大家都懂吧…… frames per second 每秒帧数。 大多游戏都是有这个）
        fcclock.tick(settingInfo.screen_fps)

        # 调用pygame自己的update函数来刷新页面
        pygame.display.update()


# 创建模拟人员函数
def create_viruses(settingInfo, screen, persons):

    while True:

        person = Person(settingInfo, screen)
        person.draw_person()
        persons.add(person)
        if persons.__len__() >= settingInfo.person_count:
            break


# 检测消息函数
def check_events(settingInfo, screen, persons, infect_button):
    # 检查鼠标点击事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:  # 检测鼠标按下消息
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # 执行鼠标点击函数
            check_infect_button(settingInfo, persons, infect_button, mouse_x,
                                mouse_y)


# 鼠标点击事件处理
def check_infect_button(settingInfo, persons, infect_button, mouse_x, mouse_y):

    button_clicked = infect_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked:
        randomNumber = random.randint(0, len(persons) - 1)
        person = persons[randomNumber]
        person.infect(settingInfo)


# 运行主函数
run_simulator()
