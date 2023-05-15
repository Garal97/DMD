from configparser import ConfigParser

file = 'config.ini'
config = ConfigParser()
config.read(file) #configuracion para simplificar el trabajo con las funciones
keyData = ''
keyMode = ''

def update(key, mode, data): #se introduce la tecla, el modo y la informacion todo como string
    config ['mode'][key] = mode     #se crea un config con la informacion actualizada
    with open (file, 'w') as configfile:
        config.write (configfile) #se escribe la nueva informacion en el fichero de configuracion
    config ['data'][key] = data
    with open (file, 'w') as configfile:
        config.write (configfile)

def read (key): #se introduce la tecla de la que queremos sacar su configuracion
    global keyMode
    keyMode = config ['mode'][key] #se guarda el modo y la informacion en su respectiva variable
    #print (keyMode)
    global keyData
    keyData = config ['data'][key]
    #print (keyData)
    global keyFile
    keyFile = config ['filename'][key]
    return keyMode, keyData, keyFile

def updateName(key, name):
    config ['filename'][key] = name
    with open (file, 'w') as configfile:
        config.write (configfile)

def latest_file (audioName):
    config ['filename']['latest_file'] = audioName
    global audioFile
    audioFile = config ['filename']['latest_file']
    with open (file, 'w') as configfile:
        config.write (configfile)
#update ('key7', '1', 'helloworld') #ejemplo

#read ('key7')

#print (config.sections())


#print (config ['mode']['key0'])
#config ['data']['key0'] = '1'

#print (config ['mode']['key0'])

#with open (file, 'w') as configfile:
#    config.write(configfile)

