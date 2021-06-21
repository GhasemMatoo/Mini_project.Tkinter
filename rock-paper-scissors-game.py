# import modules
from tkinter import *   
from tkinter import messagebox
from functools import partial
import random
import os

#----------------------------function--ALL------
##------------------------------F_Rest_os cod---
def Reset():
    os.execl(sys.executable, sys.executable, *sys.argv)
#--------------------------------F-Exit--------
def Exit():
    win.destroy()
#-----------------------------------------F_code_choose--
def b_result(label_result , str1 , str2):
    string = (str1.get())
    random = str2
    list_text=("rock","paper","scissors")
    while True:
        if string in list_text:
            ans_text="Game Overs"
            if string == 'rock':
                if random == 'scissors':
                    ans="Game Overs"
                    break
                ans="WIIIIN"
            elif string == 'paper':
                if random == 'rock':
                    ans="Game Overs"
                    break
                ans="WIIIIN"
            elif string == 'scissors':
                if random == 'paper':
                    ans="Game Overs"
                    break
                ans="WIIIIN"
            messagebox.showinfo("Hello" , ans)
            ans_text=ans
            break
        ans_text='invalid: choose any one -- rock, paper, scissors'
        break
    
    label_result.config(text=ans_text,font='arial 12 bold')
    return
    
#--------------------- win config-----------
win = Tk()  
win.geometry("400x400")
win.resizable(0,0)
win.config(bg ='#93776c')
win.title('Game')
#-------------------------------Random Rock, Paper ,Scissors----
random = random.randint(1,3)
if random == 1:
    random = 'rock'
elif random == 2:
    random = 'paper'
else:
    random = 'scissors'
#-----------------------------set type variable------
str1 = StringVar() 
#-------------------------------label--------------
Label(win, text = 'Rock, Paper ,Scissors' ,
      font='arial 20 bold', bg = '#ecd0d9').pack()
Label(win, text = 'Please choose: Rock, Paper ,Scissors' ,
      font='arial 15 bold',
      fg='#4c4611',bg = '#cec1bc').place(x=20,y=100)
name = Label(win, text = "Write Choose :",
             font='Times',bg ='#93776c').place(x = 30,y =150)
labelResult =Label(win, text='Please choose: Rock, Paper ,Scissors'
                ,font='arial 15 bold',
                 fg='#4c4611',bg = '#cec1bc')   
labelResult.place(x=20,y=250)
#--------------------------input-sting--
input_1 = Entry(win,font='Times 15',textvariable=str1).place(x = 130, y = 150)  
b_result = partial(b_result,labelResult,str1,random)
#----------------------------Buttom-----
sw = Button(win, text ="Start Game",
            command= b_result ,activebackground = "red"
            ,bg='blue',font=('Helvetica', '12'),
            fg='white',width=10,pady=5).place(x=150,y=190)
sw_reset = Button(win, text ="RESET Game",
            command= Reset ,activebackground = "blue"
            ,bg='Green',font=('Helvetica', '12'),
            fg='white',width=15,pady=5).place(x=250,y=300)
  
sw_exit = Button(win, text ="Exit Game",
            command= Exit ,activebackground = "red"
            ,bg='red',font=('Helvetica', '12'),
            fg='white',width=10,pady=5).place(x=10,y=300)

win.mainloop()  
  


