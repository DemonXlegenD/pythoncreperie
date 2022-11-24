#Ingredients listés selon la saveur
ingredients = {
    "Sucrée" : ["Nutella", "Sucre", "Chantilly", "Pomme", "Poire", "Framboise", "Fraise",  "Confiture de Pomme", "Confiture de Poire", "Confiture de Framboise", "Confiture de Fraise"],
    "Salée" : ["Jambon", "Poulet", "Kebab", "Steack Haché", "Tenders"],
    "Végétarienne" : ["Tomate", "Salade", "Oignon", "Poivron", "Emmental", "Mozzarela", "Cheddar", "Chèvre"]
}

class Ingredient():

    def __init__(self, saveur, i):
        self.nom = ingredients[saveur][i]
        self.prix = 0
        self.saveur = 0
        self.suplement = "Aucun"


#Prix de chaque ingrédient

prix= {
    "Jambon" : 1,
    "Poulet" : 1,
    "Kebab" : 1,
    "Steack haché" : 1,
    "Tenders" : 1.50,
    "Emmental" : 0.50,
    "Mozzarela" : 1,
    "Cheddar" : 0.50,
    "Chèvre" : 1,
    "Nutella" : 0.50,
    "Sucre" : 0.50,
    "Chantilly": 0.50,
    "Pomme" : 1,
    "Poire" : 1,
    "Framboise": 1,
    "Fraise" : 1,
    "Confiture de pomme" : 1.50,
    "Confiture de poire" : 1.50,
    "Confiture de framboise" : 1.50,
    "Confiture de fraise" : 1.50,
    "Tomate" : 1,
    "Salade" : 1,
    "Oignon" : 1,
    "Poivron" : 1
}
