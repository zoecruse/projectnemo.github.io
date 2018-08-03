import pygame
import time
import random
from math import pi
import math
from pygame.locals import *
import sys
import os

W, H = 1280, 720
HW, HH = W / 2, H / 2
AREA = W * H
x= 570
y = 110

a = 370
b = 110

c = 770
d = 110

purpleImg = pygame.image.load('purple.png')
purpleImg = pygame.transform.scale(purpleImg, (100,100))

reddyImg = pygame.image.load('reddy.png')
reddyImg = pygame.transform.scale(reddyImg, (100,100))

turtleImg = pygame.image.load('turtle.png')
turtleImg = pygame.transform.scale(turtleImg, (100,100))

sharkImg = pygame.image.load('shark.png')
sharkImg = pygame.transform.scale(sharkImg, (100,100))


pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("code.Pylet - Seamless Background Scrolling")
FPS = 500

black = (0,0,0)
white = (255,255,255)
blue = (66, 200, 244)
red = (255,0,0)
pink = (255,192,203)
block_color = (53,115,255)
block2_color = (244, 66, 206)
trash_color = (153,50,204)

puffer_width = 73
trash_width = 73
    #define some colors
BLACK=(0,0,0,255)
WHITE=(255,255,255,255)
def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
def initial_message():
    message_display('Choose your Avatar (press 1, 2 or 3)')
def initial_initialmessage():
    message_display("The StoryOnce upon a time, there lived a fish named Nemo. He and his fellow fishy friends loved to frolic in the brightly colored corals that thrived in his neighborhood. But as time passed, Nemo realized that his precious corals transformed from vibrant pinks and greens to muted greys.The warm sunlight that had once filtered down from the sky was blocked by floating pieces of debris. Yet the water continued to get warmer. Suddenly, Nemo felt unbearably hot. “What’s happening to our home?! What’s happening to our weather?!” Nemo cried to his dad. “ Trash and chemicals are being dumped into our reef, and global warming is making our waters too warm to live in,” his Dad sadly replied. …... Determined, Nemo sets out on a mission to save his home. Help him collect all the trash! Use the arrow keys (all) to move. Good luck!")
# k = pygame.key.get_pressed()
# if k[K_RIGHT]:
#     main()

def main():
    initial_message()
    purple(x,y)
    reddy(a,b)
    turtle(c,d)

def render_multi_line(text,fsize):
    lines = text.splitlines()
    largeText = pygame.font.Font('freesansbold.ttf', 30)
    for i, l in enumerate(lines):
        TextSurf, TextRect = text_objects(l, largeText)
        TextRect.center = ((W/2),(H/8+fsize*i))
        DS.blit(TextSurf, TextRect)
def main1():
    render_multi_line("The Story\nOnce upon a time, there lived a fish named Nemo.\n He and his fellow fishy friends loved to frolic in the brightly colored corals that thrived\n in his neighborhood. But as time passed, Nemo realized that his precious corals\n transformed from vibrant pinks and greens to muted greys.The warm sunlight that\n had once filtered down from the sky was blocked by floating pieces of debris. Yet the\n water continued to get warmer. Suddenly, Nemo felt unbearably hot. “What’s\n happening to our home?! What’s happening to our weather?!” Nemo cried to his dad.\n “ Trash and chemicals are being dumped into our reef,\n and global warming is making our waters too warm to live in,” his Dad sadly replied. \n... \nDetermined, Nemo sets out on a mission to save his home.\n Help him collect all the trash! Use the arrow keys (all) to move. Good luck!", 50)
    k = pygame.key.get_pressed()
    if k[K_RIGHT]:
        main()

def main2():
    message_display("weoeroiverv")
    k = pygame.key.get_pressed()
    if k[K_RIGHT]:
        main()


def purple(x,y):
    DS.blit(purpleImg,(x,y))

def reddy(x,y):
    DS.blit(reddyImg,(x,y))

def turtle(x,y):
    DS.blit(turtleImg,(x,y))

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',40)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((W/2),(H/2))
    DS.blit(TextSurf, TextRect)


    # pygame.display.update()



def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def game_loop1(pufferImg):


    def events():
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

    def puffer(x,y):
        DS.blit(pufferImg,(x,y))

    def trash(x,y):
        DS.blit(trashImg, [int(trash_startx), int(trash_starty)])

    def shark(a,b):
        DS.blit(sharkImg, [int(shark_startx), int(shark_starty)])


    def net_dodged(count):
        font = pygame.font.SysFont(None, 25)
        text = font.render("Dodged: "+str(count), True, black)
        DS.blit(text,(0,0))


    def trash_dodged(count):
        font = pygame.font.SysFont(None, 25)
        text = font.render("caught: "+str(count), True, black)
        DS.blit(text,(0,50))

    def shark_dodged(count):
        font = pygame.font.SysFont(None, 25)
        text = font.render("hit: "+str(count), True, black)
        DS.blit(text,(0,0))

    def things(thingx, thingy, thingw, thingh, color):
        pygame.draw.circle(DS, color, [int(thingx), int(thingy)], 50)

    def block2(block2x, block2y, block2w, block2h, color):
        pygame.draw.circle(DS, color, [int(block2x), int(block2y)], 50)

    def net(netx, nety, netw, neth, color):
        pygame.draw.rect(DS, color, [netx, nety, netw, neth])

    def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def message_display(text):
        DS.fill(pink)
        largeText = pygame.font.Font('freesansbold.ttf',50)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((W/2),(H/2))
        DS.blit(TextSurf, TextRect)


        pygame.display.update()


        time.sleep(1)

        game_loop1(pufferImg)

    def message_good_display(text):
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((W/2),(H/2))
        DS.blit(TextSurf, TextRect)

        pygame.display.update()

        # time.sleep(1)
    def render_multi_line(text,fsize):
        DS.fill(pink)
        lines = text.splitlines()
        largeText = pygame.font.Font('freesansbold.ttf', 30)
        for i, l in enumerate(lines):
            TextSurf, TextRect = text_objects(l, largeText)
            TextRect.center = ((W/2),(H/8+fsize*i))
            DS.blit(TextSurf, TextRect)
            pygame.display.update()

            time.sleep(3)

    def crash():
        message_display('The shark caught you too many times! Try again!')

    def boo():
        message_display('heyy')

    def ew():
        message_good_display('trash')

    def ew2():
        message_good_display('trashyyyy')
    # def lev2_mess():
    #     render_multi_line('You made it to the next level n/ now try to collect all the bottles! n/ beware, they go faster!', 50)


    def collide(x, y, r, objX, objY, objR):
        #adjustedx = x + 50
        #adjustedy = y
        h = abs(objY-y)
        w = abs(objX-x)
        dist = math.sqrt(h**2 + w**2)
        radiuses = r + objR
        if radiuses > dist:
            return True
        else:
            return False





    # define.display textSurface
    W, H = 1280, 720
    HW, HH = W / 2, H / 2
    AREA = W * H

    pink = (255,192,203)
    #setuppygame
    pygame.init()
    CLOCK = pygame.time.Clock()
    DS = pygame.display.set_mode((W, H))
    pygame.display.set_caption("code.Pylet - Seamless Background Scrolling")
    FPS = 500

    black = (0,0,0)
    white = (255,255,255)
    blue = (66, 200, 244)
    red = (255,0,0)
    pink = (255,192,203)

    block_color = (53,115,255)
    block2_color = (244, 66, 206)
    trash_color = (153,50,204)

    puffer_width = 73
    trash_width = 73
    #define some colors
    BLACK=(0,0,0,255)
    WHITE=(255,255,255,255)

    # pufferImg = pygame.image.load('reddy.png')
    # pufferImg = pygame.transform.scale(pufferImg, (100,100))

    trashImg = pygame.image.load('trash.png')
    trashImg = pygame.transform.scale(trashImg, (200,200))

    sharkImg = pygame.image.load('shark.png')
    sharkImg = pygame.transform.scale(sharkImg, (200,200))


    bg=pygame.image.load("water.png").convert()
    bg=pygame.transform.scale(bg,(1280, 720))
    bgWidth,bgHeight=bg.get_rect().size
    x=0

    stageWidth= bgWidth*3
    stagePosX=0

    startScrollingPosX = HW

    circleRadius=50


    playerPosX=circleRadius
    playerPosY=50
    playerVelocityX=0

    x_change = 0
    y_change = 0

    thing_starty = random.randrange(0 + 50, H-50)
    thing_startx = 1650
    thing_speed = -7
    thing_width = 90
    thing_height = 90

    trash_starty = random.randrange(0 + 50, H-50)
    trash_startx = 1450
    trash_speed = -7
    trash_width = 90
    trash_height = 90

    shark_starty = random.randrange(0 + 50, H-50)
    shark_startx = 1250
    shark_speed = -7
    shark_width = 90
    shark_height = 90

    block2_starty = random.randrange(0 + 50, H - 50)
    block2_startx = 1250
    block2_speed = -7
    block2_width = 90
    block2_height = 90

    thingCount = 1
    block2Count = 1
    trashCount = 1

    dodged = 0
    hit = 0
    caught = 0
    sharky = 0


    #main loop
    while True:
        events()
        x= 50
        y= 50
        a = 50
        b = 50





        k = pygame.key.get_pressed()
        if k[K_RIGHT]:
            playerVelocityX = 15
        elif k[K_LEFT]:
            playerVelocityX = -15
        else:
            playerVelocityX = 0

        playerPosX += playerVelocityX
        if playerPosX>stageWidth - circleRadius:
            playerPosX=stageWidth-circleRadius
        if playerPosX<circleRadius:
            playerPosX = circleRadius

        if playerPosX<startScrollingPosX:
            playerPosX = playerPosX
        elif playerPosX>stageWidth - startScrollingPosX:
            playerPosX= playerPosX - stageWidth + W
        else:
            playerPosX = startScrollingPosX
            stagePosX += -playerVelocityX

        if k[K_DOWN]:
            playerVelocityY = 15
        elif k[K_UP]:
            playerVelocityY = -15
        else:
            playerVelocityY = 0

        playerPosY += playerVelocityY
        if playerPosY > H - 50:
            playerPosY = H - 50
        if playerPosY < 0:
            playerPosY = 0



        rel_x=stagePosX % bgWidth
        DS.blit(bg,(rel_x - bgWidth, 0))
        if rel_x < W:
            DS.blit(bg,(rel_x,0))




        # things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        # block2(block2_startx, block2_starty, block2_width, block2_height, block2_color)
        trash(trash_startx, trash_starty)
        shark(shark_startx, shark_starty)

        # thing_startx += thing_speed
        puffer(int(playerPosX),int(playerPosY) - int(circleRadius))
        # things_dodged(dodged)

        # block2_startx += block2_speed
        # block2_dodged(hit)

        trash_startx += trash_speed
        if (playerPosX >= startScrollingPosX):
            trash_startx-= playerVelocityX
        trash_dodged(caught)

        shark_startx += shark_speed
        if (playerPosX >= startScrollingPosX):
            shark_startx-= playerVelocityX
        shark_dodged(hit)

        # if playerPosX > W - puffer_width:
        #     playerPosX = W -50
        # if playerPosX < 0:
        #     playerPosX = 0 +50
        # if playerPosY > H - puffer_width:
        #     playerPosY = H - 50
        # if playerPosY < 0:
        #     playerPosY = 0 + 50







        # adjustedx = playerPosX + 50
        # adjustedy = playerPosY
        # pygame.draw.circle(DS, red, [int(adjustedx), int(adjustedy)], 10)
        # h = abs(thing_starty-adjustedy)
        # w = abs(thing_startx-adjustedx)
        # dist = math.sqrt(h**2 + w**2)
        # radiuses = 85
        # if radiuses > dist:
        #     crash()


        # adjustedx = playerPosX + 50
        # adjustedy = playerPosY
        # pygame.draw.circle(DS, blue, [int(adjustedx), int(adjustedy)], 10)
        # h = abs(block2_starty-adjustedy)
        # w = abs(block2_startx-adjustedx)
        # dist = math.sqrt(h**2 + w**2)
        # radiuses = 85
        # if radiuses > dist:
        #     boo()

        if trash_startx + 50 < 0:
            trash_startx = W - block2_width
            trash_starty = random.randrange(0,H)
            caught += 0
            trash_speed -= 1
            trash_width += (dodged * 1.0)
        if collide(playerPosX, playerPosY, 50, trash_startx, trash_starty, 50):
            trash_startx = W - block2_width
            trash_starty = random.randrange(0,H)
            caught += 1
            trash_speed -= 1
            trash_width += (dodged * 1.0)
            # if caught >= 5:
            #     lev2_mess()


        if shark_startx + 50 < 0:
            shark_startx = W - block2_width
            shark_starty = random.randrange(0,H)
            hit += 0
            shark_speed -= 1
            shark_width += (dodged * 1.0)
        if collide(playerPosX, playerPosY, 50, shark_startx, shark_starty, 90):
            shark_startx = W - block2_width
            shark_starty = random.randrange(0,H)
            hit += 1
            shark_speed -= 1
            shark_width += (dodged * 1.0)
            if hit >= 3:
                crash()
        # adjustedx = playerPosX + 50
        # adjustedy = playerPosY
        # pygame.draw.circle(DS, pink, [int(adjustedx), int(adjustedy)], 10)
        # h = abs(trash_starty-adjustedy)
        # w = abs(trash_startx-adjustedx)
        # dist = math.sqrt(h**2 + w**2)
        # radiuses = 85
        # if radiuses > dist:
        #     ew()
        # if x > trash_startx and x < trash_startx + trash_width or x+puffer_width > trash_startx and x + radiuses < trash_startx+trash_width:
        #     print('x crossover')
        #     ew2()





        pygame.display.update()
        CLOCK.tick(FPS)
        DS.fill(BLACK)

# def game_loop(pufferImg):
#
#
#     def events():
#         for event in pygame.event.get():
#             if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
#                 pygame.quit()
#                 sys.exit()
#
#     def puffer(x,y):
#         DS.blit(pufferImg,(x,y))
#
#     def trash(x,y):
#         DS.blit(trashImg, [int(trash_startx), int(trash_starty)])
#
#
#     def net_dodged(count):
#         font = pygame.font.SysFont(None, 25)
#         text = font.render("Dodged: "+str(count), True, black)
#         DS.blit(text,(0,0))
#
#     def things_dodged(count):
#         font = pygame.font.SysFont(None, 25)
#         text = font.render("Dodged: "+str(count), True, black)
#         DS.blit(text,(0,15))
#
#     def block2_dodged(count):
#         font = pygame.font.SysFont(None, 25)
#         text = font.render("hit: "+str(count), True, black)
#         DS.blit(text,(0,0))
#
#     def trash_dodged(count):
#         font = pygame.font.SysFont(None, 25)
#         text = font.render("caught: "+str(count), True, black)
#         DS.blit(text,(0,50))
#
#     def things(thingx, thingy, thingw, thingh, color):
#         pygame.draw.circle(DS, color, [int(thingx), int(thingy)], 50)
#
#     def block2(block2x, block2y, block2w, block2h, color):
#         pygame.draw.circle(DS, color, [int(block2x), int(block2y)], 50)
#
#     def net(netx, nety, netw, neth, color):
#         pygame.draw.rect(DS, color, [netx, nety, netw, neth])
#
#     def text_objects(text, font):
#         textSurface = font.render(text, True, black)
#         return textSurface, textSurface.get_rect()
#
#     def message_display(text):
#         largeText = pygame.font.Font('freesansbold.ttf',115)
#         TextSurf, TextRect = text_objects(text, largeText)
#         TextRect.center = ((W/2),(H/2))
#         DS.blit(TextSurf, TextRect)
#
#         pygame.display.update()
#
#         time.sleep(1)
#
#         game_loop()
#
#     def message_good_display(text):
#         largeText = pygame.font.Font('freesansbold.ttf',115)
#         TextSurf, TextRect = text_objects(text, largeText)
#         TextRect.center = ((W/2),(H/2))
#         DS.blit(TextSurf, TextRect)
#
#         pygame.display.update()
#
#         # time.sleep(1)
#
#     def crash():
#         message_display('You Crashed')
#
#     def boo():
#         message_display('heyy')
#
#     def ew():
#         message_good_display('trash')
#
#     def ew2():
#         message_good_display('trashyyyy')
#
#     def collide(x, y, objX, objY):
#         adjustedx = x + 50
#         adjustedy = y
#         pygame.draw.circle(DS, pink, [int(adjustedx), int(adjustedy)], 10)
#         h = abs(objY-adjustedy)
#         w = abs(objX-adjustedx)
#         dist = math.sqrt(h**2 + w**2)
#         radiuses = 85
#         if radiuses > dist:
#             return True
#         else:
#             return False
#
#
#
#
#
#     # define.display textSurface
#     W, H = 1280, 720
#     HW, HH = W / 2, H / 2
#     AREA = W * H
#
#
#     #setuppygame
#     pygame.init()
#     CLOCK = pygame.time.Clock()
#     DS = pygame.display.set_mode((W, H))
#     pygame.display.set_caption("code.Pylet - Seamless Background Scrolling")
#     FPS = 500
#
#     black = (0,0,0)
#     white = (255,255,255)
#     blue = (66, 200, 244)
#     red = (255,0,0)
#     pink = (255,192,203)
#
#     block_color = (53,115,255)
#     block2_color = (244, 66, 206)
#     trash_color = (153,50,204)
#
#     puffer_width = 73
#     trash_width = 73
#     #define some colors
#     BLACK=(0,0,0,255)
#     WHITE=(255,255,255,255)
#
#
#     trashImg = pygame.image.load('trash.png')
#     trashImg = pygame.transform.scale(trashImg, (100,100))
#
#
#     bg=pygame.image.load("water.png").convert()
#     bg=pygame.transform.scale(bg,(1280, 720))
#     bgWidth,bgHeight=bg.get_rect().size
#     x=0
#
#     stageWidth= bgWidth*3
#     stagePosX=0
#
#     startScrollingPosX = HW
#
#     circleRadius=50
#
#
#     playerPosX=circleRadius
#     playerPosY=50
#     playerVelocityX=0
#
#     x_change = 0
#     y_change = 0
#
#     thing_starty = random.randrange(0, H)
#     thing_startx = 1650
#     thing_speed = -7
#     thing_width = 90
#     thing_height = 90
#
#     trash_starty = random.randrange(0, H)
#     trash_startx = 1450
#     trash_speed = -7
#     trash_width = 90
#     trash_height = 90
#
#     block2_starty = random.randrange(0, H)
#     block2_startx = 1250
#     block2_speed = -7
#     block2_width = 90
#     block2_height = 90
#
#     thingCount = 1
#     block2Count = 1
#     trashCount = 1
#
#     dodged = 0
#     hit = 0
#     caught = 0
#
#     #main loop
#     while True:
#         events()
#         x= 50
#         y= 50
#
#
#
#
#
#         k = pygame.key.get_pressed()
#         if k[K_RIGHT]:
#             playerVelocityX = 15
#         elif k[K_LEFT]:
#             playerVelocityX = -15
#         else:
#             playerVelocityX = 0
#
#         playerPosX += playerVelocityX
#         if playerPosX>stageWidth - circleRadius:
#             playerPosX=stageWidth-circleRadius
#         if playerPosX<circleRadius:
#             playerPosx = circleRadius
#
#
#         if playerPosX<startScrollingPosX:
#             playerPosX = playerPosX
#         elif playerPosX>stageWidth - startScrollingPosX:
#             playerPosX= playerPosX - stageWidth + W
#         else:
#             playerPosX = startScrollingPosX
#             stagePosX += -playerVelocityX
#
#         if k[K_DOWN]:
#             playerVelocityY = 15
#         elif k[K_UP]:
#             playerVelocityY = -15
#         else:
#             playerVelocityY = 0
#
#         playerPosY += playerVelocityY
#
#
#
#
#         rel_x=stagePosX % bgWidth
#         DS.blit(bg,(rel_x - bgWidth, 0))
#         if rel_x < W:
#             DS.blit(bg,(rel_x,0))
#
#
#
#
#         things(thing_startx, thing_starty, thing_width, thing_height, block_color)
#         block2(block2_startx, block2_starty, block2_width, block2_height, block2_color)
#         trash(trash_startx, trash_starty)
#
#         thing_startx += thing_speed
#         puffer(int(playerPosX),int(playerPosY) - int(circleRadius))
#         things_dodged(dodged)
#
#         block2_startx += block2_speed
#         block2_dodged(hit)
#
#         trash_startx += trash_speed
#         trash_dodged(caught)
#
#         # if x > W - puffer_width or x < 0:
#         #     crash()
#
#
#
#         if thing_startx + 50 < 0:
#             thing_startx = W - thing_width
#             thing_starty = random.randrange(0,H)
#             dodged += 1
#             thing_speed -= 1
#             thing_width += (dodged * 1.0)
#         if collide(playerPosX, playerPosY, thing_startx, thing_starty):
#             #crash()
#             hit += 1
#             thing_startx = W - thing_width
#             thing_starty = random.randrange(0,H)
#             dodged += 0
#             thing_speed -= 1
#             thing_width += (dodged * 1.0)
#
#
#         # adjustedx = playerPosX + 50
#         # adjustedy = playerPosY
#         # pygame.draw.circle(DS, red, [int(adjustedx), int(adjustedy)], 10)
#         # h = abs(thing_starty-adjustedy)
#         # w = abs(thing_startx-adjustedx)
#         # dist = math.sqrt(h**2 + w**2)
#         # radiuses = 85
#         # if radiuses > dist:
#         #     crash()
#
#         if block2_startx + 50 < 0:
#             block2_startx = W - block2_width
#             block2_starty = random.randrange(0,H)
#             hit += 0
#             block2_speed -= 1
#             block2_width += (dodged * 1.0)
#         if collide(playerPosX, playerPosY, block2_startx, block2_starty):
#             hit += 1
#             boo()
#
#         # adjustedx = playerPosX + 50
#         # adjustedy = playerPosY
#         # pygame.draw.circle(DS, blue, [int(adjustedx), int(adjustedy)], 10)
#         # h = abs(block2_starty-adjustedy)
#         # w = abs(block2_startx-adjustedx)
#         # dist = math.sqrt(h**2 + w**2)
#         # radiuses = 85
#         # if radiuses > dist:
#         #     boo()
#
#         if trash_startx + 50 < 0:
#             print(stagePosX)
#             trash_startx = W - block2_width
#             trash_starty = random.randrange(0,H)
#             caught += 0
#             trash_speed -= 1
#             trash_width += (dodged * 1.0)
#         if collide(playerPosX, playerPosY, trash_startx, trash_starty):
#             print(stagePosX)
#             trash_startx = W - block2_width
#             trash_starty = random.randrange(0,H)
#             caught += 1
#             trash_speed -= 1
#             trash_width += (dodged * 1.0)
#
#         # adjustedx = playerPosX + 50
#         # adjustedy = playerPosY
#         # pygame.draw.circle(DS, pink, [int(adjustedx), int(adjustedy)], 10)
#         # h = abs(trash_starty-adjustedy)
#         # w = abs(trash_startx-adjustedx)
#         # dist = math.sqrt(h**2 + w**2)
#         # radiuses = 85
#         # if radiuses > dist:
#         #     ew()
#         # if x > trash_startx and x < trash_startx + trash_width or x+puffer_width > trash_startx and x + radiuses < trash_startx+trash_width:
#         #     print('x crossover')
#         #     ew2()
#
#
#
#
#
#         pygame.display.update()
#         CLOCK.tick(FPS)
#         DS.fill(BLACK)
#         DS.fill(BLACK)


def menu_loop():
    W, H = 1280, 720
    HW, HH = W / 2, H / 2
    AREA = W * H
    pygame.init()
    CLOCK = pygame.time.Clock()
    DS = pygame.display.set_mode((W, H))
    pygame.display.set_caption("code.Pylet - Seamless Background Scrolling")
    FPS = 500

    black = (0,0,0)
    white = (255,255,255)
    blue = (66, 200, 244)
    red = (255,0,0)
    pink = (255,192,203)

    block_color = (53,115,255)
    block2_color = (244, 66, 206)
    trash_color = (153,50,204)

    puffer_width = 73
    trash_width = 73
    #define some colors
    BLACK=(0,0,0,255)
    WHITE=(255,255,255,255)
    PINK=(255, 182, 193)

    turtleImg = pygame.image.load('turtle.png')
    turtleImg = pygame.transform.scale(turtleImg, (100,100))

    trashImg = pygame.image.load('trash.png')
    trashImg = pygame.transform.scale(trashImg, (100,100))

    purpleImg = pygame.image.load('purple.png')
    purpleImg = pygame.transform.scale(purpleImg, (100,100))

    reddyImg = pygame.image.load('reddy.png')
    reddyImg = pygame.transform.scale(reddyImg, (100,100))

    bg=pygame.image.load("water.png").convert()
    bg=pygame.transform.scale(bg,(1280, 720))
    bgWidth,bgHeight=bg.get_rect().size
    x=0

    stageWidth= bgWidth*3
    stagePosX=0

    startScrollingPosX = HW

    circleRadius=50
    circlePosX=circleRadius

    playerPosX=circleRadius
    playerPosY=50
    playerVelocityX=0

    x_change = 0
    y_change = 0

    thing_starty = random.randrange(0, H)
    thing_startx = 1250
    thing_speed = -7
    thing_width = 90
    thing_height = 90

    trash_starty = random.randrange(0, H)
    trash_startx = 1250
    trash_speed = -7
    trash_width = 90
    trash_height = 90

    block2_starty = random.randrange(0, H)
    block2_startx = 1250
    block2_speed = -7
    block2_width = 90
    block2_height = 90

    thingCount = 1
    block2Count = 1
    trashCount = 1

    dodged = 0
    hit = 0
    caught = 0
    inMenu = True
    # k = pygame.key.get_pressed()




    while True:
        events()
        k = pygame.key.get_pressed()
        if k[K_SPACE]:
            menu_loop2()
        elif k[K_1]:
            game_loop(purpleImg)
        elif k[K_2]:
            game_loop(reddyImg)
        elif k[K_3]:
            game_loop(turtleImg)
        else:
            main1()

        pygame.display.update()
        DS.fill(PINK)
        CLOCK.tick(FPS)

def menu_loop2():
    W, H = 1280, 720
    HW, HH = W / 2, H / 2
    AREA = W * H
    pygame.init()
    CLOCK = pygame.time.Clock()
    DS = pygame.display.set_mode((W, H))
    pygame.display.set_caption("code.Pylet - Seamless Background Scrolling")
    FPS = 500

    black = (0,0,0)
    white = (255,255,255)
    blue = (66, 200, 244)
    red = (255,0,0)
    pink = (255,192,203)

    block_color = (53,115,255)
    block2_color = (244, 66, 206)
    trash_color = (153,50,204)

    puffer_width = 73
    trash_width = 73
    #define some colors
    BLACK=(0,0,0,255)
    WHITE=(255,255,255,255)
    PINK=(255, 182, 193)

    turtleImg = pygame.image.load('turtle.png')
    turtleImg = pygame.transform.scale(turtleImg, (100,100))

    trashImg = pygame.image.load('trash.png')
    trashImg = pygame.transform.scale(trashImg, (100,100))

    purpleImg = pygame.image.load('purple.png')
    purpleImg = pygame.transform.scale(purpleImg, (100,100))

    reddyImg = pygame.image.load('reddy.png')
    reddyImg = pygame.transform.scale(reddyImg, (100,100))

    bg=pygame.image.load("water.png").convert()
    bg=pygame.transform.scale(bg,(1280, 720))
    bgWidth,bgHeight=bg.get_rect().size
    x=0

    stageWidth= bgWidth*3
    stagePosX=0

    startScrollingPosX = HW

    circleRadius=50
    circlePosX=circleRadius

    playerPosX=circleRadius
    playerPosY=50
    playerVelocityX=0

    x_change = 0
    y_change = 0

    thing_starty = random.randrange(0, H)
    thing_startx = 1250
    thing_speed = -7
    thing_width = 90
    thing_height = 90

    trash_starty = random.randrange(0, H)
    trash_startx = 1250
    trash_speed = -7
    trash_width = 90
    trash_height = 90

    block2_starty = random.randrange(0, H)
    block2_startx = 1250
    block2_speed = -7
    block2_width = 90
    block2_height = 90

    thingCount = 1
    block2Count = 1
    trashCount = 1

    dodged = 0
    hit = 0
    caught = 0
    inMenu = True
    # k = pygame.key.get_pressed()




    while True:
        events()
        k = pygame.key.get_pressed()
        if k[K_SPACE]:
            game_loop1()
        elif k[K_1]:
            game_loop1(reddyImg)
        elif k[K_2]:
            game_loop1(purpleImg)
        elif k[K_3]:
            game_loop1(turtleImg)
        else:
            main()

        pygame.display.update()
        DS.fill(PINK)
        CLOCK.tick(FPS)



if __name__ == "__main__":
    menu_loop()

    pygame.quit()
    quit()
