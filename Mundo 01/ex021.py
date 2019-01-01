#Exercício Python 021: Faça um programa em Python
#que abra e reproduza o áudio de um arquivo MP3.
import pygame
print('\033[4;33m--=DESAFIO 21=--')
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
print('Migos - Deadz feat. 2 Chainz!')
input()
pygame.event.wait()
