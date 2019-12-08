import sys, pygame, math
from pygame.locals import *

class Proyectil(pygame.sprite.Sprite):
	def __init__(self, posx,posy, ruta, personaje):
		pygame.sprite.Sprite.__init__(self)

		self.imageProyectil = pygame.image.load(ruta)

		self.rect = self.imageProyectil.get_rect()

		self.velocidadDisparo = 10

		self.rect.top = posy
		self.rect.left = posx

		self.disparoPersonaje = personaje
		#personaje = true si es la nave

	def trayectoria(self,pausa):
		if not pausa:
			if self.disparoPersonaje == True:
				self.rect.top = self.rect.top - self.velocidadDisparo
			else:
				self.rect.top = self.rect.top + self.velocidadDisparo

	def dibujar(self, superficie):
		superficie.blit(self.imageProyectil, self.rect)

