import affichage
import recursif
import mouvement_piece
import time
import dico


def coup_auto(echequier):
    input("votre coup est ... ")
    affichage.photo()
    ecart = 30
    coup = affichage.verif_couleur(ecart)
    while len(coup)<2:
        ecart += 1
        coup = affichage.verif_couleur(ecart)

    coup = affichage.verif_milieux(coup)
    echequier.move(coup[0],coup[1])
    print(retour_coup((coup[0], coup[1])))

lettre_coup="abcdefgh"


mouvements_pieces = {
            "cavalier": mouvement_piece.mouv_cavalier,
            "tour": mouvement_piece.mouv_tour,
            "fou": mouvement_piece.mouv_fou,
            "pion": mouvement_piece.mouv_pion,
            "dame": mouvement_piece.mouv_dame,
            "roi": mouvement_piece.mouv_roi
        }

avance_piece = {
            "roi": 1,
            "cavalier": 4,
            "fou": 3,
            "dame": 0,
            "pion": 6,
            "tour": 1
        }

bonus_piece = {
            "roi": 0,
            "cavalier": 53,
            "fou": 23,
            "dame": 9,
            "pion": 3,
            "tour": 11
        }


def mouv_humain(input,cerveau,couleur):
    t = cerveau.coup_legaux(couleur,cerveau.echequier_lie)
    if not t:
        quit()
    else:
        deplacement(input)
def coup(cerveau,echequier,couleur):
    return cerveau.coup_legaux_test(couleur,echequier,cerveau.possibilite(couleur,echequier,echequier.reconnaissance_piece(couleur)))
def remplacement(echequier):
    return [[Piece(j,i,echequier.liste[j][i].couleur,echequier.liste[j][i].type) for i in range(8)] for j in range(8)]
def deplacement(cases):
    test.move((lettre_coup.index(cases[0]),int(cases[1])-1),(lettre_coup.index(cases[3]),int(cases[4])-1))
def retour_coup(coo):
    depart,arrive=coo
    return lettre_coup[depart[0]]+str(depart[1]+1)+"/"+lettre_coup[arrive[0]]+str(arrive[1]+1)

def save_position(echiquier):
    return [echiquier.liste[i//8][i%8].type for i in range(64)]

def choix_coup(echiquier, cerveau, couleur, profondeur, alpha, beta):
    tri = []
    echiquier_de_test = Echequier()
    echiquier_de_test.liste = remplacement(echiquier)
    t = coup(cerveau,echiquier,couleur)

    if not t:
        if echiquier.is_in_check(couleur,cerveau):
            return [10000000 * (profondeur + 1) * affichage.signe_couleur(affichage.not_couleur(couleur))]
        else:
            return [0]

    if profondeur == 0:
        a = cerveau.evaluation(echiquier)
        cerveau.position.append(save_position(echiquier))
        cerveau.valeur_position.append((profondeur,a))
        return [a]

    for i in range(len(t)):
        for j in t[i][1]:
            echiquier_de_test.move(t[i][0], j)
            tri += [((t[i][0], j),echiquier_de_test.compte_points())]
            echiquier_de_test.liste = remplacement(echiquier)

    if couleur == "Blanc":
        tri.sort(key=lambda a: a[1], reverse=True)
    else:
        tri.sort(key=lambda a: a[1])



    if profondeur == cerveau.profondeur:
        retour = 0
        if couleur == "Blanc":
            MaxEval = -100000000000
            for mouvement, eval in tri:
                echiquier_de_test.move(mouvement[0], mouvement[1])
                evaluation = choix_coup(echiquier_de_test, cerveau, "Noir", profondeur - 1, alpha, beta)
                echiquier_de_test.liste = remplacement(echiquier)
                MaxEval = max(MaxEval, evaluation[0])
                alpha = max(alpha, evaluation[0])
                if MaxEval == evaluation[0]:
                    retour = mouvement
                if beta <= alpha:
                    break

            return retour
        else:
            MinEval = 100000000000
            for mouvement, eval in tri:
                echiquier_de_test.move(mouvement[0], mouvement[1])
                evaluation = choix_coup(echiquier_de_test, cerveau, "Blanc", profondeur - 1, alpha, beta)
                echiquier_de_test.liste = remplacement(echiquier)
                MinEval = min(MinEval, evaluation[0])
                beta = min(beta, evaluation[0])
                if MinEval == evaluation[0]:
                    retour = mouvement
                if beta <= alpha:
                    break
            return retour
    else:
        if cerveau.profondeur >= 4:
            tri = tri[:(20//(cerveau.profondeur))*profondeur]

        if couleur == "Blanc":
            MaxEval = -100000000000
            for mouvement, eval in tri:
                echiquier_de_test.move(mouvement[0], mouvement[1])
                evaluation = choix_coup(echiquier_de_test, cerveau, "Noir", profondeur - 1, alpha, beta)
                echiquier_de_test.liste = remplacement(echiquier)
                MaxEval = max(MaxEval, evaluation[0])
                alpha = max(alpha, evaluation[0])
                if beta <= alpha:
                    break

            return [MaxEval]
        else:
            MinEval = 100000000000
            for mouvement, eval in tri:
                echiquier_de_test.move(mouvement[0], mouvement[1])
                evaluation = choix_coup(echiquier_de_test, cerveau, "Blanc", profondeur - 1, alpha, beta)
                echiquier_de_test.liste = remplacement(echiquier)
                MinEval = min(MinEval, evaluation[0])
                beta = min(beta, evaluation[0])
                if beta <= alpha:
                    break

            return [MinEval]


def modif(string):
    return ([i for i in range(8) if string[0]==lettre_coup[i]][0],int(string[1])-1)

def setup(piece):
    piece_couleur = "sans"
    piece_type = "rien"
    if piece.y <= 1:
        piece_couleur = "Blanc"
        if piece.y == 1:
            piece_type = "pion"
        elif piece.x == 0 or piece.x == 7:
            piece_type = "tour"
        elif piece.x == 1 or piece.x == 6:
            piece_type = "cavalier"
        elif piece.x == 2 or piece.x == 5:
            piece_type = "fou"
        elif piece.x == 3:
            piece_type = "dame"
        elif piece.x == 4:
            piece_type = "roi"
    if piece.y >= 6:
        piece_couleur = "Noir"
        if piece.y == 6:
            piece_type = "pion"
        elif piece.x == 0 or piece.x == 7:
            piece_type = "tour"
        elif piece.x == 1 or piece.x == 6:
            piece_type = "cavalier"
        elif piece.x == 2 or piece.x == 5:
            piece_type = "fou"
        elif piece.x == 3:
            piece_type = "dame"
        elif piece.x == 4:
            piece_type = "roi"
    return Piece(piece.x, piece.y, piece_couleur, piece_type)

class Piece:
    def __init__(self,posX,posY,couleur="sans",type="rien"):
        self.couleur=couleur
        self.type=type
        self.x = posX
        self.y = posY
        if type=="cavalier":
            self.point=30000
        if type=="fou":
            self.point=30000
        if type=="pion":
            self.point=10000
        if type=="dame":
            self.point=90000
        if type=="tour":
            self.point=50000
        if type=="roi":
            self.point=10000
        if type=="rien":
            self.point=0
    def get_couleur(self):
        return self.couleur
    def get_type(self):
        return self.type
    def get_point(self):
        return self.point
    def get_attributs(self):
        return self.couleur , self.type , self.point

def mouv_simplifie(echequier, depart, arrive):
    x, y = depart
    dx, dy = arrive

    echequier.liste[x][y].y = dy
    echequier.liste[x][y].x = dx
    echequier.liste[dx][dy] = echequier.liste[x][y]
    echequier.liste[x][y] = Piece(x, y)

def rock(echequier,couleur,cote):
    if couleur == "Blanc":
        y = 0
    else:
        y = 7
    if cote == "O-O":
        mouv_simplifie(echequier,(4,y),(6,y))
        mouv_simplifie(echequier,(7,y),(5,y))
    elif cote == "O-O-O":
        mouv_simplifie(echequier,(4,y),(2,y))
        mouv_simplifie(echequier,(0,y),(3,y))

class Echequier:
    def __init__(self, position = [[setup(Piece(i , j)) for j in range(8)] for i in range(8)]):
        self.liste = position

    def move(self , depart , arrive):
        x , y = depart
        dx , dy = arrive

        if x == 4 and (dx == 2 or dx == 6) and self.liste[x][y].type == "roi":
            if dx == 2:
                sens = "O-O-O"
            else:
                sens = "O-O"
            couleur = self.liste[x][y].couleur
            rock(self,couleur,sens)
            self.passant_supr()

        else:
            if self.liste[dx][dy].type=="en passant" and self.liste[x][y].type=="pion":
                self.liste[dx][dy+1]=Piece(dx,dy+1)
                self.liste[dx][dy-1] = Piece(dx, dy-1)
            self.passant_supr()

            if self.liste[x][y].type=="pion" and (dy==0 or dy==7):
                self.liste[x][y].type="dame"
                self.liste[x][y].point = 18000

            if (y==1 or y==6) and (dy==3 or dy==4) and self.liste[x][y].type=="pion":
                self.liste[x][y+affichage.signe_couleur(self.liste[x][y].couleur)].type="en passant"

            self.liste[x][y].y = dy
            self.liste[x][y].x = dx
            self.liste[dx][dy] = self.liste[x][y]
            self.liste[x][y]=Piece(x,y)

    def passant_supr(self):
        for i in range(8):
            for j in range(8):
                if self.liste[i][j].type=="en passant":
                    self.liste[i][j].type = "rien"
                    return

    def compte_points(self):
        somme=0
        for i in range(8):
            for j in range(8):
                if self.liste[j][i].couleur=="Blanc":
                    somme+=self.liste[j][i].point
                if self.liste[j][i].couleur=="Noir":
                    somme-=self.liste[j][i].point
        return somme

    def reconnaissance_piece(self,couleur_coup):
        return recursif.couleur_interliste(self.liste,couleur_coup)

    def surete(self,echequier,couleur,localisation):
        if not localisation:
            return 0
        x,y = localisation[0]
        if echequier.liste[x][y].type=="roi":
            return -7 * len(mouvement_piece.mouv_dame(echequier,couleur,x,y))
        else:
            return self.surete(echequier,couleur,localisation[1:])

    def table(self,echequier,couleur,localisation):
        retour = 0
        if couleur == "Blanc":
            for (x,y) in localisation:
                retour += dico.bonus[echequier.liste[x][y].type][7-y][x]*7
        else:
            for (x,y) in localisation:
                retour += dico.bonus[echequier.liste[x][y].type][y][x]*7
        return retour


    def avance(self,echequier,couleur,localisation):
        if not localisation:
            return 0
        else:
            x,y = localisation[0]
            if couleur == "Blanc":
                return 2 * y * avance_piece[echequier.liste[x][y].type] + self.avance(echequier,couleur,localisation[1:])
            else:
                return 2 * (7 - y) * avance_piece[echequier.liste[x][y].type] + self.avance(echequier,couleur,localisation[1:])

    def controle_centre(self,couleur,piece):
        if not piece:
            return 0
        else:
            retour = 0
            x,y = piece[0]
            if x >= 3 and x<=4 and y >= 3 and y<=4:
                retour += 10
            retour += bonus_piece[self.liste[x][y].type] * len(mouvements_pieces[self.liste[x][y].type](self,couleur,x,y))
            return retour + self.controle_centre(couleur,piece[1:])

    def is_in_check(self,couleur,cerveau):
        piece = self.reconnaissance_piece(affichage.not_couleur(couleur))
        poss = cerveau.possibilite(affichage.not_couleur(couleur), self, piece)
        for i in range(len(poss)):
            for x, y in poss[i][1]:
                if self.liste[x][y].type == "roi":
                    return True
        return False

class Cerveau:
    def __init__(self,echequier,couleur_piece,profondeur):
        self.echequier_lie=echequier
        self.couleur_joue = couleur_piece
        self.profondeur = profondeur
        self.position = []
        self.valeur_position = []

    def possibilite(self, couleur, echequier, localisation):
        if not localisation:
            return []
        else:
            piece_type = echequier.liste[localisation[0][0]][localisation[0][1]].type
            if piece_type in mouvements_pieces:
                return [(localisation[0], mouvements_pieces[piece_type](echequier, couleur, localisation[0][0],localisation[0][1]))] + self.possibilite(couleur, echequier, localisation[1:])

    def coup_legaux(self,couleur,echequier):
        poss = self.possibilite(couleur,echequier,echequier.reconnaissance_piece(couleur))
        echequier_de_test = Echequier(remplacement(echequier))
        retour=[]
        for i in range(len(poss)):
            coup=[]
            for j in poss[i][1]:
                echequier_de_test.liste = remplacement(echequier)
                echequier_de_test.move(poss[i][0],j)
                if not echequier_de_test.is_in_check(couleur,self):
                    coup += [j]
            if len(coup) != 0:
                retour += [(poss[i][0],coup)]
        return retour

    def coup_legaux_test(self,couleur,echequier,possibilite):
        if not possibilite:
            return []
        else:
            echequier_de_test = Echequier(remplacement(echequier))
            coup = []
            for i in possibilite[0][1]:
                echequier_de_test.liste = remplacement(echequier)
                echequier_de_test.move(possibilite[0][0], i)
                if not echequier_de_test.is_in_check(couleur, self):
                    coup += [i]
            if not coup:
                return self.coup_legaux_test(couleur,echequier,possibilite[1:])
            else:
                return [(possibilite[0][0],coup)] + self.coup_legaux_test(couleur,echequier,possibilite[1:])

    def evaluation(self,echequier):
        reco_blanc = echequier.reconnaissance_piece("Blanc")
        reco_noir = echequier.reconnaissance_piece("Noir")
        retour = echequier.compte_points()
        retour += 3*echequier.controle_centre("Blanc",reco_blanc) - echequier.controle_centre("Noir",reco_noir)
        retour += echequier.surete(echequier,"Blanc",reco_blanc) - echequier.surete(echequier,"Noir",reco_noir)
        retour += echequier.avance(echequier,"Blanc",reco_blanc) - echequier.avance(echequier,"Noir",reco_noir)
        retour += echequier.table(echequier,"Blanc",reco_blanc) - echequier.table(echequier,"Noir",reco_noir)
        retour += recursif.attaque(self.possibilite("Blanc",echequier,reco_blanc),echequier.liste) - recursif.attaque(self.possibilite("Noir",echequier,reco_noir),echequier.liste)
        return retour

    def position_choix(self):

        choix = coup(self,self.echequier_lie,self.couleur_joue)

        if not choix:
            print("checkmate or draw")
            affichage.afficher_echequier(self.echequier_lie)
            quit()

        start = time.time()
        retour = choix_coup(self.echequier_lie,self,self.couleur_joue,self.profondeur,-100000000000,100000000000)
        end = time.time()
        print(end-start)
        affichage.auto_souris(retour)

        self.position = []
        self.valeur_position = []
        self.echequier_lie.move(retour[0], retour[1])
        return retour_coup((retour[0], retour[1]))

test = Echequier()
cerveau_blanc = Cerveau(test,"Blanc",3)
cerveau_noir = Cerveau(test,"Noir",3)


opening = ["e2/e4","c7/c5"]

for i in opening:
    deplacement(i)
    affichage.afficher_echequier(test)
    print("#")

while 1:
    print(cerveau_blanc.position_choix())
    print(cerveau_noir.position_choix())
