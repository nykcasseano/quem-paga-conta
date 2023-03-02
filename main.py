#Split string method
import random

names_string = input("Me forneça os nomes de todos, separadamente pela virgula")

names = names_string.split(",")

#Get the total number of items in list.
#num_items = len(names)

# #Generate random numbers between 0 and the last index.
# random_choice = random.randint(0, num_items -1)
# person_who_will_pay = names[random_choice]

person_who_will_pay = random.choice(names)
print(person_who_will_pay + "is going to pay the bill today!")