import random
player=''
n=1
p_count=c_count=0
LIST=['rock','paper','scissor','scissor','rock','paper']
COMBINATIONS={"rock":"scissor","scissor":"paper","paper":"rock"}
def main():
    global player,n
    
    print("------PLAYER V/S COMPUTER--------")
    player = input("Enter the name::: ") 
    n=int(input("Enter the number of times the game to be played:: "))
    for i in range(1,n+1):
        each_turn(i)
    if(p_count>c_count):
        print(f"{player} wins!!!!")
    elif(p_count<c_count):
        print("Computer wins!!")
    else:
        print("Its a tie!!")

def computer_turn():
    ch=random.choice(LIST)
    print(f"Computer turn's:: {ch}")
    return ch

def player_turn():
    ch=input("Enter your choice::: ")
    ch=ch.lower()
    return ch

def check_win(p,c):
    for key,value in COMBINATIONS.items():
        if(p==key):
            if(c==value):
                return 1 #p wins this turn
        elif(c==key):
            if(p==value):
                return 2 #c wins this turn
        else:
            continue
        
    
def each_turn(n):
    global p_count
    global c_count
    print(f"Turn {n}:: ")
    print("Computer has chosen....")
    player_ch=player_turn()
    while True:
        if player_ch not in LIST:
            player_ch=player_turn()
        else:
            break
    comp_ch=computer_turn()
    res=check_win(player_ch,comp_ch)
    if res==1:
        print(f"{player_ch}>>>{comp_ch}")
        p_count+=1
    elif res==2:
        print(f"{comp_ch}>>>{player_ch}")
        c_count+=1
    else:
        print(f"{player_ch}==={comp_ch}")
        print("Its a tie!")

    print(f"{player}:{p_count}")
    print(f"Computer:{c_count}")
    print("\n\n")

        




if __name__ == '__main__':
    main()
