'''
Simulacro Turno Tarde

Un gimnasio quiere medir el progreso de sus clientes, para ello se debe ingresar:

*Nombre

*Edad (debe ser mayor a 12)

*Altura (no debe ser negativa)

*Días que asiste a la semana (1, 3, 5)

*Kilos que levanta en peso muerto (no debe ser cero, ni negativo)

 

No sabemos cuántos clientes serán consultados. SI NO SE SABEN LA CANTIDAD DE ITERACIONES WHILE = TRUE

Se debe informar al usuario:

El promedio de kilos que levantan las personas que asisten solo 3 días a la semana.

El porcentaje de clientes que asiste solo 1 día a la semana.

Nombre y edad del cliente con más altura.

Determinar si los clientes eligen más ir 1, 3 o 5 días

Nombre y cantidad de kilos levantados en peso muerto, de la persona más joven que solo asista 5 días a la semana.
'''


import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        seguir = True

        contador_clientes = 0
        contador_kg = 0

        contador_dia_1 = 0
        contador_dia_3 = 0
        contador_dia_5 = 0

        bandera_altura_max = False      #HACER SIMPRE MAXIMOS CON BANDERA (ESTA SOLO SIRVE PARA LA CONDICION DE 3 DIAS A LA SEMANA)


        bandera_edad_min = False        #HACER SIMPRE MINIMOS CON BANDERA

        dia_mas_elegido = 0
        
        while seguir:
            nombre = prompt("nombre","Ingrese su nombre")
            edad = prompt("edad","Ingrese su edad")
            edad = int(edad)
            while edad < 12:
                edad = prompt("edad","Debe ser mayor de 12 años")
                edad = int(edad)
            altura = prompt("altura","Ingrese su altura")
            altura = int(altura)
            while altura < 0:
                altura = prompt("altura","La altura no puede ser negativa")
                altura = int(altura)
            dias = prompt("dias","Ingrese los dias que asiste en la semana")
            dias = int(dias)
            while dias != 1 and dias != 3 and dias != 5:
                dias = prompt("dias","Ingrese una cantidad de dias valida")
                dias = int(dias)
            kilos = prompt("kg","Ingrese los kilos que levanta de peso muerto")
            kilos = int(kilos)
            while kilos < 1:
                kilos = prompt("kg","Los kilos no pueden ser 0 o negativos")
                kilos = int(kilos)

            contador_clientes = contador_clientes + 1

            match dias:
                case 3:
                    contador_dia_3 = contador_dia_3 + 1

                    if contador_clientes > 0:
                        contador_kg = contador_kg + kilos
                        promedio_kg_3_dias = contador_kg / contador_clientes
                        promedio_kg_3_dias = int(promedio_kg_3_dias)
                case 1:
                    contador_dia_1 = contador_dia_1 + 1
                case _:
                    contador_dia_5 = contador_dia_5 + 1

                    if edad < edad_min or bandera_edad_min == False:
                        edad_min = edad
                        nombre_min = nombre
                        kilos_min = kilos
                        bandera_edad_min = True  #SIEMPRE FINALIZAR VOLVIENDO A PONER LA BANDERA EN TRUE!!

            porcentaje_clientes_1_dia  = (contador_dia_1 * 100) / contador_clientes

            if contador_dia_1 == contador_dia_3 and contador_dia_1 == contador_dia_5:
                dia_mas_elegido = "las tres posibilidades son igual de elegidas"


            elif contador_dia_3 > contador_dia_1 and contador_dia_3 > contador_dia_5:
                dia_mas_elegido = "Ir 3 dias a la semana fue el mas elegido"
            elif contador_dia_1 > contador_dia_5:
                dia_mas_elegido = "Ir 1 dia a la semana fue el mas elegido"


            elif contador_dia_1 == contador_dia_3:
                dia_mas_elegido = "Ir 1 y 3 dias a la semana fueron las mas elegidas elegidas"
            elif contador_dia_1 == contador_dia_5:
                dia_mas_elegido = "Ir 1 y 5 dias a la semana fueron las mas elegidas elegidas"
            elif contador_dia_3 == contador_dia_5:
                dia_mas_elegido = "Ir 3 y 5 dias a la semana fueron las mas elegidas elegidas"


            else:
                dia_mas_elegido = "Ir 5 dias a la semana fue el mas elegido"

            if altura > altura_max or bandera_altura_max == False:  #MAXIMOS CON BANDERA
                altura_max = altura
                mas_alto = nombre
                edad_mas_alto = edad
                bandera_altura_max = True
                

            seguir = question("","Desea ingresar un nuevo cliente?")

        alert("", f"El promedio de kilos que levantan las personas que asisten 3 dias es {promedio_kg_3_dias}")
        alert("", f"El porcentaje de clientes que van un dia es {porcentaje_clientes_1_dia}%")
        alert("", f"El cliente mas alto es {mas_alto} de {edad_mas_alto} años con {altura_max}cm")
        alert("", f"El o los dias mas elegidos para ir fueron {dia_mas_elegido} dias")
        alert("", f"El cliente mas chico es {nombre_min} de {edad_min} años y levanta {kilos_min} kilos")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()