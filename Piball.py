
###################################################### Importing needed libraries  ###########################################################
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox#to show the user their score at the end 
import time#to pause the game
import random#for the starting position of the ball
from tkinter import filedialog
import pygame
#Main Screen
master = Tk()
master.title('Piball v0.5')
master.geometry('700x1000')
master.resizable(False, False)
master.iconbitmap("galaxy.ico")
master.config(bg="black")
gravity = 0.25
#Canvas around the main screen
WIDTH, HEIGHT = 600,930
canvas = Canvas(master, width=WIDTH, height = HEIGHT, bg= "Grey")
canvas.pack(padx=0, pady=10, side = RIGHT)
messagebox.showinfo(title='Information', message="Register your name after clicking 'OK' by following (MENU -> PLAY -> REGISTER)                                                                            Have Fun ")

############################################        Creating Objects         #######################################################
#Paddles
rectangle = canvas.create_rectangle(0,850,220,870,fill="#34cfeb" )
base1 =canvas.create_oval(80,805,0,880, fill='#34cfeb')
rectangle_right= canvas.create_rectangle(340,850,560,870,fill="#34cfeb")
base2= canvas.create_oval(490,805,570,880, fill='#34cfeb')
#Creating Obstacles
DownObstacle1 = canvas.create_rectangle(450, 450, 480, 700, fill="lightblue")
DownObstacle2= canvas.create_rectangle(80, 450, 110, 700, fill="lightblue")
Obstacle1 = canvas.create_oval(250, 200, 350, 300, fill="green")
Obstacle2 = canvas.create_oval(40, 55, 140, 155, fill="blue")
Obstacle3 = canvas.create_oval(425,55 ,525, 155, fill= "red")
Obstacle4 = canvas.create_oval(150,550 ,200, 600, fill= "red")
Obstacle5 = canvas.create_oval(270,450 ,320, 500, fill= "red")
Obstacle6 = canvas.create_oval(270,650 ,320, 700, fill= "red")
Obstacle7 = canvas.create_oval(375,550 ,425, 600, fill= "red")
Line = canvas.create_line(570,900, 570,0, smooth=1)
Blocker = canvas.create_rectangle(570,870,600,890, fill = "pink")
Jumpgate = canvas.create_rectangle(570,0,600,30, fill = "#67A3A9")



##############################################        Moving the Arms/Paddles and the Spring  ##########################################################
#Defining what should happen to the left paddle when keys are pressed 
def upleft(event):
    x = 40
    y = -15
    canvas.move(rectangle, x, y)
def downleft(event):
    canvas.moveto(rectangle, 0, 850)
#Defining what should happen to the right paddle when keys are pressed  
def upright(event):
    x = -55
    y = -15
    canvas.move(rectangle_right, x, y)
def downright(event):
    canvas.moveto(rectangle_right, 340,850)
#Defining what should happen to the Blocker when keys are pressed   
def Blocker_Down(event):
    x = 0
    y = 20
    canvas.move(Blocker, x, y)
def Blocker_up(event):
    global yspeed , xspeed
    x = 0
    y = -20
    yspeed = yspeed -30
    canvas.moveto(Blocker, 570,870)

#listening to the keyboard
master.bind("<Left>", upleft)
master.bind("<KeyRelease-Left>", downleft)
master.bind("<Right>", upright)
master.bind("<KeyRelease-Right>", downright)
master.bind("<Down>", Blocker_Down)
master.bind("<KeyRelease-Down>", Blocker_up)



###############################################         Making score and labels       ################################################################
score = 0
scoreLabel = Label(canvas, text= "Your Score: " + str(score), background = "pink", foreground = "black")
scoreLabel.place(x=485, y=5)
print("Your Name is the password to start the game  :)")
#Name = input("Whats Your Name? :")

#Making hearts\ allowances heart
global hearts
hearts = 3
heartLabel = Label(canvas, text= "❤: " + str(hearts), background = "grey", foreground = "red", font=('Helvatical bold',20))
heartLabel.place(x=10, y= 5)
#Telling the user they are in max speed
MaxSpeed = Label(canvas, text= "MAX SPEED" , background = "grey", foreground = "red", font=('Helvatical bold',33))
MaxSpeed.place(x=-500, y= 100)



########################################################   Moving the ball    ###################################################################
ball=canvas.create_oval(10, 10, 25, 25, fill='Orange')
canvas.moveto(ball, 580, 800)
xspeed = 0 
yspeed = 0



########################################################    Buttons in game     #################################################################

#Restarting The Game
def Box():
    master.destroy()
    import Piball
#Pausing the background song
def stop_music():
    pygame.mixer.music.stop()
#Playing the background song
def play_mus():
    pygame.mixer.music.play(-1)
#Importing the main menu
def Menu():
    import LogIn

#TopLevel screen to display high scores  
def high_scores():
    window3 = Toplevel(master)
    window3.title("High Scores")
    window3.geometry("500x700")
    window3.resizable(0,0)
    
#Where Score is displayed
    with open('Names.txt', 'r') as file:#reading and using the names which the user puts
        Name = file.readlines()[-1].replace('\n', '')
        
    def textfile():#writing in the text file for the score
        text_file = open("Sboard.txt", 'a+')
        #concatinating the score and the users name which is stored in two different text files
        text_file.write(Name + "'s " + " Score: " + str(score)+ "\n" )
        text_file.close()
        text_file = open("Sboard.txt", 'r')
        readthefile = text_file.readline()
        Save["state"] = "disabled"
    def open_text():
       Text_File = open("Sboard.txt", "r")#reading whats inside the scoreboard
       readthefile = Text_File.readlines()
       numbers = (readthefile)
       numbers = ("".join(numbers))
       my_text.insert(END, numbers)#puting whats in the text file into the label 
       Text_File.close()
       show["state"] = "disabled"
    
   
    my_text = Text(window3, width = 50, height=30)
    my_text.pack(pady= 10, padx=10)
    show = Button(window3, text="Click To Reveal", width=30, command = open_text) 
    show.pack(padx= 10, pady = 40)

    Save = Button(window3, text="Save Your Score", width=30, command = textfile) 
    Save.pack(padx= 10, pady = 10)
    canvas.destroy()
    

b1 = Button(master , text = "RESTART", command = Box)
b1.pack(padx =10, pady=10 , side= TOP)
b2 = Button(master ,text = "MENU",command = Menu)
b2.pack(padx =10, pady=50 , side= TOP)
b3 = Button(master ,text = "Score Board",command = high_scores)
b3.pack(padx =10, pady=50 , side= TOP)
#Drop Down Button
#What makes the mainloop runs
paused = False


def selected(event):
    global xspeed, yspeed, paused
    if clicked.get() == 'MUTE':
        pygame.mixer.music.stop()
    if clicked.get() == 'UNMUTE':
        pygame.mixer.music.play()
    if clicked.get() == 'EXIT GAME':
        master.destroy()
    if clicked.get() == 'CONTINUE':
        paused == False
        print (paused)
    if clicked.get() == 'PAUSE':
           paused = True
           print (paused)
drops = ["",
           "OPTIONS" ,
           "MUTE",
         "UNMUTE",
         "MUTE SOUND EFFECTS",
         "UNMUTE SOUND EFFECTS",
           "PAUSE",
         "CONTINUE",
           "EXIT GAME" ]
clicked = StringVar()
clicked.set(drops[1])
drop = OptionMenu(master, clicked, *drops, command = selected)
drop.pack(padx = 0, pady = 50, side = TOP)
######################################          Volume        ##########################################################################
#Create Volume Function
def volume(x):
    pygame.mixer.music.set_volume(volume_slider.get())
#Identifying Volume Adjuster
VolumeAdjust = Label(master, text = "Volume: ",background = "black", foreground = "Orange", font=('Helvatical bold',11))
VolumeAdjust.pack()
#Creating a slider to adjust the volume
volume_slider = Scale(master,from_=0,to=1, orient = VERTICAL, value=1, command=volume)
volume_slider.pack(padx=10, pady=10)
#Needed Sound Effects and Songs
pygame.mixer.init()
jump = pygame.mixer.Sound("Bip.mp3")
boink = pygame.mixer.Sound("boink.mp3")
teleporting = pygame.mixer.Sound("Transporting.mp3")
Hop = pygame.mixer.Sound("Stretch.mp3")
cartoon = pygame.mixer.Sound("Cartoon.mp3")
Music = pygame.mixer.music.load("BG.mp3")
pygame.mixer.music.play(-1)



########################################################     Collision Detection and rebound ###################################################
#Making the ball moveS

while paused == False:
       def bouncing():
           global xspeed, yspeed
           global num
           lan = canvas.move(ball,xspeed,yspeed)
       #renaming objects for ease purposes
           a = canvas.bbox(ball)
           b = canvas.bbox(rectangle_right)
           c = canvas.bbox(rectangle)
           d = canvas.bbox(base1)
           e = canvas.bbox(base2)
           f = canvas.bbox(DownObstacle1)
           f1 = canvas.bbox(DownObstacle2)
           g = canvas.bbox(Obstacle2)
           g1= canvas.bbox(Obstacle1)
           g2 = canvas.bbox(Obstacle3)
           g3 = canvas.bbox(Obstacle4)
           g4 = canvas.bbox(Obstacle5)
           g5 = canvas.bbox(Obstacle6)
           g6 = canvas.bbox(Obstacle7)  
           h = canvas.bbox(Line)
           i = canvas.bbox(Blocker)
           j = canvas.bbox(Jumpgate)
       #Randomising the speed, when it hits the paddles it chooses a random speed    
           accelerator = [-40,-36,-30, -25, -20,-17,-16,-15,-13,-12,-11,-10]
           random.shuffle(accelerator)
           accelerator[0]
       #ckecking if the ball goes out of the canvas
           global score, hearts, sound
           if a[0] <= 0 or a[2] >= 570:
               xspeed *= -1
           if a[1] <= 0 :
               yspeed *= -1
               cartoon.play()
           elif clicked.get() == 'UNMUTE SOUND EFFECTS':
                 pass  
           else:
               if clicked.get() == 'MUTE SOUND EFFECTS':
                   cartoon.stop()
       #taking away the hearts when the ball is below the paddles
           if a[3] >= 910:
               hearts = hearts -1
               canvas.moveto(ball ,580, 800)
               heartLabel.config(text = "❤: " + str(hearts))
               Continue = messagebox.askyesno(title="" + str(hearts) + " HEARTS REMAINING ❤ ", message="CONTINUE? ")
       #If users answer to the pop up is no then the game ends and displays a message
               if Continue == False:
                   master.destroy()
                   message = messagebox.showinfo(title='Well Played!!', message="Your score is : " + str(score) )
               xspeed = 0
               yspeed = 1#ball goes stright down in the starting area
       #Ball interacting with the paddles
           if b[0] < a[2] < b[2] and b[1] < a[1] < b[3]:
               yspeed = accelerator[0]
               score = score +1
               cartoon.play()
           elif clicked.get() == 'UNMUTE SOUND EFFECTS':
                 pass  
           else:
               if clicked.get() == 'MUTE SOUND EFFECTS':
                   cartoon.stop()    
           if c[0] < a[2] < c[2] and c[1] < a[1] < c[3]:
               yspeed = accelerator[0]
               score = score +1
               cartoon.play()
           elif clicked.get() == 'UNMUTE SOUND EFFECTS':
                 pass  
           else:
               if clicked.get() == 'MUTE SOUND EFFECTS':
                   cartoon.stop()
       #Ball interacting with the bases of the paddles
           if d[0]< a[2] < d[2] and d[1] < a[1] < d[3]:
               yspeed = accelerator[0]
               cartoon.play()
           if e[0]< a[2] < e[2] and e[1] < a[1] < e[3]:
               yspeed = accelerator[0]
               cartoon.play()
           elif clicked.get() == 'UNMUTE SOUND EFFECTS':
                 pass  
           else:
               if clicked.get() == 'MUTE SOUND EFFECTS':
                   cartoon.stop()
       #Defining what should happen when the game ends
           if hearts == 0:
               canvas.itemconfig(ball, fill='red')
               canvas.itemconfig(rectangle_right, fill='red')
               canvas.itemconfig(rectangle, fill='red')
               canvas.itemconfig(base1, fill='red')
               canvas.itemconfig(base2, fill='red')
               canvas.itemconfig(DownObstacle1, fill='red')
               canvas.itemconfig(Obstacle2, fill='red')
               canvas.itemconfig(Obstacle1, fill='red')
               canvas.itemconfig(Obstacle3, fill='red')
               canvas.itemconfig(Obstacle4, fill='red')
               canvas.itemconfig(Obstacle5, fill='red')
               canvas.itemconfig(Obstacle6, fill='red')
               canvas.itemconfig(Obstacle7, fill='red')
               canvas.itemconfig(Blocker, fill='red')
               canvas.itemconfig(Jumpgate, fill='red')
               scoreLabel.config(background = 'red')
               canvas.itemconfig(DownObstacle2, fill='red')
               canvas.delete(ball)
               message = messagebox.showinfo(title='Failed!', message="Your score is : " + str(score) + " Please close the game and restart!")
               heartLabel.place(x= 175 , y= 325)
               heartLabel.config(font=('Helvatical bold',80), foreground = "black")
               import End
       #When the ball is in the maximum speed this applies;
           if yspeed == -40:
               canvas.itemconfig(ball, fill='purple')
               canvas.itemconfig(rectangle_right, fill='purple')
               canvas.itemconfig(rectangle, fill='purple')
               canvas.itemconfig(base1, fill='purple')
               canvas.itemconfig(base2, fill='purple')
               canvas.itemconfig(DownObstacle1, fill='purple')
               canvas.itemconfig(Obstacle1, fill='purple')
               canvas.itemconfig(Obstacle2, fill='purple')
               canvas.itemconfig(Obstacle3, fill='purple')
               canvas.itemconfig(Obstacle4, fill='purple')
               canvas.itemconfig(Obstacle5, fill='purple')
               canvas.itemconfig(Obstacle6, fill='purple')
               canvas.itemconfig(Obstacle7, fill='purple')
               canvas.itemconfig(DownObstacle2, fill='purple')
               MaxSpeed.place(x=155, y=50)
           if a[1] <= 0:
               canvas.itemconfig(ball, fill='orange')
               canvas.itemconfig(rectangle_right, fill='#34cfeb')
               canvas.itemconfig(rectangle, fill='#34cfeb')
               canvas.itemconfig(base1, fill='#34cfeb')
               canvas.itemconfig(base2, fill='#34cfeb')
               canvas.itemconfig(DownObstacle1, fill='lightblue')
               canvas.itemconfig(Obstacle1, fill='#c217d1')
               canvas.itemconfig(Obstacle2, fill='#c217d1')
               canvas.itemconfig(Obstacle3, fill='#c217d1')
               canvas.itemconfig(Obstacle4, fill='#c217d1')
               canvas.itemconfig(Obstacle5, fill='#c217d1')
               canvas.itemconfig(Obstacle6, fill='#c217d1')
               canvas.itemconfig(Obstacle7, fill='#c217d1')
               canvas.itemconfig(DownObstacle2, fill='lightblue')
               MaxSpeed.place(x=-500, y= 100)
           elif a[0] >= WIDTH:
               
               canvas.itemconfig(ball, fill='orange')
               canvas.itemconfig(rectangle_right, fill='#34cfeb')
               canvas.itemconfig(rectangle, fill='#34cfeb')
               canvas.itemconfig(base1, fill='#34cfeb')
               canvas.itemconfig(base2, fill='#34cfeb')
               canvas.itemconfig(DownObstacle1, fill='lightblue')
               canvas.itemconfig(Obstacle1, fill='#c217d1')
               canvas.itemconfig(Obstacle2, fill='#c217d1')
               canvas.itemconfig(Obstacle3, fill='#c217d1')
               canvas.itemconfig(Obstacle4, fill='#c217d1')
               canvas.itemconfig(Obstacle5, fill='#c217d1')
               canvas.itemconfig(Obstacle6, fill='#c217d1')
               canvas.itemconfig(Obstacle7, fill='#c217d1')
               canvas.itemconfig(DownObstacle2, fill='lightblue')
               MaxSpeed.place(x=-500, y= 100)
           elif a[2] >= 570:
               canvas.itemconfig(ball, fill='orange')
               canvas.itemconfig(rectangle_right, fill='#34cfeb')
               canvas.itemconfig(rectangle, fill='#34cfeb')
               canvas.itemconfig(base1, fill='#34cfeb')
               canvas.itemconfig(base2, fill='#34cfeb')
               canvas.itemconfig(DownObstacle1, fill='lightblue')
               canvas.itemconfig(Obstacle1, fill='#c217d1')
               canvas.itemconfig(Obstacle2, fill='#c217d1')
               canvas.itemconfig(Obstacle3, fill='#c217d1')
               canvas.itemconfig(Obstacle4, fill='#c217d1')
               canvas.itemconfig(Obstacle5, fill='#c217d1')
               canvas.itemconfig(Obstacle6, fill='#c217d1')
               canvas.itemconfig(Obstacle7, fill='#c217d1')
               canvas.itemconfig(DownObstacle2, fill='lightblue')
               MaxSpeed.place(x=-500, y= 100)  
       #Collision Detection with Down obstacle 1
           if f[0] < a[2] < f[2] and f[1] < a[1] < f[3] and f[1] < a[3] < f[3]:
               xspeed *= -1
               xspeed = xspeed + 1 or +2 or +3 or +4 or +5 or -1 or -2 or -3 or -4 or -5
               yspeed = yspeed + 1 or +2 or +3 or +4 or +5 or -1 or -2 or -3 or -4 or -5
               canvas.itemconfig(DownObstacle1, fill='blue')
               Hop.play()
           #Mutes the sound effect
           elif clicked.get() == 'UNMUTE SOUND EFFECTS':
                 pass  
           else:
               if clicked.get() == 'MUTE SOUND EFFECTS':
                   Hop.stop()
           if f[2] < a[0] < f[0] and f[3] < a[3] < f[1] and f[3] < a[1] < f[1] :
               yspeed *= -1
               xspeed = xspeed + 1 or +2 or +3 or +4 or +5 or -1 or -2 or -3 or -4 or -5
               yspeed = yspeed + 1 or +2 or +3 or +4 or +5 or -1 or -2 or -3 or -4 or -5
               canvas.itemconfig(DownObstacle1, fill='blue')
               Hop.play()
           #Mutes the sound effect
           elif clicked.get() == 'UNMUTE SOUND EFFECTS':
                 pass  
           else:
               if clicked.get() == 'MUTE SOUND EFFECTS':
                   Hop.stop()
       #Collision Detection with DownObstacle2
           if f1[0] < a[2] < f1[2] and f1[1] < a[1] < f1[3] and f1[1] < a[3] < f1[3]:
               xspeed *= -1
               xspeed = xspeed + 1 or +2 or +3 or +4 or +5 or -1 or -2 or -3 or -4 or -5
               yspeed = yspeed + 1 or +2 or +3 or +4 or +5 or -1 or -2 or -3 or -4 or -5
               canvas.itemconfig(DownObstacle2, fill='blue')
               Hop.play()
           #Mutes the sound effect
           elif clicked.get() == 'UNMUTE SOUND EFFECTS':
                 pass  
           else:
               if clicked.get() == 'MUTE SOUND EFFECTS':
                   Hop.stop()
           if f1[2] < a[0] < f1[0] and f[3] < a[3] < f1[1] and f1[3] < a[1] < f1[1] :
               yspeed *= -1
               xspeed = xspeed + 1 or +2 or +3 or +4 or +5 or -1 or -2 or -3 or -4 or -5
               yspeed = yspeed + 1 or +2 or +3 or +4 or +5 or -1 or -2 or -3 or -4 or -5
               canvas.itemconfig(DownObstacle2, fill='blue')
               Hop.play()
           #Mutes the sound effect
           elif clicked.get() == 'UNMUTE SOUND EFFECTS':
                 pass  
           else:
               if clicked.get() == 'MUTE SOUND EFFECTS':
                   Hop.stop()
       #Collision Detection with Obstacl 
           if g[0] < a[2] < g[2] and g[1] < a[1] < g[3]:
               xspeed *= -1
               xspeed = xspeed + 1 or +2 or +3 or +4 or +5 or -1 or -2 or -3 or -4 or -5
               yspeed = yspeed + 1 or +2 or +3 or +4 or +5 or -1 or -2 or -3 or -4 or -5
               canvas.itemconfig(Obstacle2, fill='blue')
               boink.play()
           #Mutes the sound effect
           elif clicked.get() == 'UNMUTE SOUND EFFECTS':
                 pass  
           else:
               if clicked.get() == 'MUTE SOUND EFFECTS':
                   boink.stop()
           if g[0] < a[0] < g[2] and g[1] < a[3] < g[3]:
               yspeed *= -1
               xspeed = xspeed + 1 or +2 or +3 or +4 or +5 or -1 or -2 or -3 or -4 or -5
               yspeed = yspeed + 1 or +2 or +3 or +4 or +5 or -1 or -2 or -3 or -4 or -5
               canvas.itemconfig(Obstacle2, fill='yellow')
               boink.play()
           #Mutes the sound effect
           elif clicked.get() == 'UNMUTE SOUND EFFECTS':
                 pass  
           else:
               if clicked.get() == 'MUTE SOUND EFFECTS':
                   boink.stop()
       #Collision Detection with Obstacle2
           if g1[0] < a[2] < g1[2] and g1[1] < a[1] < g1[3]:
               xspeed *= -1
               xspeed = xspeed + 1 or +2 or +3 or +4 or +5 or -1 or -2 or -3 or -4 or -5
               yspeed = yspeed + 1 or +2 or +3 or +4 or +5 or -1 or -2 or -3 or -4 or -5
               canvas.itemconfig(Obstacle1, fill='blue')
               boink.play()
           #Mutes the sound effect
           elif clicked.get() == 'UNMUTE SOUND EFFECTS':
                 pass  
           else:
               if clicked.get() == 'MUTE SOUND EFFECTS':
                   boink.stop()
           if g1[0] < a[0] < g1[2] and g1[1] < a[3] < g1[3]:
               yspeed *= -1
               xspeed = xspeed + 1 or +2 or +3 or +4 or +5 or -1 or -2 or -3 or -4 or -5
               yspeed = yspeed + 1 or +2 or +3 or +4 or +5 or -1 or -2 or -3 or -4 or -5
               canvas.itemconfig(Obstacle1, fill='yellow')
               boink.play()
           #Mutes the sound effect
           elif clicked.get() == 'UNMUTE SOUND EFFECTS':
                 pass  
           else:
               if clicked.get() == 'MUTE SOUND EFFECTS':
                   boink.stop()
       #Collision Detection with obstacle3
           if g2[0] < a[2] < g2[2] and g2[1] < a[1] < g2[3]:
               xspeed *= -1
               xspeed = xspeed + 1 or +2 or +3 or +4 or +5 or -1 or -2 or -3 or -4 or -5
               yspeed = yspeed + 1 or +2 or +3 or +4 or +5 or -1 or -2 or -3 or -4 or -5
               canvas.itemconfig(Obstacle3, fill='blue')
               boink.play()
           #Mutes the sound effect
           elif clicked.get() == 'UNMUTE SOUND EFFECTS':
                 pass  
           else:
               if clicked.get() == 'MUTE SOUND EFFECTS':
                   boink.stop()
           if g2[0] < a[0] < g2[2] and g2[1] < a[3] < g2[3]:
               yspeed *= -1
               xspeed = xspeed + 1 or +2 or +3 or +4 or +5 or -1 or -2 or -3 or -4 or -5
               yspeed = yspeed + 1 or +2 or +3 or +4 or +5 or -1 or -2 or -3 or -4 or -5
               canvas.itemconfig(Obstacle3, fill='yellow')
               boink.play()
           #Mutes the sound effect
           elif clicked.get() == 'UNMUTE SOUND EFFECTS':
                 pass  
           else:
               if clicked.get() == 'MUTE SOUND EFFECTS':
                   boink.stop()
       #Collision Detection with obstacle4
           if g3[0] < a[0] < g3[2] and g3[1] < a[3] < g3[3]:
               yspeed *= -1
               xspeed = xspeed + 1 or +2 or +3 or +4 or +5 or -1 or -2 or -3 or -4 or -5
               yspeed = yspeed + 1 or +2 or +3 or +4 or +5 or -1 or -2 or -3 or -4 or -5
               canvas.itemconfig(Obstacle4, fill='yellow')
               boink.play()
           #Mutes the sound effect
           elif clicked.get() == 'UNMUTE SOUND EFFECTS':
                 pass  
           else:
               if clicked.get() == 'MUTE SOUND EFFECTS':
                   boink.stop()
       #Collision Detection with obstacle5
           if g4[0] < a[0] < g4[2] and g4[1] < a[3] < g4[3]:
               yspeed *= -1
               xspeed = xspeed + 1 or +2 or +3 or +4 or +5 or -1 or -2 or -3 or -4 or -5
               yspeed = yspeed + 1 or +2 or +3 or +4 or +5 or -1 or -2 or -3 or -4 or -5
               canvas.itemconfig(Obstacle5, fill='yellow')
               boink.play()
           #Mutes the sound effect
           elif clicked.get() == 'UNMUTE SOUND EFFECTS':
                 pass  
           else:
               if clicked.get() == 'MUTE SOUND EFFECTS':
                   boink.stop()
       #Collision Detection with obstacle6
           if g5[0] < a[0] < g5[2] and g5[1] < a[3] < g5[3]:
               yspeed *= -1
               xspeed = xspeed + 1 or +2 or +3 or +4 or +5 or -1 or -2 or -3 or -4 or -5
               yspeed = yspeed + 1 or +2 or +3 or +4 or +5 or -1 or -2 or -3 or -4 or -5
               canvas.itemconfig(Obstacle6, fill='yellow')
               boink.play()
           #Mutes the sound effect
           elif clicked.get() == 'UNMUTE SOUND EFFECTS':
                 pass  
           else:
               if clicked.get() == 'MUTE SOUND EFFECTS':
                   boink.stop()
       #Collision Detection with obstacle7
           if g6[0] < a[0] < g6[2] and g6[1] < a[3] < g6[3]:
               yspeed *= -1
               xspeed = xspeed + 1 or +2 or +3 or +4 or +5 or -1 or -2 or -3 or -4 or -5
               yspeed = yspeed + 1 or +2 or +3 or +4 or +5 or -1 or -2 or -3 or -4 or -5
               canvas.itemconfig(Obstacle7, fill='yellow')
               boink.play()
           #Mutes the sound effect
           elif clicked.get() == 'UNMUTE SOUND EFFECTS':
                 pass  
           else:
               if clicked.get() == 'MUTE SOUND EFFECTS':
                   boink.stop()
       #Starting Position

           if i[0] < a[2] < i[2]  and i[1] < a[3] < i[3]:
               yspeed = -yspeed
               jump.play()
           #Mutes the sound effect
           elif clicked.get() == 'UNMUTE SOUND EFFECTS':
                 pass  
           else:
               if clicked.get() == 'MUTE SOUND EFFECTS':
                   jump.stop()

                   
       #Teleporting ball to the main game area from the starting point
           if j[0] < a[0] < j[2] and j[1] < a[1] < j[3]:
               canvas.delete(bouncing)
               startx = [-3, -2, -1, 1, 2, 3,4,5,6,7,8,9,10]
               random.shuffle(startx)
               startx[0]
               yspeed = 6
               xspeed = startx[0]
               canvas.moveto(ball, 250, 300)
               teleporting.play()
           elif clicked.get() == 'UNMUTE SOUND EFFECTS':
                 pass  
           else:
               if clicked.get() == 'MUTE SOUND EFFECTS':
                   teleporting.stop()

           scoreLabel.config(text = "Your Score: " + str(score))
           canvas.after(30, bouncing)
           yspeed += gravity

       canvas.after(1, bouncing)
       
       master.mainloop()


    
