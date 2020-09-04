import pygame
import sys
pygame.init()

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Um joguin daora ae xD")

janela_aberta = True
while janela_aberta:
  for event in pygame.event.get():
    if event == pygame.QUIT:
      janela_aberta = False

pygame.quit()      