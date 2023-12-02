# Initialisation du jeu

# 1 - Importez les bibliothèques nécessaires : Tkinter et tkinter.messagebox.
# Pour importer les bibliothèques nécessaires, il faut procéder ainsi
import tkinter as tk
from tkinter import messagebox

# 2 - Créez une fenêtre Tkinter avec le titre "TIC-TAC-TOE".
# Pour créer une fenêtre Tkinter avec le titre "TIC-TAC-TOE"
fenetre = tk.Tk()
fenetre.title("TIC-TAC-TOE")

# 3 - Définissez une liste appelée chiffres avec les chiffres de 1 à 9 pour représenter les positions disponibles sur le plateau de jeu.
# Définissez une liste appelée chiffres avec les chiffres de 1 à 9 pour représenter les positions disponibles sur le plateau de jeu
chiffres = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 4 - Initialisez la variable mark à une chaîne vide ('').
# Initialisez la variable mark à une chaîne vide ('')
mark = ''

# 5 - Définissez la variable count sur 0 pour suivre le nombre de mouvements.
# Définissez la variable count sur 0 pour suivre le nombre de mouvements
count = 0

# 6 - Créez une liste appelée panneaux avec 10 éléments, où le premier élément est un espace réservé (« panneau »)
# et le reste représente les positions du plateau de jeu.
# Créez une liste appelée panneaux avec 10 éléments, où le premier élément est un espace réservé et le reste représente les positions du plateau de jeu
panneaux = [' '] * 10

