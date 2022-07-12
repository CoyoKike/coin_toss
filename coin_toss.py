import random

while True:
    choice = input("""Choose 
    1) Head
    2) Tail
    3) Exit""")
    if choice == "3" or choice.lower() == 'exit':
        quit()
    else:
        toss = random.randint(1, 10)
        if toss <= 5:
            print("Head!")
        else:
            print("Tail!")
