"""Premier exemple avec Tkinter.

On crée une fenêtre simple qui souhaite la bienvenue à l'utilisateur.

"""

# On importe Tkinter
from tkinter import *

class Interface(Frame):
    
    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""
    
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, **kwargs)
        self.pack(fill=BOTH)
        self.nb_clic = 0
        
        # On crée un label (ligne de texte) souhaitant la bienvenue
        # Note : le premier paramètre passé au constructeur de Label est notre
        # interface racine
        self.champ_label = Label(self, text="Bonjour dans notre application de reconnaissance faciale !")

        # On affiche le label dans la fenêtre
        self.champ_label.pack()

        self.var_case = IntVar()
        self.case = Checkbutton(self, text="Ne plus poser cette question", variable=self.var_case)
        self.case.pack()



        self.var_choix = StringVar()

        self.choix_rouge = Radiobutton(self, text="Rouge", variable=self.var_choix, value="rouge")
        self.choix_vert = Radiobutton(self, text="Vert", variable=self.var_choix, value="vert")
        self.choix_bleu = Radiobutton(self, text="Bleu", variable=self.var_choix, value="bleu")

        self.choix_rouge.pack()
        self.choix_vert.pack()
        self.choix_bleu.pack()




        self.var_texte = StringVar()
        self.ligne_texte = Entry(self, textvariable=self.var_texte, width=30)
        self.ligne_texte.pack()

        self.cadre = Frame(self, width=768, height=576, borderwidth=1)
        self.cadre.pack(fill=BOTH)

        self.message = Label(self.cadre, text="Notre fenêtre")
        self.message.pack(side="top", fill=X)

        self.bouton_quitter = Button(self, text="Quitter", command=self.clickQuiter)
        self.bouton_quitter.pack()
        # On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
    
##    def cliquer(self):
##        """Il y a eu un clic sur le bouton.
##        
##        On change la valeur du label message."""
##        
##        self.nb_clic += 1
##        self.message["text"] = "Vous avez cliqué {} fois.".format(self.nb_clic)
##
    def clickQuiter(self):
        self.ligne_texte["textvariable"] = self.var_choix
        print("i m doing s.th")
# On crée une fenêtre, racine de notre interface
fenetre = Tk()
interface = Interface(fenetre)

interface.mainloop()
interface.destroy()
