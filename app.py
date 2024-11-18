from pyswip import Prolog 
import tkinter as tk
from tkinter import messagebox

prolog = Prolog()
prolog.consult("personalities.pl")

root = tk.Tk()
root.title("Test de personalidad compatible")

# Aqui agreguen sus preguntas por favor 
questions = [
    "Haces nuevos amigos con frecuencia"
]

answers = [
    "De acuerdo", 
    "Un poco de acuerdo", 
    "Ni de acuerdo ni desacuerdo", 
    "Un poco en desacuerdo", 
    "desacuerdo"
]

i = 0
puntaje = {
    "introvertido": 0, 
    "extrovertido": 0, 
    "sensacion": 0, 
    "intuicion": 0, 
    "pensamiento": 0, 
    "sentimiento": 0, 
    "juicio": 0, 
    "percepcion": 0
}

def next_question(option):
    global i 
    
    answer = answers[option]
    prolog_query = f"score('{answer.lower()}', P), update_feature(P, '{answers[i].lower()}', score)."
    list(prolog.query(prolog_query))
    
    i += 1 
    
    if i < len(answers):
        print("Siguiente pregunta...")
        question_label.config(text=questions[i])
    else:
        evaluate()
    
def evaluate():
    print(list(prolog.query("compatible_personalidad(Persona, Compatible).")))
    
question_label = tk.Label(root, text=questions[i], wraplength=400)
question_label.pack(pady=20)

for i, ans in enumerate(answers):
    btn = tk.Button(root, text=ans, command=lambda i=i: next_question(i))
    btn.pack(fill="x")
    
root.mainloop()