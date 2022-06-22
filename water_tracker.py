from dataclasses import dataclass


from functools import reduce# needed for using reduce function

import numpy as np
import matplotlib.pyplot as plt


VOLUME_GOAL = 3000 #liters
today = []
today_water = []
today_fruit = []
today_beverage = []
today_food = []

@dataclass
class Water:
    name : str
    volume : float

def populate(good):
    if good.name == "water":
        today_water.append(good)
    elif good.name == "fruit":
        today_fruit.append(good)
    elif good.name == "beverage":
        today_beverage.append(good)
    else:
        today_food.append(good)


#menu

done = False

while not done:
    print("""
    (1) Add a new consumption
    (2) Visualize progress
    (Q) Quit
    """)


    choice = input("Choose an option: ")

    if choice == "1":
        print("Adding a new consumption!")
        
        #submenu

        sub_done = False

        print("""
        (1) Water (eg: bottle, glass)
        (2) Fruit (eg: orange, apple)
        (3) Beverage (eg: milk, coca-cola, beer)
        (4) Food (eg: meet, salad)
        (Q) Quit
        """)

        sub_choice = input("Choose an option: ")

        if sub_choice == "1":
            print("Adding water ")
            volume = int(input("mL of water: "))
            water = Water("water", volume)
            today.append(water)
        
        elif sub_choice == "2":
            print("Adding fruit ")
            volume = int(input("mL of water contained: "))
            fruit = Water("fruit", volume)
            today.append(fruit)

        elif sub_choice == "3":
            print("Adding beverage ")
            volume = int(input("How much mL of water have you drunk? "))
            beverage = Water("beverage", volume)
            today.append(beverage)

        elif sub_choice == "4":
            print("Adding food ")
            volume = int(input("mL of water contained: "))
            food = Water("food", volume)
            today.append(food)

        elif sub_choice.upper() == "Q":
            print("Exit")
            sub_done = True

        else:
            print("ERROR!")

    elif choice == "2":
        for good in today: populate(good)

        water_sum = sum(water.volume for water in today_water)
        fruit_sum = sum(fruit.volume for fruit in today_fruit)
        beverage_sum = sum(beverage.volume for beverage in today_beverage)
        food_sum = sum(food.volume for food in today_food)
        total_water_sum = water_sum + fruit_sum + beverage_sum + food_sum


        fig, axs = plt.subplots(2, 2)
        
        labels = ["Water", "Fruit", "Beverage", "Food"]
        axs[0, 0].pie([water_sum, fruit_sum, beverage_sum, food_sum], labels = labels, autopct = lambda pct: f"{round ( pct )}%")
        axs[0, 0].set_title("Water Distribution")
        
        axs[0, 1].bar(labels, [water_sum, fruit_sum, beverage_sum, food_sum], width = 0.4)
        axs[0, 1].set_title("Distribution amount")

        axs[1, 0].pie([total_water_sum, VOLUME_GOAL - water_sum], labels = ["Already drunk", "GOAL"], autopct = lambda pct: f"{round ( pct )}%")
        axs[1, 0].set_title("Water goal")

        axs[1, 1].plot(list(range(len( today ))), np.cumsum([good.volume for good in today]), label = "Water drunk" )  
        axs[1, 1].plot(list(range(len( today ))), [VOLUME_GOAL] * len(today), label = "Water goal" )  
        axs[1, 1].legend()
        axs[1, 1].set_title("History")  
        

        fig.tight_layout()
        plt.show()




    elif choice.upper() == "Q":
        print("Exit")
        done = True
    
    else:
        print("ERROR!")
