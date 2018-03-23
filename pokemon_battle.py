
opponent = input("Now choose an opponent(Squirtle,Charmander,Bulbaseur)").upper()

hp_opponent = 0
hp_pikachu = 35

if opponent == "SQUIRTLE":
    hp_opponent = 50
if opponent == "CHARMANDER":
    hp_opponent = 45
if opponent == "BULBASEUR":
    hp_opponent = 40

while hp_pikachu > 0 and hp_opponent > 0:

    attack = input ("choose an attack(Spark / Volt Ball)").upper()
    if attack == "SPARK":
        hp_opponent -=10
        print("You have done 10 damage")

    if attack == "VOLT BALL":
        hp_opponent -=20
        print ("You have done 20 damage")

    print("Hp of enemy {}".format(hp_opponent))

    if opponent == "SQUIRTLE":
            hp_pikachu -=5
    if opponent == "BULBASUER":
            hp_pikachu -=5
    if opponent == "CHARMANDER":
            hp_pikachu -=5

    print ("Hp of Pickahu {}".format(hp_pikachu))

print ("Combat has finished")

if hp_pikachu <= 0:
    print ("You Lost")

if hp_opponent <=0:
    print("You Win")
