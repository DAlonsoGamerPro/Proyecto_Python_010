from tkinter import *

root = Tk()
root.geometry("1500x400")
root.title("Diccionario")
root.configure(background = 'navajowhite')

Label_of_programacion = Label(root)
Label_of_peces = Label(root)
Label_of_cabellera = Label(root)

dictionary = {'Programar' : 'Viene a ser el proceso de crear un software fiable mediante la escritura, prueba, depuración, compilación o interpretación, y mantenimiento del código fuente.',
              'Peces' : 'Son animales vertebrados primariamente acuáticos, Suelen estar recubiertos por escamas, y están dotados de aletas, que permiten su movimiento continuo en los medios acuáticos, y branquias, con las que captan el oxígeno disuelto en el agua.',
              'Cabellera' : 'Continuación del cuero cabelludo formada por una fibra de queratina y constituido por una raíz y un tallo que crece principalmente en la piel de algunos mamíferos.'}

def programacion():
    Label_of_programacion["text"] = dictionary['Programar']

def peces():
    Label_of_peces["text"] = dictionary['Peces']
    
def cabellera():
    Label_of_cabellera["text"] = dictionary['Cabellera']
    

button_programacion = Button(root, text="Significado de Programar", command=programacion)
button_programacion.place(relx=0.5, rely=0.2, anchor=CENTER)
Label_of_programacion.place(relx=0.5, rely=0.3, anchor=CENTER)
    
button_peces = Button(root, text="Significado de Peces", command=peces)
button_peces.place(relx=0.5, rely=0.5, anchor=CENTER)
Label_of_peces.place(relx=0.5, rely=0.6, anchor=CENTER)

button_cabellera = Button(root, text="Significado de Cabellera", command=cabellera)
button_cabellera.place(relx=0.5, rely=0.8, anchor=CENTER)
Label_of_cabellera.place(relx=0.5, rely=0.9, anchor=CENTER)   

root.mainloop()