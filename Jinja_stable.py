#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Angot Rémi, Lacroix Olivier"
__license__ = "CC-BY-SA"
__version__ = "0.0.0.0.6"
__status__ = "Production"

import jinja2, math, os
from random import *
from decimal import *

## personnalisation
dossierModeles = "modeles"
memoiredesordres=[]

class listeAleatoire(list) :
    """Classe définissant un objet list étendu par un remplissage aléatoire de nombres lors de l'instanciation.
    Les nombres ajoutés à la liste sont compris entre a et b entiers, avec un incrément à préciser.
    Facultatif : une liste de valeurs à supprimer (par exemple [0]), la longueur de la liste à générer (par défaut 100).
    """
    def __init__(self,a,b,increment=1,listeASupprimer=[],nbreValeursSouhaitees=100) :
        #list.__init__(self)
        #self.append(10)
        nombreDeValeurs = int((b-a)/increment+1)
        if nombreDeValeurs >= 2 : # en dessous de deux valeurs, on ne remplit pas.
            if nombreDeValeurs == 2 : # s'il n'y a que deux valeurs, on utilise un alea réel
                for i in range(nbreValeursSouhaitees) :
                    super().append(choice([a,b]))
            else :
                while len(self) < nbreValeursSouhaitees :
                    L = []
                    for i in range(a,b+1,increment) :
                        L.append(i)
                    for aEliminer in listeASupprimer :
                        if aEliminer in L :
                            L.remove(aEliminer)
                    shuffle(L)
                    del L[101:]
                    super().extend(L)
        else :
            print("Nombre de valeurs incorrect : ", nombreDeValeurs)
                    
# position d'un point tikz à partir d'une valeur d'angle
def pointPosition(angleFourni) :
    """ retourne une position tikz valide en fonction de l'angle fourni, en degrés."""
    angle = angleFourni%360
    if angle < 22.5 :
        return "right"
    elif angle < 90 - 22.5 :
        return "above right"
    elif angle < 135 - 22.5 :
        return "above"
    elif angle < 180 - 22.5 :
        return "above left"
    elif angle < 225 - 22.5 :
        return "left"
    elif angle < 270 - 22.5 :
        return "below left"
    elif angle < 315 - 22.5 :
        return "below"
    elif angle < 360 - 22.5 :
        return "below right"
    else :
        return "right"

# nature de l'angle
def natureAngle(angle) :
    """retourne une chaine de caractère correspondant à la nature de l'angle compris entre 0 et 180 degrés fourni"""
    if angle == 0 :
        return "nul"
    elif angle < 90 :
        return "aïgu"
    elif angle == 90 :
        return "droit"
    elif angle < 180 :
        return "obtus"
    else :
        return "plat"
    
# Variables à regrouper ici
def variables(version,fichier) :
    """crée toutes les variables aléatoires utiles et retourne un dictionnaire contenant :
        - les variables globales (autres fonctions de ce module, utiles dans jinja, comme terme(), facteur()...),
        - les variables locales à cette fonction comme version (utile pour numéroter les fiches) et toutes les listes de nombres aléatoires ci-dessous).

        Arguments : un entier (version) correspondant à la version du document créé.
                    une chaine de caractère correspondant au nom d'un fichier texte (valide) dans lequel seront écrites à la fin les nouvelles variables générées ou lues les variables déjà générées avant.
    """
    global classes, dictLocals
    # on génère de nouvelles variables car aucune existante.
    N = listeAleatoire(1,9)
    M = listeAleatoire(1,9)
    n = listeAleatoire(2,9)
    m = listeAleatoire(2,9)
##  m[i] différent de n[i] commenté...    
##    m=['' for i in range(100)]
##    for i in range(100):
##        m[i]=randint(2,9)
##        while m[i]==n[i]:
##            m[i]=randint(2,9)   
    nZ = listeAleatoire(-9,9,1,[0])
    mZ = listeAleatoire(-9,9,1,[0])
    N2 = listeAleatoire(1,2)
    N3 = listeAleatoire(1,3)
    N4 = listeAleatoire(1,4)
    N5 = listeAleatoire(1,5)
    N6 = listeAleatoire(1,6)
    N7 = listeAleatoire(1,7)
    N8 = listeAleatoire(1,8)
    N9 = listeAleatoire(1,9)
    N10 = listeAleatoire(1,10)
    Z = listeAleatoire(-10,10)
    Z2 = listeAleatoire(-10,10)
    ZE = listeAleatoire(-10,10,1,[0])
    ZE2 = listeAleatoire(-10,10,1,[0])
    DCM = [choice([10,100,1000]) for i in range(100)]
    DCM2 = [choice([10,100,1000]) for i in range(100)]
    D = listeAleatoire(10,90,10)
    S = listeAleatoire(-1,1,1,[0])
    NN = listeAleatoire(1,99)
    NNN = listeAleatoire(1,999)
    NNO = listeAleatoire(10,990,10)
    h = listeAleatoire(1,12)
    H = listeAleatoire(1,24)
    min = listeAleatoire(1,60)
    s = listeAleatoire(1,60)
    L1=[]
    L2=[]
    L3=[]
    L4=[]
    L5=[]
    L6=[]
    L7=[]
    L8=[]
    L9=[]
    L = [choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']) for i in range(100)]
    for i in range(10):
        Huitlettres=sample(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],9)
        L1.append(Huitlettres[0])
        L2.append(Huitlettres[1])
        L3.append(Huitlettres[2])
        L4.append(Huitlettres[3])
        L5.append(Huitlettres[4])
        L6.append(Huitlettres[5])
        L7.append(Huitlettres[6])
        L8.append(Huitlettres[7])
        L9.append(Huitlettres[8])
    NNvNN = [round(i/100,2) for i in listeAleatoire(1,9999)]
    NNvNO = [round(i/10,2) for i in listeAleatoire(1,999)]
    NvNN = [round(i/100,2) for i in listeAleatoire(1,999)]
    NvNO = [round(i/10,2) for i in listeAleatoire(1,99)]
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

    # ajout des variables du script compagnon.py
    dictGlobals = {}
    if os.path.exists(fichier[:-13]+".py") :
        exec(open(os.path.join(chemin,nom_fichier_modele+".py"),encoding="utf8").read(), dictGlobals, dictLocals)
    retour = locals()
    retour.update(dictLocals)
    # Pour envoyer toutes les variables au modèle
    # regroupement dans un seul dictionnaire retour de toutes les fonctions et variables définies ici.
    # => utilisables dans la fonction traiter(...)
    retour.update(globals())

    # on enregistre les variables locals() créées dans le fichier fvar
    # enregistrment déplacé après l'exécution de jinja pour récupérer les variables générés dans jinja.
    #enregistrerVariables(fichier, retour)
    return retour

def alea(a,b,nom='nepasmemoriser') : 
    """Avec <<var[nom]>> on pourra récupérer la valeur d'un entier aléatoire entre a et b"""
    global alea
    if nom=='nepasmemoriser':
        return randint(a,b)
    else:
        var[nom] = randint(a,b)
        return var[nom]
    # Début de travail pour """ générer de nouvelles variables (des listes autres que celles prédéfinies) directement dans le document LaTeX"""
    # def alea(nom,a,b,increment=1,listeASupprimer=[],nbreValeursSouhaitees=100)  :
    #global varCreee
    #exec(nom + "=listeAleatoire(" + str(a) + "," + str(b) + "," + str(increment) + "," + str(listeASupprimer) + "," + str(nbreValeursSouhaitees) + ")")
    #print(locals())
    #globals().update(locals())

def aleadecimal(nom) : # Un nombre décimal dont la partie entière a 1 à 3 chiffres et la partie décimale a 1 à 3 chiffres
    global alea
    var[nom] = Decimal(str(randint(1,10**randint(1,3)))+'.'+str(randint(1,10**randint(1,3))))
    return var[str(nom)]

def affectealeadecimal(nom):
    global alea
    aleadecimal(nom)
    return ''

def affecte(valeur,nom) :
    global alea
    var[nom] = valeur
    return ''

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
        retour = "+" + ecriture_decimale(a)
    else :
        retour = ecriture_decimale(a)
    return retour

def facteur(a):
    """Formatage correct de nombre d'un produit.
    Exemple 1 : facteur(2) retourne "2"
    Exemple 2 : facteur(-4) retourne "(-4)"
    """
    if float(a) < 0 :
        retour = "(" + ecriture_decimale(a) + ")"
    else :
        retour = ecriture_decimale(a)
    return retour

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
    """Ecriture dans le fichier LaTeX aléatoirisé généré des fins de versions"""
    if version!=nombre_de_versions :
        fichierChgtVersion = "changement-version.tex"
        if os.path.exists(fichierChgtVersion) :
            file = open(fichierChgtVersion, "r",encoding="utf8")
            chgtVersionPersonnalise = file.read()
            file.close()
            fichier.write(chgtVersionPersonnalise)
        else :
            fichier.write('\n')
            fichier.write('%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n')
            fichier.write('\\newpage\n')
            fichier.write('\\setcounter{section}{0}\n')
    else :
        fichier.write('\n')
        fichier.write('\\end{document}')

def listeFichierTexProposes(dossier) :
    """ retourne la liste des fichiers .tex du dossier passé en argument (et de ses sous-dossiers) en excluant :
            - les fichiers cachés commençant par un point
            - les fichiers dont le nom se termine par "cor"
            - les fichiers dont le nom se termine par "aleatoirise"
            - les fichiers dont le nom se termine par "preambule" (prise en compte des préambules par fichier modèle).
    """
    fichList = [ os.path.join(dossier,f) for f in os.listdir(dossier) if os.path.isfile(os.path.join(dossier, f)) and os.path.splitext(os.path.basename(os.path.join(dossier, f)))[0][0] != "." and os.path.splitext(os.path.basename(os.path.join(dossier, f)))[0][-3:] != "cor" and os.path.splitext(os.path.basename(os.path.join(dossier, f)))[0][-9:] != "preambule" and os.path.splitext(os.path.basename(os.path.join(dossier, f)))[0][-11:] != "aleatoirise" and os.path.splitext(os.path.basename(os.path.join(dossier, f)))[1] == ".tex"]
    dirList = [ d for d in os.listdir(dossier) if os.path.isdir(os.path.join(dossier,d)) and d != ".git" ]
    for sousDossier in dirList :
        retour = listeFichierTexProposes(os.path.join(dossier,sousDossier))
        if retour != [] : # si le sousDossier a des fichiers intéressants.
            fichList = fichList + retour
    return fichList


def choixFichier(dossier) :
    """ propose les fichiers .tex du dossier fourni pour les aléatoiriser
        retourne le nom du fichier choisi par l'utilisateur.
    """
    ReposeLaQuestion = True
    while ReposeLaQuestion :
        listeProposee = listeFichierTexProposes(dossier)
        print(listeProposee)
        j=0
        for fichier in listeProposee :
            print(str(j) + " - " + fichier[len(dossier)+1:])
            j = j + 1
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

##def lireVariables(fvar) :
##    """ retourne la liste des lignes du fichier fvar
##        cela permet de récupérer les variables d'une version générée antérieurement.
##    """
##        print( fvar.readlines())
##        print("lecture réussie")
##    except :
##        print("lecture en échec", )
##        liste =[]
##    return liste
        
def enregistrerVariables(fichier, dictionnaire) :
    """ Filtre du dictionnaire toutes les listes (qui contiennent les variables aléatoires) + le dictionnaire var (spécifique) en excluant tous les autres dictionnaires (fonctions,...).
        Enregistre dans fvar un dictionnaire contenant des listes de nombres aléatoires : permet de mémoriser les variables d'une version.
    """
    dictionnaireTraite = {}
    for element in dictionnaire.keys() :
        if isinstance(dictionnaire.get(element),list) or element == "var" :
            dictionnaireTraite[element] = dictionnaire.get(element)
    #print(dictionnaireTraite)
##    try :
##        fvar.read() # positionnement à la fin
##    except :
##        True
    #fvar.seek(-1,2) # positionnement à la fin (surement inutile car on est déjà à la fin)
    with open(fichier, "a",encoding="utf8") as fvar:
        fvar.write(str(dictionnaireTraite)+"\n") # une ligne par version
        fvar.close()

def choixCompilationImmediate(fichierAleatoirise,chemin) :
    """ propose de compiler immédiatement avec xelatex par défaut, si trouvé sur le système
    Remarque : adapté pour texlive sur macosX en attendant de trouver les chemins sur les autres OS
    """
    xelatex = 0
    pdflatex = 0
    if os.path.exists("/Library/TeX/texbin/xelatex") :
        xelatex = 1
        print("Choix possibles :")
        print("- x pour xelatex")
    if os.path.exists("/Library/TeX/texbin/pdflatex") :
        if xelatex == 0 :
            print("Choix possibles :")
        print("- p pour pdflatex")
        pdflatex = 1
    if xelatex == 1 or pdflatex == 1 :
        reponse = input("Compiler avec latex ? (laisser vide pour ne pas compiler)")
        if reponse != "" :
            if reponse[0] == "x" :
                compilateur = "/Library/TeX/texbin/xelatex"
            else :
                compilateur = "/Library/TeX/texbin/pdflatex"
            if len(reponse) >1 and reponse[1] == "2" : # en cas de réponse x2 ou p2, on procède à une double compilation pour que tout apparaisse correctement.
                nombre = 2
            else :
                nombre = 1
            fichierACompiler = os.path.join(chemin, fichierAleatoirise)
            retour = compiler(compilateur, chemin, fichierACompiler, nombre)
            # idem pour le corrigé s'il existe
            fichierACompiler = os.path.join(chemin, fichierAleatoirise[:-4]+"-cor.tex")
            if os.path.exists(fichierACompiler) :
                compiler(compilateur, chemin, fichierACompiler, nombre)
                retour = retour + " + corrigé"
        else :
            retour = ""
        return retour

def compiler(compilateur, chemin, fichierACompiler, nombre) :
    """ compilation latex avec le compilateur de son choix et suppression des fichiers de compilation"""
    for i in range(nombre) :
        os.system(compilateur + " -synctex=1 -interaction=nonstopmode -output-directory=" + chemin + " " + fichierACompiler)
    # suppression des fichiers de compilation.
    aSupprimer = fichierACompiler[:-4] + ".aux "  + fichierACompiler[:-4] + ".log " + fichierACompiler[:-4] + ".out " + fichierACompiler[:-4] + ".synctex.gz "
    os.system("rm "+aSupprimer)
    # affichage dans le lecteur de pdf par défaut.
    os.system("open " + fichierACompiler[:-4] + ".pdf")
    retour = "Compilation avec " + compilateur + " du fichier alétoirisé effectuée."
    return retour


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
    # génération du fichier aléatoirisé + affichage de ce qui est fait au fur et à mesure
    print("Fichier choisi : " , os.path.join(chemin,nom_fichier_modele+".tex").replace("\\","/"))
    template = env.get_template(os.path.join(chemin,nom_fichier_modele+".tex").replace("\\","/"), parent=chemin.replace("\\","/"))
    if __name__ == "__main__":
        f = open(os.path.join(dossierDestination, nomfichier), "w",encoding="utf8")
    else :
        f = open(os.path.join(chemin,nomfichier), "w",encoding="utf8")
    # prise en compte d'un éventuel préambule personnalisé dans le dossier.
    nom_fichier_preambule = nom_fichier_modele + "-preambule.tex"
    if os.path.exists(os.path.join(chemin, nom_fichier_preambule)) :
        retour = "Prise en compte du " + nom_fichier_preambule + ". "
        file = open(os.path.join(chemin , nom_fichier_preambule), "r",encoding="utf8")
        preambule_personnalise = file.read()
        file.close()
    else :
        nom_fichier_preambule = "preambule-perso.tex"
        if os.path.exists(os.path.join(chemin, nom_fichier_preambule)) :
            retour = "Prise en compte du " + nom_fichier_preambule + ". "
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
    # prise en compte d'un fichier pour enregistrer les variables générées antérieurement.
    nomFichierVariables = os.path.join(dossierDestination, nom_fichier_modele+"_aleatoirise-var-memo.txt")
    lignesVariables = []
    if os.path.exists(nomFichierVariables) and os.stat(nomFichierVariables).st_size != 0 :
        # ouverture du fichier de variables personnalisées qui existe et est non vide
        with open(nomFichierVariables, "r",encoding="utf8") as fvar:
            lignesVariables= fvar.read().splitlines()
            print("Récupération du jeu de variables enregistré pour ", len(lignesVariables)," versions.")
            #print(lignesVariables)
            fvar.close()
    # Affichage plus succint des jeux de variables utilisés
    if nombre_de_versions <= len(lignesVariables):
        print("Utilisation des jeux de variables n°1 à n°", nombre_de_versions)
    else :
        print("Génération de nouveaux jeux de variables pour les versions n°",len(lignesVariables)+1 , " à n°", nombre_de_versions)
    # RENDU DES VERSIONS DEMANDEES
    for version in range(1,nombre_de_versions+1) :
        # utilisation des variables standards aléatoires si enregistrés dans un fichier txt du même nom
        if len(lignesVariables) < version :
            print("Génération d'un nouveau jeu de variables pour la version ",version)
            dictVariables = variables(version, nomFichierVariables)
            nouveauJeuDeVariables = True
        else :
            print("Utilisation du jeu de variables n°", version)
            dictVariables = eval(lignesVariables[version - 1])
            dictVariables.update(globals())
            nouveauJeuDeVariables = False
        # ajout de versions au dictionnaire transmis
        dictVariables['version']=version
        # mise à jour du dictionnaire de variables afin de disposer de tout.
        dictVariables.update(dictLocals)
        # cas spécifique de la variable classes
        if "classes" in dictLocals :
            classes = dictLocals["classes"]
        #print(dictVariables)
        # création du rendu
        f.write(template.render(**dictVariables))
        # enregistrement du jeu de variables générés dans python et jinja.
        if nouveauJeuDeVariables :
            enregistrerVariables(nomFichierVariables, dictVariables)
        # fin de version générée
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

# fin des fonctions utiles à ce présent script

# version non GUI :
if __name__ == "__main__":
    var={} # Pour créer des variables dans le modèle .tex
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
        print(choixCompilationImmediate(filename + "_aleatoirise.tex","fichiers-aleatoirises"))
    else :
        print("Pas de dossier 'modeles' dans le dossier courant du script.")
