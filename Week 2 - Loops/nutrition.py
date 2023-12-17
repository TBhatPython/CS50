def main():
    #Get input and convert to lowercase to prevent case confusion
    fruit = input("Item: ").lower()
    getCalories(fruit)

def getCalories(fruit):

    #The dictionary with fruits and corresponding calories
    fruitDict = {"apple" : 130, "avocado" : 50, "banana" : 110, "cantaloupe" : 50, 
                "grapefruit" : 60, "grapes" : 90, "honeydew melon" : 50, "kiwifruit" : 90,
                "lemon" : 15,"lime" : 20,"nectarine" : 60, "orange" : 80,
                "peach" : 60,"pear" : 110,"pineapple" : 50, "plums" : 70,
                "strawberries" : 50,"sweet cherries" : 100,"tangerine" : 50, "watermelon" : 80,
    }

    #Access the calories of the fruit given
    print("Calories : ", fruitDict[fruit])


main()