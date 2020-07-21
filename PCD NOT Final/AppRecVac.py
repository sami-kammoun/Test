from tkinter import *
import os
import shutil
from tkinter.filedialog import askopenfilename
import tkinter.filedialog as tkFileDialog

class Interface(Frame):
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, **kwargs)
        self.pack(fill=X, side=BOTTOM)
        self.path = "C:/Users/samso/OneDrive/Bureau/pcd_v1/"
        self.list_name = {}
        
        self.champ_label = Label(self, text="Bonjour dans notre application de reconnaissance faciale !")
        self.champ_label.grid(row=0, columnspan=12)

        self.var_nom = StringVar()
        self.var_nom.set("Nom & Prénom")
        self.ligne_nom = Entry(self, textvariable = self.var_nom, width=15)
        self.ligne_nom.grid(row=1, column=6, columnspan=3, sticky=W+E)

        self.var_path_add = StringVar()
        self.var_path_add.set("Path du dossier des images à ajouter")
        self.ligne_path_add = Entry(self, textvariable=self.var_path_add, width=30)
        self.ligne_path_add.grid(row=1, column=0, columnspan=3, sticky=W+E)

        self.bouton_parc1 = Button(self, text="Parcourir", command=self.parc_add)
        self.bouton_parc1.grid(row=1, column=3, columnspan=3, sticky=W+E)
        
        self.bouton_add = Button(self, text="ADD", command=self.add)
        self.bouton_add.grid(row=1, column=9, columnspan=3, sticky=W+E)

        self.bouton_embed = Button(self, text="Embed", command=self.embed)
        self.bouton_embed.grid(row=3, column=0,columnspan=4, sticky=W+E)
        
        self.bouton_train = Button(self, text="Train", command=self.train)
        self.bouton_train.grid(row=3, column=4,columnspan=4, sticky=W+E)

        self.bouton_redo = Button(self, text="Delete", command=self.delete)
        self.bouton_redo.grid(row=3, column=8,columnspan=4, sticky=W+E)
        
        self.var_path_detect = StringVar()
        self.var_path_detect.set("Path de l'image ou la video")
        self.ligne_path_detect = Entry(self, textvariable=self.var_path_detect, width=30)
        self.ligne_path_detect.grid(row=2, column=0, columnspan=3, sticky=W+E)

        self.bouton_parc2 = Button(self, text="Parcourir", command=self.parc_det)
        self.bouton_parc2.grid(row=2, column=3, columnspan=3, sticky=W+E)

        self.bouton_detect_photo = Button(self, text="Detect photo", command=self.det_photo)
        self.bouton_detect_photo.grid(row=2, column=6, columnspan=3, sticky=W+E)

        self.bouton_detect_video = Button(self, text="Detect video", command=self.det_vid)
        self.bouton_detect_video.grid(row=2, column=9, sticky=W+E)

    def parc_add(self):
        self.var_path_add.set(tkFileDialog.askdirectory(initialdir='C:/'))
    
    def parc_det(self):
        self.var_path_detect.set(askopenfilename())
    
    def add(self):
        personne = self.var_nom.get()
        path_to_your_files = self.var_path_add.get()
        copy_to_path = self.path+'dataset/'+ personne
        if not os.path.exists(copy_to_path):
            os.makedirs(copy_to_path)
            self.list_name[personne]=0
        os.system('python '+self.path+'Add_path.py --ptyf '+path_to_your_files+' --ctp '+copy_to_path)
        print('python '+self.path+'Add_path.py --ptyf '+path_to_your_files+' --ctp '+copy_to_path)
        self.list_name[personne]+=len([name for name in os.listdir(path_to_your_files) if os.path.isfile(name)])

    def embed(self):
        os.system('python '+self.path+'extract_embeddings.py --dataset '+self.path+'dataset --embeddings '+self.path+'output/embeddings.pickle --detector '+self.path+'face_detection_model --embedding-model '+self.path+'openface_nn4.small2.v1.t7')

    def det_photo(self):
        print('python '+self.path+'recognize.py --detector '+self.path+'face_detection_model --embedding-model '+self.path+'openface_nn4.small2.v1.t7 --recognizer '+self.path+'output/recognizer.pickle --le '+self.path+'output/le.pickle --image '+self.var_path_detect.get())
        os.system('python '+self.path+'recognize.py --detector '+self.path+'face_detection_model --embedding-model '+self.path+'openface_nn4.small2.v1.t7 --recognizer '+self.path+'output/recognizer.pickle --le '+self.path+'output/le.pickle --image '+self.var_path_detect.get())

    def det_vid(self):
        os.system('python '+self.path+'recognize_video.py --detector '+self.path+'face_detection_model --embedding-model '+self.path+'openface_nn4.small2.v1.t7 --recognizer '+self.path+'output/recognizer.pickle --le '+self.path+'output/le.pickle --video '+self.var_path_detect.get())

    def train(self):
        os.system('python '+self.path+'train_model.py --embeddings '+self.path+'output/embeddings.pickle --recognizer '+self.path+'output/recognizer.pickle --le '+self.path+'output/le.pickle')
    
    def delete(self):
        folder = self.path+'output'
        os.system('python '+self.path+'delete_all.py --folder '+folder)

fenetre = Tk()
fenetre.title("Application de reconnaissance faciale")
interface = Interface(fenetre)

interface.mainloop()

interface.quit()
