#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Angot Rémi, Lacroix Olivier"
__license__ = "CC-BY-SA"
__version__ = "0.0.0.0.2"
__status__ = "Production"

from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from Jinja_stable import *
from subprocess import *

def ouvrir():#fonction qui sélectionne le fichier 
    #cadre.delete()
    file_name = ""
    file_name = askopenfilename(filetypes=[("Fichier LaTeX", ("*.tex")),("Tous", ("*"))])#on choisit le modèle
    #cadre.update()
    #topframe.pack()
    if file_name != "" :
        # suppression du .tex si présent en extension pour assurer la compatibilité avec les fonctions métiers existantes
        if file_name[-4:] == ".tex" :
            file_name = file_name[:-4]
        monFichier.configure(text = file_name)
        monFichier.grid(row = 0)
        maZoneDeSaisieLabel.grid(row=1, column=0)
        maZoneDeSaisie.grid(row=1,column=1 )
        b2.grid(row=0,column=1 )
    else :
        monFichier.grid_forget()
        maZoneDeSaisieLabel.grid_forget()
        maZoneDeSaisie.grid_forget()
        b2.grid_forget()
        maZoneDeMessages.grid_forget()
    topframe.pack(side=TOP)
    bottomframe.pack(side=BOTTOM)
    app.update()

def generer():
    retourFonction = ""
    if maZoneDeSaisie.get() == "" :
        maZoneDeSaisie.delete(0,END)
        maZoneDeSaisie.insert(0, "1")
        app.update()
    nom = monFichier.cget("text")
    (filepath, filename) = os.path.split(nom)
    nbre = int(maZoneDeSaisie.get())
    print(traiter(filename,filepath, nbre))
    try :
        retourFonction = traiter(filename,filepath, nbre)
        generationOK = True
    except :
        retourFonction = "Une erreur s'est produite en exécutant le modèle fourni"
        generationOK = False
    ## Bouton de compilation à activer quand la compilation fonctionnera via un subprocess.call ou autre dans la fonction compilerListe(...) ci-dessous...
    ## if generationOK :
        ## b3.grid(row=0,column=2 )
    alimenterMaZoneDeMessages(retourFonction + "\n")
    maZoneDeMessages.grid(row=2)
    topframe.pack(side=TOP)
    app.update()

def compiler():
    nom = monFichier.cget("text")
    listeFichiers = [ nom + "_aleatoirise.tex" ]
    (filepath, filename) = os.path.split(nom)
    corrigePotentiel = os.path.join(filepath, filename + "_aleatoirise-cor.tex")
    if os.path.exists(corrigePotentiel) :
        # le corrigé est présent, on le compile aussi
        listeFichiers.append(corrigePotentiel)
    compilerListe(listeFichiers)
        
 
def compilerListe(listeFichiers):
    #à faire fonctionner sous windows : comment trouver pdflatex ?
    i = 0
    while i < len(listeFichiers) :
        (filepath, filename) = os.path.split(listeFichiers[i])
        alimenterMaZoneDeMessages(" Compilation de " + filename + ".\n")
        maZoneDeMessages.update()
        os.chdir(filepath)
        ### LIGNE A PROBLEME : la compilation ne fonctionne pas. Est ce à cause des espaces dans le nom de dossier, ou autre ? 
        result = run(["pdflatex", "-output-directory=" + filepath, listeFichiers[i]], shell=True, check=True)
        print(result)
        i = i + 1
    alimenterMaZoneDeMessages(" Compilation(s) avec pdflatex effectuée(s).")
    maZoneDeMessages.update()
    app.update()

def alimenterMaZoneDeMessages(texteSupplementaire) :
    texteActuel = maZoneDeMessages.cget("text")
    maZoneDeMessages.configure(text=texteActuel + texteSupplementaire)

def modifieLeTexte(event) :
    motSaisi = maZoneDeSaisie.get()
    try :
        if motSaisi != "" :
            nombreEntier = int(motSaisi)
    except :
        maZoneDeSaisie.delete(0,END)
        maZoneDeSaisie.insert(0, "1")
    #maZoneDeSaisie.grid(row=1,column=1 )
    #maZoneDeSaisie.update()
    #topframe.update()
    app.update()

#---------------------------main--------------------------------------

## TESTS EN COURS : aucun concluant pour compiler
##args = ' -output-directory=/Users/Olivier/ /Users/Olivier/Dropbox/exemples-formatage-python_aleatoirise.tex'
##print(args)
##print(call ('pdflatex /Users/Olivier/Dropbox/exemples-formatage-python_aleatoirise.tex', shell=True))


app=Tk()
app.title("Jinja : création de sujets-corrigés aléatoires à partir de modèles.")
 
topframe= Frame(app, borderwidth=2, relief=GROOVE)#un frame pour afficher le nom du fichier sélectionné et le nombre choisi
monFichier = Label(topframe, text="")
maZoneDeSaisieLabel = Label(topframe, text="Saisir le nombre d'exemplaires souhaités :")
maZoneDeSaisie = Entry(topframe)
maZoneDeSaisie.bind("<Any-KeyRelease>", modifieLeTexte)
maZoneDeMessages = Label(topframe, text="")
topframe.pack(side=TOP)
 
bottomframe= Frame(app, borderwidth=2, relief=GROOVE)# un frame pour les boutton
bottomframe.pack(side=BOTTOM)
 
b1 = Button(bottomframe, text = "Sélectionner", command = ouvrir)
b1.grid(row=0,column=0 )
 
b2 = Button(bottomframe, text = "Générer", command = generer)

b3 = Button(bottomframe, text = "Compiler", command = compiler)

app.update()
app.mainloop()
