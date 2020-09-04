import pygame
pygame.init()
x = 400
y = 300
velocidade = 5

janela = pygame.display.set_mode((800,600)) # DISPLAY DA TELA / LARGURA X ALTURA / 800 DE LARGURA X 600 DE ALTURA
pygame.display.set_caption("Um joguin daora ae xD") #TÍTULO DA JANELA

janela_aberta = True
while janela_aberta:        #ENQUANTO A JANELA FOR VERDADEIRA ELA PERMANECERÁ ABERTA, ISSO DAQUI EH PARA NAO FECHAR A TELA INICIAR O PROGRAMA.
  pygame.time.delay(50)
  for event in pygame.event.get():
    if event.type == pygame.QUIT: ####### NESSE TRECHO AQUI, ELE VAI PEGAR CADA EVENTO GERADO E VAI VERIFICAR SE O EVENTO RECEBIDO VAI SER IGUAL A QUIT(BOTAO DE FECHAR DA JANELA), SE FOR, VAI TORNAR A VARIAVEL JANELA_ABERTA FALSA E TORNAR A CONDIÇÃO DO WHILE FALSA.
      janela_aberta = False
  comandos = pygame.key.get_pressed()
  if comandos[pygame.K_UP]:
    y -= velocidade
  if comandos[pygame.K_DOWN]:
    y += velocidade
  if comandos[pygame.K_RIGHT]:
    x += velocidade
  if comandos[pygame.K_LEFT]:
    x -= velocidade
    
  janela.fill((0,0,0))                                   
  pygame.draw.circle(janela, (0,255,0),(x,y), 50)   
  #PARAMETROS: ONDE SERÁ DESENHADO O CIRCULO, COR EM RGB, POSIÇÃO NA TELA, RAIO DO CÍRCULO(EM PX).      
  
  pygame.display.update() 
  #AQUI ELE VAI DAR UM UPDATE NO DISPLAY.

pygame.quit()      