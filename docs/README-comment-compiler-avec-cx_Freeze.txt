# DocAléa JinjaPyLaTeX compilation

## Avec cx_Freeze

### Prérequis

* [Python 3](https://www.python.org/downloads/)
* Installer Jinja2 : dans un terminal taper `pip install Jinja2` ou `pip3 install Jinja2` (lorsque Python2 et Python3 sont installés sur l'ordinateur)
* (sudo) pip3 install cx_Freeze asyncio



### Compilation

Dans le dossier contenant les sources Jinja_stable.py, Jinja-GUI_stable.py et setup.py, exécuter la commande :

* python3 setup.py build

La version compilée destinée à votre OS se trouve alors dans le dossier build.

Pour générer une version windows, mac, linux, il faudra procéder de même dans chaque environnement. (à vérifier si possible autrement) 


## Avec Cython et cython_freeze

### Prérequis

* [Python 3](https://www.python.org/downloads/)
* Installer Jinja2 : dans un terminal taper `pip install Jinja2` ou `pip3 install Jinja2` (lorsque Python2 et Python3 sont installés sur l'ordinateur)
* (sudo) pip3 install Cython requests docopt path.py

Compilation non aboutie en l'état des recherches.