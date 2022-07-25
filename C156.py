from tkinter import *
import random
from PIL import ImageTk,Image
root=Tk()
root.title("Endless Pokemon Game")
root.geometry("800x400")
root.configure(background="orange")
img1=ImageTk.PhotoImage(Image.open("button.jpg"))
pikachu=ImageTk.PhotoImage(Image.open("pikachu.jpg"))
charmender=ImageTk.PhotoImage(Image.open("charmender.jpg"))
bulbasour=ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
squirtle=ImageTk.PhotoImage(Image.open("squirtle.jpg"))
iyvasour=ImageTk.PhotoImage(Image.open("Iyvasour.jpg"))
ratata=ImageTk.PhotoImage(Image.open("ratata.jpg"))
paras=ImageTk.PhotoImage(Image.open("paras.jpg"))
meowth=ImageTk.PhotoImage(Image.open("meowth.jpg"))
nidoking=ImageTk.PhotoImage(Image.open("nidoking.jpg"))
kadabra=ImageTk.PhotoImage(Image.open("kadabra.jpg"))
jigglypuff=ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
persion=ImageTk.PhotoImage(Image.open("persion.jpg"))
abra=ImageTk.PhotoImage(Image.open("abra.jpg"))
label1=Label(root,bg="red",fg="white",text="Player1")
label1.place(relx=0.1,rely=0.3,anchor=CENTER)
label2=Label(root,bg="red",fg="white",text="Player2")
label2.place(relx=0.9,rely=0.3,anchor=CENTER)
labelp1=Label(root,bg="red",fg="white")
labelp1.place(relx=0.1,rely=0.1,anchor=CENTER)
labelp2=Label(root,bg="red",fg="white")
labelp2.place(relx=0.9,rely=0.1,anchor=CENTER)
labelpoke=Label(root,bg="red",fg="white")
labelpoke.place(relx=0.5,rely=0.5,anchor=CENTER)
pokemon_list=[pikachu,bulbasour,iyvasour,charmender,squirtle,ratata,jigglypuff,meowth,persion,abra,kadabra]
power_list=[200,60,100,50,50,40,70,60,70,30,70,50,60]
player1_score=0
def player1():
    global player1_score
    random_no=random.randint(0,10)
    random_pokemon=pokemon_list[random_no]
    labelpoke["image"]=random_pokemon
    random_power=power_list[random_no]
    player1_score=player1_score+random_power
    labelp1["text"]=str(player1_score)
    
player2_score=0
def player2():
    global player2_score
    random_no2=random.randint(0,10)
    random_pokemon2=pokemon_list[random_no2]
    labelpoke["image"]=random_pokemon2
    random_power2=power_list[random_no2]
    player2_score=player2_score+random_power2
    labelp2["text"]=str(player2_score)
    
button1= Button(root, image=img1,command=player1)
button1.place(relx=0.1,rely=0.6,anchor=CENTER)
button2= Button(root, image=img1,command=player2)
button2.place(relx=0.9,rely=0.6,anchor=CENTER)
root.mainloop()