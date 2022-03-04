###################################################### Importing needed libraries  ###########################################################

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox#to show the user their score at the end 
import time#to pause the game
import random#for the starting position of the ball
import asyncio
import os

master = Tk()
master.title('Piball v0.4')
master.resizable(False, False)
master.iconbitmap("galaxy.ico")
master.config(bg="black")


gravity = 0.05



########################################################    Creating a Ball,2 Paddles and Canvas     ###########################################

#Canvas
WIDTH, HEIGHT = 500,750
canvas = Canvas(master, width=WIDTH, height = HEIGHT, bg= "Grey")
canvas.pack(padx=10, pady=10)

#Ball
#ball_x = random.shuffle(1-100)
ball=canvas.create_rectangle(10, 10, 25, 25, fill='Orange')

#Paddles
rectangle = canvas.create_rectangle(175,670,-50,690,fill="green", )
base1 =canvas.create_oval(40,625,-50,700, fill='red')
rectangle_right= canvas.create_rectangle(325,670,550,690,fill="red")
base2= canvas.create_oval(460,625,550,700, fill='green')
#Creating Obstacles
#DownObstacle1 = canvas.create_rectangle(380, 450, 480, 550, fill="red")

########################################################     Moving the Arms/Paddles   ##########################################################



#Defining what should happen when keys are pressed for left paddle
def upleft(event):
    print("upleft event")
    x = 40
    y = -15
    canvas.move(rectangle, x, y)
def downleft(event):
    print("downleft event")
    x = -40   
    y = 15
    canvas.move(rectangle, x, y)
#Defining what should happen when keys are pressed for right paddle
def upright(event):
    print("upright event")
    x = -55
    y = -15
    canvas.move(rectangle_right, x, y)
def downright(event):
    print("downright event")
    x = 55
    y = 15
    canvas.move(rectangle_right, x, y)
    
#listening to the keyboard
master.bind("<Right>", upleft)
master.bind("<KeyRelease-Right>", downleft)
master.bind("<Left>", upright)
master.bind("<KeyRelease-Left>", downright)

#Making a score and a score label
score = 0
scoreLabel = Label(canvas, text= "Your Score: " + str(score), background = "orange", foreground = "grey")
scoreLabel.place(x=410, y=10)


##############################################################    Moving the ball    ###################################################################
num = 5
xspeed = yspeed = num

########################################################    Buttons in game     #################################################################
def Box():
    master.destroy()
    import Piball

b1 = Button(master ,text = "Restart", command = Box,)
b1.pack(padx=10, pady=10)    


#Making the ball bounce off from the edges
def bouncing():
    global xspeed, yspeed
    global num
    
    
    canvas.move(ball,xspeed,yspeed)




########################################################     Collision Detection and rebound ###################################################

#check if ball is in canvas
    a = canvas.bbox(ball)
    b = canvas.bbox(rectangle_right)
    c = canvas.bbox(rectangle)
    d = canvas.bbox(base1)
    e = canvas.bbox(base2)
    #f = canvas.bbox(DownObstacle1)

#ckecking if the ball goes out of the canvas
    global score
    if a[0] <= 0 or a[2] >= WIDTH:
          xspeed *= -1
    if a[1] <= 0 or a[3] >= HEIGHT:
          yspeed *= -1
          
    if a[3] >= 730:
        
        message = messagebox.showinfo(title='Failed!', message="Your score is : " + str(score) + " Please close the game and restart!")
        canvas.delete(ball)
#Ball Collusion with Obstacles


        
        
        #python = sys.executable
        #os.execl(python, python, * sys.argv)



#Ball interacting with the paddles


    if b[0] < a[2] < b[2] and b[1] < a[1] < b[3]:
        yspeed *= -1
        score = score +1
    if c[0] < a[2] < c[2] and c[1] < a[1] < c[3]:
        yspeed *= -1
        score = score +1

  
    scoreLabel.config(text = "Your Score: " + str(score))
        
    canvas.after(30, bouncing)
    yspeed += gravity


canvas.after(1, bouncing)

master.mainloop()


    
