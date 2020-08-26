#Importa Librerie
import pygame 
from pygame.locals import *
import random
import copy
import sys
import ctypes

#Carica immagini
icona = pygame.image.load('resources/icon.png')
retrocarta = pygame.image.load('resources/cards/cardback.png')
quadriA = pygame.image.load('resources/cards/ad.png')
fioriA = pygame.image.load('resources/cards/ac.png')
cuoriA = pygame.image.load('resources/cards/ah.png')
piccheA = pygame.image.load('resources/cards/as.png')
quadri2 = pygame.image.load('resources/cards/2d.png')
fiori2 = pygame.image.load('resources/cards/2c.png')
cuori2 = pygame.image.load('resources/cards/2h.png')
picche2 = pygame.image.load('resources/cards/2s.png')
quadri3 = pygame.image.load('resources/cards/3d.png')
fiori3 = pygame.image.load('resources/cards/3c.png')
cuori3 = pygame.image.load('resources/cards/3h.png')
picche3 = pygame.image.load('resources/cards/3s.png')
quadri4 = pygame.image.load('resources/cards/4d.png')
fiori4 = pygame.image.load('resources/cards/4c.png')
cuori4 = pygame.image.load('resources/cards/4h.png')
picche4 = pygame.image.load('resources/cards/4s.png')
quadri5 = pygame.image.load('resources/cards/5d.png')
fiori5 = pygame.image.load('resources/cards/5c.png')
cuori5 = pygame.image.load('resources/cards/5h.png')
picche5 = pygame.image.load('resources/cards/5s.png')
quadri6 = pygame.image.load('resources/cards/6d.png')
fiori6 = pygame.image.load('resources/cards/6c.png')
cuori6 = pygame.image.load('resources/cards/6h.png')
picche6 = pygame.image.load('resources/cards/6s.png')
quadri7 = pygame.image.load('resources/cards/7d.png')
fiori7 = pygame.image.load('resources/cards/7c.png')
cuori7 = pygame.image.load('resources/cards/7h.png')
picche7 = pygame.image.load('resources/cards/7s.png')
quadri8 = pygame.image.load('resources/cards/8d.png')
fiori8 = pygame.image.load('resources/cards/8c.png')
cuori8 = pygame.image.load('resources/cards/8h.png')
picche8 = pygame.image.load('resources/cards/8s.png')
quadri9 = pygame.image.load('resources/cards/9d.png')
fiori9 = pygame.image.load('resources/cards/9c.png')
cuori9 = pygame.image.load('resources/cards/9h.png')
picche9 = pygame.image.load('resources/cards/9s.png')
quadri10 = pygame.image.load('resources/cards/10d.png')
fiori10 = pygame.image.load('resources/cards/10c.png')
cuori10 = pygame.image.load('resources/cards/10h.png')
picche10 = pygame.image.load('resources/cards/10s.png')
quadriJ = pygame.image.load('resources/cards/jd.png')
fioriJ = pygame.image.load('resources/cards/jc.png')
cuoriJ = pygame.image.load('resources/cards/jh.png')
piccheJ = pygame.image.load('resources/cards/js.png')
quadriQ = pygame.image.load('resources/cards/qd.png')
fioriQ = pygame.image.load('resources/cards/qc.png')
cuoriQ = pygame.image.load('resources/cards/qh.png')
piccheQ = pygame.image.load('resources/cards/qs.png')
quadriK = pygame.image.load('resources/cards/kd.png')
fioriK = pygame.image.load('resources/cards/kc.png')
cuoriK = pygame.image.load('resources/cards/kh.png')
piccheK = pygame.image.load('resources/cards/ks.png')

pygame.display.set_icon(icona)
nero = (0,0,0)
bianco = (255,255,255)
grigio = (192,192,192)

carte = [ quadriA, fioriA, cuoriA, piccheA, \
          quadri2, fiori2, cuori2, picche2, \
          quadri3, fiori3, cuori3, picche3, \
          quadri4, fiori4, cuori4, picche4, \
          quadri5, fiori5, cuori5, picche5, \
          quadri6, fiori6, cuori6, picche6, \
          quadri7, fiori7, cuori7, picche7, \
          quadri8, fiori8, cuori8, picche8, \
          quadri9, fiori9, cuori9, picche9, \
          quadri10, fiori10, cuori10, picche10, \
          quadriJ, fioriJ, cuoriJ, piccheJ, \
          quadriQ, fioriQ, cuoriQ, piccheQ, \
          quadriK, fioriK, cuoriK, piccheK ]
assi = [ quadriA, fioriA, cuoriA, piccheA ]
due = [ quadri2, fiori2, cuori2, picche2 ]
tre = [ quadri3, fiori3, cuori3, picche3 ]
quattro = [ quadri4, fiori4, cuori4, picche4 ]
cinque = [ quadri5, fiori5, cuori5, picche5 ]
sei = [ quadri6, fiori6, cuori6, picche6 ]
sette = [ quadri7, fiori7, cuori7, picche7 ]
otto = [ quadri8, fiori8, cuori8, picche8 ]
nove = [ quadri9, fiori9, cuori9, picche9 ]
dieci = [ quadri10, fiori10, cuori10, picche10, \
            quadriJ, fioriJ, cuoriJ, piccheJ, \
            quadriQ, fioriQ, cuoriQ, piccheQ, \
            quadriK, fioriK, cuoriK, piccheK ]


