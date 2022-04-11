#Deepjyoti karmakar
#SORRY FOR THE SPELLING MISTAKES 
from tkinter import *
from tkinter import messagebox 
from random import randint,shuffle
from time import sleep
import pygame

root=Tk()
root.title("Rock Paper Sissor")
pygame.mixer.init()
pygame.init()
root.geometry("899x1899")
frame_button=Frame(root).pack(side="bottom")
class buttonmaker:
	def __init__(self,command2,command_name,witchc):
		self.witchc=witchc
		self.command_name=command_name
		self.command2=command2
	def make_button(self,file_name,bgcolor):
		self.file_name=file_name#file name
		self.bgcolor=bgcolor#nackground color
		butto=Button(frame_button,image=self.file_name,bd=23,bg=self.bgcolor,command=lambda c=self.witchc: [self.command_name(c),self.command2]).pack(side="left",anchor="s")

def play_Boo():
	""""WILL PLAY THE BOO SOUND"""
	pygame.mixer.music.load("Boo.mp3")
	pygame.mixer.music.play()
def play_aplause():
	"""WILL PLAY APLAUSE"""
	pygame.mixer.music.load("Applause.mp3")
	pygame.mixer.music.play()
def creatPho(namefi):
	"""WILL RETURN AN PHOTOIMAGE OBJECT"""
	ob_image=PhotoImage(file=namefi)
	return ob_image
pho_rock_ob=creatPho("Rock.png")
pho_rock_ob_2=creatPho("Rock.png")#second rock object
labelR=Label(root,image=pho_rock_ob)#creating frist label to show
pho_paper_ob=creatPho("Paperimage.png")
pho_sissor_ob=creatPho("Sissor.png")
show_heighst=0
def show_heighst_score():
	"""IT WILL SHOW THE HEIGHST SCORE"""
	global show_heighst
	with open("/storage/emulated/0/MyTKINTER PROJECTS/GUIROCKPAPERSISSOR/Score.txt","r")as re:
		text_re=re.read()
		if int(text_re)<your_score:
			with open("/storage/emulated/0/MyTKINTER PROJECTS/GUIROCKPAPERSISSOR/Score.txt","w")as wr:
				la=Label(root,text="hel").pack()
				wr.write(str(your_score))
				if show_heighst==0:
					messagebox.showinfo("ROCKPAPERSISSOR", "highest score") 
					show_heighst+=1
#show function
def youwon():
	root.config(bg="green")
def youloose():
	root.config(bg="red")
def draw():
	root.config(bg="orange")
count_to=0
your_score=1
def delet_label():
	"""THIS WILL DELETE THE PREVIOUS IMAGE AND LERP GOING"""
	global labelR,random_created,count_to,file_name,bottton_color_is,your_score
	lis_ob=["Paperimage.png","Rock.png","Sissor.png"]
	shuffle(lis_ob)
	if count_to==39:
		count_to=0
		#lad=Label(root,text=user_enter).pack()
		#user_enter==capital file_name or random appearance is ==small
		if user_enter==file_name:
			draw()
			bottton_color_is="orange"
			
		elif user_enter=="R":
			if file_name=="P":
				youloose()
				play_Boo()
				bottton_color_is="green"
			elif  file_name=="S":
				youwon()
				add_score()
				play_aplause()
				your_score+=1#will count score
				show_heighst_score()
		elif user_enter=="P":
			if file_name=="R":
				youwon()
				add_score()
				play_aplause()
				bottton_color_is="red"
				your_score+=1
				show_heighst_score()
			elif file_name=="S":
				youloose()
				play_Boo()
		elif user_enter=="S":
			if file_name=="P":
				youwon()
				add_score()
				play_aplause()
				your_score+=1
				show_heighst_score()
			elif file_name=="R":
				youloose()
				play_Boo()
		else:
			bottton_color_is="blue"
			
	else:
		if lis_ob[0]=="Paperimage.png":
			file_name="P"
			random_created=pho_paper_ob
		elif lis_ob[0]=="Rock.png":
			file_name="R"#what has occared in the image
			random_created=pho_rock_ob_2
		elif lis_ob[0]=="Sissor.png":
			file_name="S"
			random_created=pho_sissor_ob
		else:
			pass
		labelR=Label(root,image=random_created)
		root.after(43,showlabel)

	count_to+=1
	
def showlabel():
	"""THIS WILL PLACE THE FRIST LABEL IN THE SCREEN"""
	labelR.place(x=308,y=500)
	root.after(33,delet_label)

def witch_co(val):
	"""THIS WILL HELP WITCH BOTTON  IS CLICKED AND WILL PROSSESS IT"""
	global user_enter
	user_enter=val
	root.after(1,showlabel)

bottton_color_is=None
#FOR ROCK
bu=buttonmaker(showlabel,witch_co,"R")#This R is refaring to the botton 
pho=PhotoImage(file="Rock.png")#crating photo object
bu.make_button(pho,bottton_color_is)#and giving the object to the function 
#FOR PAPER
bu2=buttonmaker(showlabel,witch_co,"P")
pho2=PhotoImage(file="Paperimage.png")
bu2.make_button(pho2,bottton_color_is)
#FOR SISSOR
bu3=buttonmaker(showlabel,witch_co,"S")
pho3=PhotoImage(file="Sissor.png")
bu3.make_button(pho3,bottton_color_is)
label_score=Label(root,text="Point ",font=("Comic Sans MS", 14, "bold"),bg="black",fg="white").place(x=300,y=30)
Scoree=Label(root,text=str(your_score),font=("Comic Sans MS", 14, "bold"))
#THIS TWO FUNCTIONS ARE TO ADD SCORE
def delet_sco():
	global Scoree
	Scoree=Label(root,text=str(your_score),font=("Comic Sans MS", 14, "bold"))
	#root.after(3,add_score)
def add_score():
	Scoree.place(x=500,y=30)
	root.after(3,delet_sco)
root.mainloop()
