'''
Enunciado 1 : De 5  personas que ingresan al hospital se deben tomar y validar los siguientes datos.

nombre , 
temperatura, entre 35 y 42 
sexo( f, m , nb ) 
 edad(mayor a 0)
pedir datos por prompt y mostrar por print
Punto A-informar cual fue el sexo mas ingresado
Punto B-el porcentaje de personas con fiebre y el porcentaje sin fiebre

Punto C - por el número de DNI del alumno
DNI terminados en  8 o 9

1))informar la cantidad de personas menores de edad (menos de 18 años)
2)la temperatura promedio en total de todas las personas menores de edad
3) el nombre de la persona de sexo femenino  con la temperatura mas baja(si la hay)
'''

import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        contador_personas = 0
        contador_con_fiebre = 0
        contador_sin_fiebre = 0
        
        contador_m = 0
        contador_f = 0
        contador_nb = 0

        contador_menores = 0
        acumulador_temp = 0

        temp_min = 0

        
        for i in range(5):
            nombre = prompt("nombre", "Ingrese su nombre")
            contador_personas = contador_personas + 1
            temperatura = prompt("temperatura", "Ingrese su temperatura")
            temperatura = int(temperatura)
            while temperatura < 35 or temperatura > 42:
                temperatura = prompt("temperatura", "Ingrese una temperatura correcta")
                temperatura = int(temperatura)
            sexo = prompt("sexo", "Ingrese su sexo")
            while sexo != "f" and sexo != "m" and sexo != "nb":
                sexo = prompt("sexo", "Ingrese un sexo valido")
            edad = prompt("edad", "Ingrese su edad")
            edad = int(edad)
            while edad <= 0:
                edad = prompt("edad", "Ingrese una edad correcta")
                edad = int(edad)

            if edad < 18:
                contador_menores = contador_menores + 1
                acumulador_temp = acumulador_temp + temperatura
            else:
                alert("menores","No se ingresaron menores")
            
            match sexo:
                case "f":
                    contador_f = contador_f + 1
                    if temperatura < temp_min:
                        temp_min = temperatura
                case "m":
                    contador_m = contador_m + 1
                case "nb":
                    contador_nb = contador_nb + 1

            if temperatura > 38:
                contador_con_fiebre = contador_con_fiebre + 1
            else:
                contador_sin_fiebre = contador_sin_fiebre + 1

        if contador_f > contador_m and contador_nb < contador_f:
            alert("femenino", f"El sexo mas ingresado fue el femenino {contador_f}")
        elif contador_f < contador_m and contador_nb < contador_m:
            alert("masculino", f"El sexo mas ingresado fue el masculino {contador_m}")
        else:
            alert("nb", f"El sexo mas ingresado fue el no binario {contador_nb}")

        porcentaje_fiebre = (contador_con_fiebre * 100) / contador_personas
        porcentaje_sin_fiebre = (contador_sin_fiebre * 100) / contador_personas

        promedio_temp_menores = acumulador_temp / contador_menores

        alert("fibre", f"El porcentaje de personas con fiebre es {porcentaje_fiebre}%")
        alert("sin fibre", f"El porcentaje de personas sin fiebre es {porcentaje_sin_fiebre}%")

        alert("menor", f"La cantidad de menores de edad es {contador_menores}")

        alert("temp menores", f"La temperatura promedio de los menores es {promedio_temp_menores}")

        alert("temp min f", f"La paciente femenina con la temperatura mas baja es {nombre} con {temp_min}")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
