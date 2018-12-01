#no_look_passpy
__author__ = 'trendousdev@gmail.com'

import pygame, random
import color

pad_width = 1000
pad_height = 561
caption = "노룩패스"
left = 0
center = 1
right = 2
score = 0

def drawObject(obj, x, y):
    global gamepad
    gamepad.blit(obj,(x, y))
    pass

def textObject(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def drawText(text, size, color, x, y, align):
    global gamepad
    textFont = pygame.font.Font('font/godoMaum.ttf', size)
    TextSurf, TextRect = textObject(text, textFont, color)
    if align == left:
        TextRect.midleft = (x, y)
        pass
    elif align == center:
        TextRect.center = (x, y)
        pass
    elif align == right:
        TextRect.midright = (x, y)
        pass
    gamepad.blit(TextSurf, TextRect)
    pass

def initGame():
    global gamepad, clock
    global background, mr, ass, car

    mr = []
    ass = []
    car = []
    
    pygame.init()

    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption(caption)

    background = pygame.image.load('image/background.png')

    mr.append(pygame.image.load('image/mr_basic.png'))
    mr.append(pygame.image.load('image/mr_left.png'))
    mr.append(pygame.image.load('image/mr_right.png'))

    ass.append(pygame.image.load('image/ass_left.png'))
    ass.append(pygame.image.load('image/ass_right.png'))
    ass.append(pygame.image.load('image/ass_car_left.png'))
    ass.append(pygame.image.load('image/ass_car_right.png'))

    car.append(pygame.image.load('image/car_left.png'))
    car.append(pygame.image.load('image/car_right.png'))

    clock = pygame.time.Clock()
    mainScreen()
    pass

def mainScreen():
    global gamepad, background

    i = 1
    msgDisp = False
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    runGame()
                    pass
                pass
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                pass
            pass
        if i % 30 == 0:
            if msgDisp:
                i = 0
                msgDisp = False
                pass
            else:
                msgDisp = True
                pass
            pass
        i += 1

        gamepad.fill(color.white)
        drawObject(background, 0, 0)
        drawText("노룩패스", 100, color.black, pad_width / 2, pad_height / 2 - 60, center)
        drawText("ⓒ Trendous Development Alliance, 2018-2019 & trendousdev@gmail.com", 30, color.black, pad_width / 2, pad_height - 30, center)
        if msgDisp:
            drawText("스페이스 키로 시작!", 50, color.black, pad_width / 2, pad_height / 2 + 100, center)
        pygame.display.update()
        clock.tick(60)
        pass
    pass

def gameOver():
    global gamepad
    pass

def runGame():
    global gamepad, clock
    global background, mr, ass, car

    ass_txy = []
    car_txy = []

    speed = 3

    mr_t_cooltime = 0
    mr_t = 0
    mr_x = pad_width / 2 - 50
    mr_y = 130
    
    count = 0
    score = 0

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    mr_t = 1
                    mr_t_cooltime = 0
                    car_txy.append([car[0], mr_x - 20, mr_y + 210])
                    pass
                elif event.key == pygame.K_d:
                    mr_t = 2
                    mr_t_cooltime = 0
                    car_txy.append([car[1], mr_x + 120, mr_y + 210])
                    pass
                pass
            if event.type == pygame.QUIT:
                crashed = True
                pass
            pass

        speed = 3 + count * 0.05

        ass_spawn = random.randrange(0, int(700/speed))

        if ass_spawn == 1:
            ass_txy.append([ass[0], -100, mr_y + 50, 0])
            pass
        elif ass_spawn == 2:
            ass_txy.append([ass[1], pad_width, mr_y + 50, 0])
            pass

        if not len(ass_txy) == 0:
            for i, a in enumerate(ass_txy):
                if a[0] == ass[0]:
                    a[1] += speed
                    ass_txy[i][1] = a[1]
                    if a[1] > pad_width:
                        try:
                            ass_txy.remove(a)
                            pass
                        except:
                            pass
                        pass
                    pass
                elif a[0] == ass[1]:
                    a[1] -= speed
                    ass_txy[i][1] = a[1]
                    if a[1] < -100:
                        try:
                            ass_txy.remove(a)
                            pass
                        except:
                            pass
                        pass
                    pass
                pass
            pass

        if not len(car_txy) == 0:
            for i, c in enumerate(car_txy):
                if c[0] == car[0]:
                    c[1] -= speed * 1.2
                    pass
                elif c[0] == car[1]:
                    c[1] += speed * 1.2
                    pass
                car_txy[i][1] = c[1]
                if c[1] < -100 or c[1] > pad_width:
                    try:
                        car_txy.remove(c)
                        pass
                    except:
                        pass
                    pass
                pass
            pass
        
        gamepad.fill(color.white)

        drawObject(background, 0, 0)

        if not len(ass_txy) == 0:
            for at, ax, ay, acooltime in ass_txy:
                drawObject(at, ax, ay)
                pass
            pass

        if not len(car_txy) == 0:
            for ct, cx, cy in car_txy:
                drawObject(ct, cx, cy)
                pass
            pass

        if mr_t_cooltime == 10:
            mr_t_cooltime = 0
            mr_t = 0
            pass
        else:
            mr_t_cooltime += 1
            pass

        if mr_t == 0:
            mr_x = pad_width / 2 - 50
            pass
        else:
            mr_x = pad_width / 2 - 80
            pass

        
        drawObject(mr[mr_t], mr_x, mr_y)
        pygame.display.update()
        clock.tick(60)
        pass

    pygame.quit()
    quit()
    pass

if __name__ == '__main__':
    initGame()
    pass
