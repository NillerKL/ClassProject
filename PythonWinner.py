import turtle as t
import playsound
from time import sleep

def Win(Tekst):
    Winner = t.Screen()
    playsound.playsound('SoundWinning.mp3', block=False)
    Winner.title("Winner")
    Winner.setup(1920, 1080)
    Winner.bgpic("BgrWinner.gif")

    Teksten = t.Turtle()
    Teksten.penup()
    Teksten.hideturtle()
    Teksten.speed(0)
    Teksten.goto(0,-300)
    Teksten.color("White")
    Teksten.write(Tekst, font=("Verdana",30, "normal"), align="center")
    sleep(6)
    exit()

    Winner.mainloop()

