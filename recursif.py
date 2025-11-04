def reco_couleur(liste,couleur):
    if len(liste)==0:
        return []
    elif liste[0].couleur==couleur:
        return [(liste[0].x,liste[0].y)] + reco_couleur(liste[1:],couleur)
    else:
        return reco_couleur(liste[1:],couleur)

def couleur_interliste(liste,couleur):
    if len(liste) == 0:
        return []
    else:
        return reco_couleur(liste[0],couleur) + couleur_interliste(liste[1:],couleur)

def index(taille,liste,val):
    if not(liste):
        return []
    else:
        if liste[0]==val:
            return [taille-len(liste)] + index(taille,liste[1:],val)
        else:
            return index(taille,liste[1:],val)

def attaque(possibilite, liste):
    if not possibilite:
        return 0
    elif not possibilite[0][1]:
        return attaque(possibilite[1:], liste)
    elif isinstance(possibilite[0][1], list) and possibilite[0][1]:
        if liste[possibilite[0][1][0][0]][possibilite[0][1][0][1]].couleur != "sans":
            return liste[possibilite[0][1][0][0]][possibilite[0][1][0][1]].point / 1000 + attaque(possibilite[0][1][1:], liste)
        else:
            return attaque(possibilite[0][1][1:], liste)
    else:
        return 0