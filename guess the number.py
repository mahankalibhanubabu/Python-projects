def main():
    ans = input("Game Adudhama? (Y/N): ").capitalize()
    if(ans == "Y"):
        start_game()
    else:
        print("Mooskoni aadu, choice ledu ikkada")
        start_game()

def start_game():
    print("Game chaala easy ga untundi.... ani ANUKOKU")
    print("inka start chedham paa")
    print("<---- Guess the number ---->")
    x = int(input("What's x? "))
    print("Orini... asal neeku nenu range ae ivaledu, mari ela aadudham anukunav pechodaa?")
    print("Range: 1 - 10")
    x = int(input("What's x? "))
    count = 3
    while(x != 9):
        count -= 1
        print("Chepinana, nuvvu wastuu, pakkaki velu")
        print("Malli aadu, yedavaku\n")
        print(f"Neeku inka {count} chances ye unnai")
        if(count == 0):
            print("Odipoyanu ani badhapadakunda, velli chaduvuko, asale masth time waste chesinav")
            break
        x = int(input("What's x? "))
    if(count == 0):
        print()
        aadu = input("Sarle malli aduthava? (Y/N)")
        print()
        print("Ippude cheppina... poi chaduvuko ani. DHOBEYYYYYYYY")
    else:
        print("Gelichi peekindhi emi ledu nuvvu")

main()