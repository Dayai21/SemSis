import tkinter as tk
from tkinter import messagebox
from pyswip import Prolog

prolog = Prolog()
prolog.consult("personalities.pl")  

# Función para determinar personalidad
def determine_personality(scores):
    query = (
        f"determine_mbti({scores['EI']}, {scores['SN']}, {scores['TF']}, {scores['JP']}, Personality)."
    )
    for result in prolog.query(query):
        return result['Personality']

# Obtener afinidades e incompatibilidades
def get_affinities(personality):
    compatible_query = f"compatible('{personality}', CompatibleList)."
    incompatible_query = f"incompatible('{personality}', IncompatibleList)."

    compatible = []
    incompatible = []

    for result in prolog.query(compatible_query):
        compatible = result['CompatibleList']

    for result in prolog.query(incompatible_query):
        incompatible = result['IncompatibleList']

    return compatible, incompatible

# Interfaz gráfica
class MBTITestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MBTI Test")
        self.questions = []
        self.current_question = 0
        self.scores = {'EI': 0, 'SN': 0, 'TF': 0, 'JP': 0}

        self.load_questions()
        self.create_widgets()

    def load_questions(self):
        # Cargar las preguntas desde Prolog
        self.questions = [
            result
            for result in prolog.query("question(ID, Text, Axis, Opt1, Opt2).")
        ]

    def create_widgets(self):
        # Crear widgets
        self.question_label = tk.Label(self.root, text="", wraplength=400, font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.option1_button = tk.Button(self.root, text="", command=lambda: self.answer(1))
        self.option1_button.pack(pady=10, fill=tk.X, padx=50)

        self.option2_button = tk.Button(self.root, text="", command=lambda: self.answer(2))
        self.option2_button.pack(pady=10, fill=tk.X, padx=50)

        self.update_question()

    def update_question(self):
        # Actualizar la pregunta actual
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.question_label.config(text=question['Text'])
            self.option1_button.config(text="De acuerdo")
            self.option2_button.config(text="En desacuerdo")
        else:
            # Mostrar resultados
            self.show_results()

    def answer(self, choice):
        # Procesar la respuesta
        question = self.questions[self.current_question]
        if choice == 1:
            self.scores[question['Axis']] += question['Opt1']
        elif choice == 2:
            self.scores[question['Axis']] += question['Opt2']

        self.current_question += 1
        self.update_question()

    def show_results(self):
        # Determinar la personalidad y mostrar resultados
        personality = determine_personality(self.scores)
        compatible, incompatible = get_affinities(personality)

        messagebox.showinfo(
            "Resultados",
            f"Tu tipo de personalidad es: {personality}\n\n"
            f"Personalidades compatibles: {', '.join(compatible)}\n"
            f"Personalidades incompatibles: {', '.join(incompatible)}"
        )
        self.root.quit()

# Iniciar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = MBTITestApp(root)
    root.mainloop()
