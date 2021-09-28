#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = []) -> list:
    for i in range(0, 10):
        a = input("Entrer une valeur entière, string ou float : ")
        values.append(a)
        print("La liste est : ", values)
    values.sort()
    return values


def anagrams(words: list = None) -> bool:

    word1 = input("Entrer le premier mot: ")
    word2 = input("Entrer le deuxieme mot: ")

    if sorted(word1.upper()) == sorted(word2.upper()):
        return "Oui"
    else:
        return "Non"


def contains_doubles(items: list) -> bool:
    for element in items:
        if items.count(element) > 1:
            return "Oui"
            break
        else:
            return "Non"


def best_grades(student_grades: dict) -> dict:
    max = 0
    grades_moy = {"Nom": "" , "Moyenne": 0}
    for student in student_grades:
        liste = student_grades[student]
        moy = 0
        for each in liste:
            moy = moy + each
        moy = moy/len(liste)
        if moy > max:
            max = moy
            grades_moy = {student : max}
    return grades_moy


def frequence(sentence: str) -> dict:
    my_dict  = {}
    for each in sentence.replace(" ", ""):
        compt = sentence.count(each)

        if compt > 5:
            my_dict[each] =  compt

    return my_dict


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    livre = {}
    ing_list = []
    print("Entrer stop pour arrêter d'enregistrer.")
    recette = input("Entrer le nom d'une recette afin de l'enregistrer: ")
    while recette != "stop":
        print("Puis entrer les ingrédients de la recette ", recette, " :")
        print("Faites stop pour arrêter.")
        ing = input("> ")
        del ing_list[:]
        while ing != "stop":
            ing_list.append(ing)
            print("Vos ingrédients sont: ", ing_list)
            print("Entrer les ingrédients de la recette ", recette, " :")
            print("Faites stop pour arrêter.")
            ing = input("> ")
        livre[recette] = ing_list
        print("Votre livre de recette ressemble à ", livre)
        print("Entrer stop pour arrêter d'enregistrer.")
        recette = input("Entrer le nom d'une recette afin de l'enregistrer: ")
    return livre


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    demande = input("Entrer le nom d'une recette afin de l'afficher : ")
    if demande in ingredients:
        print("Les ingrédients pour cette recette éxistent.")
        return ingredients[demande]
    else:
        return "Les ingrédients n'éxistent pas."


def main() -> None:
    #print(f"On essaie d'ordonner les valeurs...")
    #print("La liste en ordre: ",order())

    #print(f"On vérifie les anagrammes...")
    #print("Est-ce que ce sont des anagrammes? ",anagrams())

    #my_list = [3, 3, 5, 6, 1, 1]
    #print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    #grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    #best_student = best_grades(grades)
    #print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    #sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    #print("Voiçi un dictionnaire avec les occurences de chaque lettre > 5: \n",frequence(sentence))

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print(print_recipe(recipes))



if __name__ == '__main__':
    main()
