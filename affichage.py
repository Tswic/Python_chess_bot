import pyautogui
from PIL import Image
def afficher_echequier(echequier):
    for i in range(8):
        for j in range(8):
            if j!=7:
                print(echequier.liste[j][7-i].type,end="/")
            else:
                print(echequier.liste[7][7-i].type)
def not_couleur(couleur):
    if couleur=="Blanc":
        return "Noir"
    elif couleur=="Noir":
        return "Blanc"

def reco_couleur(couleur):
    if couleur=="Blanc":
        return 1
    elif couleur=="Noir":
        return 0

def signe_couleur(couleur):
    if couleur=="Blanc":
        return 1
    elif couleur=="Noir":
        return -1

def click(x,y):
    pyautogui.moveTo(300+x*63,622-y*63)
    pyautogui.click()

def auto_souris(mouvement):
    x,y = mouvement[0]
    dx,dy = mouvement[1]
    click(x,y)
    click(dx,dy)
    click(dx, dy)

def couleur_pixel(x,y):
    img = Image.open('image_reco_echequier.jpg')
    return img.getpixel((310 + 63 * x,595 - 63 * y))

def photo():
    screen = pyautogui.screenshot()
    screen.save('image_reco_echequier.jpg')

def verif_couleur(ecart):
    retour = []
    for i in range(8):
        for j in range(8):
            if len(retour) == 2:
                return retour
            (r,g,b) = couleur_pixel(i,j)
            if (((245 - ecart < r) and (r < 245 + ecart)) and ((246 - ecart < g) and (g < 246 + ecart)) and ((129 - ecart < b) and (b < 129 + ecart))) or (((187 - ecart < r) and (r < 187 + ecart)) and ((205 - ecart < g) and (g < 205 + ecart)) and ((68 - ecart < b) and (b < 68 + ecart))):
                retour += [(i,j)]
    return retour

def verif_milieux(coup):
    ecart = 30
    img = Image.open('image_reco_echequier.jpg')
    (r,g,b) = img.getpixel((287 + 63 * coup[0][0],618 - 63 * coup[0][1]))
    if (245 - ecart < r and r < 245 + ecart and 246 - ecart < g and g < 246 + ecart and 129 - ecart < b and b < 129 + ecart) or (187 - ecart < r and r < 187 + ecart and 205 - ecart < g and g < 205 + ecart and 68 - ecart < b and b < 68 + ecart):
        return [coup[0],coup[1]]
    else:
        return [coup[1],coup[0]]
