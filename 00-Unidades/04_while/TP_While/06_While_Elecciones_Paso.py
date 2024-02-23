import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Santiago
apellido: Locaso
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos              x
b. nombre y edad del candidato con menos votos     x
c. el promedio de edades de los candidatos
d. total de votos emitidos.                        x
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        seguir = True

        contador_total_votos = 0
        acumulador_candidatos = 0
        contador_edades = 0
        votos_maximos = 0
        votos_minimos = float('inf')
        
        while seguir:
            nombre = prompt("nombre", "Ingrese el nombre del candidato")
            acumulador_candidatos +=1
            edad = prompt("edad", "Ingrese la edad del candidato")
            edad = int(edad)
            while edad < 25:
                edad = prompt("edad","El candidato debe ser mayor de 25")
                edad = int(edad)
            votos = prompt("votos", "Ingrese los votos que recibio el candidato")
            votos = int(votos)
            while votos < 0:
                votos = prompt("votos", "Los votos no pueden ser menor a cero, ingrese votos validos")
                votos = int(votos)

            contador_total_votos += votos

            if votos > votos_maximos:
                votos_maximos = votos
                mas_votado = nombre
            if votos < votos_minimos:
                votos_minimos = votos
                menos_votado = nombre

            if acumulador_candidatos > 0:
                contador_edades += edad
                promedio_edades = contador_edades / acumulador_candidatos
                promedio_edades = int(promedio_edades)

            seguir = question("seguir", "¿Desea ingresar un nuevo candidato?")
        
        alert("nombre", f"El candidato mas votado fue {mas_votado} con {votos_maximos} votos")
        alert("nombre", f"El candidato menos votado fue {menos_votado} con {votos_minimos} votos")
        alert("edad", f"El promedio de edades de los candidatos es {promedio_edades}")
        alert("votos totales", f"los votos totales fueron {contador_total_votos}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
