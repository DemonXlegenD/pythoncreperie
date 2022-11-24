from ingredient import Ingredient


class Crepe():

    def __init__(self, composition):
        self.nom = crepe[composition]["nom"]
        self.saveur = crepe[composition]["saveur"]
        self.prix = crepe[composition]["prix"]
        self.ingredient = crepe[composition]["ingrédients"]

"""-------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""--------------------------------------------------------------------------\DICTIONAIRES UTILES/---------------------------------------------------------------------------"""
"""-------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
    
crepe_nutella = {
    "nom" : "Crêpe Nutella",
    "saveur": "Sucrée",
    "prix": 6.90,
    "ingrédients": [Ingredient("Sucrée", 0).nom]
}
crepe_emmental = {
    "nom" : "Crêpe Emmental",
    "saveur": "Végétarienne",
    "prix": 6.90,
    "ingrédients": [Ingredient("Végétarienne", 4).nom]

}

crepe_fraise_chantilly = {
    "nom" : "Crêpe Fraise Chantilly",
    "saveur": "Sucrée",
    "prix": 7.90,
    "ingrédients": [Ingredient("Sucrée", 6).nom, Ingredient("Sucrée", 2).nom]

}

crepe_jambon_emmental = {
    "nom" : "Crêpe Jambon Emmental",
    "saveur": "Salée",
    "prix": 7.90,
    "ingrédients": [Ingredient("Salée", 0).nom, Ingredient("Salée", 1).nom]

}

crepe_kebab_poulet = {
    "nom" : "Crêpe Kebab Poulet",
    "saveur": "Salée",
    "prix": 8.90,
    "ingrédients": [Ingredient("Salée", 2).nom, Ingredient("Salée", 1).nom]

}

crepe_perso = {
    "nom" : "Crêpe Perso",
    "saveur": "Au choix",
    "prix": 10,
    "prixsupp": 0,
    "ingrédients": "3 ingrédients au choix"

}
    
crepe = {
    "Nutella" : crepe_nutella,
    "Fraise Chantilly" : crepe_fraise_chantilly,
    "Emmental" : crepe_emmental,
    "Jambon Emmental" : crepe_jambon_emmental,
    "Kebab Poulet" : crepe_kebab_poulet,
    "Perso" : crepe_perso    
}

