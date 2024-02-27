import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Santiago
apellido: Locaso
---
Ejercicio: for_09
---
Enunciado:
Al comenzar el juego generamos un número secreto del 1 al 100, se pedira al usuario el ingreso de un numero por prompt y si el número ingresado es el mismo que el número secreto 
se dará por terminado el juego con un mensaje similar a este: 

En esta oportunidad el juego evaluará tus aptitudes a partir de la cantidad de intentos, por lo cual se informará lo siguiente:
    1° intento: “Usted es un psíquico”.
	2° intento: “Excelente percepción”.
	3° intento: “Esto es suerte”.
	4° hasta 6° intento: “Excelente técnica”.
	7 intentos: “Perdiste, suerte para la próxima”.

de no ser igual se debe informar si 
“Falta…”  para llegar al número secreto  o si 
“Se pasó…”  del número secreto.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        secreto = 45

        for intento in range(1, 8):
            numero = prompt("", "Ingrese un numero")
            numero = int(numero)

            if numero == secreto:
                if intento == 1:
                    alert("","Usted es un psíquico")
                elif intento == 2:
                    alert("","Excelente percepción")
                elif intento == 3:
                    alert("","Esto es suerte")
                else:
                    alert("","Excelente técnica")
                break

            elif numero < secreto:
                alert("", "Falta...")
            else:
                alert("", "Se pasó...")
            
            if intento == 7:
                alert("","Perdiste, suerte para la proxima")
                break

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()