with open("students.csv", "a") as file:
    
    #Splitting the input into the name and house
    name, house = input("input: ").split(",")

    #Writing the name and house into the students.csv
    file.write(f"{name}, {house}")