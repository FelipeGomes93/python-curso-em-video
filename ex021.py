'''Faça um programa que abra e reproduza um arquivo .MP3'''
import pygame
pygame.init()
pygame.mixer.music.load('ga.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
input("Pressione ENTER para parar a música...")
pygame.mixer.music.stop()

