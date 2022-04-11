import random

# Rock Paper Scissors
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chose stone
    elif comp == 'st':
        if you=='sr':
            return False
        elif you=='p':
            return True
    
    # Check for all possibilities when computer chose paper
    elif comp == 'p':
        if you=='st':
            return False
        elif you=='sr':
            return True
    
    # Check for all possibilities when computer chose sissor
    elif comp == 'sr':
        if you=='p':
            return False
        elif you=='st':
            return True

print("Comp Turn:Stone(st) Paper(p) or Sissor(sr)?\n")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 'st'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 'sr'

you = input("Your Turn:\n1.Stone(st)\n2.Paper(p)\n3.Sissor(sr)?\n")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")