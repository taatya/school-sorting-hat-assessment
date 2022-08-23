import pygame
from sys import exit


# Written by Taatya

gold=(255, 215, 0)

home_screen = True

color = (255, 255, 255)

color_light = (170, 170, 170)

color_dark = (100, 100, 100)

pygame.mixer.init()
pygame.mixer.music.load("harry_potter_loop.mp3")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1)

pygame.font.init()
font = pygame.font.Font('HARRYP__.ttf', 35)
bigFont = pygame.font.Font('HARRYP__.ttf', 50)
smallFont = pygame.font.Font('HARRYP__.ttf', 29)


screenWidth = 800
screenHeight = 400

pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Testing Pygame For Fun")
clock = pygame.time.Clock()

home_screen = True

# create a text surface object,
# on which text is drawn on it.
text = bigFont.render('Sorting Hat Quiz', True, gold)

# Body
body2 = font.render('Are  you  a  brave  Gryffindor?   Are  you  an  intelligent  Ravenclaw?', True, gold)
body3 = font.render('An  emphatatic  Hufflepuff?      Are you an ambitious Slytherin?', True, gold)
body4 = font.render('Take  this  quiz  to  find  out! ', True, gold)

# create a rectangular object for the
# text surface object
textRect = text.get_rect()
body2Rect = body2.get_rect()
body3Rect = body3.get_rect()
body4Rect = body4.get_rect()

# set the center of the rectangular object.
textRect.center = (screenWidth // 2, screenHeight // 10)
body2Rect.center = (screenWidth // 2, screenHeight // 3.5)
body3Rect.center = (screenWidth // 2, screenHeight // 2.5)
body4Rect.center = (screenWidth // 2, screenHeight // 2)



# Simple logic code

mouse = pygame.mouse.get_pos()

global gpoints, hpoints, rpoints, spoints
gpoints = 0
hpoints = 0
rpoints = 0
spoints = 0

buttonPadding = 5

class Option:
    def __init__(self, text, gp, hp, rp, sp):
        self.text = text
        self.hp = hp
        self.rp = rp
        self.gp = gp
        self.sp = sp

    def selected(self):
        global gpoints, spoints, rpoints, hpoints
        gpoints += self.gp
        spoints += self.sp
        rpoints += self.rp
        hpoints += self.hp


buttons = pygame.sprite.Group()
class Button(pygame.sprite.Sprite):
    def __init__(self, corrOp, w, h, screen, position, text, size, colors="white on blue"):
        super().__init__()
        self.corrOp = corrOp
        self.colors = colors
        self.fg, self.bg = self.colors.split(" on ")
        self.font = font
        self.text_render = self.font.render(text, 1, self.fg)
        self.image = self.text_render
        # self.x, self.y, self.w , self.h = self.text_render.get_rect()
        self.w = w
        self.h = h
        self.x, self.y = position
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.position = position
        self.update()
        buttons.add(self)

    def update(self):
        global l1, l2, l3, l4, f
        self.fg, self.bg = self.colors.split(" on ")
        l1 = pygame.draw.line(screen, (150, 150, 150), (self.x, self.y), (self.x + self.w , self.y), 5)
        l2 = pygame.draw.line(screen, (150, 150, 150), (self.x, self.y - 2), (self.x, self.y + self.h), 5)
        l3 = pygame.draw.line(screen, (50, 50, 50), (self.x, self.y + self.h), (self.x + self.w , self.y + self.h), 5)
        l4 = pygame.draw.line(screen, (50, 50, 50), (self.x + self.w , self.y + self.h), [self.x + self.w , self.y], 5)
        f = pygame.draw.rect(screen, self.bg, (self.x, self.y, self.w , self.h))
        screen.blit(self.text_render, self.position)

        # self.rect = screen, position, text, size, colors="white on blue"screen.blit(self.text_render, (self.x, self.y))

    def selected(self):
        bg = pygame.Surface((screenWidth-100, screenHeight-100))
        textCover = pygame.Surface((screenWidth, 100))
        screen.blit(bg, (0, 0))
        screen.blit(textCover, (0, 0))
        self.corrOp.selected()

quitOp = Option('Quit', 0, 0, 0, 0)
quit = Button(quitOp, 60, 30, screen, (screenWidth-70, screenHeight-40), "Quit", 20, "black on white")

nullOp = Option('', 0, 0, 0, 0)

class Question:
    def __init__(self, question, options, done):
        self.bList = []
        self.options = options
        self.done = done
        self.oLen = len(self.options)
        self.question = question


    def drawScene(self):
        screen.fill((0, 0, 0))
        quit = Button(quitOp, 60, 30, screen, (screenWidth - 70, screenHeight - 40), "Quit", 20, "black on white")
        question_render = bigFont.render(self.question, 1, gold)
        screen.blit(question_render, (0, 20))
        buttonSize = screenWidth/self.oLen
        buttonSize -= buttonPadding*2
        opNum = 0
        padNum = 1
        self.bList = []
        for i in self.options:
            option = Button(i, buttonSize-buttonPadding*2, 70, screen, (int((buttonPadding*padNum*2)+(buttonSize*opNum)),screenHeight/2), i.text, 20, "black on white")
            self.bList.append(option)
            opNum += 1
            padNum += 1

    def delete(self):
        for i in self.bList:
            i.corrOp = nullOp

    def Selection(self):
        option.selected()
        self.done = True

startFont = pygame.font.Font("HARRYP__.ttf", 200)
startText = startFont.render("Start!", True, gold)
start = Button(nullOp, 60, 30, screen, (screenWidth/2-20, screenHeight/2+50), 'Start!', 900, "gold on black")


questions = []
q1 = Question("How would your friends best describe you?", [Option('Loyal', 10, 20, 5, 5), Option('Funny', 20, 20, 15, 15), Option('Brave', 30, 15, 15, 25), Option('Lazy', 10, 5, 10, 30)], False)
questions.append(q1)
q2 = Question("Someone is in danger, what do you do? ", [Option('Walk away', 5, 30, 25, 30), Option('Help them', 30, 15, 20, 20), Option('Call other to help them', 5, 15, 15, 15)], False)
questions.append(q2)
q3 = Question("In a fight, do you defend or attack?", [Option("Defend", 15, 10, 10, 20), Option("Attack", 20, 10, 10, 10)], False)
questions.append(q3)
q4 = Question("What would you never like to be called?", [Option("Ignorant", 10, 10, 30, 20), Option("Cowardly", 30, 10, 10, 20), Option("Selfish", 20, 30, 10, 10), Option("Ordinary", 20, 10, 10, 30)], False)
questions.append(q4)
q5 = Question("What would you most want to study at hogwarts?", [Option("Everything", 20, 10, 30, 10), Option("Magical Creatures", 20, 30, 10, 10), Option("Hexes", 20, 10, 10, 30), Option("School Secrets", 20, 10, 20, 20)], False)
questions.append(q5)
q6 = Question("What are you most afraid of?", [Option("Heights", 10, 20, 20, 10), Option("A Dark Room", 10, 20, 20, 10), Option("Nightmares", 10, 20, 10, 20)], False)
questions.append(q6)


def display_results():
    screen.fill((0, 0, 0))
    points = (gpoints, hpoints, spoints, rpoints)
    if gpoints == max(points):
        win_text = bigFont.render("You are a Gryffindor!", True, gold)
    if rpoints == max(points):
        win_text = bigFont.render("You are a Ravenclaw!", True, gold)
    if spoints == max(points):
        win_text = bigFont.render("You are a Slytherin!", True, gold)
    if hpoints == max(points):
        win_text = bigFont.render("You are a Hufflepuff!", True, gold)
    text_rect = win_text.get_rect(center=(screenWidth / 2, screenHeight / 2))
    screen.blit(win_text, text_rect)



while True:
    clock.tick(60)

    if home_screen:
        screen.blit(text, textRect)
        screen.blit(body2, body2Rect)
        screen.blit(body3, body3Rect)
        screen.blit(body4, body4Rect)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for q in questions:
                for option in q.bList:
                    if option.rect.collidepoint(pygame.mouse.get_pos()):
                        q.Selection()

            if start.rect.collidepoint(pygame.mouse.get_pos()):
                home_screen = False
                screen.fill((0, 0, 0))
                q1.drawScene()

            if quit.rect.collidepoint(pygame.mouse.get_pos()):
                exit()
    if q1.done:
        q1.delete()
        q2.drawScene()
    if q2.done:
        q2.delete()
        q3.drawScene()
    if q3.done:
        q3.delete()
        q4.drawScene()
    if q4.done:
        q4.delete()
        q5.drawScene()
    if q5.done:
        q5.delete()
        q6.drawScene()
    if q6.done:
        q6.delete()
        display_results()
        quit = Button(quitOp, 60, 30, screen, (screenWidth - 70, screenHeight - 40), "Quit", 20, "black on white")



    pygame.display.update()

