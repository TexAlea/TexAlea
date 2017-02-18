#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fichier de compilation de notre script Jinja en mode interface graphique."""

from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "Maths aléatoires avec Python-Jinja-LaTeX",
    version = "0.1",
    description = "Ce programme génère, à partir d'un modèle, un fichier LaTeX contenant des exercices aux données aléatoires (et son corrigé, si prévu).",
    executables = [Executable("Jinja-GUI_stable.py")],
    options = {
        'build_exe': {
            'packages': ['encodings', 'asyncio']
        },
    }
)
