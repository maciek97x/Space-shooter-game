import pygame, sys, random, time
from pygame.locals import *

from graphics import *

from files import *

from stages import *

from enemy_types import *

from stages import *

Data = getData()

pygame.init()
mainClock = pygame.time.Clock()

windowSurface = pygame.display.set_mode((WindowWidth, WindowHeight), 0, 32)
pygame.display.set_caption('SpaceShip v2')

def terminate():
    pygame.quit()
    sys.exit()

def drawText(text, size, color, surface, x, y):
    font = pygame.font.SysFont(None, size)
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def collision(rect1, rect2):
    if rect1.left < rect2.right and rect1.right > rect2.left and rect1.top < rect2.bottom and rect1.bottom > rect2.top:
        return True
    else:
        return False
    
Opening = pygame.Surface((WindowWidth, WindowHeight))
Opening.fill((0,0,0))
while True:
    Skip = False
    for x in range(102):
        if Skip:
            break
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_s:
                    Skip = True
        Opening.set_alpha(255-x*2.5)
        drawText("SpaceShip v2", 120, Colors["LBlue"], windowSurface, 70, 200)
        windowSurface.blit(Opening, pygame.Rect(0,0,WindowWidth,WindowHeight))
        pygame.display.update()
        mainClock.tick(100)
    mainClock.tick(10000)
    for x in range(51):
        if Skip:
            break
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_s:
                    Skip = True
        Opening.set_alpha(x*5)
        drawText("SpaceShip v2", 120, Colors["LBlue"], windowSurface, 70, 200)
        windowSurface.blit(Opening, pygame.Rect(0,0,WindowWidth,WindowHeight))
        pygame.display.update()
        mainClock.tick(100)
    
    for x in range(51):
        if Skip:
            break
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_s:
                    Skip = True
        Opening.set_alpha(255 - x*5)
        windowSurface.blit(MenuBkg, pygame.Rect(0,0,WindowWidth,WindowHeight))
        drawText("Start Game", 70, Colors["LBlue"], windowSurface, 100, 100)
        drawText("Ranking", 50, Colors["LBlue"], windowSurface, 120, 200)
        drawText("Quit", 50, Colors["LBlue"], windowSurface, 120, 300)
        windowSurface.blit(Opening, pygame.Rect(0,0,WindowWidth,WindowHeight))
        pygame.display.update()
        mainClock.tick(200)
    
    Start = False
    Option = 0
    Selected = False
    while not Start:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    Option += 1
                if event.key == K_UP:
                    Option -= 1
                if event.key == K_SPACE:
                    Selected = True
        if Option > 2 or Option < 0:
            Option = Option % 3
        windowSurface.blit(MenuBkg, pygame.Rect(0,0,WindowWidth,WindowHeight))
        if Option == 0:
            drawText("Start Game", 70, Colors["LBlue"], windowSurface, 100, 100)
        else:
            drawText("Start Game", 50, Colors["LBlue"], windowSurface, 120, 100)
        if Option == 1:
            drawText("Ranking", 70, Colors["LBlue"], windowSurface, 100, 200)
        else:
            drawText("Ranking", 50, Colors["LBlue"], windowSurface, 120, 200)
        if Option == 2:
            drawText("Quit", 70, Colors["LBlue"], windowSurface, 100, 300)
        else:
            drawText("Quit", 50, Colors["LBlue"], windowSurface, 120, 300)
        pygame.display.update()
        
        if Selected:
            if Option == 0:
                Start = True
                
            if Option == 1:
                for x in range(51):
                    Opening.set_alpha(x*5)
                    windowSurface.blit(MenuBkg, pygame.Rect(0,0,WindowWidth,WindowHeight))
                    drawText("Start Game", 50, Colors["LBlue"], windowSurface, 120, 100)
                    drawText("Ranking", 70, Colors["LBlue"], windowSurface, 100, 200)
                    drawText("Quit", 50, Colors["LBlue"], windowSurface, 120, 300)
                    windowSurface.blit(Opening, pygame.Rect(0,0,WindowWidth,WindowHeight))
                    pygame.display.update()
                    mainClock.tick(200)
                
                for x in range(51):
                    Opening.set_alpha(255 - x*5)
                    windowSurface.blit(MenuBkg, pygame.Rect(0,0,WindowWidth,WindowHeight))
                    drawText("Ranking", 70, Colors["LBlue"], windowSurface, 100, 60)
                    drawText("Name", 40, Colors["LBlue"], windowSurface, 100, 140)
                    drawText("Score", 40, Colors["LBlue"], windowSurface, 400, 140)
                    drawText("Press esc to  back to menu", 40, Colors["LBlue"], windowSurface, 100, 400)
                    for x in range(min(len(Data) - 1, 5)):
                        drawText(str(x+1) + ". " + Data[x].split()[0], 40, Colors["White"], windowSurface, 100, 180 + 40*x)
                        drawText(Data[x].split()[1], 40, Colors["White"], windowSurface, 400, 180 + 40*x)
                    windowSurface.blit(Opening, pygame.Rect(0,0,WindowWidth,WindowHeight))
                    pygame.display.update()
                    mainClock.tick(200)
                Selected = False
                ExitRank = False
                while not ExitRank:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            terminate()
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                ExitRank = True
                    windowSurface.blit(MenuBkg, pygame.Rect(0,0,WindowWidth,WindowHeight))
                    drawText("Ranking", 70, Colors["LBlue"], windowSurface, 100, 60)
                    drawText("Name", 40, Colors["LBlue"], windowSurface, 100, 140)
                    drawText("Score", 40, Colors["LBlue"], windowSurface, 400, 140)
                    drawText("Press esc to  back to menu", 40, Colors["LBlue"], windowSurface, 100, 400)
                    for x in range(min(len(Data) - 1, 5)):
                        drawText(str(x+1) + ". " + Data[x].split()[0], 40, Colors["White"], windowSurface, 100, 180 + 40*x)
                        drawText(Data[x].split()[1], 40, Colors["White"], windowSurface, 400, 180 + 40*x)
                    pygame.display.update()
                
                for x in range(51):
                    Opening.set_alpha(x*5)
                    windowSurface.blit(MenuBkg, pygame.Rect(0,0,WindowWidth,WindowHeight))
                    drawText("Ranking", 70, Colors["LBlue"], windowSurface, 100, 60)
                    drawText("Name", 40, Colors["LBlue"], windowSurface, 100, 140)
                    drawText("Score", 40, Colors["LBlue"], windowSurface, 400, 140)
                    drawText("Press esc to  back to menu", 40, Colors["LBlue"], windowSurface, 100, 400)
                    for x in range(min(len(Data) - 1, 5)):
                        drawText(str(x+1) + ". " + Data[x].split()[0], 40, Colors["White"], windowSurface, 100, 180 + 40*x)
                        drawText(Data[x].split()[1], 40, Colors["White"], windowSurface, 400, 180 + 40*x)
                    windowSurface.blit(Opening, pygame.Rect(0,0,WindowWidth,WindowHeight))
                    pygame.display.update()
                    mainClock.tick(200)
                
                for x in range(51):
                    Opening.set_alpha(255 - x*5)
                    windowSurface.blit(MenuBkg, pygame.Rect(0,0,WindowWidth,WindowHeight))
                    drawText("Start Game", 50, Colors["LBlue"], windowSurface, 120, 100)
                    drawText("Ranking", 70, Colors["LBlue"], windowSurface, 100, 200)
                    drawText("Quit", 50, Colors["LBlue"], windowSurface, 120, 300)
                    windowSurface.blit(Opening, pygame.Rect(0,0,WindowWidth,WindowHeight))
                    pygame.display.update()
                    mainClock.tick(200)
                
            if Option == 2:
                for x in range(51):
                    Opening.set_alpha(x*5)
                    windowSurface.blit(MenuBkg, pygame.Rect(0,0,WindowWidth,WindowHeight))
                    drawText("Start Game", 50, Colors["LBlue"], windowSurface, 120, 100)
                    drawText("Ranking", 50, Colors["LBlue"], windowSurface, 120, 200)
                    drawText("Quit", 70, Colors["LBlue"], windowSurface, 100, 300)
                    windowSurface.blit(Opening, pygame.Rect(0,0,WindowWidth,WindowHeight))
                    pygame.display.update()
                    mainClock.tick(200)
                
                terminate()
        # Start animation
    start_x, start_y, start_z = 0, 0, 0
    Skip = False
    while start_z < 85:
        if Skip:
            break
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_s:
                    Skip = True
        windowSurface.blit(MenuBkg, pygame.Rect(0,0,WindowWidth,WindowHeight))
        Opening.set_alpha(2*start_x)
        windowSurface.blit(Opening, pygame.Rect(0,0,WindowWidth,WindowHeight))
        drawText("Start Game", 70, (50,150,200), windowSurface, 100 - start_z ** 2, 100)
        drawText("Ranking", 50, (50,150,200), windowSurface, 120 - start_y ** 2, 200)
        drawText("Quit", 50, (50,150,200), windowSurface, 120 - start_x ** 2, 300)
        pygame.display.update()
        mainClock.tick(100)
        start_x += 1
        if start_x > 20:
            start_y += 1
        if start_y > 20:
            start_z += 1
        # Ship selection
    Start = False
    SelectedShip = 0
    SelectedMove = 0
    Selected = False
    Stars1 = [[random.randint(-600,1300), random.randint(-500,1000), StarColors[random.randint(0,len(StarColors)-1)] ] for x in range(9000)]
    
    for x in range(51):
        if Skip:
            break
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_s:
                    Skip = True
        SelBkg = pygame.transform.scale(SelectionBackgroundIMG, (WindowWidth + 4, WindowHeight + 4))
        windowSurface.blit(SelBkg, pygame.Rect(-2, -2, WindowWidth + 4, WindowHeight + 4))
        
        for star in Stars1:
            pygame.draw.circle(windowSurface, star[2], (int(350 + (star[0] - 350)/(100 ** 0.2)), int(250 + (star[1] - 350)/(100 ** 0.2))) , 0)
        drawText("Select ship", 70, Colors["LBlue"], windowSurface, 200, 200)
        Opening.set_alpha(255 - 5*x)
        windowSurface.blit(Opening, pygame.Rect(0,0,WindowWidth,WindowHeight))
        pygame.display.update()
        mainClock.tick(200)
        
    for x in range(51):
        if Skip:
            break
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_s:
                    Skip = True
        SelBkg = pygame.transform.scale(SelectionBackgroundIMG, (WindowWidth + 4, WindowHeight + 4))
        windowSurface.blit(SelBkg, pygame.Rect(-2, -2, WindowWidth + 4, WindowHeight + 4))
        
        for star in Stars1:
            pygame.draw.circle(windowSurface, star[2], (int(350 + (star[0] - 350)/(100 ** 0.2)), int(250 + (star[1] - 350)/(100 ** 0.2))) , 0)
        drawText("Select ship", 70, Colors["LBlue"], windowSurface, 200, 200)
        pygame.display.update()
        mainClock.tick(200)
        
    ShipName = Ships[SelectedShip]["Name"]
    ShipSpeed = Ships[SelectedShip]["Speed"]
    ShipDmg = Ships[SelectedShip]["Damage"]
    ShipHP = Ships[SelectedShip]["Health"]
    ShipSD = Ships[SelectedShip]["Shields"]
    ShipIMG = Ships[SelectedShip]["Image"][0]
    ShipSize = Ships[SelectedShip]["Size"]
    ShipRect = pygame.Rect(WindowWidth/2 - ShipSize[0]/2, WindowHeight/2 - ShipSize[1]/2, ShipSize[0], ShipSize[1])
    
    for x in range(1,100):
        if Skip:
            break
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_s:
                    Skip = True
        y = 100 -x
        SelBkg = pygame.transform.scale(SelectionBackgroundIMG, (WindowWidth + 400/y, WindowHeight + 400/y))
        windowSurface.blit(SelBkg, pygame.Rect(-200/y, -200/y, WindowWidth + 400/y, WindowHeight + 400/y))
        
        for star in Stars1:
            pygame.draw.circle(windowSurface, star[2], (int(350 + (star[0] - 350)/(y ** 0.2)), int(250 + (star[1] - 350)/(y ** 0.2))) , 0)
        if x < 10:
            drawText("Select ship", 70, (50/x,150/x,200/x), windowSurface, 200, 200)    
        if y < 20:
            ShipRect = pygame.Rect(WindowWidth/2 - ShipSize[0]/(2*y), WindowHeight/2 - ShipSize[1]/(2*y), ShipSize[0]/y, ShipSize[1]/y)
            ShipIMG = pygame.transform.scale(ShipIMG, (ShipSize[0]/y, ShipSize[1]/y))
            windowSurface.blit(ShipIMG, ShipRect)
            drawText(ShipName, 30/y, Colors["LBlue"], windowSurface, 350 - 280/y, 250 + 100/y)
            drawText("Speed  ", 20/y, Colors["LBlue"], windowSurface, 350 - 290/y, 250 + 150/y)
            for x in range(Ships[SelectedShip]["Speed"]):
                pygame.draw.rect(windowSurface, Colors["White"], pygame.Rect(350 - 300/y + 10*x/y, 250 + 170/y, 10/y, 6/y))
            drawText("Reload ", 20/y, Colors["LBlue"], windowSurface, 350 - 170/y, 250 + 150/y)
            for x in range(Ships[SelectedShip]["Reload"]/5):
                pygame.draw.rect(windowSurface, Colors["Orange"], pygame.Rect(350 - 180/y + 10*x/y, 250 + 170/y, 10/y, 6/y))
            drawText("Damage ", 20/y, Colors["LBlue"], windowSurface, 350 - 50/y, 250 + 150/y)
            for x in range(Ships[SelectedShip]["Damage"]):
                pygame.draw.rect(windowSurface, Colors["Red"], pygame.Rect(350 - 60/y + 10*x/y, 250 + 170/y, 10/y, 6/y))
            drawText("Health ", 20/y, Colors["LBlue"], windowSurface, 350 + 70/y, 250 + 150/y)
            for x in range(Ships[SelectedShip]["Health"]):
                pygame.draw.rect(windowSurface, Colors["Green"], pygame.Rect(350 + 60/y + 10*x/y, 250 + 170/y, 10/y, 6/y))
            drawText("Shields", 20/y, Colors["LBlue"], windowSurface, 350 + 190/y, 250 + 150/y)
            for x in range(Ships[SelectedShip]["Shields"]):
                pygame.draw.rect(windowSurface, Colors["Blue"], pygame.Rect(350 + 180/y + 10*x/y, 250 + 170/y, 10/y, 6/y))
        
        pygame.display.update()
        mainClock.tick(30)
    
    while not Start:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    SelectedMove = -1
                if event.key == K_RIGHT:
                    SelectedMove = 1
                if event.key == K_SPACE:
                    Start = True
                                                                    #Statystyki Statku
        ShipName = Ships[SelectedShip]["Name"]
        ShipSpeed = Ships[SelectedShip]["Speed"]
        ShipDmg = Ships[SelectedShip]["Damage"]
        ShipReload = Ships[SelectedShip]["Reload"]
        ShipHP = Ships[SelectedShip]["Health"]
        ShipSD = Ships[SelectedShip]["Shields"]
        ShipIMG = Ships[SelectedShip]["Image"][0]
        ShipSize = Ships[SelectedShip]["Size"]
        ShipRect = pygame.Rect(WindowWidth/2 - ShipSize[0]/2, WindowHeight/2 - ShipSize[1]/2, ShipSize[0], ShipSize[1])
        
        
        if SelectedMove == -1 and SelectedShip > 0:
            for x in range(25):
                ShipRect = pygame.Rect(WindowWidth/2 - ShipSize[0]/2 + x*16, WindowHeight/2 - ShipSize[1]/2, ShipSize[0], ShipSize[1])
                windowSurface.blit(ShipIMG, ShipRect)
                
                SelBkg = pygame.transform.scale(SelectionBackgroundIMG, (WindowWidth + 400, WindowHeight + 400))
                windowSurface.blit(SelBkg, pygame.Rect(-200, -200, WindowWidth + 400, WindowHeight + 400))
                
                for star in Stars1:
                    pygame.draw.circle(windowSurface, star[2], (star[0],star[1]), 0)
                
                windowSurface.blit(ShipIMG, ShipRect)
                
                mainClock.tick(60)
                pygame.display.update()
            SelectedShip -= 1
            ShipIMG = Ships[SelectedShip]["Image"][0]
            ShipSize = Ships[SelectedShip]["Size"]
            for x in range(25):
                ShipRect = pygame.Rect(WindowWidth/2 - ShipSize[0]/2 - 400 + x*16, WindowHeight/2 - ShipSize[1]/2, ShipSize[0], ShipSize[1])
                windowSurface.blit(ShipIMG, ShipRect)
                
                SelBkg = pygame.transform.scale(SelectionBackgroundIMG, (WindowWidth + 400, WindowHeight + 400))
                windowSurface.blit(SelBkg, pygame.Rect(-200, -200, WindowWidth + 400, WindowHeight + 400))
                
                for star in Stars1:
                    pygame.draw.circle(windowSurface, star[2], (star[0],star[1]), 0)
                
                windowSurface.blit(ShipIMG, ShipRect)
                
                mainClock.tick(60)
                pygame.display.update()
            SelectedMove = 0
        if SelectedMove == 1 and SelectedShip < len(Ships) -1:
            for x in range(25):
                ShipRect = pygame.Rect(WindowWidth/2 - ShipSize[0]/2 - x*16, WindowHeight/2 - ShipSize[1]/2, ShipSize[0], ShipSize[1])
                windowSurface.blit(ShipIMG, ShipRect)
                
                SelBkg = pygame.transform.scale(SelectionBackgroundIMG, (WindowWidth + 400, WindowHeight + 400))
                windowSurface.blit(SelBkg, pygame.Rect(-200, -200, WindowWidth + 400, WindowHeight + 400))
                
                for star in Stars1:
                    pygame.draw.circle(windowSurface, star[2], (star[0],star[1]), 0)
                
                windowSurface.blit(ShipIMG, ShipRect)
                
                mainClock.tick(60)
                pygame.display.update()
            SelectedShip += 1
            ShipIMG = Ships[SelectedShip]["Image"][0]
            ShipSize = Ships[SelectedShip]["Size"]
            for x in range(25):
                ShipRect = pygame.Rect(WindowWidth/2 - ShipSize[0]/2 + 400 - x*16, WindowHeight/2 - ShipSize[1]/2, ShipSize[0], ShipSize[1])
                windowSurface.blit(ShipIMG, ShipRect)
                
                SelBkg = pygame.transform.scale(SelectionBackgroundIMG, (WindowWidth + 400, WindowHeight + 400))
                windowSurface.blit(SelBkg, pygame.Rect(-200, -200, WindowWidth + 400, WindowHeight + 400))
                
                for star in Stars1:
                    pygame.draw.circle(windowSurface, star[2], (star[0],star[1]), 0)
                
                windowSurface.blit(ShipIMG, ShipRect)
                
                mainClock.tick(60)
                pygame.display.update()
            SelectedMove = 0

            
        SelBkg = pygame.transform.scale(SelectionBackgroundIMG, (WindowWidth + 400, WindowHeight + 400))
        windowSurface.blit(SelBkg, pygame.Rect(-200, -200, WindowWidth + 400, WindowHeight + 400))

        for star in Stars1:
            pygame.draw.circle(windowSurface, star[2], (star[0],star[1]), 0)
        
        windowSurface.blit(ShipIMG, ShipRect)
        
        drawText(ShipName, 30, Colors["LBlue"], windowSurface, 70, 350)
        drawText("Speed  ", 20, Colors["LBlue"], windowSurface, 60, 400)
        for x in range(Ships[SelectedShip]["Speed"]):
            pygame.draw.rect(windowSurface, Colors["White"], pygame.Rect(50 + 10*x, 420, 10, 6))
        drawText("Reload ", 20, Colors["LBlue"], windowSurface, 180, 400)
        for x in range(Ships[SelectedShip]["Reload"]/5):
            pygame.draw.rect(windowSurface, Colors["Orange"], pygame.Rect(170 + 10*x, 420, 10, 6))
        drawText("Damage ", 20, Colors["LBlue"], windowSurface, 300, 400)
        for x in range(Ships[SelectedShip]["Damage"]):
            pygame.draw.rect(windowSurface, Colors["Red"], pygame.Rect(290 + 10*x, 420, 10, 6))
        drawText("Health ", 20, Colors["LBlue"], windowSurface, 420, 400)
        for x in range(Ships[SelectedShip]["Health"]):
            pygame.draw.rect(windowSurface, Colors["Green"], pygame.Rect(410 + 10*x, 420, 10, 6))
        drawText("Shields", 20, Colors["LBlue"], windowSurface, 540, 400)
        for x in range(Ships[SelectedShip]["Shields"]):
            pygame.draw.rect(windowSurface, Colors["Blue"], pygame.Rect(530 + 10*x, 420, 10, 6))
        
        pygame.display.update()
    Skip = False
    for y in range(1,100):
        if Skip:
            break
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_s:
                    Skip = True
        SelBkg = pygame.transform.scale(SelectionBackgroundIMG, (WindowWidth + 400/y, WindowHeight + 400/y))
        windowSurface.blit(SelBkg, pygame.Rect(-200/y, -200/y, WindowWidth + 400/y, WindowHeight + 400/y))
        
        for star in Stars1:
            pygame.draw.circle(windowSurface, star[2], (int(350 + (star[0] - 350)/(y ** 0.2)), int(250 + (star[1] - 350)/(y ** 0.2))) , 0)
        
        if y < 20:
            ShipRect = pygame.Rect(WindowWidth/2 - ShipSize[0]/(2*y), WindowHeight/2 - ShipSize[1]/(2*y), ShipSize[0]/y, ShipSize[1]/y)
            ShipIMG = pygame.transform.scale(ShipIMG, (ShipSize[0]/y, ShipSize[1]/y))
            windowSurface.blit(ShipIMG, ShipRect)
            drawText(ShipName, 30/y, Colors["LBlue"], windowSurface, 350 - 280/y, 250 + 100/y)
            drawText("Speed  ", 20/y, Colors["LBlue"], windowSurface, 350 - 290/y, 250 + 150/y)
            for x in range(Ships[SelectedShip]["Speed"]):
                pygame.draw.rect(windowSurface, Colors["White"], pygame.Rect(350 - 300/y + 10*x/y, 250 + 170/y, 10/y, 6/y))
            drawText("Reload ", 20/y, Colors["LBlue"], windowSurface, 350 - 170/y, 250 + 150/y)
            for x in range(Ships[SelectedShip]["Reload"]/5):
                pygame.draw.rect(windowSurface, Colors["Orange"], pygame.Rect(350 - 180/y + 10*x/y, 250 + 170/y, 10/y, 6/y))
            drawText("Damage ", 20/y, Colors["LBlue"], windowSurface, 350 - 50/y, 250 + 150/y)
            for x in range(Ships[SelectedShip]["Damage"]):
                pygame.draw.rect(windowSurface, Colors["Red"], pygame.Rect(350 - 60/y + 10*x/y, 250 + 170/y, 10/y, 6/y))
            drawText("Health ", 20/y, Colors["LBlue"], windowSurface, 350 + 70/y, 250 + 150/y)
            for x in range(Ships[SelectedShip]["Health"]):
                pygame.draw.rect(windowSurface, Colors["Green"], pygame.Rect(350 + 60/y + 10*x/y, 250 + 170/y, 10/y, 6/y))
            drawText("Shields", 20/y, Colors["LBlue"], windowSurface, 350 + 190/y, 250 + 150/y)
            for x in range(Ships[SelectedShip]["Shields"]):
                pygame.draw.rect(windowSurface, Colors["Blue"], pygame.Rect(350 + 180/y + 10*x/y, 250 + 170/y, 10/y, 6/y))
        
        pygame.display.update()
        mainClock.tick(30)
    for x in range(51):
        if Skip:
            break
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_s:
                    Skip = True
        Opening.set_alpha(x)
        windowSurface.blit(Opening, pygame.Rect(0,0,WindowWidth,WindowHeight))
        pygame.display.update()
        mainClock.tick(200)
    
    for x in range(51):
        if Skip:
            break
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_s:
                    Skip = True
        windowSurface.fill((0,0,0)) #<--------------------------------------------o tlo te co nizej
        drawText("Insert your nickname", 50, Colors["LBlue"], windowSurface, 100, 100)
        drawText("(4-12 characters)", 20, Colors["LBlue"], windowSurface, 100, 140)
        Opening.set_alpha(255 - 5*x)
        windowSurface.blit(Opening, pygame.Rect(0,0,WindowWidth,WindowHeight))
        pygame.display.update()
        mainClock.tick(200)
        
    Start = False
    Player_name = ""
    while not Start:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if pygame.key.name(event.key) in "qwertyuiopasdfghjklzxcvbnm1234567890" and len(Player_name) < 12:
                    Player_name += pygame.key.name(event.key)
                if event.key == K_BACKSPACE:
                    Player_name = Player_name[:-1]
                if event.key == K_SPACE and len(Player_name) > 3:
                    Start = True
                    
        windowSurface.fill((0,0,0))    # <---------------------------------------------------o Dodac tlo i moze napisy poprawic
        drawText("Insert your nickname", 50, Colors["LBlue"], windowSurface, 100, 100)
        drawText("(4-12 characters)", 20, Colors["LBlue"], windowSurface, 100, 140)
        drawText(Player_name, 40, Colors["White"], windowSurface, 120, 200)
        
        pygame.display.update()
        
    Skip = False
    for x in range(51):
        if Skip:
            break
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_s:
                    Skip = True
        windowSurface.fill((0,0,0)) #<--------------------------------------------o tlo 
        drawText("Insert your nickname", 50, Colors["LBlue"], windowSurface, 100, 100)
        drawText("(4-12 characters)", 20, Colors["LBlue"], windowSurface, 100, 140)
        drawText(Player_name, 40, Colors["White"], windowSurface, 120, 200)
        Opening.set_alpha(5*x)
        windowSurface.blit(Opening, pygame.Rect(0,0,WindowWidth,WindowHeight))
        pygame.display.update()
        mainClock.tick(200)
        
    for x in range(51):
        if Skip:
            break
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_s:
                    Skip = True
        windowSurface.fill((0,0,0))  #<----------------------------------------------------------o tlo dodac i wgl zrobic zeby ladnie bylo
        drawText("Select controls", 50, Colors["LBlue"], windowSurface, 100, 100)
        drawText("Keyboard", 50, Colors["White"], windowSurface, 100, 200)
        drawText("Mouse", 50, Colors["White"], windowSurface, 300, 200)
        Opening.set_alpha(255 - 5*x)
        windowSurface.blit(Opening, pygame.Rect(0,0,WindowWidth,WindowHeight))
        pygame.display.update()
        mainClock.tick(200)
    Start = False
    Sterowanie = True
    while not Start:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key in [K_LEFT, K_RIGHT]:
                    Sterowanie = not Sterowanie
                if event.key == K_SPACE:
                    Start = True
        windowSurface.fill((0,0,0))  #<----------------------------------------------------------o tlo dodac i wgl zrobic zeby ladnie bylo
        drawText("Select controls", 50, Colors["LBlue"], windowSurface, 100, 100)
        if Sterowanie:
            pygame.draw.rect(windowSurface, Colors["Gray"], pygame.Rect(80,180,200,70))
        else:
            pygame.draw.rect(windowSurface, Colors["Gray"], pygame.Rect(280,180,200,70))
        drawText("Keyboard", 50, Colors["White"], windowSurface, 100, 200)
        drawText("Mouse", 50, Colors["White"], windowSurface, 300, 200)
        pygame.display.update()
    
    Skip = False
    for x in range(51):
        if Skip:
            break
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_s:
                    Skip = True
        windowSurface.fill((0,0,0))  #<----------------------------------------------------------o tlo dodac i wgl zrobic zeby ladnie bylo
        drawText("Select controls", 50, Colors["LBlue"], windowSurface, 100, 100)
        if Sterowanie:
            pygame.draw.rect(windowSurface, Colors["Gray"], pygame.Rect(80,180,200,70))
        else:
            pygame.draw.rect(windowSurface, Colors["Gray"], pygame.Rect(280,180,200,70))
        drawText("Keyboard", 50, Colors["White"], windowSurface, 100, 200)
        drawText("Mouse", 50, Colors["White"], windowSurface, 300, 200)
        Opening.set_alpha(5*x)
        windowSurface.blit(Opening, pygame.Rect(0,0,WindowWidth,WindowHeight))
        pygame.display.update()
        mainClock.tick(200)
        
    ShipSize = (Ships[SelectedShip]["Size"][0] / 3, Ships[SelectedShip]["Size"][1] / 3)
    ShipIMG = Ships[SelectedShip]["Image"][0]
    ShipIMG = pygame.transform.scale(ShipIMG, ShipSize)
    ShipRect = pygame.Rect(100, 400, ShipSize[0], ShipSize[1])
    
    # zmienic ta animacje nizej ( 2 petle ) <------------------------------------------------------o
    
    for x in range(127):
        if Skip:
            break
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_s:
                    Skip = True
        windowSurface.blit(MenuBkg, pygame.Rect(0,0,500,700))
        for star in Stars1:
            pygame.draw.circle(windowSurface, star[2], (star[0],star[1]), 0)
        windowSurface.blit(ShipIMG, ShipRect)
        Opening.set_alpha(255-2*x)
        windowSurface.blit(Opening, pygame.Rect(0,0,WindowWidth,WindowHeight))
        pygame.display.update()
        mainClock.tick(40)
    
    for x in range(400):
        if Skip:
            break
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_s:
                    Skip = True
        windowSurface.blit(MenuBkg, pygame.Rect(0,0,500,700))
        if x < 100:
            for star in Stars1:
                pygame.draw.circle(windowSurface, star[2], (star[0] - x/2,star[1]), 0)
        else:
            for star in Stars1:
                pygame.draw.circle(windowSurface, star[2], (star[0] - x + 50,star[1]), 0)
        ShipRect.right += 2
        if x < 40:
            ShipRect.top -= 3
        elif x < 80:
            ShipRect.top -= 2
        elif x < 120:
            ShipRect.top -= 1
            ShipRect.right += 1
            
        windowSurface.blit(ShipIMG, ShipRect)
        pygame.display.update()
        mainClock.tick(40)
                
    Over = False
    
    ShipSpeed = Ships[SelectedShip]["Speed"]
    ShipDmg = Ships[SelectedShip]["Damage"]
    ShipReload = Ships[SelectedShip]["Reload"]
    ShipHP = 10 *Ships[SelectedShip]["Health"]
    ShipHP_max = ShipHP
    ShipSD = 10 *Ships[SelectedShip]["Shields"]
    ShipSD_max = ShipSD
    ShipSD_delay = 20
    ShipSD_time = 0
    ShipSize = (Ships[SelectedShip]["Size"][0] / 3, Ships[SelectedShip]["Size"][1] / 3)
    ShipIMG = Ships[SelectedShip]["Image"][0]
    ShipIMG = pygame.transform.scale(ShipIMG, ShipSize)
    ShipRect = pygame.Rect(10, 150, ShipSize[0], ShipSize[1])
    
    Score = 0
    Stage = 0
    
    while not Over:
        Next_stage = False
        IfShot = False
        Completion = 0
        MoveHorizontal = 0
        MoveVertical = 0
        Vx = 0
        Vy = 0
        Reload_delay = 0
        Shots = []
        Enemy = []
        Obstacle = []
        Enemy_time = Stages[Stage]["Resp"]
        Enemy_delay = 0
        Obstacle_time = Stages[Stage]["ObstResp"]
        Obstacle_delay = 0
        EnemyShot = []
        EnemyShot_delay = 0
        while not Next_stage:
                    # sterowanie klawiatura _____________________________________________
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                if event.type == KEYDOWN:
                    if Sterowanie:
                        if event.key == K_UP:
                            MoveVertical = -1
                        if event.key == K_DOWN:
                            MoveVertical = 1
                        if event.key == K_LEFT:
                            MoveHorizontal = -1
                        if event.key == K_RIGHT:
                            MoveHorizontal = 1
                        if event.key == K_SPACE:
                            IfShot = True
                    if event.key == K_p:
                        Pause = True
                        while Pause:
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    terminate()
                                if event.type == KEYDOWN:
                                    if event.key == K_p:
                                        Pause = False
                if event.type == KEYUP:
                    if Sterowanie:
                        if event.key in [K_UP, K_DOWN]:
                            MoveVertical = 0
                        if event.key in [K_LEFT, K_RIGHT]:
                            MoveHorizontal = 0
                        if event.key == K_SPACE:
                            IfShot = False
                        
                        # sterowanie mysza _________________________________________________-
            if not Sterowanie:
                Mouse_pos = pygame.mouse.get_pos()
                IfShot = pygame.mouse.get_pressed()[0]
                if Mouse_pos[0] < ShipRect.left + ShipSize[0]/2 - 10:
                    MoveHorizontal = -1
                elif Mouse_pos[0] > ShipRect.left + ShipSize[0]/2 + 10:
                    MoveHorizontal = 1
                else:
                    MoveHorizontal = 0
                if Mouse_pos[1] < ShipRect.top + ShipSize[1]/2 - 10:
                    MoveVertical = -1  
                elif Mouse_pos[1] > ShipRect.top + ShipSize[1]/2 + 10:
                    MoveVertical = 1
                else:
                    MoveVertical = 0
                if abs(Mouse_pos[0] - ShipRect.left - ShipSize[0]/2) < 10:
                    Vx = 0
                if abs(Mouse_pos[1] - ShipRect.top - ShipSize[1]/2) < 10:
                    Vy = 0
            
            windowSurface.fill((0,0,0))   # <-------------------------------------o dodac tlo
            if ShipHP > 0:
                if MoveVertical == 1 and Vy < ShipSpeed:
                    Vy += float(ShipSpeed) / 5
                if MoveVertical == -1 and Vy > -ShipSpeed:
                    Vy -= float(ShipSpeed) / 5
                if MoveHorizontal == 1 and Vx < ShipSpeed:
                    Vx += float(ShipSpeed) / 5
                if MoveHorizontal == -1 and Vx > -ShipSpeed:
                    Vx -= float(ShipSpeed) / 5
            
            if Vy > 0:
                Vy -= 0.1
            if Vy < 0:
                Vy += 0.1
            if Vx > 0:
                Vx -= 0.1
            if Vx < 0:
                Vx += 0.1
                
            ShipRect.top += Vy
            ShipRect.left += Vx 
            
            if ShipRect.top < 10:
                Vy += 2
                ShipRect.top += 11
            elif ShipRect.top < 20:
                Vy += 1
                ShipRect.top += 5
            if ShipRect.left < 10:
                Vx += 2
                ShipRect.left += 11
            elif ShipRect.left < 20:
                Vx += 1
                ShipRect.left += 5
            if ShipRect.bottom > 490:
                Vy -= 2
                ShipRect.bottom -= 11
            elif ShipRect.bottom > 480:
                Vy -= 1
                ShipRect.bottom -= 5
            if ShipRect.right > 670:
                Vx -= 2
                ShipRect.right -= 11
            elif ShipRect.right > 650:
                Vx -= 1
                ShipRect.right -= 5
            
            if Vy > ShipSpeed * 2 / 3:
                ShipIMG = Ships[SelectedShip]["Image"][1]
                ShipIMG = pygame.transform.scale(ShipIMG, ShipSize)
            elif Vy > ShipSpeed / 3:
                ShipIMG = Ships[SelectedShip]["Image"][2]
                ShipIMG = pygame.transform.scale(ShipIMG, ShipSize)
            elif Vy < -ShipSpeed * 2 / 3:
                ShipIMG = Ships[SelectedShip]["Image"][3]
                ShipIMG = pygame.transform.scale(ShipIMG, ShipSize)
            elif Vy < -ShipSpeed / 3:
                ShipIMG = Ships[SelectedShip]["Image"][4]
                ShipIMG = pygame.transform.scale(ShipIMG, ShipSize)
            else:
                ShipIMG = Ships[SelectedShip]["Image"][0]
                ShipIMG = pygame.transform.scale(ShipIMG, ShipSize)
                
            if ShipSD < ShipSD_max:
                ShipSD_time += 1
                if ShipSD_time > ShipSD_delay:
                    ShipSD_time = 0
                    ShipSD += 1
                
            if Reload_delay < ShipReload:
                Reload_delay += 1
            
            if IfShot and Reload_delay >= ShipReload and ShipHP > 0 and Stages[Stage]["Shot"]:
                Shots.append(pygame.Rect(ShipRect.right - 30, ShipRect.top + ShipSize[1] / 2, 50, 10))
                Reload_delay = 0
                
            for shot in Shots:
                windowSurface.blit(ShotIMG, shot)
                shot.right += 10
                if shot.left > WindowWidth + 400:
                    Shots.remove(shot)
                else:
                    for target in Enemy:
                        if collision(shot, target[0]):
                            explosion(shot.right, shot.top + 8, 16, 0, windowSurface)
                            if target[3] >= ShipDmg:
                                target[3] -= ShipDmg
                            else:
                                target[3] = 0
                                target[2] -= ShipDmg - target[3]
                            if shot in Shots:
                                Shots.remove(shot)
                            
            Enemy_delay += 1
            if Enemy_delay > Enemy_time and len(Stages[Stage]["Enemy"]) > 0:
                enemy_index = Stages[Stage]["Enemy"][random.randint(0,len(Stages[Stage]["Enemy"]) - 1)]
                Enemy_delay = 0                                                                     # [0]                                [1]            [2]                    [3]                        [4]                       [5][6]
                Enemy.append([pygame.Rect(700, random.randint(50,450), Enimes[enemy_index]["Size"][0], Enimes[enemy_index]["Size"][1]), enemy_index, Enimes[enemy_index]["HP"], Enimes[enemy_index]["SD"],Enimes[enemy_index]["SD"], 0, 0])
            
            for target in Enemy:
                target_index = target[1]
                windowSurface.blit(Enimes[target_index]["Image"], target[0])
                if target[6] == 0:
                    target[6] = random.randint(-1,1) * 30
                if target[0].top < 20:
                    target[6] = 10
                if target[0].top > 480:
                    target[6] = -10
                if target[6] > 0:
                    target[6] -= 1
                    target[0].top += Enimes[target_index]["Speed"]
                else:
                    target[6] += 1
                    target[0].top -= Enimes[target_index]["Speed"] 
                target[0].left -= Enimes[target_index]["Speed"]
                if target[3] < target[4]:
                    target[3] += 0.1
                for x in range(target[2]):
                    pygame.draw.rect(windowSurface, Colors["Red"], pygame.Rect(target[0].left + 5 * x - target[2] * 5 / 2 + Enimes[target_index]["Size"][0] / 2, target[0].top - 13, 5, 2))
                for x in range(int(target[3])):
                    pygame.draw.rect(windowSurface, Colors["LBlue"], pygame.Rect(target[0].left + 5 * x - target[3] * 5 / 2 + Enimes[target_index]["Size"][0] / 2, target[0].top - 10, 5, 2))
                if target[0].right < -50:
                    Enemy.remove(target)
                elif target[2] <= 0:
                    Enemy.remove(target)
                    Score += Enimes[target[1]]["Score"]
                target[5] += 1
                if target[5] > Enimes[target_index]["Reload"] and Stages[Stage]["Eshot"]:
                    target[5] = 0
                    EnemyShot.append([pygame.Rect(target[0].right - 30, target[0].bottom - 20, 50, 10), Enimes[target_index]["DMG"]])
            
            for eshot in EnemyShot:
                windowSurface.blit(EnemyShotIMG, eshot[0])
                eshot[0].right -= 10
                if eshot[0].right < -50:
                    EnemyShot.remove(eshot)
                elif collision(ShipRect, eshot[0]):
                    explosion(eshot[0].left, eshot[0].top + 8, 16, 0, windowSurface)
                    if ShipSD >= eshot[1]:
                        ShipSD -= eshot[1]
                    else:
                        ShipSD = 0
                        ShipHP -= eshot[1] - ShipSD
                    EnemyShot.remove(eshot)
            
            if len(Stages[Stage]["Obstacle"]) > 0:
                Obstacle_delay += 1
                if Obstacle_delay > Obstacle_time:
                    Obstacle_delay = 0
                    obstacle_index = random.randint(0,len(Stages[Stage]["Obstacle"]) - 1 )
                    obstacle_pos = random.randint(0,Obstacles[obstacle_index]["Pos"])
                    Obstacle.append([Obstacles[obstacle_index]["Image"], Obstacles[obstacle_index]["Size"], obstacle_pos, 700])
                    
            for obstacle in Obstacle:
                obstacle[3] -= Stages[Stage]["ObstSpeed"]
                Obstacle_rect = pygame.Rect(obstacle[3],125 * obstacle[2], obstacle[1][0], obstacle[1][1])
                if collision(Obstacle_rect, ShipRect):
                    ShipHP = 0
                    break
                windowSurface.blit(obstacle[0], Obstacle_rect)
                if obstacle[3] < -300:
                    Obstacle.remove(obstacle)
                
            
            for x in range(ShipHP):
                pygame.draw.rect(windowSurface, Colors["Red"], pygame.Rect(20+x,10,1,5))
            
            for x in range(ShipSD):
                pygame.draw.rect(windowSurface, Colors["LBlue"], pygame.Rect(20+x,20,1,5))
            
            for x in range(Reload_delay*5):
                pygame.draw.rect(windowSurface, Colors["Orange"], pygame.Rect(20+x,30,1,5))
            drawText("Score " + str(Score), 20, Colors["White"], windowSurface, 20, 40)
            
            windowSurface.blit(ShipIMG, ShipRect)
            
            if ShipHP < ShipHP_max / 2:
                windowSurface.blit(SmokeIMG1, pygame.Rect(ShipRect.left, ShipRect.top, 50, 40))
            if ShipHP < ShipHP_max / 3:
                windowSurface.blit(SmokeIMG1, pygame.Rect(ShipRect.right - 50, ShipRect.top, 50, 40))
            if ShipHP <= 0:
                Over = True
                break
            
            Completion += 1
            if Completion > Stages[Stage]["Length"]:
                Next_stage = True
            
            pygame.display.update()
            
            mainClock.tick(30)
            
        Stage += 1
        if Stage >= len(Stages):
            break
    # ____________________ save _________________________________________
    pos = None
    if len(Data) == 0:
        pos = 1
        Data = [Player_name +" "+str(Score)]
    else:
        for x in range(len(Data)):
            if Score > int(Data[x].split()[1]):
                if x >= 1:
                    Data = Data[:x] + [Player_name +" "+str(Score) + "\n"] + Data[x:]
                else:
                    Data = [Player_name +" "+str(Score) + "\n"] + Data[x:]
                pos = x + 1
                break
    windowSurface.fill((0,0,0))
    drawText("Score : " + str(Score), 50, Colors["LBlue"], windowSurface, 150, 200)
    drawText("Rank : " + str(pos), 50, Colors["White"], windowSurface, 150, 300)
    pygame.display.update()
    
    Start = False
    while not Start:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    Start = True
    for x in range(51):
        Opening.set_alpha(5*x)
        windowSurface.fill((0,0,0))
        drawText("Score : " + str(Score), 50, Colors["LBlue"], windowSurface, 150, 200)
        drawText("Rank : " + str(pos), 50, Colors["White"], windowSurface, 150, 300)
        windowSurface.blit(Opening, pygame.Rect(0,0,WindowWidth,WindowHeight))
        pygame.display.update()
        mainClock.tick(200)
    saveData(Data)
            
                        
                        
            
        
            
            
            
            
            
            
            
            
            
            
            
            
            
        