'''
5.[sound] Play the first 9 notes of Beethoven's "Fur Elise" (E D# E D# E B D C A) - 
check with https://onlinesequencer.net/ (modules: winsound / pygame.midi).
'''
import pygame.midi
import time

E = 76
D_diesis = 75 
B = 71
D = 74
C = 72
A = 69
max_volume = 127

song = [E, D_diesis, E, D_diesis, E, B, D, C, A]

pygame.midi.init()
player = pygame.midi.Output(1)
player.set_instrument(48,1)

print('Playing Fur Elise by Beethoven...')
for note in song:
	player.note_on(note, max_volume)
	time.sleep(0.2)
	player.note_off(note, max_volume)

time.sleep(1)

del player
pygame.midi.quit()
