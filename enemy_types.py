import pygame

EnemyShot_IMG = pygame.image.load("images/enemyshot.png")
EnemyShotIMG = pygame.transform.scale(EnemyShot_IMG, (50, 10))

EnemySize = [(10,10), (125,125), (200,100)]
Enemy_IMG = pygame.image.load("images/enemyship1.png")
EnemyIMG1 = pygame.transform.scale(Enemy_IMG, EnemySize[0])
Enemy_IMG = pygame.image.load("images/enemyship1.png")
EnemyIMG2 = pygame.transform.scale(Enemy_IMG, EnemySize[1])
Enemy_IMG = pygame.image.load("images/enemyship1.png")
EnemyIMG3 = pygame.transform.scale(Enemy_IMG, EnemySize[2])

Enimes = [{"Name" : "enemy1", "HP": 3, "SD": 4, "DMG": 4, "Reload": 20, "Speed": 3, "Image": EnemyIMG1, "Size": EnemySize[0], "Score": 4},
          {"Name" : "enemy2", "HP": 5, "SD": 10, "DMG": 10, "Reload": 40, "Speed": 2, "Image": EnemyIMG2, "Size": EnemySize[1], "Score": 10},
          {"Name" : "enemy3", "HP": 80, "SD": 20, "DMG": 20, "Reload": 100, "Speed": 1, "Image": EnemyIMG3, "Size": EnemySize[2], "Score": 50}]

ObstacleSize = [(250,125), (250,250), (250,375)]

ObsIMG1 = pygame.Surface(ObstacleSize[0])
ObsIMG2 = pygame.Surface(ObstacleSize[1])
ObsIMG3 = pygame.Surface(ObstacleSize[2])

ObsIMG1.fill((200,200,200))
ObsIMG2.fill((200,200,200))
ObsIMG3.fill((200,200,200))

Obstacles = [{"Name" : "Block", "Size" : ObstacleSize[0], "Image" : ObsIMG1, "Pos" : 3},
             {"Name" : "BigBlock", "Size" : ObstacleSize[1], "Image" : ObsIMG2, "Pos" : 2},
             {"Name" : "BigBigBlock", "Size" : ObstacleSize[2], "Image" : ObsIMG3, "Pos" : 1}]