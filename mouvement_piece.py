import affichage


def mouv_cavalier(echequier,couleur,x,y):
    possibilite=[]
    for i in range(0,5,4):
        for j in range(0,3,2):
            possibilite.append((x + (i - 2), y + (j - 1)))
            possibilite.append((x + (j - 1), y + (i - 2)))
    possibilite = [possibilite[i] for i in range(len(possibilite)) if (possibilite[i][0]>=0 and possibilite[i][0]<=7 and possibilite[i][1]>=0 and possibilite[i][1]<=7)]
    possibilite = [possibilite[i] for i in range(len(possibilite)) if echequier.liste[possibilite[i][0]][possibilite[i][1]].couleur != couleur]
    return possibilite

def mouv_tour(echequier,couleur,x,y):
    poss=[]
    mouv=[(0,1),(0,-1),(-1,0),(1,0)]
    for j in range(4):
        for i in range(7):
            poss.append((x+mouv[j][0]*(i+1),y+mouv[j][1]*(i+1)))
            if poss[-1][0]<0 or poss[-1][0]>7 or poss[-1][1]<0 or poss[-1][1]>7:
                poss.pop(-1)
                break
            if echequier.liste[poss[-1][0]][poss[-1][1]].couleur==couleur:
                poss.pop(-1)
                break
            elif echequier.liste[poss[-1][0]][poss[-1][1]].couleur==affichage.not_couleur(couleur):
                break
    return poss

def mouv_fou(echequier,couleur,x,y):
    poss=[]
    mouv=[(1,1),(-1,1),(1,-1),(-1,-1)]
    for j in range(4):
        for i in range(7):
            poss += [(x+mouv[j][0]*(i+1),y+mouv[j][1]*(i+1))]
            if poss[-1][0]<0 or poss[-1][0]>7 or poss[-1][1]<0 or poss[-1][1]>7:
                poss.pop(-1)
                break
            if echequier.liste[poss[-1][0]][poss[-1][1]].couleur==couleur:
                poss.pop(-1)
                break
            elif echequier.liste[poss[-1][0]][poss[-1][1]].couleur==affichage.not_couleur(couleur):
                break
    return poss

def mouv_dame(echiquier,couleur,x,y):
    return mouv_tour(echiquier,couleur,x,y) + mouv_fou(echiquier,couleur,x,y)

def mouv_roi(echiquier,couleur,x,y):
    poss=[]
    mouv=[(1,1),(-1,1),(1,-1),(-1,-1),(0,1),(0,-1),(-1,0),(1,0)]
    for i in range(len(mouv)):
        poss += [(x+mouv[i][0],y+mouv[i][1])]
        if poss[-1][0]<0 or poss[-1][0]>7 or poss[-1][1]<0 or poss[-1][1]>7:
            poss.pop(-1)
        if len(poss)!=0:
            if echiquier.liste[poss[-1][0]][poss[-1][1]].couleur == couleur:
                poss.pop(-1)
    return poss

def mouv_pion(echiquier,couleur,x,y):
    poss=[]
    mouv=[[(1,1),(-1,1)],[(1,-1),(-1,-1)]]
    t = affichage.reco_couleur(couleur)
    if (y == 1 and echiquier.liste[x][y].couleur=="Blanc")or (y == 6 and echiquier.liste[x][y].couleur=="Noir"):
        if echiquier.liste[x][y+(t*2)-1].couleur == "sans":
            poss += [(x,y+(t*2)-1)]
        if len(poss)==1 and echiquier.liste[x][y+(t*4)-2].couleur == "sans":
            poss += [(x,y+(t*4)-2)]
    elif echiquier.liste[x][y + (t * 2) - 1].couleur == "sans":
        poss += [(x, y + (t * 2) - 1)]
    for i in range(len(mouv)):
        poss += [(x+mouv[1-t][i][0],y+mouv[1-t][i][1])]
        if poss[-1][0] < 0 or poss[-1][0] > 7 or poss[-1][1] < 0 or poss[-1][1] > 7:
            poss.pop(-1)
        elif (echiquier.liste[poss[-1][0]][poss[-1][1]].couleur != affichage.not_couleur(couleur) and echiquier.liste[poss[-1][0]][poss[-1][1]].type != "en passant"):
            poss.pop(-1)
    return poss





