import random
print("Enter the number of friends joining (including you):")
friends_number = int(input())
friends_dict = {}
if friends_number <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range (0, friends_number):
        friends_dict[input()] = 0 
    print("Enter the total bill value:")
    bill = int(input())
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    answer = input()
    if answer == "Yes":
        try:
            lucky_friend = random.choice(list(friends_dict.keys()))
            print(f'{lucky_friend} is the lucky one!')  
            cost = round(bill / (friends_number - 1), 2)  
            friends_dict = {x: cost for x in friends_dict}
            friends_dict[lucky_friend] = 0
            print(friends_dict)
        except ValueError:
            print('error')
    else:  
        cost = round(bill / friends_number, 2)
        print("No one is going to be lucky")
        friends_dict = {x: cost for x in friends_dict}
        print(friends_dict)
        
