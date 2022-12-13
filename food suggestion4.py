from spellchecker import SpellChecker

# user ingredient input
ingredient = input("Please enter an ingredient or q to quit: ").lower()

# recipes and ingredient
recipes = [{"recipe": "Chocolate Cake",
            "ingredients": ["flour", "sugar", "cocoa powder", "butter", "egg", "milk", "vanilla extract"]},
           {"recipe": "Pancake",
            "ingredients": ["flour", "milk", "egg"]},
           {"recipe": "Apple pie",
            "ingredients": ["apple", "sugar", "flour"]},
           {"recipe": "Strawberry Smoothie",
            "ingredients": ["strawberry", "banana", "milk", "honey"]},
           {"recipe": "Egg Fried Rice",
            "ingredients": ["egg", "rice", "msg", "garlic", "shallot", "spring onion", "soy sauce"]},
           {"recipe": "Spaghetti Carbonara",
            "ingredients": ["spaghetti", "egg", "bacon", "parmesan cheese", "pepper"]},
           {"recipe": "Chicken soup",
            "ingredients": ["chicken", "broth", "carrot"]},
           
]

# Spell checking
written_correctly = SpellChecker()
# find the recipe
while ingredient != "q":
    for recipe in recipes:
        if ingredient in recipe["ingredients"]:
            print(recipe["recipe"])
            print("All the Ingredients: ",recipe["ingredients"])
# misspelling and numeric correction 
    if ingredient.isnumeric():
        print("Sorry, that's a number. Please try again!")
    elif ingredient not in written_correctly:
        misspelling = written_correctly.correction(ingredient)
        print(f"Did you mean {misspelling}?")
# repeat the process
    ingredient = input("Please enter an ingredient or q to quit: ").lower()



