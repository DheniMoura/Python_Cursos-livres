import pygame

pygame.init()

pygame.mixer.music.load('jack-sparrow.mp3')
pygame.mixer.music.play()
pygame.event.wait()
