import pygame
from time import sleep
pygame.init()
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.mixer.init()
pygame.mixer.music.load('New Horror __ Ringtone __ 2021 _trending(MP3_160K)_1.mp3')
pygame.mixer.music.play()
sleep(5)
image = pygame.image.load('wp7071249.jpg')
window.blit(image, (0,0))
pygame.display.update()
sleep(2)



