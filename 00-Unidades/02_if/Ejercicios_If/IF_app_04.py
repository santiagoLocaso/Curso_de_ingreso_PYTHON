import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Santiago
apellido: Locaso
---
Ejercicio: if_04
---
Enunciado:
Al presionar el botón 'Calcular', se deberá obtener el contenido de la caja de texto txtEdad, 
transformarlo en número y calcular si es adolescente (edad entre 13 y 17 años). Se deberá informar utilizando el Dialog alert.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        edad = int(self.txt_edad.get())

        if edad > 12 and edad < 18 :
            alert("mensaje", "es adolescente")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()


'''
TIPOS DE DATOS

String de texto
int numero entero
float numero decimal
bool -> true false


OPERADORES DE RELACION

 ==   -> si un dato es igual a otro
 >    -> si un dato es mayor a otro
 >=   -> si un dato es mayor o igual a otro  
 <=   -> si un dato es menor o igual a otro
 <    -> si un dato es menor a otro


OPERADORES LOGICOS 

 AND  -> y, ej. si edad > a 12 Y edad < 18
 OR   -> o
 NOT  -> no, niega una condicion, 


TABLAS DE VERDAD

 AND ->
    VERDADERO Y VERDADERO  -> VERDADERO
    VERDADERO Y FALSO      -> FALSO
    FALSO Y VERDADERO      -> FALSO
    FALSO Y FALSO          -> FALSO

 OR ->
    VERDADERO Y VERDADERO  -> VERDADERO
    VERDADERO Y FALSO      -> VERDADERO
    FALSO Y VERDADERO      -> VERDADERO
    FALSO Y FALSO          -> FALSO

 NOT -> si la condicion es verdadera pasa a ser falsa y si es falsa pasa a verdadera 
    
    
'''