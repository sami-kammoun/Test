from tkinter import *
from tkinter.messagebox import * # Appel du sous-module boîtes de messages showinfo
import time
######################################
######### Commandes du Menu ##########
######################################

def callback():
    if askyesno('Titre 1', 'Êtes-vous sûr de vouloir faire ça?'):
        showinfo('Titre 2', 'okay')
    else:
        showinfo('Titre 3', 'try again')
def Enregistrer(): # Fonction  de l'appel command=du même nom
    showinfo("Confirmation", "MRIGUEL! :3") #test fonction avec une boite message info
 
def Enregistrersous(): # Fonction  de l'appel command=du même nom
    showinfo("Confirmation", "C'EST BON! ")    #test fonction avec une boite message info
 
def Apropos(): # Fonction  de l'appel command=du même nom
    #nb=len(LisNom)  #test fonction avec une boite message info
    showinfo("A PROPOS", "Gestion de liste simple, coding: utf-8, D A-B, 12/02/2018")    #test fonction avec une boite message info
 
def Trilistcroi(): ##### TRI LA LISTE DE CROISSANT
    temp_list = list(LisNum.get(0, END))#Liste temporaire = Liste
    temp_list.sort()#tri dans l'ordre alphabétique
    LisNum.delete(0, END)#Efface la liste"
    for item in temp_list:#prend toutes les valeurs de la liste temporaire
        LisNum.insert(END, item)#copie dans la liste en partant de la fin
 
def Trilistdec(): ##### TRI LA LISTE DECROISSANT
    temp_list = list(LisNum.get(0, END))#Liste temporaire = Liste
    temp_list.sort()#Ordonne la liste temporaire
    LisNum.delete(0, END)#Efface la liste"
    for item in temp_list:#prend toutes les valeurs de la liste temporaire
        LisNum.insert(0, item)#copie dans la liste en partant du début
 
def DelListe():##### EFFACE LA LISTE
    LisNum.delete(0, END)#Efface toutes les valeurs de la Liste


##########################################
###         COMMANDES FONCTIONS        ###
##########################################    
 
def addEntry () : ##### AJOUTE À LA LISTE LA VARIABLE SAISIE DANS LE CHAMP ENTRÉE
    try:
        LisNum.insert(0, int(ChpNum.get()))#colle la variable entrée au début de la liste
        VarNum.set("")#vide la variable entrée 
    except:
        showinfo('Titre 2', 'donner un entier svp!')
def DelIndex(): ##### EFFACE LA SÉLECTION EN COURS DANS LA LISTE
    try:
        index = LisNum.curselection()#calcule l'index de la selection en cours dans la liste
        LisNum.delete(index)#supprime la sélection correspondante
    except IndexError:
           pass
 
def Modifier(): ##### DÉPLACE LA SÉLECTION EN COURS DANS LA LISTE VERS SAISIE DANS LE CHAMP ENTRÉE
    try:
     index = LisNum.curselection() #calcule l'index de la selection en cours dans la liste
     ChpModif = LisNum.get(index) #affecte un nom à l'index correspondant
     ChpNum.delete(0, 100) #supprime tous les cractères du Champ de saisie"
     ChpNum.insert(0, int(ChpModif))#copie la variable correspondante dans 
     DelIndex() #efface la variable de la liste        
    except:
     showinfo('Titre 2', 'donner un entier svp!')
def tri():
    
    temp_list = list(LisNum.get(0, END))#Liste temporaire = Liste
    temp_list=trirapide(temp_list)#tri dans l'ordre numerique
    LisNum.delete(0, END)#Efface la liste"
    for item in temp_list:#prend toutes les valeurs de la liste temporaire
        LisNum.insert(END, item)#copie dans la liste en partant de la fin

def trirapide(L):
    """trirapide(L): tri rapide (quicksort) de la liste L"""
    def trirap(L, g, d):
        pivot = L[(g+d)//2]
        i = g
        j = d
        while True:
            while L[i]<pivot:
                i+=1
            while L[j]>pivot:
                j-=1
            if i>j:
                break
            if i<j:
                L[i], L[j] = L[j], L[i]
            i+=1
            j-=1
        if g<j:
            trirap(L,g,j)
        if i<d:
            trirap(L,i,d)
 
    g=0
    d=len(L)-1
    trirap(L,g,d)
    return L     
##########################################
###       MISE EN PAGE PRNCIPALE       ###
##########################################
 
W1 = Tk() #Fenêtre principale
W1.title("TRI D'UN TABLEAU                                                                                                                 **REALISE PAR Emna Guermazi**") #Titre 


Zon1W1 = Frame(W1) #Zone1 de mise en page 
Zon1W1.pack() #type de mise page zone1



##################################
######### Barre de Menu ##########
##################################
 
menubar = Menu(W1)
W1.config(menu=menubar)
 
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Enregistrer", command=Enregistrer)
menu1.add_command(label="Enregistrer sous", command=Enregistrersous)
menu1.add_separator()
menu1.add_command(label="Quitter", command=W1.quit)
menubar.add_cascade(label="Sauvegarder", menu=menu1)
 
menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Vider le tableau", command=DelListe)
menu2.add_command(label="Trier ordre croissant", command=Trilistcroi)
menu2.add_command(label="Trier ordre décroissant", command=Trilistdec)
menubar.add_cascade(label="Organiser", menu=menu2)
 
menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=Apropos)
menubar.add_cascade(label="Aide", menu=menu3)
 
##########################################
###           CDES FONCTIONS           ###
##########################################

TitChpNum = Label(Zon1W1, text = 'Nouveau element: ',font=('arial',20,'bold'),fg='#009999', anchor= E, width=20,height=10) # Titre du champ de saisie elt
VarNum=IntVar() # Variable saisie de type texte
TitlisNum = Label(Zon1W1, text = 'Le tableau : ',font=('arial',14,'bold'),fg='#009999', anchor= E, width=20,height=10) # Titre du champ de saisie liste



ChpNum = Entry(Zon1W1, textvariable= VarNum,font=('arial',16,'bold'), width=40, bg ='#fbfbec', fg='#CC33CC')# Champ de saisie Evènement
b1 = Button(Zon1W1,text="Ajouter au tableau",font=('arial',16,'bold'),relief=RAISED,bg="#6699ff",fg='#ff0066', cursor="plus", command=addEntry)
b2 = Button(Zon1W1,text="Supprimer l'element ",font=('arial',12,'bold'),fg='#ff0066',bg="#6699ff",relief=RAISED, cursor="pirate",command=DelIndex)
b3 = Button(Zon1W1,text="Modifier l'element",font=('arial',12,'bold'),fg='#ff0066',relief=RAISED, bg="#6699ff",cursor="exchange",command=Modifier)
b4 = Button(Zon1W1,text="tri  rapide",font=('arial',20,'bold'),bg='#ff0066',relief=RAISED, fg="#6699ff",cursor="heart",command=tri)
ScrListNum = Scrollbar(Zon1W1) #Barre de défilement liste
ScrListNum.grid(column=2,row=1,sticky= 'WNS') #Position barre de défilement
LisNum = Listbox(Zon1W1, yscrollcommand=ScrListNum.set,font=('arial',13,'bold'),width=70, bg ='#fbfbec', fg='#CC0066', height=10)# Liste
LisNum.grid(column=1,row=1,sticky= 'W') # Position de la liste
ScrListNum.config(command=LisNum.yview) # Barre de défilement liste verticale
 
##########################################
###    MISE EN PAGE CDES FONCTIONS     ###
##########################################

 
##Spa1 = Label(Zon1W1).grid(row=0) #Espace1 saut de ligne
##Spa2 = Label(Zon1W1).grid(row=2) #Espace2 saut de ligne
Spa3 = Label(Zon1W1).grid(row=5) #Espace2 saut de ligne
TitChpNum.grid(column=0,row=0) #Position du Label
TitlisNum.grid(column=0,row=1) #Position du Label
ChpNum.grid(column=1,row=0,sticky= 'W',columnspan=3) #Position du champ de saisie
b1.grid(column=2,row=0,padx= 10, sticky= 'W') # Position bouton
b2.grid(column=1,row=4,sticky= 'E') # Position bouton
b3.grid(column=1,row=4,sticky= 'W') # Position bouton
b4.grid(column=1,row=6,sticky= 'W') # Position bouton


W1.mainloop()
