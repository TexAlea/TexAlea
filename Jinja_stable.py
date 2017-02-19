#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Angot Rémi, Lacroix Olivier"
__license__ = "CC-BY-SA"
__version__ = "0.0.0.0.2"
__status__ = "Production"

import jinja2, math, os
from random import *
#from decimal import *
#getcontext().prec = 2  # est ce bien utile désormais puisque l'on a un formatage des prix ?

## personnalisation
dossierModeles = "modeles"


# Variables à regrouper ici quand cela fonctionnera : plus facile à modifier.
def variables(version) :
    """crée toutes les variables aléatoires utiles et retourne un dictionnaire contenant :
        - les variables globales (autres fonctions de ce module, utiles dans jinja, comme terme(), facteur()...),
        - les variables locales à cette fonction comme version (utile pour numéroter les fiches) et toutes les listes de nombres aléatoires ci-dessous).
    """
    N = [randint(1,9) for i in range(100)]
    M = [randint(1,9) for i in range(100)]
    n = [randint(2,9) for i in range(100)]
    m = [randint(2,9) for i in range(100)]
    nZ = [choice([-1,1])*randint(2,9) for i in range(100)]
    mZ = [choice([-1,1])*randint(2,9) for i in range(100)]
    N2 = [randint(1,2) for i in range(100)]
    N3 = [randint(1,3) for i in range(100)]
    N4 = [randint(1,4) for i in range(100)]
    N5 = [randint(1,3) for i in range(100)]
    N6 = [randint(1,6) for i in range(100)]
    N7 = [randint(1,7) for i in range(100)]
    N8 = [randint(1,8) for i in range(100)]
    N9 = [randint(1,9) for i in range(100)]
    Z = [randint(-10,10) for i in range(100)]
    Z2 = [randint(-10,10) for i in range(100)]
    ZE = [choice([-1,1])*randint(1,9) for i in range(100)]
    ZE2 = [choice([-1,1])*randint(1,9) for i in range(100)]
    DCM = [choice([10,100,1000]) for i in range(100)]
    DCM2 = [choice([10,100,1000]) for i in range(100)]
    D = [10*randint(1,9) for i in range(100)]
    S = [choice([-1,1]) for i in range(100)]
    NN = [randint(1,99) for i in range(100)]
    NNN = [randint(1,999) for i in range(100)]
    NNO = [10*randint(1,99) for i in range(100)]
    h = [randint(1,12) for i in range(100)]
    H = [randint(1,24) for i in range(100)]
    min = [randint(1,60) for i in range(100)]
    s = [randint(1,60) for i in range(100)]
    L1=[]
    L2=[]
    L3=[]
    L4=[]
    L = [choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']) for i in range(100)]
    for i in range(100):
        Quatrelettres=sample(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],4)
        L1.append(Quatrelettres[0])
        L2.append(Quatrelettres[1])
        L3.append(Quatrelettres[2])
        L4.append(Quatrelettres[3])
    NNvNN = [round(randint(1,9999)/100,2) for i in range(100)]
    NNvNO = [round(randint(1,999)/10,2) for i in range(100)]
    NvNN = [round(randint(1,999)/100,2) for i in range(100)]
    NvNO = [round(randint(1,99)/10,2) for i in range(100)]
    prenom=[]
    garcon=[]
    fille=[]
    ListeGarcon=['Olivier','Rémi','Christophe','Thibault','Yazid','Nathan','Lucas','Enzo','Léo','Louis','Benjamin','Mathias','Abdel','Karim','Younès','Mehdi','Ethan','Jules','Julien','Pierre']
    ListeFille=['Léa','Emma','Chloé','Inès','Manon','Lola','Jade','Camille','Sarah','Louise','Yasmine','Margot','Maelle','Alicia']
    ListePrenom=ListeGarcon+ListeFille
    for i in range(10):
        prenom.append(choice(ListePrenom))
        garcon.append(choice(ListeGarcon))
        fille.append(choice(ListeFille))


    # Pour spécifier les bornes du nombre aléatoire dans le modèle .tex
    mem=['']*100
    def r(a,b,i) :
        mem[i] = randint(a,b)
        return mem[i]

    var={}
    def alea(a,b,i) :
        var[i] = randint(a,b)
        return var[i]

    # Pour envoyer toutes les variables au modèle
    retour = locals()
    retour.update(globals())
    return retour



# Fonctions de formatage des résultats
def terme(a):
    """Formatage correct de nombre d'une somme.
    Exemple 1 : terme(0) retourne ""
    Exemple 2 : terme(3) retourne "+3"
    Exemple 3 : terme(-4) retourn "-4"
    """
    if a == 0 :
        retour = ""
    elif a > 0 :
        retour = "+" + str(a)
    else :
        retour = a
    return retour # vive le type dynamique de python !!

def facteur(a):
    """Formatage correct de nombre d'un produit.
    Exemple 1 : facteur(2) retourne "2"
    Exemple 2 : facteur(-4) retourne "(-4)"
    """
    if a < 0 :
        retour = "(" + str(a) + ")"
    else :
        retour = a
    return retour # vive le type dynamique de python !!

def prix(a) :
    """Formatage correct d'un prix sous forme d'un nombre décimal avec deux chiffres après la virgule ou sous forme d'un entier si c'est le cas.
    Exemple : prix(3.4) retourne 3,40
    Exemple 2 : prix(
    """
    if int(a) == a :
        retour = a
    else :
        retour = '{0:.2f}'.format(a).replace(".",",")
    return retour

def pint(a) :
    """Retourne la partie entière du nombre fourni
    Raison de la création de cette fonction : jinja ne connaît pas int(...)
    """
    return int(a)

def HMS(h,m,s) :
    """ Formatage d'une durée au format HMS
    """
    retour='$'
    if h!=0 :
        retour+=str(h)+'~\\text{h}~'
    if m!=0 :
        retour+=str(m)+'~\\text{min}~'
    if s!=0 :
        retour+=str(s)+'~\\text{s}'
    retour+='$'
    return retour



# fin fonctions de formatage des résultats.

# fonctions python utiles à ce présent script
def finDeVersion(fichier, version, nombre_de_versions) :
    """Ecriture dans le fichier LaTeX généré des fins de versions"""
    if version!=nombre_de_versions :
        fichier.write('\n')
        fichier.write('%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n')
        fichier.write('\\newpage\n')
        fichier.write('\\setcounter{exo}{0}\n')
        fichier.write('\\setcounter{section}{0}\n')
    else :
        fichier.write('\n')
        fichier.write('\\end{document}')

def listeFichierTexProposes(dossier, indiceInitial) :
    """ affiche et retourne la liste des fichiers .tex du dossier passé en argument (et de ses sous-dossiers) en excluant :
            - les fichiers cachés commençant par un point
            - les fichiers dont le nom se termine par "cor"
            - les fichiers dont le nom se termine par "aleatoirise"
    """
    fichList = [ os.path.join(dossier,f) for f in os.listdir(dossier) if os.path.isfile(os.path.join(dossier, f)) and os.path.splitext(os.path.basename(os.path.join(dossier, f)))[0][0] != "." and os.path.splitext(os.path.basename(os.path.join(dossier, f)))[0][-3:] != "cor" and os.path.splitext(os.path.basename(os.path.join(dossier, f)))[0][-11:] != "aleatoirise" and os.path.splitext(os.path.basename(os.path.join(dossier, f)))[1] == ".tex"]
    dirList = [ d for d in os.listdir(dossier) if os.path.isdir(os.path.join(dossier,d)) and d != ".git" ]
    #print(fichList, dirList)
    j = indiceInitial
    for fichier in fichList :
        print(str(j) + " - " + fichier)
        j = j + 1
    for sousDossier in dirList :
        #print("appel de : listeFichierTexProposes(", os.path.join(dossier,sousDossier) , "," ,j)
        retour = listeFichierTexProposes(os.path.join(dossier,sousDossier), j)
        if retour != [] : # si le sousDossier a des fichiers intéressants.
            fichList = fichList + retour
            j = j + 1
    return fichList

#dossier = "docs"
#print(os.listdir(dossier))
#print([ d for d in os.listdir(dossier) if os.path.isdir(os.path.join(dossier,d) )])
#listeFichierTexProposes(".", 0)
#input("est ce que c bon?")

def choixFichier(dossier) :
    """ propose les fichiers .tex du dossier fourni pour les aléatoiriser
        retourne le nom du fichier choisi par l'utilisateur.
    """
    ReposeLaQuestion = True
    while ReposeLaQuestion :
        listeProposee = listeFichierTexProposes(dossier,0)
        #print(listeProposee)
        nom_fichier_modele=input("Nom du fichier modèle (sans extension) ou numéro de celui-ci :")
        try :
            # teste si un entier correct est fourni :
            numero = int(nom_fichier_modele)
            if numero >=0 and numero < len(listeProposee) :
                nom_fichier_modele = listeProposee[numero][:-4]
                ReposeLaQuestion = False
            else :
                ReposeLaQuestion = True
                print("Ce numéro n'est pas valide !")
        except :
            # teste si la chaine de caractère (non numérique) fournie est un nom de fichier valide.
            if os.path.exists(nom_fichier_modele+".tex") :
                ReposeLaQuestion = False
            else :
                ReposeLaQuestion = True
                print("Ce fichier n'existe pas !")
    return nom_fichier_modele

# fin des fonctions utiles à ce présent script

def traiter(nom_fichier_modele , chemin, nombre_de_versions) :
    """ Traitement par Jinja du fichier modèle.
    Retourne un texte d'information sur les actions réalisées :
    - présence ou non du préambule personnalisé,
    - présence ou non du corrigé correspondant.
    """
    retour = ""
    # paramètres Jinja
    env = jinja2.Environment(
        block_start_string = '##',
        block_end_string = '##',
        variable_start_string = '<<',
        variable_end_string = '>>',
        comment_start_string = '\#{',
        comment_end_string = '}',
        line_statement_prefix = '%%',
        line_comment_prefix = '%#',
        trim_blocks = True,
        autoescape = False,
        loader=jinja2.FileSystemLoader(".")
    )
    dossierDestination = "fichiers-aleatoirises"
    if not os.path.exists(dossierDestination) :
        os.mkdir(dossierDestination)
    nomfichier=nom_fichier_modele+"_aleatoirise.tex"
    #print(os.path.join(chemin,nom_fichier_modele+".tex")," parent= ", chemin)
    template = env.get_template(os.path.join(chemin,nom_fichier_modele+".tex"), parent=chemin)
    if __name__ == "__main__":
        f = open(os.path.join(dossierDestination, nomfichier), "w",encoding="utf8")
    else :
        f = open(os.path.join(chemin,nomfichier), "w",encoding="utf8")
    # prise en compte d'un éventuel préambule personnalisé dans le dossier.
    nom_fichier_preambule = "preambule-perso.tex"
    if os.path.exists(os.path.join(chemin, nom_fichier_preambule)) :
        retour = "Prise en compte du preambule-perso.tex. "
        file = open(os.path.join(chemin , nom_fichier_preambule), "r",encoding="utf8")
        preambule_personnalise = file.read()
        file.close()
    else :
        preambule_personnalise = '\\documentclass[a4paper,11pt,fleqn]{article}\n\\input{preambule}\n\\begin{document}\n\\pagestyle{empty}\n\n\n'
    f.write(preambule_personnalise)
    # fin prise en compte du préambule personnalisé.
    # prise en compte optionnelle du corrigé personnalisé.
    nom_fichier_corrige = nom_fichier_modele + "-cor.tex"
    presenceDuCorrige = os.path.exists(os.path.join(chemin, nom_fichier_corrige))
    if presenceDuCorrige :
        nomFichierCorrige=nom_fichier_modele+"_aleatoirise-cor.tex"
        templatecor = env.get_template(os.path.join(chemin, nom_fichier_corrige))
        if __name__ == "__main__":
            fcor = open(os.path.join(dossierDestination, nomFichierCorrige), "w",encoding="utf8")
        else :
            fcor = open(os.path.join(chemin, nomFichierCorrige), "w",encoding="utf8")
        fcor.write(preambule_personnalise)
    # RENDU DES VERSIONS DEMANDEES
    for version in range(1,nombre_de_versions+1) :
        # rendu
        dictVariables = variables(version)
        f.write(template.render(**dictVariables))
        finDeVersion(f, version, nombre_de_versions)
        if presenceDuCorrige :
            fcor.write(templatecor.render(**dictVariables))
            finDeVersion(fcor, version, nombre_de_versions)
    retour = retour + "Création du fichier aléatoirisé en " +str( nombre_de_versions) + " version(s) réalisée. "
    f.close()
    if presenceDuCorrige :
        retour = retour + "Création du fichier corrigé correspondant."
        fcor.close()
    return retour


# version non GUI :
if __name__ == "__main__":
    # Demande le modele en proposant les noms de fichiers valides du dossier courant :
    nomFichierModele = choixFichier(dossierModeles) # pour l'instant, on ne propose que le dossier courant
    print("Fichier choisi : ",nomFichierModele)
    nombreVersions=int(input("Nombre d'exemplaires souhaités :"))
    (filepath, filename) = os.path.split(nomFichierModele)
    #print(filename, "/", filepath, "/" , nombreVersions)
    print(traiter(filename, filepath, nombreVersions))
