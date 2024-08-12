import pygame



#pygame.mixer.quit()
pygame.init()

my_sound = pygame.mixer.Sound('/home/david/code/audio/StarWars60.wav')
#my_sound = pygame.mixer.Sound('/home/david/code/audio/out.wav')
my_sound.play()

