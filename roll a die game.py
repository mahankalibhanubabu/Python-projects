print ("****welcome to my world **** \n let's play a game called die roll :-")
ps1 = 0
ps2 = 0
for x in range(3):
    pv1= int(input("enter player-1 rolled value :"))
    if pv1 > 6:
        print("invalid rolled value")
        print(" please enter valid rolled value")
        pcv1= int(input("second chance enter player-1 rolled value :"))
        ps1=ps1+ pcv1
    else :
        ps1=ps1+ pv1   
    pv2 = int(input("enter player-2 rolled value :")) 
    if pv2 > 6:
        print("invaild rolled value")
        print("u lost ur choice please enter valid rolled value")
        pcv2= int(input("second chance enter player-2 rolled value :"))
        ps2=ps2+ pcv2
    else :
        ps2=ps2+ pv2
    print("score of player 1: " ,ps1)
    print("score of player 2: " ,ps2)
    print ("roll again :")  
print("Total score of player 1: ",ps1)
print("Total score of player 2: ",ps2)
if ps1 > ps2:
    print("player 1 wins ")
elif ps2 > ps1:
    print("player 2 wins")
else:
    print("It's a draw")

input("Press enter to continue.")  

print("### Game Over ###")
print("Player 1 score:",ps1)
print("Player 2 score:", ps2)