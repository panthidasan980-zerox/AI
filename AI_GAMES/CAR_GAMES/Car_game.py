import pygame
import cv2 as cv
from teachable_machine import TeachableMachine
pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Car Game🚗")
camera = cv.VideoCapture(0)

player_x = 220
player_y = 550


model = TeachableMachine(model_path = "keras_model.h5", labels_file_path= "labels.txt")

running = True 
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    ret,frame = camera.read()

    if ret:
        cv.imshow("Camera", frame)
        cv.imwrite("frame.jpg",frame)
        result = model.classify_image("frame.jpg")
        print(result)
        label = result["class_name"]

        if "Left" in label:
            player_x = player_x - 2
        elif "Right" in label:
            player_x = player_x + 2

        if player_x < 40:
            player_x = 40
        
        if player_x > 460:
            player_x = 460



    screen.fill((255,255,255))
    player_rect = pygame.Rect(player_x,280,50,100)
    pygame.draw.rect(screen,(23,233,123),player_rect)
   
    pygame.display.update()
