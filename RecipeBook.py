
recipes = [] #stores all Recipes

class Error(BaseException):
    pass

class RecipeDoesNotExistException(Exception):
    
    def __init__(self):
        Exception.__init__(self,"This recipe does not exist yet.")


class Ingredient(object):
    

    def __init__(self, name):
        
        self.name = name
        
    def __str__(self):
        return self.name 
    
    def get_name(self):
        return self.name

        
class Recipe(object):
   
    def __init__(self, name, ingredients, instructions):
        
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        
    def __str__(self):
        a = ""
        for i in range(len(self.ingredients)):
            a += str(self.ingredients[i]) + "\n"
        a = a.strip()
        return "Recipe: " + self.name + "\n" + "Ingredients: \n" + str(a) + "\n" + "Instructions:\n " + self.instructions
    
    def print_ingredients(self):
        for i in self.ingredients:
            print(str(i))
    
    def get_name(self):
        return self.name
    
    def set_name(self,name):
        self.name = name
    
    def get_ingredients(self):
        return self.ingredients
    
    def set_ingredients(self,ingredients):
        self.ingredients = ingredients
        
    def get_instructions(self):
        return self.instructions
    
    def set_instructions(self,instruct):
        self.instructions = instruct
        
def main():
    print ("Welcome to your Recipe Book")
    print()
    while(True):
        print("1. Add new Recipe manually")
        print("2. Add new Recipe(s) from file")
        print("3. Search for a Recipe by name")
        print("4. Search for Recipes by ingredient(s)")
        print("5. Edit existing Recipe")
        print("6. Write all recipes to a file")
        print("7. View all recipes")
        print("8. Exit")
        
        while(True):
            try:
                choice = int(input())
                break
            except ValueError:
                print("Please enter a number between 1 and 7")
                pass
  
        if choice == 1:
            name = input("Recipe name?")
            name = name.lower() 
            
            ingredients = input("Recipe ingredients? (separate with commas)\nExample: 1/4 tea basil, 2 eggs, 1 strip bacon\n")
            instructions = input("Recipe instructions.\n")
            instructions = instructions.lower()
            
            #split the ingredients
            ingredients = ingredients.lower()
                
            f = ingredients.split(",")
            v = []
            
            ing_name = []
            for i in f:
              x = i.strip()
              ing_name.append(x)
            #print(ing_name)#remove
            
            ing_list = []
            for i in range(len(ing_name)):
                x = Ingredient(ing_name[i])
                ing_list.append(x)            
            
            #create new Recipe
            x = Recipe(name, ing_list, instructions)
            print(str(x))
            recipes.append(x)
            
        elif choice == 2:
            
            print("Please enter the name of file. \n Format: \n 1 \n Cookies \n 1. 1/4 tea butter \n 2. 2 cup, flour \n 3. 1 cup, chocolate chips\n Bake at 300 for 1 hour")
            file_name = input()
            with open(file_name,"r+") as file:
                num = file.readline()#number of recipes in file
                 
                try:
                    num = int(num)
                except ValueError:
                    print("Incorrect file format. The first line should be the number of recipes in the file.")
                    break
                z = file.readline()
                name = z.strip()
                name = name.lower()
                
                check = 0 #count number recipes read in so far
                names = []#store name of each ingredient 
                
                prev_line = False
                
                for line in file:
                    
                    l = line
                    l = l.strip()
                    l = l.lower()
                    
                    if l != "": 
                        if l[0].isdigit() and l[1] == ".":
                            
                            a = l[2:len(l)]
                            a = a.strip()
#                             
#                             g = []
#                             g.append(a)
#                             
                            y = a.split(",")
                            
                            names.append(y[0].lstrip())
#                             print(y[0])
#                             print(y[1])
                                
                        elif not prev_line:
                            instructions = l
                    
                        elif prev_line:
                            name = l
                            prev_line = False
                        
                    elif l == "":
                        ingred = []#stores all the Ingredients
                        for ingredient in range(len(names)):
                            
                            e = Ingredient(names[ingredient])
                            ingred.append(e)
                            
                        recipe = Recipe(name,ingred,instructions)
                        print(str(recipe) + "\n")
                        
                        recipes.append(recipe)
                        check += 1
                        if(check == num):
                            break
                        prev_line = True
                    
                        names[:] = []#clear the names
                        
                #to add the final item
                ingred = []#stores all the Ingredients
                for ingredient in range(len(names)):
                    
                    e = Ingredient(names[ingredient])
                    ingred.append(e)
                    
                recipe = Recipe(name,ingred,instructions)
                print(str(recipe) + "\n")
                recipes.append(recipe)
                
        elif choice == 3:
            name = input("Name of recipe?")
            name = name.lower()
            name = name.strip()
            a = []
            
            for recipe in recipes:
                if name in recipe.get_name():
                    print(str(recipe))
                    a.append(recipe)
            if len(a) == 0:
                print("There are no recipes with that name in the recipe book.\n" )
                 
        elif choice == 4:
            ing = input("Name of the ingredient(s)? (separate with commas)\n")
            ing = ing.lower()
            ing = ing.split(",")
            ing_list = []
            
            for i in ing:
                x = i.strip()
                ing_list.append(x)
            
            z = []
            al = []
            
            for recipe in recipes:
                for i in recipe.get_ingredients():
                    for m in ing_list:
                        if(i.get_name() == m):
                            z.append(i)
                            al.append(recipe)
                if(len(z) != len(ing_list)):       
                    z = [] 
            if len(al) == 0:
                print("No recipes contain that ingredient.")
                print()
                
            for i in al:
                print(str(i)) 
                
        elif choice == 5:
            name = input("Name of the recipe?\n")
            name = name.lower()
            name = name.strip()
            exist = False#to check if there are no matching recipes
            
            for recipe in recipes:
                if name == recipe.get_name():
                    exist = True#recipe found
                    #print(str(recipe) + "\n")
                    c = input("What would you like to change? (name, ingredient(s) and/or instructions)\nExample: name,   instructions\n")
                    c = c.lower()
                    c = c.strip()
                    check = True
                    
                    change = c.split(",")#split the changes
                    for i in range(len(change)):
                        check = True
                        while(check):
                            if not change[i] == "name" and not change[i] == "instructions" and not change[i] == "ingredients" and not change[i] == "ingredient":
                                c = input("Please make sure all entries are either name, ingredients, or instructions.")
                                c = c.lower()
                                c = c.strip()
                                change[:] = []
                                change = c.split(",")
                                for m in change:
                                    pass
                            else:
                                check = False
                                
                    changes = []
                    for i in change:
                        x = i.strip()
                        changes.append(x)
                    for i in changes:
                        
                        if i == "name":
                            n = input("What would you like the new name to be?\n")
                            name = n.lower()
                            name = name.strip()
                            
                            recipe.set_name(name)
                            
                        elif i == "instructions":
                            n = input("What would you like the new instructions to be?\n")
                            ins = n.lower()
                            ins = ins.strip()
                            
                            recipe.set_instruction(ins)
                            
                        elif i == "ingredients":
                            n = input("Would you like to delete, add, or edit an ingredient?\n")
                            n = n.lower()
                            n = n.strip()
                            while not n == "delete" and not n == "add" and not n == "edit":
                                n = input("Please enter delete, add, or edit.")
                            
                            if n == "delete":
                                
                                #to store new ingredient list
                                ing = []
                                #print out all the ingredients in the recipe
                                recipe.print_ingredients()
                                item = input("Which ingredient would you like to delete?\n")
                                item = item.lower()
                                item = item.strip()
                                
                                for i in recipe.get_ingredients():
                                    if not i.get_name() == item:
                                        ing.append(i)
                                
                            
                    
            if not exist:
                print("There are recipes with that name in the recipe book.\n")
            
        elif choice == 6:
            file_name = input("Name of output file? (end name with .txt)")#get name of file
            
            #if file does not end in .txt, wait until the input does
            while file_name[len(file_name)-4:len(file_name)] != ".txt":
                file_name = input("Please enter a name that ends with .txt")
                
            file = open(str(file_name), "w+")
            for recipe in recipes:
                file.write(str(recipe) + "\n\n")
                
            file.close()
        
        elif choice == 7:
            for recipe in recipes:
                print(str(recipe) + "\n")
        
        elif choice == 8:
            print("Goodbye!")
            break
                
        
main()


