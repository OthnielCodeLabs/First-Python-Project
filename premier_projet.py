
def moyenne_liste(liste):
    return sum(liste)/len(liste) 


def ajoute_dictionnaire(dictionnaire,cle,valeur):
    dictionnaire[cle] = valeur


while True :
    try :
        nom_etudiant = input("entrez le nom de l'étudiant :")
    except ValueError as e :
        print(f"erreur : {e}")
    liste_notes = []
    try:
        for i in range(5):
            n = int(input(f"Entrez une des notes de l'étudiant {nom_etudiant} :"))
            liste_notes.append(n)
    except ValueError as e :
        print(f"erreur : {e}")
    else :
        pass        

    for i in liste_notes:
        print(i)

    moyenne_etudiant = moyenne_liste(liste_notes)
    etudiant={}
    ajoute_dictionnaire(etudiant,f"Moyenne de l'étudiant {nom_etudiant}",moyenne_etudiant)
    for cle,valeur in etudiant.items() :
        print(cle," : ",valeur)
    try:
        demander = int(input("voulez vous quitter 1 pourquitter/0 pour continuer :"))
    except ValueError as e:
        print(f"erreur : {e}")
    if demander == 1 :
        print("fin du programme")
        break 