#Deepjyoti karmakar
#i think there is some problem and i will fix it 
from tkinter import Button,Label,PhotoImage,Tk,Frame,messagebox 
from random import randint,shuffle
from time import sleep
from pygame import mixer,init

root=Tk()
root.title("Rock Paper Sissor")
mixer.init()
init()
root.geometry("899x1899")
frame_button=Frame(root).pack(side="bottom")
class buttonmaker:
	def __init__(self,command2,command_name,witchc):
		self.witchc=witchc
		self.command_name=command_name
		self.command2=command2
	def make_button(self,file_name):
		self.file_name=file_name#file name
		butto=Button(frame_button,image=self.file_name,bd=23,command=lambda c=self.witchc: [self.command_name(c),self.command2]).pack(side="left",anchor="s")
def play_Boo():
	""""WILL PLAY THE BOO SOUND"""
	mixer.music.load("Boo.mp3")
	mixer.music.play()
def play_aplause():
	"""WILL PLAY APLAUSE"""
	mixer.music.load("Applause.mp3")
	mixer.music.play()
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
	global show_heighst,text_re
	with open("/storage/emulated/0/MyTKINTER PROJECTS/GUIROCKPAPERSISSOR/Score.txt","r")as re:
		text_re=re.read()
		if int(text_re)<your_score:
			with open("/storage/emulated/0/MyTKINTER PROJECTS/GUIROCKPAPERSISSOR/Score.txt","w")as wr:
				la=Label(root,text="hel").pack()
				wr.write(str(your_score-1))
				if show_heighst==0:
					messagebox.showinfo("ROCKPAPERSISSOR", "highest score") 
					show_heighst+=1
label_high_score=Label(root,text="HighScore",fg="white",bg="black",font=("Comic Sans MS", 11, "bold")).place(x=260,y=5)
with open("/storage/emulated/0/MyTKINTER PROJECTS/GUIROCKPAPERSISSOR/Score.txt","r") as kk:
	kk2=kk.read()
highst_score=Label(root,text=str(kk2),fg="black",font=("Comic Sans MS", 11, "bold")).place(x=560,y=5)
#show function
def youwon():
	root.config(bg="green")
def youloose():
	root.config(bg="red")
def draw():
	root.config(bg="orange")
count_to=0
your_score=1
my_bg="white"
def delet_label():
	"""THIS WILL DELETE THE PREVIOUS IMAGE AND LERP GOING"""
	global labelR,random_created,count_to,file_name,my_bg,your_score
	lis_ob=["Paperimage.png","Rock.png","Sissor.png"]
	shuffle(lis_ob)
	lab0=creatPho(lis_ob[0])
	kk=Label(root,image=lab0)
	if count_to==30:
		count_to=0
		#lad=Label(root,text=user_enter).pack()
		#user_enter==capital file_name or random appearance is ==small
		if user_enter==file_name:
			draw()
			bottton_color_is="orange"
			my_bg="orange"
		elif user_enter=="R":
			if file_name=="P":
				youloose()
				my_bg="red"
				play_Boo()
			elif  file_name=="S":
				youwon()
				add_score()
				play_aplause()
				your_score+=1#will count score
				my_bg="green"
				show_heighst_score()
		elif user_enter=="P":
			if file_name=="R":
				youwon()
				add_score()
				play_aplause()
				your_score+=1
				my_bg="green"
				show_heighst_score()
			elif file_name=="S":
				youloose()
				my_bg="red"
				play_Boo()
		elif user_enter=="S":
			if file_name=="P":
				youwon()
				add_score()
				play_aplause()
				your_score+=1
				my_bg="green"
				show_heighst_score()
			elif file_name=="R":
				youloose()
				my_bg="red"
				play_Boo()
		else:
			pass
			
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
		labelR=Label(root,image=random_created,bg=my_bg)
		root.after(30,showlabel)

	count_to+=1
	
def showlabel():
	"""THIS WILL PLACE THE FRIST LABEL IN THE SCREEN"""
	labelR.place(x=308,y=500)
	root.after(30,delet_label)

def witch_co(val):
	"""THIS WILL HELP WITCH BOTTON  IS CLICKED AND WILL PROSSESS IT"""
	global user_enter
	user_enter=val
	root.after(1,showlabel)

#FOR ROCK
bu=buttonmaker(showlabel,witch_co,"R")#This R is refaring to the botton 
pho=PhotoImage(file="Rock.png")#crating photo object
bu.make_button(pho)#and giving the object to the function 
#FOR PAPER
bu2=buttonmaker(showlabel,witch_co,"P")
pho2=PhotoImage(file="Paperimage.png")
bu2.make_button(pho2)
#FOR SISSOR
bu3=buttonmaker(showlabel,witch_co,"S")
pho3=PhotoImage(file="Sissor.png")
bu3.make_button(pho3)
label_score=Label(root,text="Point ",font=("Comic Sans MS", 14, "bold"),bg="black",fg="white").place(x=300,y=88)
Scoree=Label(root,text=str(your_score),font=("Comic Sans MS", 14, "bold"))
#THIS TWO FUNCTIONS ARE TO ADD SCORE
lab_del=Label(root,text="0",font=("Comic Sans MS", 14, "bold")).place(x=500,y=88)
def delet_sco():
	global Scoree
	Scoree=Label(root,text=str(your_score),font=("Comic Sans MS", 14, "bold"))
	#root.after(3,add_score)
def add_score():
	global lab_del
	if your_score==1:
		score2=Label(root,text="1",font=("Comic Sans MS", 14, "bold")).place(x=500,y=88)
		root.after(1,delet_sco)
	else:
		Scoree.place(x=500,y=88)
		root.after(1,delet_sco)
root.mainloop()
