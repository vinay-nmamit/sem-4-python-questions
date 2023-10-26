
print("Options: \n1. Rock \n2. Paper \n3. Scissors")
plsc1 = 0
plsc2 = 0

while True:
    a = int(input("Player 1: "))
    b = int(input("Player 2: "))

    if ((a == 1 and b == 2) or (a == 3 and b == 1) or (a == 2 and b == 3)):
        print("Congrats Player 2")
        plsc2 += 1

    if ((a == 2 and b == 1) or (a == 1 and b == 3) or (a == 3 and b == 2)):
        print("Congrats Player 1")
        plsc1 += 1

    if a == b:
        print("It's a tie!!!")

    if plsc1 == 5 or plsc2 == 5:
        print("Player 1 score: ", plsc1)
        print("Player 2 score: ", plsc2)
        if plsc1 > plsc2:
            print("Player 1 wins")
        elif plsc1 < plsc2:
            print("Player 2 wins")
        else:
            print("It's a tie")
        break  # End the game when a player reaches a score of 5

        
    

           



    
