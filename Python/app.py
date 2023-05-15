import tkinter as tk
from tkinter import filedialog, Text, ttk
import os
import config
import dmd

#root = tk.Tk() #inicializacion tkinter
#root.wm_title("DMD") #nombre ventana principal del programa

DICE = [        #Array con los tipos de dados
"d4",
"d6",
"d8",
"d10",
"d12",
"d20",
"d100"
]

global macroType #variable global para el tipo de macro; 0 para musica, 1 para dado, 2 para recursos
macroType = ''

global state
state = 0

def selectFunction(key):
    global key_
    key_ = 'key' + key
    print (key_)
    global newwindow
    newwindow= tk.Toplevel (root, bg="#202225") #creo pop up window fijada a root con background color
    newwindow.wm_title ("Selecionar accion")
    newwindow.geometry ('500x200') #window size
    action_1 = tk.Button (newwindow, text= 'Musica', padx= 10, pady= 10, fg='white', bg = "#36393f", command = musicMacro) #creo un boton para las acciones
    action_1.place (x= 75, y=75)
    action_2 = tk.Button (newwindow, text= 'Dados', padx= 10, pady= 10, fg='white', bg = "#36393f", command= diceType) #command se refiere a la funcion que ejecuta al pulsar el boton
    action_2.place (x= 225, y=75)
    action_3 = tk.Button (newwindow, text= 'Recursos', padx= 10, pady= 10, fg='white', bg = "#36393f", command = resources)
    action_3.place (x= 375, y=75)

def musicMacro():
    global musicwindow
    musicwindow = tk.Toplevel(root, bg="#202225")
    musicwindow.wm_title ("Musica")
    musicwindow.geometry ('500x200')
    global url_var      #creo una variable global para llevar el tracking del valor del campo
    url_var= tk.StringVar()
    name_entry = tk.Entry(musicwindow, textvariable= url_var, width = 65) #creo una caja de texto para escribir la url
    name_entry.place (x= 50, y=50)
    submitButton= tk.Button (musicwindow, text= 'Aceptar', command=submitMusic) #creo boton para aceptar y guardar los datos
    submitButton.place (x= 225, y= 75)

def submitMusic ():
    macroType = '0'       #selecciono el tipo de macro
    url = url_var.get() #llamo a la variable para poder trabajar con ella y la guardo en otra
    print (url)
    musicwindow.destroy () #mato las ventanas sobrantes
    newwindow.destroy()
    config.update (key_, macroType, url)#actualizo el archivo de configuracion

def diceType():
    global diceWindow
    diceWindow = tk.Toplevel (root, bg="#202225")
    diceWindow.wm_title ("Tipo de dado")
    diceWindow.geometry ('500x200')
    global dice_value
    dice_value =tk.StringVar ()
    dice_value.set("Select an Option")
    diceMenu = tk.OptionMenu (diceWindow, dice_value, *DICE) #creo un menu desplegable con los valores de un array predefinido
    diceMenu.place (x=175, y = 50)
    submitButton= tk.Button (diceWindow, text= 'Aceptar', command=submitDice)
    submitButton.place (x= 225, y= 100)

def submitDice ():
    macroType = '1'
    dice = dice_value.get()
    print (dice)
    diceWindow.destroy()
    newwindow.destroy()
    config.update (key_, macroType, dice) #guardo las variables en el archivo de configuracion y mato la ventana

def resources ():
    macroType = '2'
    filename = filedialog.askopenfilename (initialdir= "/", title = "Select resource", 
    filetypes= (("pdf files", "*.pdf"), ("all files", "*.*")))  #abro una  ventana para seleccionar archivos pdf o cualquier otro archivo y guardo el path en la variable

    print (filename)
    newwindow.destroy()
    config.update (key_, macroType, filename) #mato la ventana despues de guardar el path

def run(com_port):
    com_port = com_port.get()
    dmd.port = com_port.split ()[0]
    dmd.port = dmd.port [:-1]  #Modifico el string del puerto com para poder pasarselo a dmd.py
    #dmd.initializeDMD()
    #dmd.downloadMusic()
    dmd.runDMD()

def createApp ():

    dmd.checkCOM()

    global root
    root = tk.Tk() #inicializacion tkinter
    root.wm_title("DMD") #nombre ventana principal del programa

    canvas= tk.Canvas(root, height = 500, width= 500, bg = "#202225" ) #inicializo el lienzo
    canvas.pack ()

    frame = tk.Frame (root, bg="#202225" ) #inicializo la ventana
    frame.place (relwidth= 1, relheight=1) #relacion de tamaño entre el lienzo y la ventana

    tecla_1 = tk.Button (frame, text= 'Tecla 1', padx= 10, pady= 10, fg='white', bg = "#36393f", command= lambda:selectFunction ('0') ) 
    tecla_1.place (x= 75, y=75)

    tecla_2 = tk.Button (frame, text= 'Tecla 2', padx= 10, pady= 10, fg='white', bg = "#36393f", command= lambda:selectFunction ('1') ) 
    tecla_2.place (x= 225, y=75)

    tecla_3 = tk.Button (frame, text= 'Tecla 3', padx= 10, pady= 10, fg='white', bg = "#36393f", command= lambda:selectFunction ('2') ) 
    tecla_3.place (x= 375, y=75)

    tecla_4 = tk.Button (frame, text= 'Tecla 4', padx= 10, pady= 10, fg='white', bg = "#36393f", command= lambda:selectFunction ('3') ) 
    tecla_4.place (x= 75, y=225)

    tecla_5 = tk.Button (frame, text= 'Tecla 5', padx= 10, pady= 10, fg='white', bg = "#36393f", command= lambda:selectFunction ('4') ) 
    tecla_5.place (x= 225, y=225)

    tecla_6 = tk.Button (frame, text= 'Tecla 6', padx= 10, pady= 10, fg='white', bg = "#36393f", command= lambda:selectFunction ('5') ) 
    tecla_6.place (x= 375, y=225)

    tecla_7 = tk.Button (frame, text= 'Tecla 7', padx= 10, pady= 10, fg='white', bg = "#36393f", command= lambda:selectFunction ('6') ) 
    tecla_7.place (x= 75, y=375)

    tecla_8 = tk.Button (frame, text= 'Tecla 8', padx= 10, pady= 10, fg='white', bg = "#36393f", command= lambda:selectFunction ('7') ) 
    tecla_8.place (x= 225, y=375)

    tecla_9 = tk.Button (frame, text= 'Tecla 9', padx= 10, pady= 10, fg='white', bg = "#36393f", command= lambda:selectFunction ('8') ) #creo los botones de la aplicacion y les asigno una funcion (la misma para todos)
    tecla_9.place (x= 375, y=375)

    global com_port
    com_port =tk.StringVar ()
    com_port.set("Select an Option")
    com_menu = tk.OptionMenu (frame, com_port, *dmd.COM_PORTS) #creo un menu desplegable con los valores de los puertos COM
    com_menu.place (x=190, y = 25)


    tecla_run = tk.Button (frame, text= 'Iniciar', padx= 5, pady= 5, fg= 'white', bg= "#36393f", command= lambda:run(com_port))
    tecla_run.place (x= 225, y = 450) #Creo el boton de iniciar asignado a la funcion run


    root.mainloop () #ejecutamos la ventana

