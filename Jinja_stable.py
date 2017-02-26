#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Angot Rémi, Lacroix Olivier"
__license__ = "CC-BY-SA"
__version__ = "0.0.0.0.2"
__status__ = "Production"

import jinja2, math, os
from random import *
from decimal import *

## personnalisation
dossierModeles = "modeles"
memoiredesordres=[]


# Variables à regrouper ici quand cela fonctionnera : plus facile à modifier.
def variables(version) :
    """crée toutes les variables aléatoires utiles et retourne un dictionnaire contenant :
        - les variables globales (autres fonctions de ce module, utiles dans jinja, comme terme(), facteur()...),
        - les variables locales à cette fonction comme version (utile pour numéroter les fiches) et toutes les listes de nombres aléatoires ci-dessous).

        Arguments : un entier (version) correspondant à la version du document créé.
                    un dictionnaire des variables locales définies dans les fichiers personnalisés.
    """

    N = [randint(1,9) for i in range(100)]
    M = [randint(1,9) for i in range(100)]
    n = [randint(2,9) for i in range(100)]
    #m = [randint(2,9) for i in range(100)]
    m=['' for i in range(100)]
    for i in range(100):
        m[i]=randint(2,9)
        while m[i]==n[i]:
            m[i]=randint(2,9)   
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
    L5=[]
    L6=[]
    L7=[]
    L8=[]
    L = [choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']) for i in range(100)]
    for i in range(100):
        Quatrelettres=sample(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],8)
        L1.append(Quatrelettres[0])
        L2.append(Quatrelettres[1])
        L3.append(Quatrelettres[2])
        L4.append(Quatrelettres[3])
        L5.append(Quatrelettres[4])
        L6.append(Quatrelettres[5])
        L7.append(Quatrelettres[6])
        L8.append(Quatrelettres[7])
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
    
    # Pour créer des variables dans le modèle .tex
  

    var={}
    def alea(a,b,nom='nepasmemoriser') : # Avec <<var[nom]>> on pourra récupérer la valeur d'un entier aléatoire entre a et b
        if nom=='nepasmemoriser':
            return randint(a,b)
        else:
            var[nom] = randint(a,b)
            return var[nom]

    def aleadecimal(nom) : # Un nombre décimal dont la partie entière a 1 à 3 chiffres et la partie décimale a 1 à 3 chiffres
        var[nom] = Decimal(str(randint(1,10**randint(1,3)))+'.'+str(randint(1,10**randint(1,3))))
        return var[str(nom)]

    def affectealeadecimal(nom):
        aleadecimal(nom)
        return ''

    def affecte(valeur,nom) :
        var[nom] = valeur
        return ''

    # Pour envoyer toutes les variables au modèle
    # regroupement dans un seul dictionnaire retour de toutes les fonctions et variables définies ici.
    # => utilisables dans la fonction traiter(...)
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
        retour = str(a).replace('.0','')
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

def ecriture_decimale(d,type=1):
    d=str(d)
    partie_decimale=Decimal(d)%1
    partie_entiere=round(Decimal(d)-partie_decimale)
    puissance=len(str(partie_decimale))-2
    if partie_decimale==0:
        retour=('\\nombre{'+d+'}').replace('.0','')
    else :
        if type==2:
            retour='\\dfrac{\\nombre{'+d.replace('.','')+'}}{\\nombre{'+str(10**puissance)+'}}'
        elif type==3:
            retour=str(partie_entiere)+'+\\dfrac{\\nombre{'+str(partie_decimale).replace('0.','')+'}}{\\nombre{'+str(10**puissance)+'}}'
        else :
            retour='\\nombre{'+d+'}'
    return retour

def rearrangement(l):
    liste = sample([i for i in range(1,l+1)],l)
    return liste



def melanger(liste):
    ordre=rearrangement(len(liste))
    memoiredesordres.append(ordre)
    listemelangee = [ liste[i-1] for i in ordre]
    retour=' '.join(listemelangee)
    print(memoiredesordres)
    return retour

def melanger_corr(liste):
    ordre=memoiredesordres[0]
    del memoiredesordres[0]
    listemelangee = [ liste[i-1] for i in ordre]
    retour=' '.join(listemelangee)
    print(memoiredesordres)
    return retour


def melangeritemize(liste):
    ordre=rearrangement(len(liste))
    memoiredesordres.append(ordre)
    listemelangee = [ liste[i-1] for i in ordre]
    retour='\n\\begin{itemize}\n    \\item '
    retour+='\n    \\item '.join(listemelangee)
    retour+='\n\\end{itemize} \n'   
    return retour

def melangeritemize_corr(liste):
    ordre=memoiredesordres[0]
    del memoiredesordres[0]
    listemelangee = [ liste[i-1] for i in ordre]
    retour='\n\\begin{itemize}\n    \\item '
    retour+='\n    \\item '.join(listemelangee)
    retour+='\n\\end{itemize} \n'   
    return retour

def melangerenumerate(liste):
    ordre=rearrangement(len(liste))
    memoiredesordres.append(ordre)
    listemelangee = [ liste[i-1] for i in ordre]
    retour='\n\\begin{enumerate}\n    \\item '
    retour+='\n    \\item '.join(listemelangee)
    retour+='\n\\end{enumerate} \n'   
    return retour

def melangerenumerate_corr(liste):
    ordre=memoiredesordres[0]
    del memoiredesordres[0]
    listemelangee = [ liste[i-1] for i in ordre]
    retour='\n\\begin{enumerate}\n    \\item '
    retour+='\n    \\item '.join(listemelangee)
    retour+='\n\\end{enumerate} \n'   
    return retour

def melangernewline(l):
    ordre=memoiredesordres[0]
    del memoiredesordres[0]
    listemelangee = [ liste[i-1] for i in ordre]
    retour='\\\\\n'.join(listemelangee)   
    return retour

def melangerhfill(l):
    ordre=memoiredesordres[0]
    del memoiredesordres[0]
    listemelangee = [ liste[i-1] for i in ordre]
    retour='\\hfill '.join(l)   
    return retour


# fin fonctions de formatage des résultats.

# fonctions python de personnalisation : un sujet par élève d'une classe  
def eleve(classe, version):
    """Pré requis : la variable "classe" doit être définie quelque part :
        - dans le document LaTeX sous la forme
            %% set classe="6ème 3"
        - dans un des scripts personnalisés : variables_perso.py sous la forme :
            classe = "6ème 3"
        Retourne le nom de l'élève correspondant au numéro de version fourni pour la classe fournie.
        Si la classe n'existe pas ou si la liste est plus courte que "version", retourne "".
    """
    global classes
    #print("FUSION" , locals())
    if classe in classes :
        listeEleves = classes[classe]
        #print(classe, version, listeEleves)
        if version <= len(listeEleves) :
            retour = listeEleves[version-1]
        else :
            retour = ""
    else :
        retour = ""
    return retour
# FIN des fonctions python de personnalisation : un sujet par élève d'une classe


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
        print(str(j) + " - " + fichier[8:])
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

def choixNbreVersions() :
    """ retourne un entier correspondant au nombre de versions choisies :
        1. soit par saisie d'un entier par l'utilisateur
        2. soit par recherche du nom de la classe dans la liste des classes présentes. Retourne automatiquement le nombre d'élèves.
    """
    global classes, dictLocals
    # lecture des variables personnalisées d'un fichier général variables_perso.py
    dictGlobals = {}
    dictLocals = {}
    if os.path.exists("variables_perso.py") :
        exec(open("variables_perso.py",encoding="utf8").read(), dictGlobals, dictLocals)
        print("Prise en compte du fichier variables_perso.py")
        globals().update(dictLocals)
    # choix utilisateur
    ReposeLaQuestion = True
    while ReposeLaQuestion :
        # affiche les classes disponibles
        for niemeClasse in classes.keys() :
            print(" - " , str(niemeClasse)) 
        nombre=input("Nombre d'exemplaires souhaités ou classe choisie (parmi ci-dessus) :")
        try :
            # teste si un entier correct est fourni :
            numero = int(nombre)
            if numero >=0 :
                retour = numero
                dictLocals["classe"] = "" # pour éviter des erreurs si la variable classe est absente du document LaTeX et que l'on demande .
                ReposeLaQuestion = False
            else :
                print("Ce nombre n'est pas valide car négatif !")
        except :
            if nombre in classes :
                dictLocals["classe"] = nombre
                retour = len(classes[nombre])
                ReposeLaQuestion = False
            else :
                print("La 'classe' n'existe pas : saisir un nombre entier ou un nom de classe valide.")
    return retour

# fin des fonctions utiles à ce présent script

def traiter(nom_fichier_modele , chemin, nombre_de_versions) :
    """ Traitement par Jinja du fichier modèle.
    Retourne un texte d'information sur les actions réalisées :
    - présence ou non du préambule personnalisé,
    - présence ou non du corrigé correspondant.
    """
    global classes, dictLocals
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
    print("Fichier choisi : " , os.path.join(chemin,nom_fichier_modele+".tex").replace("\\","/"))
    template = env.get_template(os.path.join(chemin,nom_fichier_modele+".tex").replace("\\","/"), parent=chemin.replace("\\","/"))
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
        templatecor = env.get_template(os.path.join(chemin, nom_fichier_corrige).replace("\\","/"))
        if __name__ == "__main__":
            fcor = open(os.path.join(dossierDestination, nomFichierCorrige), "w",encoding="utf8")
        else :
            fcor = open(os.path.join(chemin, nomFichierCorrige), "w",encoding="utf8")
        fcor.write(preambule_personnalise)
    # lecture de variables d'un fichier python .py de même nom que le fichier .tex
    dictGlobals = {}
    if os.path.exists(os.path.join(chemin,nom_fichier_modele+".py")) :
        exec(open(os.path.join(chemin,nom_fichier_modele+".py"),encoding="utf8").read(), dictGlobals, dictLocals)
        print("Prise en compte du fichier ",os.path.join(chemin,nom_fichier_modele+".py"))

    # RENDU DES VERSIONS DEMANDEES
    for version in range(1,nombre_de_versions+1) :
        # récupération des variables standards
        dictVariables = variables(version)
        # mise à jour du dictionnaire de variables afin de disposer de tout.
        dictVariables.update(dictLocals)
        # cas spécifique de la variable classes
        classes = dictLocals["classes"]
        #print(dictVariables)
        # création du rendu
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
    classes = {}# variable globale juste intialisée.
    dictLocals = {}# variable globale juste intialisée.
    # Demande le modele en proposant les noms de fichiers valides du dossier courant :
    if os.path.exists(dossierModeles): 
        nomFichierModele = choixFichier(dossierModeles) # pour l'instant, on ne propose que le dossier courant
        print("Fichier choisi : ",nomFichierModele)
        nombreVersions=choixNbreVersions()
        print("Nombre de versions choisies :",nombreVersions)
        (filepath, filename) = os.path.split(nomFichierModele)
        #print(filename, "/", filepath, "/" , nombreVersions)
        print(traiter(filename, filepath, nombreVersions))
    else :
        print("Pas de dossier 'modeles' dans le dossier courant du script.")
