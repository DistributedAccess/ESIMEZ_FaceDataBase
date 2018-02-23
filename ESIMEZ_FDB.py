from picamera import Picamera
import Deteccion
import Menu
import os

camera = Picamera()

def Crear_Directorios_P():
    Directorio = os.listdir("/home/verriva/Tesis/ESIMEZ_FaceDatabase/ESIMEZ")
    a = "/U" + str(len(Directorio) + 1)
    path = "/home/verriva/Tesis/ESIMEZ_FaceDatabase/ESIMEZ"+a
    darth = len(Directorio) + 1
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        Directorio = natsorted(Directorio)           #   Ordenamos los Directorios
        a = Directorio.pop()                         #   Ultimo directorio
        b = "/U" + str(int(a.replace("U", ""))+1)      #   Se guarda el numero del dir
        path = "/home/verriva/Tesis/ESIMEZ_FaceDatabase/ESIMEZ"+b
        os.mkdir(path)
        darth = int(a.replace("U", ""))+1

    return darth #REGRESA EL NUMERO DE USARIO

def Captura(Dir, i):
    #   Dir & i son valores dados por un for
    camera.capture('ESIMEZ/U%s/Imagen%s.jpg' % (Dir, i+1))  #   ESTE METODO TOMA UNA FOTO
    try:
        Rostro = Deteccion_LBP('ESIMEZ/U%s/Imagen%s.jpg' % (Dir, i+1))
        #Rostro2 = Deteccion_Haar('ESIMEZ/U%s/Imagen%s.jpg' % (Dir, i+1))
        return "OK"
    except IndexError:
        Captura(Dir, i)

def Ingresar_Nuevo():

    #camera.rotation = 180
    camera.start_preview()

if __name__ == "__main__":

    while(True):
        Menu.Inicio()
