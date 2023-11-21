import os

cmd ="curl https://raw.githubusercontent.com/ksu-is/Recipe-Assistant/main/accepted_ingredients.txt -o accepted_ingredients.txt" #link to list of ingredients the user is allowed to enter, currently incomplete

os.system(cmd) #opens the ingredients link, reads the content, and converts it into a list
ingredients = open("accepted_ingredients.txt", "r")
ingredients_text = ingredients.read()
accepted_ingredients_list = ingredients_text.split("\n") #accepted ingredients list

cmd1 ="curl https://raw.githubusercontent.com/ksu-is/Recipe-Assistant/main/recipes.txt -o recipes.txt" #link to list of recipes the program can suggest, currently incomplete

os.system(cmd1) #opens the recipes link, reads the content, and converts it into a list
recipes = open("recipes.txt", "r")
recipes_text = recipes.read()
recipes_list = recipes_text.split("\n") #recipes list

#print(ingredients_list) tested these two to make sure they worked, and they did
#print(recipes_list)

user_ingredients_list = [""] #list of ingredients the user has -- user will enter data into this list

def add_ingredients(): #adds ingredients to the user's list of ingredients
    while True:
        ingredients_input = input('Enter an ingredient you have, or type "exit" to return to the main menu\n')
        ingredients_input = ingredients_input.lower()
        if ingredients_input=="exit":
            return
        elif ingredients_input in accepted_ingredients_list:
            user_ingredients_list += ingredients_input #this doesnt work but i will solve this later
        else:
            display_accepted_ingredients = input("Sorry, I don't recognize that ingredient. Would you like to see a list of ingredients I accept? Type 'yes' or 'no'.\n")
            display_accepted_ingredients = display_accepted_ingredients.lower()
            if display_accepted_ingredients == "yes":
                accepted_ingredients()
            elif display_accepted_ingredients == "no":
                print("Understood! Returning to ingredient input menu...")
            else:
                print("Sorry, I don't understand! Returning to ingredient input menu...")


def accepted_ingredients(): #prints a list displaying the ingredients the program accepts
    print(accepted_ingredients_list)

def suggest_recipe(): #suggests a recipe using ingredients the user has -- **plan to add an option that says something along the lines of "dont like? let me suggest a different recipe!"**
    print()

def all_recipes(): #prints all recipes the program knows by name of recipe, user will then have the option to select a recipe to see more details
    print()

def random_recipe(): #prints a random recipe
    print()

print("Welcome chef! I am your personal recipe assistant. Let's get to cooking!")
while True: #prints the menu where users can select how they want to navigate the program, until user ends the program with option 6. options run one of the above functions
    menu_selection = input("How can I help you plan your next meal?\n1. Add Ingredients\n2. View Accepted Ingredients\n3. Suggest a Recipe\n4. View All Recipes\n5. Random Recipe\n6. Exit Program\n")
    if menu_selection=="1":
        add_ingredients()
    elif menu_selection=="2":
        accepted_ingredients()
    elif menu_selection=="3":
        suggest_recipe()
    elif menu_selection=="4":
        all_recipes()
    elif menu_selection=="5":
        random_recipe()
    elif menu_selection=="6":
        break
    else:
        print("Invalid menu selection. Chef, please choose a number 1-6:")