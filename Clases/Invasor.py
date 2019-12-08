import sys, pygame, math
from pygame.locals import *
from random import randint
from . import Proyectil


class Invasor(pygame.sprite.Sprite):
	def __init__(self, posx, posy, distancia, imagenUno, imagenDos):
		#propiedades del invasor
		pygame.sprite.Sprite.__init__(self)
		self.frec = 1

		self.imagenA = pygame.image.load(imagenUno)
		self.imagenB = pygame.image.load(imagenDos)

		self.listaImagenes = [self.imagenA, self.imagenB]
		self.posImagen = 0

		self.imagenInvasor = self.listaImagenes[self.posImagen]
		self.rect = self.imagenInvasor.get_rect()

		self.listaDisparo = []
		self.velocidad = 1
		self.rect.top = posy
		self.rect.left = posx

		self.rangoDisparo = 5 #entre 0 y 1000 
		self.tiempoCambio = 1

		self.conquista = False

		self.derecha = True #direccion
		self.contador = 0 #choques antes de descender
		self.Maxdescenso = self.rect.top + 10

		self.limiteDerecha = posx + distancia
		self.limiteIzquierda = posx - distancia

	def dibujar(self, superficie):
		#se dibuja la imagen actual en la lista
		self.imagenInvasor = self.listaImagenes[self.posImagen]
		superficie.blit(self.imagenInvasor, self.rect)

	def comportamiento(self, tiempo, enPausa):
		#se mueve y ataca
		#movimiento constante y disparo aleatorio

		#print (self.tiempoCambio, tiempo)
		if self.conquista == False:
			if not enPausa:
				self.__ataque()
				self.__movimientos()
			if self.tiempoCambio <= tiempo * self.frec: #animacion
				self.posImagen +=1
				self.tiempoCambio += 1

				if self.posImagen > len(self.listaImagenes)-1:
					self.posImagen = 0


	def __movimientos(self):
		if self.contador < 2:
			self.__movimientoLateral()
		else:
			self.__descenso()

	def __descenso(self):
		if self.Maxdescenso == self.rect.top:
			self.contador = 0
			self.Maxdescenso = self.rect.top + 40
		else:
			self.rect.top += 1

	def __movimientoLateral(self):
		if self.derecha == True:
			self.rect.left = self.rect.left + self.velocidad
			if self.rect.left > self.limiteDerecha: # limite der de movimiento
				self.derecha = False
				self.contador += 1

		else:
			self.rect.left = self.rect.left - self.velocidad
			if self.rect.left < self.limiteIzquierda: #limite izq
				self.derecha = True


	def __ataque(self):
		if (randint(0,10000)<self.rangoDisparo):
			self.__disparo()

	def __disparo(self):
		x,y = self.rect.center
		miProyectil = Proyectil.Proyectil(x,y, "Imagenes/disparob.jpg",False)
		self.listaDisparo.append(miProyectil)

