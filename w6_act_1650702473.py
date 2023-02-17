'''
Author  : Chaiyapon Sowanna
STD ID  : 1650702473
Week    : 6
Label   : Class Activity
Desc    : Creating Basic Grading Application
Date    : 2023-02-14
'''

from tkinter import *

def mainwindow() :
    root = Tk()
    root.geometry('500x500+400+40')
    root.title("W6-Act3 created by Chaiyapon Sowanna")
    menubar = Menu(root)

    # TODO : Complete here
    
    menu_file = Menu(menubar, tearoff=0)
    menu_file.add_command(label="Exit",command=exit)

    menu_grading = Menu(menubar, tearoff=0)
    menu_grading.add_command(label="Test Score",command=menuscore)
    menu_grading.add_command(label="Grading",command=grading)

    menubar.add_cascade(label='File', menu=menu_file)
    menubar.add_cascade(label='Grading', menu=menu_grading)

    root.option_add('*font','Garamond 16 bold')
    root.config(bg="pink",menu=menubar)

    # prevent resizing window
    root.resizable(False, False)
    return root

# function for changing page
def menuscore():
    frame1 = Frame(root,bg='yellow')
    frame1.place(x=0,y=0,width=500,height=500)
    frame1.columnconfigure((0,1),weight=1)

    for i,data in enumerate(testlist) :
        Label(frame1,text=data+" : ",bg='yellow').grid(row=i,column=0,pady=20,sticky='e')
        Entry(frame1,width=15,textvariable=spy[i],justify='right').grid(row=i,column=1,pady=20,ipady=10)

    Button(frame1,text="Grade Calculate",command=grading).grid(row=i+1,column=0,columnspan=2)

# function for changing page
def grading() :
    frame2 = Frame(root,bg='lightblue')
    frame2.place(x=0,y=0,width=500,height=500)
    frame2.columnconfigure((0,1),weight=1)
    sum = 0
    for i,data in enumerate(testlist) :
        sum = sum + spy[i].get()
        Label(frame2,text=data+" : ",bg='lightblue').grid(row=i,column=0,pady=20,sticky='e')
        Label(frame2,textvariable=spy[i],justify='right',bg='lightblue').grid(row=i,column=1,pady=20,ipady=10,sticky='w')
    showgrade = StringVar()
    gradeLB = Label(frame2,textvariable=showgrade,bg='lightblue')
    grade = ""
    if sum > -1 and sum < 101 : #checking normal score, if over score then notify an error
        # TODO : Complete here.

        if sum > 79 :
            grade = "A (Excellent)"
            gradeLB['fg'] = 'blue'
        elif sum > 69 :
            grade = "B"
            gradeLB['fg'] = 'Green'
        elif sum > 59 :
            grade = "C"
            gradeLB['fg'] = 'Orange'
        elif sum > 50 :
            grade = "D"
            gradeLB['fg'] = 'purple'
        elif sum > 49 or sum == 0:
            grade = "F"
            gradeLB['fg'] = 'white'
            gradeLB['bg'] = 'red'


        #show grade infomation on widget Lable
        showgrade.set("**** The total score = %d ,Grade = %s ****"%(sum, grade))  
    else :
        grade = "Total score is out of range (0-100) !!! "
        gradeLB['fg'] = 'red'
        gradeLB['bg'] = 'black'
        #show grade infomation on widget Lable
        showgrade.set(grade)

    gradeLB.grid(row=i+1,column=0,columnspan=2,sticky='news') 

root = mainwindow()
testlist = ['Midterm','Final','Quiz','Project']
spy = [DoubleVar() for i in testlist]
root.mainloop()