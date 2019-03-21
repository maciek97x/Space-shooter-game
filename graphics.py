import pygame

Colors = {"LBlue" : (50,150,200), "White" : (255,255,255), "Red" : (255,100,100), "Green" : (100,255,100), "Blue" : (100,100,255),
          "Orange" : (250,150,50), "Gray" : (100,100,100)}
StarColors = [(255,255,255), (220,220,255), (180,180,255)]

WindowWidth = 700
WindowHeight = 500
SelectionBackgroundIMG = pygame.image.load("background/selection_background.jpg")
SelBkg = pygame.transform.scale(SelectionBackgroundIMG, (WindowWidth + 400, WindowHeight + 400))

MenuBackgroundIMG = pygame.image.load("background/menu_background.jpg")
MenuBkg = pygame.transform.scale(MenuBackgroundIMG, (WindowWidth, WindowHeight))

Ship_size = [(384,150), (240,108)]
Ship1_IMGload = pygame.image.load("ships/ship1.png")
Ship1_IMG0 = pygame.transform.scale(Ship1_IMGload, Ship_size[0])
Ship1_IMGload = pygame.image.load("ships/ship1.png")                # 10 stopni w dol
Ship1_IMG1 = pygame.transform.scale(Ship1_IMGload, Ship_size[0])
Ship1_IMGload = pygame.image.load("ships/ship1.png")                # 5 stopni w dol
Ship1_IMG2 = pygame.transform.scale(Ship1_IMGload, Ship_size[0])
Ship1_IMGload = pygame.image.load("ships/ship1.png")                # 10 stopni w gore
Ship1_IMG3 = pygame.transform.scale(Ship1_IMGload, Ship_size[0])
Ship1_IMGload = pygame.image.load("ships/ship1.png")                # 5 stopni w gore
Ship1_IMG4 = pygame.transform.scale(Ship1_IMGload, Ship_size[0])

Ship2_IMGload = pygame.image.load("ships/ship2.png")
Ship2_IMG0 = pygame.transform.scale(Ship2_IMGload, Ship_size[1])
Ship2_IMGload = pygame.image.load("ships/ship21.png")
Ship2_IMG1 = pygame.transform.scale(Ship2_IMGload, Ship_size[1])
Ship2_IMGload = pygame.image.load("ships/ship22.png")
Ship2_IMG2 = pygame.transform.scale(Ship2_IMGload, Ship_size[1])
Ship2_IMGload = pygame.image.load("ships/ship23.png")
Ship2_IMG3 = pygame.transform.scale(Ship2_IMGload, Ship_size[1])
Ship2_IMGload = pygame.image.load("ships/ship24.png")
Ship2_IMG4 = pygame.transform.scale(Ship2_IMGload, Ship_size[1])


#_____________________________________________STATKI___________________________________________________
#                                    1-10          1-10         1-50(step 5)   1-10           1-10
Ships = [{"Name" : "Ship1", "Speed" : 5, "Damage" : 8, "Reload": 20, "Health" : 10, "Shields" : 8, "Image" : [Ship1_IMG0, Ship1_IMG1, Ship1_IMG2, Ship1_IMG3, Ship1_IMG4], "Size": Ship_size[0]},
         {"Name" : "Ship2", "Speed" : 7, "Damage" : 5, "Reload": 5, "Health" : 4, "Shields" : 7, "Image" : [Ship2_IMG0, Ship2_IMG1, Ship2_IMG2, Ship2_IMG3, Ship2_IMG4], "Size": Ship_size[1]},
         {"Name" : "Ship3", "Speed" : 10, "Damage" : 20, "Reload": 5, "Health" : 20, "Shields" : 30, "Image" : [Ship2_IMG0, Ship2_IMG1, Ship2_IMG2, Ship2_IMG3, Ship2_IMG4], "Size": Ship_size[1]} ]



Smoke_IMG1 = pygame.image.load("images/smoke1.png")
Smoke_IMG2 = pygame.image.load("images/smoke2.png")
SmokeIMG1 = pygame.transform.scale(Smoke_IMG1, (50,40))
SmokeIMG2 = pygame.transform.scale(Smoke_IMG2, (50,40))

Shot_IMG = pygame.image.load("images/lasershot.png")
ShotIMG = pygame.transform.scale(Shot_IMG, (50, 10))

ExpIMG1 = pygame.image.load("images/explosion1.png")
ExpIMG2 = pygame.image.load("images/explosion2.png")
ExpIMG3 = pygame.image.load("images/explosion3.png")
ExplosionImg = [ExpIMG1, ExpIMG2, ExpIMG3]

def explosion(x, y, size, ExpType, ExpSurface):
    ExpImg = pygame.transform.scale(ExplosionImg[ExpType], (size,size))
    ExpSurface.blit(ExpImg, pygame.Rect(x - size / 2, y - size /2, size, size))
