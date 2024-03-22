import turtle
import random
import time
class Turtle():
    turtles=[]
    def __init__(self,shape,color,left,set_pos):
        self.shape=shape
        self.color=color
        self.left=left
        self.set_pos=set_pos

    def create_turtle(self):
        turt=turtle.Turtle()
        turt.shape(self.shape)
        turt.color(self.color)
        turt.left(self.left)
        turt.penup()
        turt.setpos(self.set_pos)
        turt.pendown()
        Turtle.turtles.append(turt)

    def move_turtle(self):
        while True:
            for turt in Turtle.turtles:
                move=random.randint(1,20)
                turt.forward(move)
                x,y=turt.pos()
                if y>=HEIGHT//2+10:
                    color=turt.color()
                    return color


WIDTH,HEIGHT=500,500
COLORS=['yellow','red','green','orange','cyan','purple','black','blue','brown','pink']
def get_number_of_racers():
    while True:
        racers=input("Enter Number of racers you want to run:")
        if racers.isdigit():
            racers=int(racers)

        else:
            print("Enter a number ...Try Again!")
            continue

        if 2<=racers<=10:
            return racers
        else:
            print("Enter a number between (2-10)")

def intialize_turtle():
    screen=turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle Racing")
racers = get_number_of_racers()
random.shuffle(COLORS)
colors=COLORS[:racers]
x=WIDTH//(racers+1)

for i in range(racers):
    racer=Turtle('turtle',colors[i],90,(x*(i+1)-WIDTH//2,-HEIGHT//2+10))
    racer.create_turtle()
winner=racer.move_turtle()
time.sleep(2)
print(f'The winner is {winner[0]}')



