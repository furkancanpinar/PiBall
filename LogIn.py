##########################################                     LogIn            ###########################################################################################################
from tkinter import *
from tkinter import messagebox
import time
from tkinter import filedialog





#The window which opens when "Play" is 
def register():
    window2 = Toplevel(MS)
    window2.title("Register")
    window2.geometry("500x700")
    window2.resizable(0,0)
    def textfile():#writing in the text file
        FirstName = entry.get()#stores the first input as Name
        Surname = entry1.get()#stores the second input as Surname
        text_file = open("Names.txt", 'a+')
        text_file.write(FirstName + " " + Surname + "\n" )#saves the entry variables in text file
        text_file.close()        
        Play["state"] = "disabled"

    username = StringVar()
    password = StringVar()

    Label(window2, text = "Please enter details below").pack()
    Label(window2, text="").pack()
        
    #First Name
    u = open("Names.txt","r+")
    Fname = Label(window2, text="Name * ")
    Fname.place(relx= 0.5, rely= 0.09, anchor= CENTER)
    entry = Entry(window2, width= 20)
    entry.place(relx= 0.5, rely= 0.12, anchor= CENTER)
    #Second Name
    Sname = Label(window2, text= "Surname * ")
    Sname.place(relx= 0.5, rely= 0.16, anchor= CENTER)
    entry1 = Entry(window2, width= 20)
    entry1.place(relx= 0.5, rely= 0.19, anchor= CENTER)
    Note = Label(window2, text= "Note: Your 'Name' and 'Surname' will only be used for score system.")
    Note.place(relx= 0.5, rely= 0.5, anchor= CENTER)
    Note2 = Label(window2, text= "It will not be shared with anyone elses but used within PiBall system")
    Note2.place(relx= 0.5, rely= 0.54, anchor= CENTER)
    Note3 = Label(window2, text= "To see your score on the score board click on 'Score Board' then")
    Note3.place(relx= 0.5, rely= 0.58, anchor= CENTER)
    Note4 = Label(window2, text= "'Save Your Score' and then 'Click To Reveal' ")
    Note4.place(relx= 0.5, rely= 0.62, anchor= CENTER)
    Note5 = Label(window2, text= "Enjoy PiBall", bg = "Grey", fg = "Orange")
    Note5.place(relx= 0.5, rely= 0.45, anchor= CENTER)

    Play = Button(window2, text = "Register", width = 10, height =1, command = lambda: [textfile(), game()])
    Play.place(relx= 0.5, rely= 0.25, anchor= CENTER)





    
def game():
    import Piball


def Info():
    window4= Toplevel(MS)
    window4.title("How To Play")
    window4.geometry("500x700")
    window4.resizable(0,0)
    window4.config(bg = "lightblue")
    One = Label(window4, text= "Hi, welcome to PiBall", bg = "pink", fg = "blue")
    One.place(relx= 0.5, rely= 0.1, anchor= CENTER)
    two = Label(window4, text= "How to run the game:", bg = "Grey", fg = "Orange")
    two.place(relx= 0.3, rely= 0.15, anchor= CENTER)
    three =Label(window4, text= "To play the game you simply need to click on Play. ", bg = "Orange", fg = "Grey")
    three.place(relx= 0.5, rely= 0.2, anchor= CENTER)
    four=Label(window4, text= "After Registering your name the game will start", bg = "Orange", fg = "Grey")
    four.place(relx= 0.5, rely= 0.23, anchor= CENTER)
    five= Label(window4, text= "How To Play:", bg = "Grey", fg = "Orange")
    five.place(relx= 0.26, rely= 0.3, anchor= CENTER)
    six=Label(window4, text= "To play the game you need to use:", bg = "Orange", fg = "Grey")
    six.place(relx= 0.5, rely= 0.35, anchor= CENTER)
    seven=Label(window4, text= "Down Arrow Key: For The Spring movements", bg = "Orange", fg = "Grey")
    seven.place(relx= 0.5, rely= 0.38, anchor= CENTER)
    eight=Label(window4, text= "Left Arrow Key: For The Left Paddle movements", bg = "Orange", fg = "Grey")
    eight.place(relx= 0.5, rely= 0.41, anchor= CENTER)
    nine=Label(window4, text= "Right Arrow Key: For The Right Paddle movements", bg = "Orange", fg = "Grey")
    nine.place(relx= 0.5, rely= 0.44, anchor= CENTER)
    ten=Label(window4, text= "Whats the aim of the game?", bg = "Grey", fg = "Orange")
    ten.place(relx= 0.33, rely= 0.5, anchor= CENTER)
    aim=Label(window4, text= "The aim of the game is to keep the ball ", bg = "Orange", fg = "Grey")
    aim.place(relx= 0.5, rely= 0.55, anchor= CENTER)
    game=Label(window4, text= "above the paddles and get as much score as you can", bg = "Orange", fg = "Grey")
    game.place(relx= 0.5, rely= 0.58, anchor= CENTER)
    score=Label(window4, text= "and get your place on the score board", bg = "Orange", fg = "Grey")
    score.place(relx= 0.5, rely= 0.61, anchor= CENTER)
    score=Label(window4, text= "Hope you will enjoy the game. PiBall", bg = "black", fg = "orange" ,font = 100)
    score.place(relx= 0.5, rely= 0.7, anchor= CENTER)
def main_screen():
    global MS
    MS = Tk() 
    MS.geometry("500x700")
    MS.title("Piball v0.4")

    #TopLevel screen to display high scores  
    def high_scores():
        window3 = Toplevel(MS)
        window3.title("High Scores")
        window3.geometry("500x700")
        window3.resizable(0,0)
        
    #Where Score is displayed
        with open('Names.txt', 'r') as file:#reading and using the names which the user puts
            Name = file.readlines()[-1].replace('\n', '')
            

        def open_text():
           Text_File = open("Sboard.txt", "r")#reading whats inside the scoreboard
           readthefile = Text_File.readlines()
           numbers = (readthefile)
           numbers = ("".join(numbers))
           my_text.insert(END, numbers)
           Text_File.close()
           show["state"] = "disabled"
        
       
        my_text = Text(window3, width = 50, height=30)
        my_text.pack(pady= 10, padx=10)
        show = Button(window3, text="Click To Reveal", width=30, command = open_text) 
        show.pack(padx= 10, pady = 40)
        Note = Label(window3, text= "Note: To see your name, simply play the game and follow the games instructions")
        Note.place(relx= 0.5, rely= 0.9, anchor= CENTER)
        Note1 = Label(window3,  text= "PiBall creators wishes you good luck. Enjoy the game.")
        Note1.place(relx= 0.5, rely= 0.94, anchor= CENTER)
        P = Label(window3, bg = 'pink'  , text= "P")
        P.place(relx= 0.9, rely= 0.98, anchor= CENTER)
        i = Label(window3, bg = 'lightblue'  , text= "i")
        i.place(relx= 0.915, rely= 0.98, anchor= CENTER)
        B = Label(window3, bg = 'lightgreen'  , text= "B")
        B.place(relx= 0.935, rely= 0.98, anchor= CENTER)
        a = Label(window3, bg = 'white'  , text= "a")
        a.place(relx= 0.955, rely= 0.98, anchor= CENTER)
        l = Label(window3, bg = 'orange'  , text= "l")
        l.place(relx= 0.967, rely= 0.98, anchor= CENTER)        
        l2= Label(window3, bg = 'yellow'  , text= "l")
        l2.place(relx= 0.983, rely= 0.98, anchor= CENTER)




    #Creating a lable
    lbl1 = Label(MS, text="Click on one of the options to conteniue: ", bg="orange",fg="Black", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    MS.resizable(0,0)

    
    play= Button(MS, text="PLAY",bg="Black", fg= "Orange", width=30, height = 2, activebackground="#ba722d", activeforeground="white", command = register, font = ("Calibri", 13))
    play.place(relx=0.25, rely=0.15)
    Settings= Button(MS, text="SCORE BOARD",bg="Black", fg= "Orange", width=30, height = 2, activebackground="#ba722d", activeforeground="white", command = high_scores, font = ("Calibri", 13))
    Settings.place(relx=0.25, rely=0.35)
    How_to_play= Button(MS, text="HOW TO PLAY",bg="Black", fg= "Orange", width=30, height = 2, activebackground="#ba722d", activeforeground="white", command = Info, font = ("Calibri", 13))
    How_to_play.place(relx=0.25,rely=0.55)
    Label(text="").pack()


#Code which allows colour change on button when mouse is on the button
    def on_enter(e):
        Settings.config(bg='Orange', fg="Grey")

    def on_leave(e):
        Settings.config(bg='grey11', fg='Orange')

    def on_enter1(e):
        play.config(bg='DarkOrange1', fg="Grey")

    def on_leave1(e):
        play.config(bg='grey11', fg='Orange')

    def on_enter2(e):
        How_to_play.config(bg='DarkOrange1', fg="Grey")

    def on_leave2(e):
        How_to_play.config(bg='grey11', fg='Orange')
    Settings.bind('<Enter>', on_enter)
    Settings.bind('<Leave>', on_leave)

    play.bind('<Enter>', on_enter1)
    play.bind('<Leave>', on_leave1)

    How_to_play.bind('<Enter>', on_enter2)
    How_to_play.bind('<Leave>', on_leave2)

    
main_screen()

