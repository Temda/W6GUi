'''
Author  : Chaiyapon Sowanna
STD ID  : 1650702473
Week    : 6
Label   : Lab
Desc    : Creating Basic Grading Application
Date    : 2023-02-14
'''

from tkinter import *

def mainwindow(root):
    
    root.title("Sweety Bekery Shop by Chaiyapon Sowanna")
    root.geometry('600x600')
    menubar = Menu(root,name='piraya')
    menubar.add_command(label="Menu",command=menu)
    menubar.add_command(label="Chackout",command=chackout)
    menubar.add_command(label="Exit",command=root.quit)
    
    root.configure(bg='pink',menu=menubar)

    Label(root, image=img1, compound=CENTER, bg='pink').grid(row=0, column=0,padx=20,pady=10,columnspan=2)
    Label(root,text='...Welcome to my resturant...',font='Tahoma 22 bold', compound=CENTER, bg='pink').grid(row=1, column=0,padx=20,pady=10,columnspan=2)
    
    return root

def menu() :


    fr1 = Frame(root,bg='yellow')
    fr1.place(x=0,y=0,width=600,height=600)
    fr1.columnconfigure((0,1,2,3),weight=1)
    fr1.rowconfigure((0,1,2,3,4,5),weight=1)

    fr_menu1 = Label(fr1,image=img2,bg='yellow')
    fr_menu1.grid(row=1, column=0,sticky=N)
    fr_menu2 = Label(fr1,image=img3,bg='yellow')
    fr_menu2.grid(row=5, column=0,sticky=N)
    fr_menu3 = Label(fr1,image=img4,bg='yellow')
    fr_menu3.grid(row=1, column=1,sticky=N)
    fr_menu4 = Label(fr1,image=img5,bg='yellow')
    fr_menu4.grid(row=5, column=1,sticky=N)

    text1 = Label(fr1,text="Strawberry Cake : ",font="Tahoma 10 bold",background='yellow',fg='Black')
    text1.grid(row=0,column=0,sticky=N, ipadx=110)
    text2 = Label(fr1,text="Cheese Cake : ",font="Tahoma 10 bold",background='yellow',fg='Black')
    text2.grid(row=4,column=0,sticky=N, ipadx=110)
    text3 = Label(fr1,text="Strawberry Mixed : ",font="Tahoma 10 bold",background='yellow',fg='Black')
    text3.grid(row=0,column=1,sticky=N, ipadx=110)
    text4 = Label(fr1,text="Orange Mixed : ",font="Tahoma 10 bold",background='yellow',fg='Black')
    text4.grid(row=4,column=1,sticky=N, ipadx=110)

    Label(fr1,text="Price 85 THB",font="Tahoma 10 ",background='yellow',fg='Black').grid(row=2,column=0,sticky=N,ipadx=110)
    Label(fr1,text="Price 95 THB",font="Tahoma 10 ",background='yellow',fg='Black').grid(row=6,column=0,sticky=N,ipadx=110)
    Label(fr1,text="Price 120 THB",font="Tahoma 10 ",background='yellow',fg='Black').grid(row=2,column=1,sticky=N,ipadx=110)
    Label(fr1,text="Price 140 THB",font="Tahoma 10 ",background='yellow',fg='Black').grid(row=6,column=1,sticky=N,ipadx=110)

    choice1 = Spinbox(fr1, from_=0, to=50,textvariable=v1,background='White',foreground='Black', state="readonly")
    choice1.grid(row=3, column=0, sticky=N, ipady=4, ipadx=5, pady=50)
    choice2 = Spinbox(fr1,from_=0,to=50,textvariable=v2,background='White',foreground='Black', state="readonly")
    choice2.grid(row=7,column=0,sticky=N, ipady=4, ipadx=5, pady=50)
    choice3 = Spinbox(fr1,from_=0,to=50,textvariable=v3,background='White',foreground='Black', state="readonly")
    choice3.grid(row=3,column=1,sticky=N, ipady=4, ipadx=5, pady=50)
    choice4 = Spinbox(fr1,from_=0,to=50,textvariable=v4,background='White',foreground='Black', state="readonly")
    choice4.grid(row=7,column=1,sticky=N, ipady=4, ipadx=5, pady=50)

def chackout() :
    fr2 = Frame(root,bg='lightgreen')
    fr2.place(x=0,y=0,width=600,height=600)
    fr2.columnconfigure((0,1,2,3),weight=1)
    fr2.rowconfigure((0,1,2,3,4,5),weight=1)

    global net
    pro1 = v1.get() * 85 # value 1
    pro2 = v2.get() * 95 # value 2
    pro3 = v3.get() * 120 # value 3
    pro4 = v4.get() * 140 # value 4
    net = pro1 + pro2 + pro3 + pro4 #total

    for i,data in enumerate(menulist) :
        Label(fr2,text=data+"  ",bg='lightgreen', font='Tahoma 14').grid(row=0,column=i,pady=20,sticky='n')

    for i,data in enumerate(cakelist) :
        Label(fr2,text=data+"  ",bg='lightgreen',font='Tahoma 14 ',fg='Blue').grid(row=i+1,column=0,sticky='n')
        
    Label(fr2,text=v1.get(),justify='right',bg='lightgreen',font='Tahoma 14 ').grid(row=0+1,column=1,sticky='n')
    Label(fr2,text=v2.get(),justify='right',bg='lightgreen',font='Tahoma 14 ').grid(row=1+1,column=1,sticky='n')
    Label(fr2,text=v3.get(),justify='right',bg='lightgreen',font='Tahoma 14 ').grid(row=2+1,column=1,sticky='n')
    Label(fr2,text=v4.get(),justify='right',bg='lightgreen',font='Tahoma 14 ').grid(row=3+1,column=1,sticky='n')

    for i,data in enumerate(pricelist) :
        Label(fr2,text=data,justify='right',bg='lightgreen',font='Tahoma 14 ').grid(row=i+1,column=2,sticky='n')
        

    Label(fr2,text=pro1, justify='right',bg='lightgreen',font='Tahoma 14 ').grid(row=0+1,column=3,sticky='n')
    Label(fr2,text=pro2, justify='right',bg='lightgreen',font='Tahoma 14 ').grid(row=1+1,column=3,sticky='n')
    Label(fr2,text=pro3, justify='right',bg='lightgreen',font='Tahoma 14 ').grid(row=2+1,column=3,sticky='n')
    Label(fr2,text=pro4, justify='right',bg='lightgreen',font='Tahoma 14 ').grid(row=3+1,column=3,sticky='n')

    showgrade = StringVar()
    gradeLB = Label(fr2,textvariable=showgrade,bg='lightgreen')
    gradeLB.grid(row=5, column=0,padx=15,pady=10,columnspan=5, sticky='news') 
    gradeLB['fg'] = 'red'
    gradeLB['font'] = 'Tahoma 20'
    showgrade.set("Total Price = %d Bahts"%(net))

root = Tk()

img1 = PhotoImage(file='images/myshop.png')
img2 = PhotoImage(file='images/cake1.png')
img3 = PhotoImage(file='images/cake2.png')
img4 = PhotoImage(file='images/drink1.png')
img5 = PhotoImage(file='images/drink2.png')

root = mainwindow(root)


net = 0

v1,v2,v3,v4 = IntVar(),IntVar(),IntVar(),IntVar()


menulist = ['Menulist','Amout','Prices','Tatal(Bahts)']
spy = [IntVar() for j in menulist]


pricelist = ['58','95','120','140']
spy3 = [IntVar() for i in pricelist]

cakelist = ['Strawberry Cake :','Cheese Cake :','Strawberry Mixed :','Orange Mixed :']
spy2 = [IntVar() for i in cakelist]

root.mainloop()