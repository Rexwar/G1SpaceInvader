import sys, pygame, math
from pygame.locals import *
from . import Proyectil

class naveEspacial(pygame.sprite.Sprite):
	"""Clase para las naves"""

	def __init__(self,ancho,alto):
		pygame.sprite.Sprite.__init__(self)
		self.ImagenNave = pygame.image.load("Imagenes/nave.jpg")
		self.ImagenExplosion = pygame.image.load("Imagenes/explosion.jpg")

		self.rect = self.ImagenNave.get_rect()
		self.rect.centerx = ancho/2
		self.rect.centery = alto-30

		self.listaDisparo=[]
		self.Vida = True

		self.velocidad = 20
		self.enPausa = False
		self.sonidoDisparo = pygame.mixer.Sound("Sonidos/shoot2.wav")
		#self.sonidoExplosion = pygame.mixer
	def pausa(self,Pausa):
		self.enPausa = Pausa
		
	def movimientoDerecha(self):
		if not self.enPausa:
			self.rect.right +=self.velocidad
			self.__movimiento()

	def movimientoIzquierda(self):
		if not self.enPausa:
			self.rect.left -= self.velocidad
			self.__movimiento()

	def __movimiento(self):
		if self.Vida == True:
			if self.rect.left <=0:
				self.rect.left =0
			elif self.rect.right > 900:
				self.rect.right = 900

	def disparar(self, x,y):
		if not self.enPausa:
			miProyectil = Proyectil.Proyectil(x,y,"imagenes/disparoa.jpg", True)
			self.listaDisparo.append(miProyectil)
			self.sonidoDisparo.play()

	def destruccion(self):
		#self.sonidoExplosion.play()
		self.vida = False
		self.velocidad = 0
		self.ImagenNave = self.ImagenExplosion

	def dibujar(self, superficie):
		superficie.blit(self.ImagenNave,self.rect)
		
	def reiniciar(self):
		self.vida = True
		self.velocidad = 20
		self.ImagenNave = pygame.image.load("Imagenes/nave.jpg")
