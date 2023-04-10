#Importere alle vores Libaries
import time
import random
import turtle as t
from pygame import mixer
import playsound
from PythonWinner import Win
from PythonLoser import Lose


#Alle vores globale variabler (Ved Jonas bliver mega glad)
global Fightings
global Hero
global Character
global Enemy
global Pen
global xPos
global yPos
global EnemyMonster

xPos = -87
yPos = -310

#Starter tid til timer
StartTiden = time.time()


def Main():
    mixer.init()
    mixer.music.load('SoundAmbient.mp3')
    mixer.music.play()


    #En funktion der tjekker om spilleren er nået til en bestemt potition
    def TjekVinder():
        x = Character.xcor()
        y = Character.ycor()

        if x < -296 and x > -300:
            if y < -98 and y > -100:
                mixer.music.stop()
                Character.hideturtle()
                SlutTiden = time.time()
                Tiden = SlutTiden-StartTiden
                Tiden = round(Tiden)
                WinnerTekst = ("Du gjorde det på " + str(Tiden)+ " sekunder")
                Win(WinnerTekst)




    #Funktion til at få potition
    def GetPos():
        print(Character.xcor())
        print(Character.ycor())

    #Chance for at møde monster
    def Incounter():
        IncounterValue = random.randint(1,4)
        if IncounterValue == 4:
            Fight()

    Rækkefølgen = ["w", "w", "d", "d", "d", "d", "d", "w", "w", "a", "w", "w", "a", "a", "s", "s", "a", "a", "w", "w",
                   "a", "a", "s", "s", "a", "s", "s", "d"]

    def Rækkefølge(Input):
        global xPos
        global yPos
        if Input == Rækkefølgen[0]:
            Rækkefølgen.pop(0)
            Character.forward(105)
            xPos = Character.xcor()
            yPos = Character.ycor()

            TjekVinder()
            Character.hideturtle()
            Incounter()
            Character.showturtle()
        else:
            pass

    def RækkefølgeS(Input):
        global xPos
        global yPos
        if Input == Rækkefølgen[0]:
            Rækkefølgen.pop(0)
            Character.forward(-105)
            xPos = Character.xcor()
            yPos = Character.ycor()

            TjekVinder()
            Character.hideturtle()
            Incounter()
            Character.showturtle()
        else:
            pass


    #Laver funktioner for bevægelser
    def Op():
        global xPos
        global yPos
        VoresInput = "w"
        Rækkefølge(VoresInput)

    def Ned():
        global xPos
        global yPos
        VoresInput = "s"
        RækkefølgeS(VoresInput)

    def Venstre():
        global xPos
        global yPos
        VoresInput = "a"
        Character.left(90)
        Rækkefølge(VoresInput)
        Character.right(90)

    def Højre():
        global xPos
        global yPos
        VoresInput = "d"
        Character.right(90)
        Rækkefølge(VoresInput)
        Character.left(90)

    #Laver en Class for vores monstre
    class Monster:
        def __init__(self):
            self.type = random.randint(1,3)

        def GetType(self):
            if self.type == 1:
                print("Monster is a Fire-Element")
                return(1)
            elif self.type == 2:
                print("Monster is a Water-Element")
                return (2)
            elif self.type == 3:
                print("Monster is a Grass-Element")
                return (3)
            else:
                print("WTF is that monster")

    #Laver funktion til at lave knapper
    def MakeButton(x,y,Color,Type):
        global Pen
        Pen = t.Turtle()
        Pen.speed(0)
        Pen.hideturtle()
        Pen.penup()
        Pen.goto(x, y)
        Pen.color("White")

        for i in range(2):
            Pen.fillcolor(Color)
            Pen.begin_fill()
            Pen.pendown()
            Pen.forward(200)
            Pen.left(90)
            Pen.forward(70)
            Pen.left(90)
            Pen.end_fill()
            Pen.penup()
        Pen.goto((x+100,y+15))
        Pen.write(Type, font=("Verdana",30, "normal"), align="center")

    #Funktion der giver grafisk, ift hvilket monster det er.
    def MonsterType():
        global EnemyMonster
        EnemyMonster = Monster()

        if EnemyMonster.type == 1:
            CreateMonster("EnemyFire.gif", "SoundFireElement.mp3")



        elif EnemyMonster.type == 2:
            CreateMonster("EnemyWater.gif", "SoundElementWater.mp3")

        elif EnemyMonster.type == 3:
            CreateMonster("EnemyGrass.gif", "SoundZombie.mp3")

    #Laver vores monster i turtle
    def CreateMonster(Type,Sound):
        global Enemy
        playsound.playsound(Sound, block=False)
        Enemy = t.Turtle()
        Enemy.speed(0)
        Enemy.showturtle()
        Enemy.shape(Type)
        Enemy.penup()
        Enemy.goto(600,-100)

    #De forskellige angreb via knapperne
    def Attacks(x, y):
        global xPos
        global yPos
        if x < -500 and x > -700:
            if y > -500 and y < -430:

                if EnemyMonster.type == 3:
                    playsound.playsound('SoundHero.mp3', block=False)
                    Fightings.clear()
                    Maze()
                else:
                    Fightings.clear()
                    mixer.music.stop()
                    Lose()




        if x > -100 and x < 100:
            if y > -500 and y < -430:

                if EnemyMonster.type == 1:
                    playsound.playsound('SoundHero.mp3', block=False)
                    Fightings.clear()
                    Maze()
                else:
                    Fightings.clear()
                    mixer.music.stop()
                    Lose()



        if x > 500 and x < 700:
            if y > -500 and y < -430:

                if EnemyMonster.type == 2:
                    playsound.playsound('SoundHero.mp3', block=False)
                    Fightings.clear()
                    Maze()
                else:
                    Fightings.clear()
                    mixer.music.stop()
                    Lose()

    def Hello():
        print("Hello")

    #Laver vores Grafiske interface til kampene
    def Fight():
        global Fightings
        Fightings = t.Screen()
        Fightings.setup(1920, 1080)
        Fightings.title("FIGHT!")
        Fightings.bgpic("BgrFight.gif")
        Fightings.addshape("HeroBig.gif")
        Fightings.addshape("EnemyFire.gif")
        Fightings.addshape("EnemyWater.gif")
        Fightings.addshape("EnemyGrass.gif")

        #Vores Hero
        global Hero
        Hero = t.Turtle()
        Hero.speed(0)
        Hero.showturtle()
        Hero.penup()
        Hero.goto(-600, -100)
        Hero.shape("HeroBig.gif")

        MonsterType()

        #Mere knapper
        MakeButton(-700, -500, "Red", "Fire")
        MakeButton(-100, -500, "Blue", "Water")
        MakeButton(500, -500, "Green", "Grass")

        # Lytter til input
        Fightings.listen()
        Fightings.onscreenclick(Attacks, 1)
        Fightings.onkey(Hello, "w")
        Fightings.onkey(Hello, "s")
        Fightings.onkey(Hello, "a")
        Fightings.onkey(Hello, "d")
        Fightings.mainloop()

    def Maze():
        # Vores Labyrints baggrund
        Maze = t.Screen()
        Maze.title("Mazer Run")
        Maze.setup(1920, 1080)
        Maze.bgpic("BgrMaze.gif")
        Maze.addshape("HeroSmall.gif")

        # Laver vores karakter
        global Character
        Character = t.Turtle()
        Character.penup()
        Character.speed(0)
        Character.goto(-87, -310)
        Character.goto(xPos, yPos)
        Character.shape("HeroSmall.gif")
        Character.left(90)

        # For vores Turtle screen til at lytte og opdatere
        Maze.listen()
        Maze.update()
        Maze.onkey(Op, "w")
        Maze.onkey(Ned, "s")
        Maze.onkey(Venstre, "a")
        Maze.onkey(Højre, "d")
        Maze.onkey(GetPos, "c")

        Maze.mainloop()

    Maze()

Main()