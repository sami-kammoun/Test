from tkinter import *
import os
import shutil
from tkinter.filedialog import askopenfilename
import tkinter.filedialog as tkFileDialog

class Interface(Frame):
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, **kwargs)
        self.pack(fill=X, side=BOTTOM)

        list_name = {}
        
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
        
        self.bouton_train = Button(self, text="Train", command=self.quit)
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
        self.var_path_add.set(tkFileDialog.askdirectory(initialdir='c:/'))
    
    def parc_det(self):
        self.var_path_detect.set(askopenfilename())
    
    def add(name,path):
        path_to_your_files = path
        copy_to_path = "C:/Users/samso/OneDrive/Bureau/pcd_v1/dataset"+name
        
        ##'destination for your copy'
        
        files_list = sorted(os.listdir(path_to_your_files))
        orders = range(1, len(files_list) , 1)

        for order in orders:
            files = files_list[order] 
            shutil.copyfile(os.path.join(path_to_your_files, files), os.path.join(copy_to_path, files))  # copying images to destination folder

    def embed(self):
        os.system('python extract_embeddings.py --dataset dataset --embeddings output/embeddings.pickle --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7')

    def det_photo(path):
        os.system('')

    def det_vid(path):
        os.system('')

    def delete():
        return null
    

fenetre = Tk()
fenetre.title("Application de reconnaissance faciale")
interface = Interface(fenetre)

interface.mainloop()

interface.quit()
