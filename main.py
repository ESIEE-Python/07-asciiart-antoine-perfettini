""""
Code principale
"""
#### Imports et définition des variables globales
import sys
sys.setrecursionlimit(2000)
#### Fonctions secondaires
def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument 
        selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    c = [s[0]]
    o = [1]
    k=1
    l= []
    while k<len(s):
        if s[k] == s[k-1]:
            o[-1]+=1
        else:
            c.append(s[k])
            o.append(1)
        k=k+1
    for item in zip(c,o):
        l.append(item)
    return l


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument 
        selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    # cas de base
    # recherche nombre de caractères identiques au premier
    i=0
    if not s:
        return []
    while i+1<len(s) and s[i]==s[i+1]:
        i=i+1
    t = [(s[0],i+1)]
    # appel récursif
    return t+artcode_r(s[i+1:])
#### Fonction principale
def main():
    """"
    Fonction principale
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
