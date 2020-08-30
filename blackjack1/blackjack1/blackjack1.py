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
def somma(carta):
    #Ritorna il totale delle carte.
    if carta in assi:
        return 11
    elif carta in due:
        return 2
    elif carta in tre:
        return 3
    elif carta in quattro:
        return 4
    elif carta in cinque:
        return 5
    elif carta in sei:
        return 6
    elif carta in sette:
        return 7
    elif carta in otto:
        return 8
    elif carta in nove:
        return 9
    elif carta in dieci:
        return 10
    else:
        print ("Errore")
        exit()

def somma2(carta, utenteSomma):
    #Ritorna il totale delle carte.
    if carta in assi:
        valore = 11
        temp = valore + utenteSomma
        if temp > 21:
            return 1
        else:
            return 11
        return 11
    elif carta in due:
        return 2
    elif carta in tre:
        return 3
    elif carta in quattro:
        return 4
    elif carta in cinque:
        return 5
    elif carta in sei:
        return 6
    elif carta in sette:
        return 7
    elif carta in otto:
        return 8
    elif carta in nove:
        return 9
    elif carta in dieci:
        return 10
    else:
        print ("Errore")
        exit()

def generaCarte(mazzo, listagiocatori):
    #Genera una carta dal mazzo, la rimuove da esso, e la aggiunge alla lista giocatori.
    numeroassi = 0
    carta = random.choice(mazzo)
    mazzo.remove(carta)
    listagiocatori.append(carta)
    if carta in assi:
        numeroassi = 1
    return carta, numeroassi

def inizioGioco(mazzo, userlist, dealerlist):
    #Genera due carte per l'avversario e l'utente, una alla volta per ognuno. 
    utenteAssi = 0
    avversarioAssi = 0
    carta1, numeroassi = generaCarte(mazzo, userlist)
    utenteAssi = utenteAssi + numeroassi
    carta2, numeroassi = generaCarte(mazzo, dealerlist)
    avversarioAssi = avversarioAssi + numeroassi
    carta3, numeroassi = generaCarte(mazzo, userlist)
    utenteAssi = utenteAssi + numeroassi
    carta4, numeroassi = generaCarte(mazzo, dealerlist)
    avversarioAssi = avversarioAssi + numeroassi
    return somma(carta1) + somma(carta3), utenteAssi, somma(carta2) + somma(carta4), avversarioAssi

ef main():
    copiacarte = copy.copy(carte)
    stai = False
    partite = 0
    vittorie = 0
    pareggi = 0
    sconfitte = 0
    numerocarteutente = 0
    numerocarteavversario = 0
    utenteCarte = []
    avversarioCarte =[]
    
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("BlackJack")
    font = pygame.font.SysFont('arial', 15)
    cartaTxt = font.render('Carta', 1, nero)
    staiTxt = font.render('Stai', 1, nero)
    rigiocaTxt = font.render('Rigioca', 1, nero)
    haivintoTxt = font.render('Hai vinto!', 1, bianco)
    haipersoTxt = font.render('Hai perso!', 1, bianco)
    pariTxt = font.render('Parità!', 1, bianco)
    infoTxt = font.render('Info', 1, nero)
    utenteSomma, utenteAssi, avversarioSomma, avversarioAssi = inizioGioco(copiacarte, utenteCarte, avversarioCarte)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((80, 150, 15))
    cartaB = pygame.draw.rect(background, grigio, (10, 445, 75, 25))
    staiB = pygame.draw.rect(background, grigio, (95, 445, 75, 25))
    risultatoB = pygame.draw.rect(background, grigio, (555, 375, 75, 75))
    infoB = pygame.draw.rect(background, grigio, (555, 15, 50, 25))

    t = True
    while t:
        gameover = True if (utenteSomma > 21) or len(utenteCarte) == 5 else False
        if utenteSomma == 21 and len(utenteCarte) == 2:
                gameover = True
        elif avversarioSomma == 21 and len(avversarioCarte) == 2:
                gameover = True

        partiteTxt = font.render('Partite: %i' %partite, 1, nero)
        vittorieTxt = font.render('Vittorie: %i' %vittorie, 1, nero)
        pareggiTxt = font.render('Pareggi: %i' %pareggi, 1, nero)
        sconfitteTxt = font.render('Sconfitte: %i' %sconfitte, 1, nero)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                t = False
            elif event.type == pygame.MOUSEBUTTONDOWN and infoB.collidepoint(pygame.mouse.get_pos()):
                ctypes.windll.user32.MessageBoxW(0, "Blackjack è un gioco di carte. \nLo scopo del gioco è pescare carte il più vicino possibile a 21 punti \nsenza andare oltre (se la somma delle carte è maggiore di 21 avrai sballato). \nTutte le figure valgono 10 punti, assi valgono come 1 o 11, \ne tutte le altre carte valgono i loro valori numerici.", "Informazioni", 0)
            elif event.type == pygame.MOUSEBUTTONDOWN and not (stai or gameover) and cartaB.collidepoint(pygame.mouse.get_pos()):
                carta, numeroassi = generaCarte(copiacarte, utenteCarte)
                numerocarteutente = numerocarteutente + 1
                utenteAssi = utenteAssi + numeroassi
                utenteSomma = utenteSomma + somma2(carta, utenteSomma)
                print ('Utente: %i' % utenteSomma)
                while utenteSomma > 21 and utenteAssi > 0:
                    utenteAssi = utenteAssi - 1
                    utenteSomma = utenteSomma - 10
            elif event.type == pygame.MOUSEBUTTONDOWN and not gameover and staiB.collidepoint(pygame.mouse.get_pos()):
                stai = True
                while avversarioSomma <= utenteSomma and avversarioSomma < 17:
                    carta, numeroassi = generaCarte(copiacarte, avversarioCarte)
                    numerocarteavversario = numerocarteavversario + 1
                    avversarioAssi = avversarioAssi + numeroassi
                    avversarioSomma = avversarioSomma + somma2(carta, avversarioSomma)
                    print ('Avversario: %i' % avversarioSomma)
                    while avversarioSomma > 21 and avversarioAssi > 0:
                        avversarioAssi = avversarioAssi - 1
                        avversarioSomma = avversarioSomma - 10
            elif event.type == pygame.MOUSEBUTTONDOWN and (gameover or stai) and rigiocaB.collidepoint(pygame.mouse.get_pos()):
                partite = partite + 1
                if utenteSomma > 21 and avversarioSomma > 21:
                    pass
                elif utenteSomma == avversarioSomma:
                    if numerocarteutente == numerocarteavversario:
                        screen.blit(pariTxt, (270, 200))
                        pareggi = pareggi + 1
                    elif numerocarteutente < numerocarteavversario:
                        screen.blit(haivintoTxt, (270, 200))
                        vittorie = vittorie + 1
                    else:
                        screen.blit(haipersoTxt, (270, 200))
                        sconfitte = sconfitte + 1
                elif utenteSomma <= 21 and avversarioSomma < utenteSomma or avversarioSomma > 21:
                    screen.blit(haivintoTxt, (270, 200))
                    vittorie = vittorie + 1
                elif utenteSomma <= 21 and len(utenteCarte) == 5:
                    screen.blit(haivintoTxt, (270, 200))
                    vittorie = vittorie + 1
                else:
                    screen.blit(haipersoTxt, (270, 200))
                    sconfitte = sconfitte + 1
                gameover = False
                stai = False
                numerocarteutente = 0
                numerocarteavversario = 0
                utenteCarte = []
                avversarioCarte = []
                copiacarte = copy.copy(carte)
                utenteSomma, utenteAssi, avversarioSomma, avversarioAssi = inizioGioco(copiacarte, utenteCarte, avversarioCarte)
                rigiocaB = pygame.draw.rect(background, (80, 150, 15), (270, 225, 75, 25))

