import cv2

Recorte = None

#   USAR EL ESTANDAR ISO/IEC 19794-5
#   ALINEAR Y NORMALIZAR
#   UTULIZAR EL ALGORITMO PROPUESTO POR OPENCV EL DE ARNOLD SWATCWADSADASER JAJAJA :3

def Deteccion_Haar(Imagen):
    #   Esta_Funcion detecta los rostros de la Imagen de Entrada y regresa
    #   el array del numero de rostros y la ubicacion de cada uno

    global Recorte
    #   Cargamos la imagen
    Image = cv2.imread(Imagen)

    #   Convertimos a escala de grises
    Gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)

    #   Cargamos el clasificador
    haar_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

    #   Detectamos rostros, algunos rostros podran estar mas cercanos a la camara
    faces = haar_face_cascade.detectMultiScale(Gray, scaleFactor=1.1, minNeighbors=5);
    #return faces
    for (x,y,w,h) in faces:
        Recorte = Gray[y:y+w, x:x+h]

    return cv2.resize(Recorte, (200, 200))

def Deteccion_LBP(Imagen):
    #   Esta_Funcion detecta los rostros de la Imagen de Entrada y regresa
    #   el array del numero de rostros y la ubicacion de cada uno

    global Recorte
    #   Cargamos la imagen
    Image = cv2.imread(Imagen)

    #   Convertimos a escala de grises
    Gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)

    #   Cargamos el clasificador
    lbp_face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')

    #   Detectamos rostros
    faces = lbp_face_cascade.detectMultiScale(Gray, scaleFactor=1.1, minNeighbors=5);
    #return faces
    for (x,y,w,h) in faces:
        Recorte = Gray[y:y+w, x:x+h]

    return cv2.resize(Recorte, (200, 200))

def Dibujar_Rectangulos(Faces, Image):
    for (x, y, w, h) in Faces:
        cv2.rectangle(Image, (x,y), (x+w,y+h), (0, 255, 0), 2)

    cv2.imshow('Rostros',Image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Recortar_Rostros(Img, faces):
    for (x,y,w,h) in faces:
        return Img[y:y+w, x:x+h]

def Ajustar_Rostro(Face, Ancho, Alto):
    #Gris = cv2.cvtColor(Face, cv2.COLOR_RGB2GRAY)
    #Gris = cv2.equalizeHist(Recorte)
    #Ajuste = cv2.resize(Face, (Ancho, Alto))
    #return Ajuste
    return cv2.resize(Face, (Ancho, Alto))
