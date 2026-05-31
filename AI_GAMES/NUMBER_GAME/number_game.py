import pygame
import cv2 as cv
from teachable_machine import TeachableMachine

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Keyboard Number Display")
camera = cv.VideoCapture(0)

font = pygame.font.Font(None, 100)
model = TeachableMachine(model_path = "keras_model.h5", labels_file_path= "labels.txt")

current_number = "0"

running = True
while running:
    screen.fill("white")

    # Display current number
    text = font.render(current_number, True, "black")
    screen.blit(text, (180, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

        if event.type == pygame.KEYDOWN:
            if event.unicode.isdigit():
                current_number = event.unicode
    
    ret, frame= camera.read()
    if ret: 
        cv.imshow("Camera", frame)
        cv.imwrite("frame.jpg",frame)
        result = model.classify_image("frame.jpg")
        print(result)
        label = result["class_name"][2]

        current_number = label

    pygame.display.update()

pygame.quit()