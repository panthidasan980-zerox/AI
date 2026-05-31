import pygame
import cv2 as cv
from teachable_machine import TeachableMachine
from sys import exit

pygame.init()
screen = pygame.display.set_mode([800, 400])
pygame.display.set_caption("Runner- Learn Gravity")
camera = cv.VideoCapture(0)

model = TeachableMachine(model_path = "keras_model.h5", labels_file_path= "labels.txt")

# Colors
groundcolor = (56, 152, 68)
sky = (135, 206, 235)
playercolor = (108, 59, 170)
obstacleColor = (255, 0, 0)
black = (0,0,0)


player = pygame.Rect(80, 300, 50, 50)
gravity = 0
ground = pygame.Rect(0, 350, 800, 50)
obstacle = pygame.Rect(600, 330 ,20,20)
clock = pygame.time.Clock()

obstacle_speed = 5
score = 0

game_font = pygame.font.SysFont(None, 40)
running = True
is_on_ground = False\

ret,frame = camera.read()
if ret:
        cv.imshow("Camera", frame)
        cv.imwrite("frame.jpg",frame)
        result = model.classify_image("frame.jpg")
        print(result)
        label = result["class_name"]

#Game Loop
while running:
  #Event Loop
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()

        # Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if is_on_ground==True:
                    gravity = -20
                    is_on_ground = False

    ret,frame = camera.read()
    if ret:
        cv.imshow("Camera", frame)
        cv.imwrite("frame.jpg",frame)
        result = model.classify_image("frame.jpg")
        print(result)
        label = result["class_name"]
    
        if "Jump" in label:
            if is_on_ground ==True:
                gravity = -20
                is_on_ground = False


    obstacle.x = obstacle.x - obstacle_speed 
    
    if obstacle.right <=0:
        # Respawan obstacle
        obstacle.left = 800 
        score = score + 1
    
    if player.colliderect(obstacle):
        break
    
    if not is_on_ground:
        gravity += 1
        player.y += gravity 
        
    
    if player.bottom >= 350:
        player.bottom = 350
        gravity = 0
        is_on_ground = True
    #Graphics
    screen.fill(sky)
    pygame.draw.rect(screen, playercolor, player)     #location, color, which rect
    pygame.draw.rect(screen, groundcolor,ground )
    pygame.draw.rect(screen, obstacleColor,obstacle )
    
    score_surface =  game_font.render(f"Score: {score}", True, black)
    screen.blit(score_surface, (20,20))
    
    pygame.display.update()    
    clock.tick(60)
