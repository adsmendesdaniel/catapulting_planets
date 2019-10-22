import pygame
from pygame.locals import * # CARREGA TUDO QUE E IMPORTANTE NO PYGAME, como AS TECLAS
#import ending
	
def main(): # loop principal
	saida, settings= load() # carrega todas as informacoeS
	while not saida: # ENQUANTO A SAIDA NAO FOR SOLICIDATADA
		settings = update(settings) # ATUALIZA VARIAVEIS
		draw(settings)   # DESENHA VARIAVEIS
		saida = check_exit()  # VERIFICAR SAIDA, CONDICAO PARA MUSAR ELA E SAIR DO LOOP DO JOGO
	pygame.quit() 
	
	
def load(): # funcao para carregar as informacoes
	screen_size = (800,600)# TAMANHHO DA TELA (x , y )
	screen = pygame.display.set_mode(screen_size) # carregar tela
	circulo = pygame.Rect(300,300,1,1)# carregar o circulo na metade da tela (pixel_x, pixel_y, raio, height )
	sol     = pygame.Rect(111,111,1,1)# 
	return False, {  # configurar a saida com uma lista de variaveis
	'screen_size' : screen_size,
	'screen'      : screen,  # display
	'circulo'     : circulo,
	'sol'         : sol
	}

def update(settings): # PARA ATUALIZAR AS VARIAVEIS
	k = pygame.key.get_pressed()    # recebe tecla clicada
	screen_size = settings['screen_size'] # tamanho da tela, e um vetor de tamanhos
	circulo = settings['circulo'] # carrega o circulo
	sol = settings['sol']
	if k[K_d] or k[K_RIGHT]:	  # se apertar d ou seta_para_direita a posicao do circulo muda para direita. 
		circulo.x += 1
	if k[K_a] or k[K_LEFT]:
		circulo.x -= 1
	if k[K_w] or k[K_UP]:
		circulo.y -= 1
	if k[K_s] or k[K_DOWN]:
		circulo.y += 1
	if k[K_j]:	  # se apertar d ou seta_para_direita a posicao do circulo muda para direita. 
		sol.x += 1
	if k[K_h]:
		sol.x -= 1
	if k[K_u]:
		sol.y -= 1
	if k[K_n]:
		sol.y += 1
	# limita_bordas:
	if circulo.x < 0:
		circulo.x = 0
	if circulo.y < 0:
		circulo.y = 0
	if circulo.x + circulo.width > screen_size[0]: # lembrando que circulo.width e o tamnho em x do quadrado e screen_size[0] o limite x da tela
		circulo.x = screen_size[0] - circulo.width
	if circulo.y + circulo.height > screen_size[1]: # lembrando que circulo.width e o tamnho em x do quadrado e screen_size[0] o limite x da tela
		circulo.y = screen_size[1] - circulo.height 
	return settings


def draw(settings):
	screen = settings['screen']
	circulo = settings['circulo']
	sol = settings['sol']
	cor_preta = (0,0,0)	
	cor_branca = (255,255,255)
	screen.fill(cor_preta) # preencher com cor preta
	#### desenhar_sol:
	ball = pygame.image.load("star.jpeg")
	ballrect = ball.get_rect(topleft=(sol[0], sol[1]))
	screen.blit(ball, ballrect)

	#pygame.draw.rect(tela, cor, (x,y,width, hight), linha)# funcao de desenhar na tela do pygame
	pygame.draw.circle(screen, cor_branca, [circulo.x, circulo.y], 44) # PARA DESENHAR UMA BORDA NO CICULO BASTA COLOCAR OUTRO PARAMETRO TIPO pygame.draw.circle(screen, cor_branca, [33,33], 44, 2) # BORDA DE 2 PIXELS
	pygame.display.flip() # atualizar a tela, troca tudo que esta na tela
	pygame.time.Clock().tick(3600)# opcional, fazer o jogo rodar em tick(60) = 60 fotos por segundo



def check_exit(): # verificar saida
	k = pygame.key.get_pressed() # pegar a tecla pressionada, todas as teclas clicadas
	for e in pygame.event.get():
		if e.type == QUIT or k[K_ESCAPE]: # e.type = aceita fechar a tela, k = aceita tecla esc
			import ending
	return False

main()
	


