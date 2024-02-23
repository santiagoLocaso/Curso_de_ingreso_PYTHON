import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Santiago
apellido: Locaso
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        suma_positivos = 0
        suma_negativos = 0
        contador_positivos = 0
        contador_negativos = 0
        contador_ceros = 0

        while True:
            numero = prompt("mensaje", "Ingrese un numero")

            if numero == None:
                break

            numero = int(numero)

            if numero > 0:
                suma_positivos += numero
                contador_positivos += 1
            elif numero < 0:
                suma_negativos += numero
                contador_negativos += 1
            else:
                contador_ceros += 1

        diferencia_pos_neg =  contador_positivos - contador_negativos

        alert("", f"la suma de los positivos es: {suma_positivos}, y la suma de los negativos: {suma_negativos}")
        alert("", f"la cantidad de positivos ingresados es: {contador_positivos}, y la cantidad de negativos es: {contador_negativos}")
        alert("", f"la cantidad de ceros ingresados es: {contador_ceros}")
        alert("", f"la diferencia entre la cantidad de positivos y negativos es: {diferencia_pos_neg}")
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
