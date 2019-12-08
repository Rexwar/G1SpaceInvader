import sys, math,pygame, os
#print (sys.version)
from pygame.locals import *
from Clases import Nave, Invasor

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (120,50) # posicion pantalla

#variables globales

#pausa list00

#-reiniciar list00

#-que pasa cuando el jugador gana
ancho = 900
alto = 680
listaEnemigo = []

red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

def detenerTodo():
	for enemigo in listaEnemigo:
		for disparo in enemigo.listaDisparo:
			enemigo.listaDisparo.remove(disparo)
		enemigo.conquista = True

def cargarEnemigos():
	for i in range(1,7):
		enemigo = Invasor.Invasor(120*i+15,110,70,'Imagenes/MarcianoA.jpg', 'Imagenes/MarcianoB.jpg')
		listaEnemigo.append(enemigo)
		enemigo = Invasor.Invasor(120*i+5,190,70,'Imagenes/Marciano2A.jpg', 'Imagenes/Marciano2B.jpg')
		listaEnemigo.append(enemigo)
		enemigo = Invasor.Invasor(120*i,260,70,'Imagenes/Marciano3A.jpg', 'Imagenes/Marciano3B.jpg')
		listaEnemigo.append(enemigo)

def del_enemies():
	for enem in listaEnemigo:
		listaEnemigo.remove(enem)

def reiniciar():
	#venta.blit(ImagenFondo,(0,0))
	while len(listaEnemigo)>0:
		del_enemies()
	print (len(listaEnemigo))
	pygame.time.delay(1000)
	cargarEnemigos()



def SpaceInvader():
	pygame.init()
	venta = pygame.display.set_mode((ancho,alto))
	pygame.display.set_caption("Space Invader")

	ImagenFondo = pygame.image.load("Imagenes/Fondo.jpg")

	pygame.mixer.music.load("Sonidos/Intro.mp3")
	pygame.mixer.music.play(3)
	pygame.mixer.music.set_volume(0.3)

	miFuenteSistema = pygame.font.SysFont("Arial",50)
	Texto = miFuenteSistema.render("Fin del Juego",0,(120,100,0))

	jugador = Nave.naveEspacial(ancho,alto)
	cargarEnemigos()

	enJuego = True

	reloj = pygame.time.Clock()

	enPausa = False

	puntaje = 0

	r_presionado = False

	while True:

		reloj.tick(60)
		#jugador.movimiento()
		tiempo = pygame.time.get_ticks()/1000

		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			if enJuego ==True:
				if evento.type == pygame.KEYDOWN:
					if evento.key == K_LEFT:
						jugador.movimientoIzquierda()

					elif evento.key == K_RIGHT:
						jugador.movimientoDerecha()

					elif evento.key == K_SPACE:
						x,y = jugador.rect.center
						jugador.disparar(x,y)
					elif evento.key == K_r:
						r_presionado = True
					elif evento.key == K_p:
						if not enPausa:
							enPausa = True
							jugador.pausa(enPausa)
						else:
							enPausa = False
							jugador.pausa(enPausa)
						
#--------------------------------------FIN EVENTOS----------------


		venta.blit(ImagenFondo,(0,0))
		#print(tiempo)
		jugador.dibujar(venta)
		if len(jugador.listaDisparo)>0: #disparos jugador
			for x in jugador.listaDisparo:
				x.dibujar(venta)
				x.trayectoria(enPausa)

				if x.rect.top <-10:
					jugador.listaDisparo.remove(x)
				else:
					for enemigo in listaEnemigo:
						if x.rect.colliderect(enemigo.rect):
							listaEnemigo.remove(enemigo)
							jugador.listaDisparo.remove(x)
							puntaje += 30		

		if len(listaEnemigo)>0: #aparecer enemigos
			for enemigo in listaEnemigo:
				enemigo.comportamiento(tiempo,enPausa)
				enemigo.dibujar(venta)
				
				if enemigo.rect.colliderect(jugador.rect):
					jugador.destruccion()
					enJuego = False
					detenerTodo()

				if len(enemigo.listaDisparo)>0: #disparo enemigo
					for x in enemigo.listaDisparo:
						x.dibujar(venta)
						x.trayectoria(enPausa)

						if x.rect.colliderect(jugador.rect):
							enJuego = False
							detenerTodo()
							jugador.destruccion()

						if x.rect.top >700:
							enemigo.listaDisparo.remove(x)
						else:
							for disparo in jugador.listaDisparo:
								if x.rect.colliderect(disparo.rect):
									jugador.listaDisparo.remove(disparo)
									enemigo.listaDisparo.remove(x)

		mouse = pygame.mouse.get_pos()

        #print(mouse)
#--------------------------BOTONES----------------------------------
		if (150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450):
			pygame.draw.rect(venta, bright_green,(150,450,100,50))
			flag,__ ,__ = pygame.mouse.get_pressed()
			if (flag == 1 or r_presionado): #--------REINICIO----------------
				reiniciar()
				venta.blit(ImagenFondo,(0,0))
				enJuego = True
				puntaje = 0
				jugador.reiniciar()
				pygame.display.update()
				pygame.mixer.music.play(3)
				r_presionado = False

		else:
			pygame.draw.rect(venta, green,(150,450,100,50))

		pygame.draw.rect(venta, red,(550,450,100,50))

		Fuente = pygame.font.SysFont("ComicSans",50)
		pun = Fuente.render("Puntaje",0,(10,100,40))
		venta.blit(pun,(30,20))
		
		nro = Fuente.render(str(puntaje),0,(10,100,40))
		venta.blit(nro,(180,20))
		
		pygame.display.update()

#-------------------------------------------------------------------

		if enJuego == False:
			#en 3 seg
			pygame.mixer.music.fadeout(3000)

			venta.blit(Texto,(300,300))
		pygame.display.update()

SpaceInvader()