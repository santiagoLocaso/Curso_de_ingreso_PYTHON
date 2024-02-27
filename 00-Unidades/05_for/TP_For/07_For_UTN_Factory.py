import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Santiago
apellido: Locaso
---
TP: For_UTN_Factory
---
Enunciado:
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):

        contador_nb = 0
        contador_f = 0
        contador_m = 0
        contador_edad_f = 0
        contador_edad_m = 0
        contador_edad_nb = 0

        contador_js = 0
        contador_py = 0
        contador_asp = 0

        bandera_edad_min = False
        
        for i in range(0, 10):
            nombre = prompt("nombre","Ingrese su nombre")
            edad = prompt("edad","Ingrese su edad")
            edad = int(edad)
            while edad < 18:
                edad = prompt("edad","Debe ser mayor de edad")
                edad = int(edad)
            genero = prompt("genero","Ingrese su genero")
            while genero != "M" and genero != "F" and genero != "NB":
                genero = prompt("genero","Ingrese un genero valido")
            tecnologia = prompt("tecnologia","Ingrese una tecnologia")
            while tecnologia != "PYTHON" and tecnologia != "JS" and tecnologia != "ASP.NET":
                tecnologia = prompt("tecnologia","Ingrese una tecnologia correcta")
            puesto = prompt("puesto","Ingrese su puesto")
            while puesto != "Jr" and puesto != "Ssr" and puesto != "Sr":
                puesto = prompt("puesto","Ingrese un puesto correcto")
                
            if puesto == "Jr":
                if bandera_edad_min == False or edad < edad_min:
                    edad_min = edad
                    nombre_min = nombre
                    bandera_edad_min = True

            match genero:
                case "F":
                    contador_f = contador_f + 1
                    contador_edad_f = contador_edad_f + edad
                case "M":
                    contador_m = contador_m + 1
                    contador_edad_m = contador_edad_m + edad
                case "NB":
                    match puesto:
                        case "Ssr":
                            if (tecnologia == "ASP.NET" or tecnologia == "JS") and edad >= 24 and edad <= 40:
                                contador_nb = contador_nb + 1
                                contador_edad_nb = contador_edad_nb + edad
                        case _:
                            contador_nb = contador_nb + 1
                            contador_edad_nb = contador_edad_nb + edad
            
            match tecnologia:
                case "JS":
                    contador_js = contador_js + 1
                case "ASP.NET":
                    contador_asp = contador_asp + 1
                case _:
                    contador_py = contador_py + 1

        if contador_py > contador_js and contador_py > contador_asp:
            mas_postulantes = "Python fue la tecnologia con mas postulantes"
        elif contador_js > contador_asp:
            mas_postulantes = "JS fue la tecnologia con mas postulantes"
        else:
            mas_postulantes= "ASP.NET fue la tecnologia con mas postulantes"

        promedio_edad_f = contador_edad_f / contador_f
        promedio_edad_m = contador_edad_m / contador_m
        promedio_edad_nb = contador_edad_nb / contador_nb

        total_postulantes = contador_f + contador_m + contador_nb

        porcentaje_f = (contador_f * 100) / total_postulantes
        porcentaje_m = (contador_m * 100) / total_postulantes
        porcentaje_nb = 100 - (porcentaje_f + porcentaje_m)


        print(f"cantidad de personas NB que programan en ASP.NET o JS edad entre 25 y 40 postulados para Ssr {contador_nb}")
        print(f"Nombre del postulante Jr con menor edad {nombre_min} con {edad_min} años")
        print(f"Promedio de edades género femenino {promedio_edad_f}")
        print(f"Promedio de edades género masculino {promedio_edad_m}")
        print(f"Promedio de edades género no binario {promedio_edad_nb}")
        print(f"Tecnologia con mas postulantes fue {mas_postulantes}")
        print(f"porcentaje de postulantes género femenino {porcentaje_f}")
        print(f"porcentaje de postulantes género masculino {porcentaje_m}")
        print(f"porcentaje de postulantes género no binario {porcentaje_nb}")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
