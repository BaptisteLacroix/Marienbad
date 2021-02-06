# pip install art==4.8

from random import randint
from art import tprint
from colorama import Fore, Style


def joueur_vs_joueur():
    """
    Elle permet de :

        - Demander le nom des 2 joueurs
        - Choisir au hasard quel joueur va commencer et créer le jeu comme instance de la class Marienband
        - Lancer le jeu et jouer.

    À chaque tour, vous devez :

        - afficher l'état du jeu (voir les explications du jeu au début)
        - demander au joueur en cours le numéro du tas t et le nombre d’allumettes n qu’il désire ôter,
        - vérifier si son choix est valide, sinon indiquer l’erreur et reposer la question,
        - supprimer n allumettes du tas t,
        - vérifiez si le jeu est terminé,
        - annoncez le gagnant (ou le perdant).
    :return:
    """
    joueur1 = str(input("\nJoueur 1 choisissez un Pseudo : "))  # joueur 1 chosis son nom
    joueur2 = str(input("Joueur 2 choisissez un Pseudo : "))  # joueur 2 choisis son nom

    if joueur2 == joueur1:  # si le joueur 2 a le meme pseudo que joueur 1 alors il change de pseudo
        joueur2 = str(input("Joueur 2 choisissez un autre Pseudo (pas le même que celui de Joueur 1 : "))

    hasard = randint(1, 2)  # choisis au hasard joueur 1 ou 2
    joueur_actuel = joueur1 if hasard == 1 else joueur2
    joueur_precedent = joueur1 if joueur_actuel == joueur2 else joueur2
    jeu = Marienband(joueur_actuel, joueur_precedent)

    while not jeu.termine():
        print(jeu)
        t, n = Error()
        # -> verifie
        while not jeu.verifie(t, n):  # on verifie si possible
            print(
                "Attention Vous devez mettre un numéro compris entre 1 et 6 en fonction du tas choisis ne dépassez "
                "pas !\n")
            print(jeu)
            t, n = Error()
        # -> enlever
        jeu.enlever(t, n)  # on enleve les allumettes
        # -> termine
    joueur_actuel, prochain_joueur = jeu.ordre_joueurs()
    print(Fore.RED)
    tprint(joueur_actuel + "   a    perdu     !!!")
    print(Style.RESET_ALL)


def joueur_vs_ordi_idiot():
    """

    :return:
    """
    joueur1 = str(input("\nJoueur 1 choisissez un Pseudo : "))  # joueur 1 chosis son nom
    joueur2 = "François Pignon"

    hasard = randint(1, 2)  # choisis au hasard joueur 1 ou 2
    joueur_actuel = joueur1 if hasard == 1 else joueur2
    joueur_precedent = joueur1 if joueur_actuel == joueur2 else joueur2
    jeu = Marienband(joueur_actuel, joueur_precedent)

    while not jeu.termine():
        joueur_actuel, prochain_joueur = jeu.ordre_joueurs()
        if joueur_actuel == joueur1:
            print(jeu)
            t, n = Error()
            # -> verifie
            while not jeu.verifie(t, n):  # on verifie si possible
                print("Attention Vous devez mettre un numéro compris entre 1 et 6 en fonction du tas choisis ne "
                      "dépassez pas !\n")
                print(jeu)
                t, n = Error()
            # -> enlever
            jeu.enlever(t, n)  # on enleve les allumettes
        else:
            print(jeu)
            # -> saisie du t
            t = randint(1, 6)  # demande le tas
            # -> saisie du n
            n = randint(1, 6)  # demande le nbr d'allumettes a enlever
            # -> verifie
            while not jeu.verifie(t, n):  # on verifie si possible
                t = randint(1, 6)  # demande le tas
                n = randint(1, 6)  # demande le nbr d'allumettes a enlever
            # -> enlever
            jeu.enlever(t, n)  # on enleve les allumettes
            # -> termine
    joueur_actuel, prochain_joueur = jeu.ordre_joueurs()
    print(Fore.RED)
    tprint(joueur_actuel + "   a    perdu     !!!")
    print(Style.RESET_ALL)


def Error():
    while True:
        try:
            # -> saisie du t
            t = int(input("Donnez moi le numéro du tas (entrer un numéro : "))  # demande le tas
            break
        except ValueError:
            print("Oups ! ce n'est pas un chiffre valide. Essais encore...")
            # -> saisie du n
    while True:
        try:
            # -> saisie du n
            n = int(input(
                "Donnez le numéro du nombre d'allumettes que vous voulez enlever dans ce tas : "))  # demande le nbr
            # d'allumettes a enlever
            break
        except ValueError:
            print("Oups ! ce n'est pas un chiffre valide. Essais encore...")
    return t, n


class Marienband:
    """

    """

    def __init__(self, joueur1="joueur1", joueur2="joueur2"):
        """
        Initialise une partie du jeu Marienband.
        :param joueur1: Joueur qui débute la partie
        :param joueur2: L'autre joueur
        """
        self.tas = (1, 2, 3, 4, 5, 6)
        self.allumettes = [1, 2, 3, 4, 5, 6]
        self.tour = 1
        self.joueurs = (joueur1, joueur2)

    def __str__(self):
        """
        Affiche l’état du jeu en cours (tas, allumettes, prochain joueur)
        :return: l’état du jeu en cours (tas, allumettes, prochain joueur)
        """
        joueur_actuel, prochain_joueur = self.ordre_joueurs()
        return "\n" + Fore.MAGENTA + joueur_actuel + Style.RESET_ALL + " joue\nTas :        " + str(
            self.tas) + "\nAllumettes : " + str(self.allumettes)
        # + "\nProchain joueur : " + Fore.MAGENTA + prochain_joueur + Style.RESET_ALL

    def ordre_joueurs(self):
        """
        Retourne un tuple contenant dans l'ordre le joueur actuel et le prochain joueur
        :return: un tuple contenant dans l'ordre le joueur actuel et le prochain joueur
        """
        if self.tour % 2 != 0:  # Si le self.tour est impair c'est le joueur 1 qui commence
            joueur_actuel = self.joueurs[0]  # joueur actuel = joueur 1
            prochain_joueur = self.joueurs[1]  # prochain_joueur = joueur 2
        else:  # Sinon c'est le joueur 2
            joueur_actuel = self.joueurs[1]  # joueur actuel = joueur 2
            prochain_joueur = self.joueurs[0]  # prochain_joueur = joueur 1
        return joueur_actuel, prochain_joueur

    def verifie(self, t, n):
        """
        Renvoie un booléen : vrai s’il est possible d’enlever n allumettes dans le tas t, faux sinon
        :return: un booléen : vrai s’il est possible d’enlever n allumettes dans le tas t, faux sinon
        """
        if t not in self.tas:
            print("Attention Vous devez mettre un numéro compris entre 1 et 6 pour le tas\n")
            return False
        else:
            if 0 < n <= 6 and 0 < n <= self.allumettes[t - 1]:
                # Si le nombre n d'allumettes est compris entre 0 et 6 et que n se situes bien dans le tas t alors
                return True  # Renvoie Vrai
            return False

    def enlever(self, t: int, n: int):
        """
        Met à jour les tas en enlevant n allumettes dans le tas t
        """
        self.allumettes[t - 1] -= n

    def termine(self):
        """
        Renvoie un booléen : vrai si le jeu est terminé, faux sinon
        :return:
        """
        nombre_de_0 = 0  # on dit qu'au départ il y a 0 zéro
        for i in self.allumettes:  # on regarde dans la liste
            if i == 0:  # si i vaut zéro alors je rajoute 1 zéro
                nombre_de_0 += 1
        if nombre_de_0 == 6:  # et si il y a 6 zéro dans la variable alors je return Vrai le joueur perd
            return True
        self.tour += 1
        return False


def main():
    """
    lance la fonction joueur_vs_joueur()
    :return:
    """
    while True:
        try:
            reponse = int(input("Taper : \n 1 Joueur vs Joueur \n 2 Joueur vs ia (IA joue au hasard) \n 3 Quitter : "))
            break
        except ValueError:  # Alerte
            print("Erreur veuillez réessayer")
    if reponse == 1:
        joueur_vs_joueur()
    elif reponse == 2:
        joueur_vs_ordi_idiot()
    elif reponse == 3:
        print("Au revoir.")
    else:
        main()  # relance la fonction


if __name__ == '__main__':
    # Si le script est exécuté (pas importé)
    main()
