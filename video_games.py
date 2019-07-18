import random
def greet(player):
    if player == " ":
        return "Welcome,__. ready up"
    else:
        return "welcome," + player
name1 = input("Enter player 1's name: ")
print(greet(name1))

your_health = 100
opponent_health = 100
 
damages = {
    "pistol": 10, "Ar_15": 30, "rpg":100, "grenade":50, "cpu":random.randint(0, 100)
}

def  gun(weapon):
     if weapon  == "pistol":
        return "your opponent has lost " + str(10) + " health\n" + "you have lost " + str(damages["cpu"]) + " damage"
     if weapon  == "Ar_15":
        return "your opponent has lost " + str(30) + " health\n" + "you have lost " + str(damages["cpu"]) + " damage"
     if weapon  == "rpg":
        return "your opponent has lost " + str(100) + " health!\n" + " They're DEAD, Victory!!"
     if weapon  == "grenade":
        return "your opponent has lost " + str(50) + " health\n" + " you have lost " + str(damages["cpu"]) + " damage"

while(opponent_health > 0):
    weapon = input("Weapon Test, Choose Your WeaponS:\n  ")
    print(gun(weapon))
    
    print( "your health is " + str(your_health - damages["cpu"]))
   

   
    print( "your opponents health is " + str(opponent_health - damages[weapon]))
    if damages == 100:
            print("Your opponent is dead. you have Won!!!!")
    your_health = your_health - damages["cpu"]
    opponent_health = opponent_health - damages[weapon]
        

