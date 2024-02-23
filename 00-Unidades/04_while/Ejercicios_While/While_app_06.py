import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Santiago
apellido: Locaso
---
Ejercicio: while_06
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar 5 números mediante prompt. 
Calcular la suma acumulada y el promedio de los números ingresados. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(master=self, placeholder_text="Promedio")
        self.txt_promedio.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        contador = 0
        acumulador = 0

        while contador < 5:
            numero = prompt("Numero","Ingrese un numero")
            numero = int(numero)

            acumulador += numero
            contador += 1

        promedio = acumulador / contador

        self.txt_suma_acumulada.insert(0, acumulador)
        self.txt_promedio.insert(0, promedio)

        #ANTES DEL WHILE
            #INICIALIZACIONES
        
        #DURANTE DEL WHILE
            #PIDO UN NUMERO 5 VECES
            #SUMO LOS NUMEROS
            #CONTAR LA CANTIDAD DE NUMEROS QUE INGRESE 
        
        #DESPUES DEL WHILE
            #CALCULAR PROMEDIO
            #MOSTRAR LA SUMA Y EL PROMEDIO

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
