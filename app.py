from pyswip import Prolog 
import tkinter as tk
from tkinter import messagebox

prolog = Prolog()
prolog.consult("personalities.pl")

root = tk.Tk()
root.title("Test de personalidad compatible")

def ask_questions():
    scores = {'EI': 0, 'SN': 0, 'TF': 0, 'JP': 0}

    for result in prolog.query("question(ID, Text, Axis, Opt1, Opt2)."):
        print(f"Pregunta {result['ID']}: {result['Text']}")
        print("1. Primera opción")
        print("2. Segunda opción")
        answer = int(input("Selecciona 1 o 2: "))

        if answer == 1:
            scores[result['Axis']] += result['Opt1']
        elif answer == 2:
            scores[result['Axis']] += result['Opt2']
        else:
            print("Opción inválida, se tomará como 1.")
            scores[result['Axis']] += result['Opt1']

    return scores

def determine_personality(scores):
    """
    Determina la personalidad en base a los puntajes.
    """
    query = (
        f"determine_mbti({scores['EI']}, {scores['SN']}, {scores['TF']}, {scores['JP']}, Personality)."
    )
    for result in prolog.query(query):
        return result['Personality']

def get_affinities(personality):
    """
    Obtiene afinidades e incompatibilidades según la personalidad.
    """
    compatible_query = f"compatible('{personality}', CompatibleList)."
    incompatible_query = f"incompatible('{personality}', IncompatibleList)."

    compatible = []
    incompatible = []

    for result in prolog.query(compatible_query):
        compatible = result['CompatibleList']

    for result in prolog.query(incompatible_query):
        incompatible = result['IncompatibleList']

    return compatible, incompatible

# Flujo principal
scores = ask_questions()
personality = determine_personality(scores)
print(f"Tu tipo de personalidad es: {personality}")

compatible, incompatible = get_affinities(personality)
print(f"Personalidades compatibles: {compatible}")
print(f"Personalidades incompatibles: {incompatible}")