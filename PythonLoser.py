import turtle as t
import playsound
from time import sleep

def Lose():
    Loser = t.Screen()
    playsound.playsound('SoundLossing.mp3', block=False)
    Loser.title("Game Over")
    Loser.setup(1920, 1080)
    Loser.bgpic("BgrLoser.gif")

    WSP = t.Turtle()
    WSP.speed(0)
    WSP.hideturtle()
    sleep(7)
    exit()
    Loser.mainloop()
