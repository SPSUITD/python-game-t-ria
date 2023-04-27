import pygame
pygame.init()

win = pygame.display.set_mode((1000, 707))

pygame.display.set_caption("Angry Bunny")

walkRight = [pygame.image.load('право.png'), pygame.image.load('право1.png'), pygame.image.load('право2.png')]
walkLeft = [pygame.image.load('лево.png'), pygame.image.load('лево1.png'), pygame.image.load('лево2.png')]
#загрузка картинок для спрайта

background = pygame.image.load('фон холодный.png')
playerStand = pygame.image.load('прямо.png')

clock = pygame.time.Clock()

x = 40
y = 520
widht = 80
height = 99
speed = 5

isJump = False
jumpCount = 10

isSprint = False
SprintTime = 0

left = False
right = False
animCount = 0

def drawWindow():
    global animCount #ссылаемся на переменную
    win.blit(background, (0, 0))  # цвет окна

    if animCount + 1 >= 30:
        animCount = 0

    if left:
        win.blit(walkLeft[animCount // 10], (x, y)) #сколько кадров спрайта лево
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 10], (x, y))
        animCount += 1
    else:
        win.blit(playerStand, (x, y))



    pygame.display.update()  # обновление окна

run = True
while run:
    clock.tick(30)              #время, через которое будет выполняться цикл в милисекундах

    for event in pygame.event.get():    #получение событий из очереди
        if event.type == pygame.QUIT:
            run = False                 #окно закрывается после того, как нажимается клавиша крестик

    keys = pygame.key.get_pressed()     #помещаем кнопки
    if keys [pygame.K_LEFT] and x > 5: #чтобы объект не выходил за рамки
        x -= speed #вычитаем скорость
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 1000 - widht - 5:
        x += speed #добавляем скорость
        left = False
        right = True
    else:
        left = False
        right = False
        animCount = 0
    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:  #начинаем прыгать
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:             #опускаем игрока на землю
                y -= (jumpCount **2) / 2
            jumpCount -= 1
        else:                 #прыжок закончен
            isJump = False
            jumpCount = 10




    drawWindow()


pygame.quit() #чтобы точно закрылось