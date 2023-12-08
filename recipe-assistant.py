import random

user_ingredients_list = [] #list of ingredients the user has -- user will enter data into this list

recipes = { #dictionary of recipes this program can suggest
 'French Toast' : ['bread', 'eggs', 'syrup', 'butter'],
 'Spaghetti' : ['pasta', 'tomato sauce', 'ground beef', 'parmesan cheese'],
 'Fruit Salad' : ['apples', 'grapes', 'bananas', 'oranges'],
 'Chili' : ['ground beef', 'tomatoes', 'beans', 'chili powder'],
 'Cake' : ['flour', 'sugar', 'eggs', 'butter', 'oil'],
 'Guacamole' : ['avocados', 'lime juice', 'cilantro', 'tomatoes'],
 'Garlic Bread' : ['bread', 'butter', 'garlic'],
 'Mashed Potatoes' : ['potatoes', 'butter', 'milk'],
 'French Fries' : ['potatoes', 'oil'],
 'Scrambled Eggs' : ['eggs', 'milk', 'butter'],
 'Applesauce' : ['apples', 'sugar', 'cinnamon'],
 'Grilled Cheese' : ['bread', 'cheese', 'butter'],
 'Roasted Broccoli' : ['broccoli', 'oil', 'garlic'],
 'Hard-Boiled Eggs' : ['eggs', 'salt'],
 'Fried Chicken' : ['chicken', 'eggs', 'flour'],
 'Banana Bread' : ['bananas', 'flour', 'sugar', 'eggs'],
 'Egg Drop Soup' : ['eggs', 'chicken broth', 'cornstarch'],
 'BLT' : ['bread', 'bacon', 'lettuce', 'tomato', 'mayonnaise'],
 'Sushi' : ['rice', 'seaweed', 'fish'],
 'Chicken Quesadilla' : ['chicken', 'tortilla', 'cheese' ],
 'Mac and Cheese' : ['pasta', 'milk', 'cheese'],
}

def add_ingredients(): #adds ingredients to the user's list of ingredients
    while True:
        user_input = input("Enter an ingredient you have, or type X to return to the main menu.\n")
        user_input = user_input.lower()
        if user_input == "x":
            return user_ingredients_list
        else:
            user_ingredients_list.append(user_input)

def suggest_recipe(user_ingredients_list): #suggests a recipe using ingredients the user has
    suggested_recipes = []

    for recipe, ingredients in recipes.items():
        if all(ingredient in user_ingredients_list for ingredient in ingredients):
            suggested_recipes.append(recipe)

    if suggested_recipes:
            print("You can make the following recipes:")
            for recipe in suggested_recipes:
                print(recipe)
    else:
        print("Sorry, no recipes found with the given ingredients.")    

def all_recipes(): #prints all recipes the program knows by name of recipe, user will then have the option to select a recipe to see more details
    n = 1
    for x in recipes:
        print(f"{n}. {x}")
        n += 1
    see_more = input("Would you like to see more details about any recipe that was shown? Type 'Yes' or 'No.'\n")
    see_more = see_more.lower()
    if see_more == "yes":

        which_recipe = input("What is the name of the recipe you would like to see more about?\n")
        for a, b in recipes.items():
            if a.lower() == which_recipe.lower():
                print(f"{a}: You will need {b}")
                break
            else:
                continue
    
    elif see_more == "no":
        return
    else:
        print("Sorry, I don't understand. Returning to main menu.")
        return

def random_recipe(): #prints a random recipe
    x1, x2 = random.choice(list(recipes.items()))
    print(f"{x1}: You will need {x2}")
    another_random = input("Would you like to see another random recipe? Type 'Yes' or 'No'.\n")
    another_random = another_random.lower()
    if another_random == "yes":
        random_recipe()
    elif another_random == "no":
        return
    else: 
        print("Sorry, I don't understand. Returning to main menu.")
        return


print("Welcome chef! I am your personal recipe assistant. Let's get to cooking!")
while True: #prints the menu where users can select how they want to navigate the program, until user ends the program with option 6. options run one of the above functions
    menu_selection = input("How can I help you plan your next meal?\n1. Add Ingredients\n2. Suggest a Recipe\n3. View All Recipes\n4. Random Recipe\n5. Exit Program\n")
    if menu_selection=="1":
        add_ingredients()
    elif menu_selection=="2":
        suggest_recipe(user_ingredients_list)
    elif menu_selection=="3":
        all_recipes()
    elif menu_selection=="4":
        random_recipe()
    elif menu_selection=="5":
        break
    else:
        print("Invalid menu selection. Chef, please choose a number 1-5:")