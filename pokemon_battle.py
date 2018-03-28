
opponent = input("Now choose an opponent(Squirtle,Charmander,Bulbaseur)").upper()
# Selection
hp_opponent = 0
hp_pikachu = 35
attack_p = 0

if opponent == "SQUIRTLE":
    hp_opponent = 50
    name_opponent_v2 = "Squirtle"
    attack_p = 5

elif opponent == "CHARMANDER":
    hp_opponent = 45
    name_opponent_v2 = "Charmander"
    attack_p = 5

elif opponent == "BULBASEUR":
    hp_opponent = 40
    name_opponent_v2 = "Bulbaseur"
    attack_p = 5

while hp_pikachu > 0 and hp_opponent > 0:
# Fight
    attack = input ("choose an attack(Spark / Volt Ball)").upper()
    if attack == "SPARK":
        hp_opponent -=10
        print("You have done 10 damage")

    elif attack == "VOLT BALL":
        hp_opponent -=20
        print ("You have done 20 damage")

    print("Hp of {} is {}".format(name_opponent_v2, hp_opponent))
    print("you proved  damage")
    print ("Hp of Pikachu is {}".format(hp_pikachu))


print ("Combat has finished")

if hp_pikachu <= 0:
    print ("You Lost")

if hp_opponent <=0:
    print("You Win")
