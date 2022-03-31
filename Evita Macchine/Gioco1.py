import pygame,sys,random,time                   #importo librerie
from pygame.locals import *
from datetime import datetime

pygame.init()                                   #inizializzo pygame
pygame.display.set_caption("GIOCO LORENZO AMICI")
pygame.mixer.init()

#Definizione tempo
FPS = 60
FramePerSec = pygame.time.Clock()

#Definizione variabili
altezza = 600                                     #altezza schermo
larghezza = 400                                   #larghezza schermo
velocita = 7                                      #velocità nemici
Velocita = 5                                      #velocità player
Record = open(r"Record.txt","r")
record = Record.read()
Record.close()                                              
punteggio = 0
posizione_colore = 0
l_caricamento = 1                                 #lunghezza rettangolo caricamento

#Definizione font
font = pygame.font.SysFont("Verdana", 60)
font_medio = pygame.font.SysFont("Verdana", 35)
font_piccolo = pygame.font.SysFont("Verdana",20)
font1 = pygame.font.SysFont("Verdana",14)                                                     #verde

#Testi
text = ''
nemici = ''
lista_nemici = ["Rossa","Blu","Gialla","Viola"]
amici = ''
error = font_medio.render("ERRORE",True,(0,0,0))
error1 = font_piccolo.render("Non hai selezionato",True,(0,0,0))
error2 = font_piccolo.render("il colore della tua macchina",True,(0,0,0))
error3 = font_piccolo.render("Premi un tasto qualunque",True,(0,0,0))
condizione1 = font1.render("Se vuoi chiudere il gioco fai clic con il mouse",True,(255,255,255))
condizione2 = font1.render("Se vuoi ritornare alla home premi un tasto", True, (255,255,255))
condizione3 = font1.render("qualunque sulla tastiera", True, (255,255,255))

#Immagini
Pausa = pygame.image.load("Pausa.png")
pausa = pygame.Rect(345,10,45,45)
Destra = pygame.Rect(200,0,200,600)
Sinistra = pygame.Rect(0,0,200,600)
Resume = pygame.image.load("Resume.png")
resume = pygame.Rect(125,225,150,150)
Game_Over = pygame.image.load("GameOver.png")
box_reinizio = pygame.Rect(20, 293, 357, 71)
box_uscita = pygame.Rect(22,422,353,70)
box_regole = pygame.Rect(37, 222, 323, 86)
box_gioco = pygame.Rect(42, 379, 316, 81)
rosso = pygame.Rect(80,287,71,111)
blu = pygame.Rect(78,157,71,111)
giallo = pygame.Rect(255,152,71,111)
viola = pygame.Rect(255,286,71,111)
Errore = pygame.Rect(19,250,360,125)
sfondo = pygame.image.load("Sfondo.png")
caricamento = pygame.image.load("Caricamento.png")
DisplaySurf = pygame.display.set_mode((larghezza,altezza))
DisplaySurf.fill((255,255,255))
Prima = pygame.image.load("Prima.png")                          #prima schermata
Seconda = pygame.image.load("Seconda.png")                      #seconda schermata
regole = pygame.image.load('RegoleDelGioco.png')
x = 10000
y = 10000
attivo = True

#Definizione funzione uscita
def uscita(event):
    key_pressed = pygame.key.get_pressed()
    if event.type == QUIT or key_pressed[K_ESCAPE]:
        pygame.quit()
        sys.exit()
        Record.close()

#Definizione della funzione che crea le istanze
def crea_istanze():
    global E1
    E1 = Enemy()
    global P1
    P1 = Player()
    global B1
    B1 = Bonus()

    global all_sprites
    global bonus
    global enemies
    bonus = pygame.sprite.Group()
    bonus.add(B1)
    enemies = pygame.sprite.Group()
    enemies.add(E1)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(P1)
    all_sprites.add(E1)

    global INC_SPEED
    global bonus_speed
    INC_SPEED = pygame.USEREVENT + 1                            #ogni 8 secondi la velocità aumenta
    pygame.time.set_timer(INC_SPEED, 8300)
    bonus_speed = pygame.USEREVENT
    pygame.time.set_timer(bonus_speed,random.randint(20000,40000))


def prima():
    DisplaySurf.blit(Prima,(0,0))
    global attivo
    attivo = True
    while attivo:
        global y
        global x
        global colore
        global amici
        global nemici
        global lista_nemici
        for event in pygame.event.get():                    
            uscita(event)                                        #uscire dal gioco
            if event.type == pygame.MOUSEBUTTONDOWN:            #se schiaccio il mouse
                DisplaySurf.blit(Prima,(0,0))
                if rosso.collidepoint(event.pos):
                    x = 80
                    y = 287
                    amici = "Rossa"
                    lista_nemici.remove(amici)
                    nemici = random.choice(lista_nemici)
                    lista_nemici.insert(0,amici)
                if blu.collidepoint(event.pos):
                    x = 78
                    y = 153
                    amici = "Blu"
                    lista_nemici.remove(amici)
                    nemici = random.choice(lista_nemici)
                    lista_nemici.insert(1,amici)
                if giallo.collidepoint(event.pos):
                    x = 255
                    y = 152
                    amici = "Gialla"
                    lista_nemici.remove(amici)
                    nemici = random.choice(lista_nemici)
                    lista_nemici.insert(2,amici)
                if viola.collidepoint(event.pos):
                    x = 255
                    y = 286
                    amici = "Viola"
                    lista_nemici.remove(amici)
                    nemici = random.choice(lista_nemici)
                    lista_nemici.insert(3,amici)
                if viola.collidepoint(event.pos) == False and giallo.collidepoint(event.pos) == False and rosso.collidepoint(event.pos) == False and blu.collidepoint(event.pos) == False:
                    attivo = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    attivo = False
        
        colore = pygame.Rect(x, y, 71, 111)
        pygame.draw.rect(DisplaySurf, (255,255,255), colore, 2)
        pygame.display.update()

#Definizione del ciclo di gioco
def ciclo():
        DisplaySurf.blit(Seconda,(0,0))
        pygame.display.update()                                 #disegno la seconda schermata
        while True:
            pressed_keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                uscita(event)
            
                if event.type == pygame.MOUSEBUTTONDOWN:            #se premo il mouse
                    if box_regole.collidepoint(event.pos):
                        DisplaySurf.blit(regole, (0,0))
                        pygame.display.update()
                        time.sleep(1)
                        while True:
                            for event in pygame.event.get():
                                uscita(event)
                                    
                                if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:               #se premo un tasto qualunque
                                    ciclo()
                              
                    if box_gioco.collidepoint(event.pos):               #quando colpisco una macchina
                        time.sleep(0.5)
                        global orario
                        global orario_bonus
                        global n
                        n = 2
                        orario = (datetime.now().microsecond + datetime.now().second * 1000000 + datetime.now().minute * 60000000 + datetime.now().hour *3600000000)//1000000
                        orario_bonus = random.randint(orario+20, orario+20 + n)
                        crea_istanze()
                        global y_sfondo
                        y_sfondo = -600
                        gioco()
                
#Definzione Gioco
def gioco():
    pygame.mixer.music.load("MusicaGioco.mp3")
    pygame.mixer.music.play(-1)
    global orario_bonus
    global inizio
    global y_sfondo
    global n
    global cerchio 
    global velocita
    global Velocita
    global attivo
    global start
    global end
    inizio = 0
    start = 0
    end = 0
    attivo = False
    cerchio = False
    while True:
        if y_sfondo == 0:
            y_sfondo = -600

        DisplaySurf.blit(sfondo,(0,y_sfondo))
        DisplaySurf.blit(Pausa,(345,10))
        Punteggio = font_piccolo.render("Punteggio : " + str(punteggio), True, (0,0,0))
        Record = font_piccolo.render("Record : " + str(record), True, (0,0,0))
        DisplaySurf.blit(Punteggio, (10,10))
        DisplaySurf.blit(Record, (10,40))               #disegno record, punteggio
        #chiamo la funzione move di ogni istanza delle classi
        try:
            for personaggio in all_sprites:
                DisplaySurf.blit(personaggio.image, personaggio.rect)
                personaggio.move()
        except AttributeError:
            pass
           
        if attivo:
            DisplaySurf.blit(B1.image, B1.rect)
            B1.move(velocita)
                   
        for event in pygame.event.get():
            uscita(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pausa.collidepoint(event.pos):
                    end = 0
                    start = 0
                    start = datetime.now().microsecond + datetime.now().second * 1000000 + datetime.now().minute * 60000000 + datetime.now().hour *3600000000
                    pygame.mixer.music.stop()
                    while True:
                        DisplaySurf.blit(Resume, (125,225))
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if resume.collidepoint(event.pos):
                                    end = datetime.now().microsecond + datetime.now().second * 1000000 + datetime.now().minute * 60000000 + datetime.now().hour *3600000000
                                    pygame.mixer.music.load("MusicaGioco.mp3")
                                    pygame.mixer.music.play(-1)
                                    break
                            uscita(event)
                        if end > 0:
                            break
            elif event.type == INC_SPEED:
                velocita += 1

            elif event.type == bonus_speed:
                attivo = True
                
                            

        if pygame.sprite.spritecollideany(P1, bonus):
            inizio = int(time.strftime("%H"))*3600 + int(time.strftime("%M"))*60 + int(time.strftime("%S"))            
            Velocita = 10
            B1.move(100)
            cerchio = True

        if cerchio:
            pygame.draw.circle(DisplaySurf,(0,0,255),(370,250),20)

        if  int(time.strftime("%H"))*3600 + int(time.strftime("%M"))*60 + int(time.strftime("%S"))- (end-start)//1000000 == inizio + 8:
            Velocita = 5
            cerchio = False
        
            
        if pygame.sprite.spritecollideany(P1, enemies):             #se due istanze si scontrano
            pygame.mixer.music.stop()
            pygame.mixer.music.load("Crash.mp3")
            pygame.mixer.music.play(1)
            DisplaySurf.blit(Game_Over, (0,0))
            Punteggio_1 = font_medio.render(f"{punteggio}", True, (255,255,255))
            Record_1 = font_medio.render(f"{record}", True, (255,255,255))
            DisplaySurf.blit(Punteggio_1, (281,160))
            DisplaySurf.blit(Record_1, (240,207))
            Velocita = 5

            
            pygame.display.update()

            E1.punt()
            for entity in all_sprites:                          #eliminare istanze scontrate
                entity.kill()
            while True:
                for event in pygame.event.get():
                    uscita(event)
                
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if box_reinizio.collidepoint(event.pos):
                            velocita = 7
                            prima()
                            ciclo()
                        if box_uscita.collidepoint(event.pos):
                            E1.punt()
                            pygame.quit()
                            sys.exit() 
        y_sfondo += 2
        pygame.display.update()                     # si muove la strada
        FramePerSec.tick(FPS)                       # FPS per far andare il ciclo a una velocita costante

#Classe dei nemici        
class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        global centro_nemico
        if amici in lista_nemici:                               #gestione errore della scelta del colore dell'utente
            self.image = pygame.image.load("Macchina"+nemici+"1.png")
        else:
            pygame.draw.rect(DisplaySurf,(255,0,0),Errore)
            DisplaySurf.blit(error, (125,248))                  #visualizzazione errore
            DisplaySurf.blit(error1, (80,285))
            DisplaySurf.blit(error2, (60,310))
            DisplaySurf.blit(error3, (65,335))
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                        prima()
                        ciclo()
                        break
                 
        self.surf = pygame.Surface((44,86))
        self.rect = self.surf.get_rect(center = (100,0))
        centro_nemico = list(self.rect.center)                    
    def move(self):                                             #definizione movimento nemico
        self.rect.move_ip(0,velocita)
        if (self.rect.top > altezza):
            self.rect.bottom = 0
            self.rect.center = (random.randint(20,larghezza-20),0)
            global punteggio                                    #cambio del punteggio
            punteggio += 1
    def punt(self):                                             #quando si perde gestione di record e punteggio
            global punteggio
            global record
            if punteggio > int(record):
                Record = open(r"Record.txt","w")
                Record.write(str(punteggio))
                Record.close()
                Record = open(r"Record.txt","r")
                record = Record.read()
                Record.close()
            punteggio = 0

#Classe degli amici            
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        if amici in lista_nemici:
            self.image = pygame.image.load("Macchina"+amici+".png")
        self.surf = pygame.Surface((44,86))
        self.rect = self.surf.get_rect(center = (int(larghezza/2),altezza - 55))

    def move(self):
        mouse_pressed = pygame.mouse.get_pressed()
        key_pressed = pygame.key.get_pressed()
        if self.rect.left > -20:
            FPS = 100
            if (mouse_pressed[0] and Sinistra.collidepoint(pygame.mouse.get_pos())) or key_pressed[K_LEFT]:
                self.image = pygame.image.load("Macchina"+amici+"Sinistra.png")
                self.rect.move_ip(-Velocita,0)
            elif (mouse_pressed[0] and Destra.collidepoint(pygame.mouse.get_pos())) or key_pressed[K_RIGHT]:
                pass
            else:
                self.image = pygame.image.load("Macchina"+amici+".png")
                FPS = 60
        if self.rect.right < larghezza + 20:
            FPS = 100
            if (mouse_pressed[0] and Destra.collidepoint(pygame.mouse.get_pos())) or key_pressed[K_RIGHT]:
                self.image = pygame.image.load("Macchina"+amici+"Destra.png")
                self.rect.move_ip(Velocita,0)
            elif (mouse_pressed[0] and Sinistra.collidepoint(pygame.mouse.get_pos())) or key_pressed[K_LEFT]:
                pass
            else:
                self.image = pygame.image.load("Macchina"+amici+".png")
                FPS = 60

class Bonus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        global centro_bonus
        global centro
        self.image = pygame.image.load("Bonus.png")
        self.surf = pygame.Surface((39,48))
        centro = (random.randint(20,larghezza-20), -25)
        while True:
            centro_bonus = list(centro)
            if centro_bonus[0] in range(centro_nemico[0] - 23, centro_nemico[0] + 23) and centro_bonus[1] in range(centro_nemico[1] - 40, centro_nemico[1] +40):
                centro = (random.randint(20,larghezza-20), centro_nemico[1]-40)
            else:
                break
        self.rect = self.surf.get_rect(center = centro)

    def move(self,velocita):
        global attivo
        global orario_bonus
        global centro_bonus
        self.rect.move_ip(0,velocita)
        if self.rect.top > altezza:
            pygame.time.set_timer(bonus_speed,random.randint(10000,30000))
            self.rect.center = (random.randint(20,larghezza-20), -25)
            while True:
                centro_bonus = list(self.rect.center)
                if centro_bonus[0] in range(centro_nemico[0] - 27, centro_nemico[0] + 27) and centro_bonus[1] in range(centro_nemico[1] - 40, centro_nemico[1] +40):
                    self.rect.center = (random.randint(20,larghezza-20), centro_nemico[1]-40)
                else:
                    break
            attivo = False


#Chiamata delle funzioni
DisplaySurf.blit(caricamento,(0,0))
for i in range(330):                                            #movimento della barra di caricamento
    box_caricamento = pygame.Rect(30,160,l_caricamento,30) 
    pygame.draw.rect(DisplaySurf, (0,0,0), box_caricamento)
    pygame.display.update()
    l_caricamento += 1
    time.sleep(0.008)

prima()

ciclo()
            

