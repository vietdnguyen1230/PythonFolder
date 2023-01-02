wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 70

wizard_damage = 150
elf_damage = 100
human_damage = 20

dragon_hp = 300
dragon_damage = 50

while True:
    while True:
        print("1) Wizard")
        print("2) Elf")
        print("3) Human")
        print("4) Exit")
        character = input("Choose your character: ")
        if character == "1" or character == "Wizard":
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            print("You have chosen the character: ", character)
            print("Health: ", my_hp)
            print("Damage: ", my_damage, "\n")
            break
        elif character == "2" or character == "Elf":
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            print("You have chosen the character: ", character)
            print("Health: ", my_hp)
            print("Damage: ", my_damage, "\n")
            break
        elif character == "3" or character == "Human":
            character = human
            my_hp = human_hp
            my_damage = human_damage
            print("You have chosen the character: ", character)
            print("Health: ", my_hp)
            print("Damage: ", my_damage, "\n")
            break
        elif character == "4" or character == "exit":
            print("Goodbye!")
            exit()
        else:
            print("Unknown character")

    while True:
        dragon_hp = dragon_hp - my_damage
        my_hp = my_hp - dragon_damage
        if dragon_hp == dragon_hp:
            print("The", character, "damaged the Dragon!")
            print("the Dragon's hitpoints are now:", dragon_hp, "\n")
            if dragon_hp <= 0:
                print("The Dragon has lost the battle.")
                break
        if my_hp == my_hp:
            print("The Dragon strikes back at", character)
            print("The", character, "'s", "hitpoints are now:", my_hp, "\n")
            if my_hp <= 0:
                print("The", character, "has lost the battle.")
                break

    start = input("\nenter y to play again n to exit: ")
    if start == "y":
        continue
    else:
        if start == "n":
            print("Thanks for playing!")
            exit()
