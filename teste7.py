import pygame, math, time
from pygame.locals import * # CARREGA TUDO QUE E IMPORTANTE NO PYGAME, como AS TECLAS
	
def main(): # loop principal	
	saida = False
	while not saida: # ENQUANTO A SAIDA NAO FOR SOLICIDATADA
		saida1, settings= load() # carrega todas as informacoeS
		#lancador = 
		obj = settings['obj']
		angle = settings['angulo']
		seta = settings['p']
		angulo = lancador(settings)
		angle[0] = angulo
		v = (seta[0]-600)/20.
		print('valor_de_v')
		print(v)
		angulo_radianos = (angulo + 45)*math.pi/180.
		vx = 1.*v*math.cos(angulo_radianos)
		vy = 1.*v*math.sin(angulo_radianos)
		raio_canhao = 0.6 # LEMBRAR QUE EXISTE UMA ESCALA
		settings = update(settings)
		x_bola = -2 + raio_canhao*math.cos(angulo_radianos) + settings['p'][1]/200.
		y_bola =  1.5 - raio_canhao*math.sin(angulo_radianos) - (3 - settings['p'][2]/200.)
		print(x_bola,y_bola)
 		#obj[0],obj[1],obj[2],obj[3],obj[4],obj[5] = -1, 0, 0, 6.24, 1., 0.001 # x, y, vx, vy, massa, delta		
		obj[0],obj[1],obj[2],obj[3],obj[4],obj[5] = x_bola, y_bola, vx, -vy, 1., 0.001 # x, y, vx, vy, massa, delta
		settings = update(settings) # ATUALIZA VARIAVEIS
		draw(settings)   # DESENHA VARIAVEIS
		while not saida1: # ENQUANTO A SAIDA NAO FOR SOLICIDATADA
			settings = update(settings) # ATUALIZA VARIAVEIS
			draw(settings)   # DESENHA VARIAVEIS
			#saida = check_exit()
			saida1 = check_exit2()  # VERIFICAR SAIDA, CONDICAO PARA MUSAR ELA E SAIR DO LOOP DO JOGO
		saida = continuar(settings)
		print('apertou q')
	pygame.quit() 

  
def desenhar_barra(settings):
	#settings = update(settings)
	screen = settings['screen']
	x_barra = settings['p']
	ba= pygame.image.load("barra.png")
	barra = ba.get_rect(center=(700, 580))
	screen.blit(ba, barra)
	saida = check_exit()
	ss= pygame.image.load("seta.png")
	ss2 = ss.get_rect(center=(x_barra[0], 570))
	screen.blit(ss, ss2)
	# escrever angulo:
	pygame.font.init()
	myfont = pygame.font.SysFont('Comic Sans MS', 22)
	angulo = settings['angulo'][0] + 45
	angulo = ("%.1f" % angulo) 
	textsurface = myfont.render('Angle = '+ angulo + ' degree', False, (255, 255, 255))
	screen.blit(textsurface,(550,460))
	# fim escrever angulo
	# escrever velocidade:
	myfont = pygame.font.SysFont('Comic Sans MS', 22)
	velocidade = (settings['p'][0]-600)/20.
	velocidade = ("%.1f" % velocidade) 
	textsurface = myfont.render('V = '+ velocidade + ' AU/y', False, (255, 255, 255))
	screen.blit(textsurface,(600,500))
	# fim escrever velocidade
	saida = check_exit()
	pygame.display.flip()
	k = pygame.key.get_pressed() 
	if  k[K_DOWN]:	  # se apertar d ou seta_para_direita a posicao do circulo muda para direita. 
		x_barra[0] = x_barra[0] - 1.5
		if(x_barra[0]<600):
			x_barra[0] = 600
	if  k[K_UP]:	  # se apertar d ou seta_para_direita a posicao do circulo muda para direita. 
		x_barra[0] = x_barra[0] + 1.5
		if(x_barra[0]>800):
			x_barra[0] = 800
	
 
	
	
def load(): # funcao para carregar as informacoes
	screen_size = (800,600)# TAMANHHO DA TELA (x , y )
	screen = pygame.display.set_mode(screen_size) # carregar tela
	circulo = pygame.Rect(300,300,1,1)# carregar o circulo na metade da tela (pixel_x, pixel_y, raio, height )
	sol     = pygame.Rect(400,300,1,1)#  
	obj     = [1, 1, -1.7, 0.4, 1., 0.001] # x, y, vx, vy, massa, delta
	angulo  = [0,0]
	p       = [620,0,600] # x_barra_velocidade, x_canhao, y_canhao
	return False, { 
	'screen_size' : screen_size,
	'screen'      : screen,  
	'circulo'     : circulo,
	'sol'         : sol,
	'obj'         : obj,
	'angulo'      : angulo,
	'p'	      : p 
	}


def lancador(settings):
	i = 0
	draw(settings)   
	angulo = 0
	while(i == 0):
		settings['angulo'][0] = angulo
		screen = settings['screen']
		screen = settings['screen']
		fundo= pygame.image.load("bg_game_03.jpg")
		fundo2 = fundo.get_rect(center=(400, 300))
		screen.blit(fundo, fundo2)
		pygame.draw.circle(screen, (255,255,255), [400,300], 180, 1) # BORDA DE 2 PIXELS
		pygame.draw.circle(screen, (255,255,255), [400,300], 300, 1) # BORDA DE 2 PIXELS
		pygame.draw.circle(screen, (0,100,0), [400,300], 200, 1) # BORDA DE 2 PIXELS
		settings = update(settings) 
		sol = settings['sol']	
		ball = pygame.image.load("sun.png")
		ballrect = ball.get_rect(center=(sol[0], sol[1]))
		screen.blit(ball, ballrect)
		saida = check_exit() 
		ball1 = pygame.image.load("canhao.png")
		ball1 = pygame.transform.rotate(ball1, angulo)
		ballrect = ball1.get_rect(center=(settings['p'][1] , settings['p'][2]))
		screen.blit(ball1, ballrect)
		# escrever velocidade:
		myfont = pygame.font.SysFont('Comic Sans MS', 22)
		velocidade = (settings['p'][0]-600)/20.
		velocidade = ("%.1f" % velocidade) 
		textsurface = myfont.render('V = '+ velocidade + ' AU/y', False, (255, 255, 255))
		screen.blit(textsurface,(600,500))
		# fim escrever velocidade
		# escrever angulo:
		myfont = pygame.font.SysFont('Comic Sans MS', 22)
		angulo2 = ("%.1f" % (angulo+45)) 
		textsurface = myfont.render('Angle = '+ angulo2 + ' degree', False, (255, 255, 255))
		screen.blit(textsurface,(550,460))
		# fim escrever angulo
		desenhar_barra(settings)
		branco = (255,255,255)
		k = pygame.key.get_pressed()    
		if  k[K_RIGHT]:	 
			angulo = angulo -1
		if  k[K_LEFT]:
 			angulo = angulo +1
		#if(angulo > 45):
		#	angulo = 45
		#if(angulo < -45):
		#	angulo = -45
		if  k[K_SPACE]:
			i = 2
		print('aguardando lancamento')
		#escrever_texto(settings, 'teste', 10, 10)
	return angulo


def escrever_texto(settings, texto, x, y):
		screen = settings['screen']
		branco = (255,255,255)
		#Dice random number generation
		pygame.font.init()
		myfont = pygame.font.SysFont('Comic Sans MS', 30)
		textsurface = myfont.render(texto, False, (255, 255, 255))
		screen.blit(textsurface,(x,y))
		pygame.display.flip() # atualizar a tela, troca tudo que esta na tela
		#pygame.time.Clock().tick(3600)
		#pygame.display.flip()	



def continuar(settings):
	screen = settings['screen']
	draw(settings)
	b = pygame.image.load("continuar1_yes.png")
	ballrect1 = b.get_rect(center=(400, 300))
	screen.blit(b, ballrect1)
	saida = check_exit()
	pygame.display.flip()
	pygame.time.Clock().tick(30)# opcional, fazer o jogo rodar em tick(60) = 60 fotos por segundo
	i = 0
	j = 0
	fim = False
	saida3 = False
	while not saida3 :
		#print(i)
		#screen = settings['screen']
		screen = settings['screen']
		fundo= pygame.image.load("bg_game_03.jpg")
		fundo2 = fundo.get_rect(center=(400, 300))
		screen.blit(fundo, fundo2)
		screen.blit(b, ballrect1)
		pygame.draw.circle(screen, (255,255,255), [400,300], 180, 1) # BORDA DE 2 PIXELS
		pygame.draw.circle(screen, (255,255,255), [400,300], 300, 1) # BORDA DE 2 PIXELS
		saida3 = check_exit()  # VERIFICAR SAIDA, CONDICAO PARA MUSAR ELA E SAIR DO LOOP DO JOGO CORRIGI UM PROBLEMA DE RECEBER TECLA
		pygame.display.flip() # atualizar a tela, troca tudo que esta na tela
		pygame.time.Clock().tick(30)
		i = i+1
		k = pygame.key.get_pressed()   # recebe tecla clicada
		if  k[K_SPACE]:	
			saida3 = True
		if  k[K_LEFT]:	
			b = pygame.image.load("continuar1_yes.png")
			ballrect1 = b.get_rect(center=(400, 300))
			fim = False
		if  k[K_RIGHT]:	
			b = pygame.image.load("continuar1_no.png")
			ballrect1 = b.get_rect(center=(400, 300))
			fim = True
	if(fim == True):
			print('FIM DO JOGO ...')
	#pygame.display.flip()
	#time.sleep(1)	# pausa de 1 segundo
	return fim


def atualizar_posicao(todos): # todos_dados = [x, y, vx, vy, m_sol, h ]
	x, y, vx, vy, m, h = todos[0], todos[1], todos[2], todos[3], todos[4], todos[5]
	x = x + h*vx
	y=  y + h*vy
	r = pow(x*x+y*y,0.5)
	vx = vx -h*(4*math.pi*math.pi*x*m)/pow(r,3)
	vy = vy -h*(4*math.pi*math.pi*y*m)/pow(r,3)
	#print('veio aqui')
	#print(x,y)
	return [x,y,vx,vy]


def update(settings): # PARA ATUALIZAR AS VARIAVEIS
	obj = settings['obj']
	#print(obj)
	obj[0],obj[1],obj[2],obj[3] = atualizar_posicao([obj[0],obj[1],obj[2],obj[3],obj[4],obj[5]])
	#print(obj)
	k = pygame.key.get_pressed()   
	screen_size = settings['screen_size'] 
	circulo = settings['circulo'] 
	#print(circulo.x)
	#sol = settings['sol']
	#if k[K_d] or k[K_RIGHT]: 
	#	circulo.x += 1
	#if k[K_a] or k[K_LEFT]:
	#	circulo.x -= 1
	#if k[K_w] or k[K_UP]:
	#	circulo.y -= 1
	#if k[K_s] or k[K_DOWN]:
	#	circulo.y += 1
	if k[K_d]:	   
		settings['p'][1] += 3
	if k[K_a]:
		settings['p'][1] -= 3
	if k[K_w]:
		settings['p'][2] -= 3
	if k[K_s]:
		settings['p'][2] += 3
	# limita_bordas:
	x, y = 200*obj[0]+ 400,200*obj[1] + 300
	circulo.x,circulo.y =x,y
	#if circulo.x < 0:
	#	circulo.x = 0
	#if circulo.y < 0:
	#	circulo.y = 0
	#if circulo.x + circulo.width > screen_size[0]: # lembrando que circulo.width e o tamnho em x do quadrado e screen_size[0] o limite x da tela
	#	circulo.x = screen_size[0] - circulo.width
	#if circulo.y + circulo.height > screen_size[1]: # lembrando que circulo.width e o tamnho em x do quadrado e screen_size[0] o limite x da tela
	#	circulo.y = screen_size[1] - circulo.height 
	return settings


def draw(settings):
	screen = settings['screen']
	circulo = settings['circulo']
	angulo = settings['angulo']
	sol = settings['sol']
	x_barra = settings['p']
	cor_preta = (0,0,0)	
	cor_branca = (255,255,255)
	screen = settings['screen']
	fundo= pygame.image.load("bg_game_03.jpg")
	fundo2 = fundo.get_rect(center=(400, 300))
	screen.blit(fundo, fundo2)
	pygame.draw.circle(screen, (255,255,255), [400,300], 180, 1) # BORDA DE 2 PIXELS
	pygame.draw.circle(screen, (255,255,255), [400,300], 300, 1) # BORDA DE 2 PIXELS
	pygame.draw.circle(screen, (0,100,0), [400,300], 200, 1) # BORDA DE 2 PIXELS
	#### desenhar_sol:
	ball = pygame.image.load("sun.png")
	ballrect = ball.get_rect(center=(sol[0], sol[1]))
	screen.blit(ball, ballrect)
	ball1 = pygame.image.load("canhao.png")
	ball1 = pygame.transform.rotate(ball1, angulo[0])
	ballrect = ball1.get_rect(center=(settings['p'][1] , settings['p'][2]))
	screen.blit(ball1, ballrect)
	#pygame.draw.rect(tela, cor, (x,y,width, hight), linha)# funcao de desenhar na tela do pygame
	terra= pygame.image.load("planet_2.png")
	terra2 = terra.get_rect(center=(circulo.x, circulo.y))
	screen.blit(terra, terra2)
	#pygame.draw.circle(screen, cor_branca, [circulo.x, circulo.y], 10) # PARA DESENHAR UMA BORDA NO CICULO BASTA COLOCAR OUTRO PARAMETRO TIPO pygame.draw.circle(screen, cor_branca, [33,33], 44, 2) # BORDA DE 2 PIXELS
	ball1 = pygame.image.load("canhao.png")
	ball1 = pygame.transform.rotate(ball1, angulo[0])
	ballrect = ball1.get_rect(center=(settings['p'][1] , settings['p'][2]))
	screen.blit(ball1, ballrect)
	desenhar_barra(settings)
	pygame.font.init()
	# escrever angulo:
	myfont = pygame.font.SysFont('Comic Sans MS', 22)
	angulo = settings['angulo'][0] + 45
	angulo = ("%.1f" % angulo) 
	textsurface = myfont.render('Angle = '+ angulo + ' degree', False, (255, 255, 255))
	screen.blit(textsurface,(550,460))
	# fim escrever angulo
	# escrever velocidade:
	myfont = pygame.font.SysFont('Comic Sans MS', 22)
	velocidade = (settings['p'][0]-600)/20.
	velocidade = ("%.1f" % velocidade) 
	textsurface = myfont.render('V = '+ velocidade + ' AU/y', False, (255, 255, 255))
	screen.blit(textsurface,(600,500))
	# fim escrever velocidade
	pygame.display.flip() # atualizar a tela, troca tudo que esta na tela
	pygame.time.Clock().tick(60)# opcional, fazer o jogo rodar em tick(60) = 60 fotos por segundo



def check_exit(): # verificar saida
	k = pygame.key.get_pressed() #
	for e in pygame.event.get():
		if e.type == QUIT or k[K_ESCAPE]: 
			return True
	return False

def check_exit2(): # verificar saida
	k = pygame.key.get_pressed()
	for e in pygame.event.get():
		if k[K_q]: #
			return True
	return False


main()
	


