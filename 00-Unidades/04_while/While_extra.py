'''
UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo desarrollo en python, 
que promete revolucionar el mercado. 
Las posibles aplicaciones son las siguientes: 
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT)  

Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

Los datos a ingresar por cada encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT)   

En esta opción, se ingresaran empleados hasta que el usuario lo desee.

Una vez finalizado el ingreso, mostrar:

    #! 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
    #! 2) - Tecnología que mas se votó.
    #! 3) - Porcentaje de empleados por cada genero
    #! 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #! 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
    #! 6) - Nombre y género del empleado que voto por RV/RA con menor edad.
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
        seguir = True

        contador_IOT_IA_masc = 0

        contador_IOT = 0
        contador_IA = 0
        contador_RV = 0

        contador_masc = 0
        contador_fem = 0
        contador_otro = 0

        contador_IOT_edad = 0

        contador_IA_fem = 0
        acumulador_edad_fem_IA = 0

        bandera_primer_RV_RA = False

        minimo_edad = 0

        while seguir:
            #pedir datos
            nombre = input("Ingrese su nombre: ")#prompt("nombre","Ingrese su nombre")
            edad = input("Ingrese su edad: ") #prompt("edad","Ingrese su edad")
            edad = int(edad)
            while edad < 18:
                edad = input ("Ingrese una edad correcta: ") #prompt("edad","Ingrese una edad correcta")
                edad = int(edad)
            genero = input("Ingrese su genero: ") #prompt("genero","Ingrese su genero")
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = input("Ingrese un genero valido: ") #prompt("genero","Ingrese un genero valido")
            tecnologia = input("Ingrese una tecnologia: ") #prompt("tecnologia","Ingrese tecnologia")
            while tecnologia != "IA" and tecnologia != "IOT" and tecnologia != "RV/RA":
                tecnologia = input("Ingrese una tecnologia correcta: ") #prompt("tecnologia","Ingrese una tecnologia correcta") 
            
            #procesar datos dentro del while(se repite)
    #1°
            if genero == "Masculino" and (tecnologia == "IOT" or tecnologia == "IA") and edad >= 25 and edad <= 50:
                contador_IOT_IA_masc += 1
    #2°
            # if tecnologia == "IOT":
            #     contador_IOT += 1
            # elif tecnologia == "IA":
            #     contador_IA += 1
            # else:
            #     contador_RV += 1
        #otra posible solucion
            match tecnologia:
                case "IOT":
                    contador_IOT += 1
            #4°
                    if (edad > 18 and edad < 25) or (edad > 33 and edad < 42):
                        contador_IOT_edad += 1
                case "IA":
                    contador_IA += 1
                case "RV/RA":
                    contador_RV += 1
            #6°
                    if edad < minimo_edad or bandera_primer_RV_RA == False:
                        minimo_edad = edad
                        nombre_minimo = nombre
                        genero_minimo = genero
                        bandera_primer_RV_RA = True
                        
    #3°
            match genero:
                case "Masculino":
                    contador_masc += 1
                case "Femenino":
                    contador_fem += 1
            #5°
                    if tecnologia == "IA":
                        contador_IA_fem += 1
                        acumulador_edad_fem_IA += edad
                case "Otro":
                    contador_otro += 1

            seguir = question("seguir", "¿Desea ingresar un nuevo empleado?")

        #procesar datos fuera del while (no se repite)
    #2°
        if contador_IA == contador_IOT and contador_IA == contador_RV:
            mas_votado = "2° las tres tecnologias obtuvieron los mismos votos"
        elif contador_IOT > contador_IA and contador_IOT > contador_RV:
            mas_votado = "2° IOT fue la tecnologia mas votada"
        elif contador_IA > contador_RV:
            mas_votado = "2° IA fue la tecnologia mas votada"
        elif contador_IA == contador_IOT:
            mas_votado = "2° IA e IOT obtuvieron los mismos votos"
        elif contador_IA == contador_RV:
            mas_votado = "2° IA y RV/RA obtuvieron los mismos votos"
        elif contador_IOT == contador_RV:
            mas_votado = "2° IOT Y RV/RA obtuvieron los mismos votos"
        else:
            mas_votado = "2° RV/RA fue la tecnologia mas votada"

    #3°
        total_empleados = contador_otro + contador_fem + contador_masc

        porcentaje_fem = (contador_fem * 100) / total_empleados
        porcentaje_masc = (contador_masc * 100) / total_empleados
        porcentaje_otro = 100 - (porcentaje_fem + porcentaje_masc)

    #4°
        porcentaje_IOT_edad = (contador_IOT_edad * 100) / total_empleados
    
    #5°
        if contador_IA_fem > 0:
            promedio_edad_fem = acumulador_edad_fem_IA / contador_IA_fem    
        else:
            promedio_edad_fem = "No se ingresaron votos de empleadas femeninas"
        #salida de datos
        print(f"1° La cantidad de empleados masculinos entre 25 y 50 años que votaron IOT o IA es: {contador_IOT_IA_masc}")
        print(f"2° {mas_votado}")
        print(f"3° Porcentaje: \n\tMasculino: {porcentaje_masc}%\n\tFemenino: {porcentaje_fem}%\n\tOtro{porcentaje_otro}")
        print(f"4° Porcentaje IOT rango edad: {porcentaje_IOT_edad}")
        print(f"5° promedio de edad empleadas femeninas que votaron IA: {promedio_edad_fem}")
        print(f"6° El empleado menor de edad que voto RV/RA es: {nombre_minimo} de {minimo_edad} años {genero_minimo}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
