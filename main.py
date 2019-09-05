
# List = []
# List.append("1111")
# print(List)
# def funcx(y): return y**2
# print(funcx(5))


# numbers = list(range(3, 8))
# print(numbers)

# numbers = list(range(5, 20, 2))
# print(numbers)

# words = ["hello", "world", "spam", "eggs"]
# counter = 0
# max_index = len(words) - 1

# while counter <= max_index:
#    word = words[counter]
#    print(word + "!")
#    counter = counter + 1


# words = ["hello", "world", "spam", "eggs"]
# for word in words:
#   print(word + "!")

# for i in range(5):
#   print("hello!")

""" calculator"""
# while True:
#    print("Options:")
#    print("Enter 'add' to add two numbers")
#    print("Enter 'subtract' to subtract two numbers")
#    print("Enter 'multiply' to multiply two numbers")
#    print("Enter 'divide' to divide two numbers")
#    print("Enter 'quit' to end the program")
#    user_input = input(": ")

#    if user_input == "quit":
#       break
#    if user_input == "add":

#         num1 = float(input("Enter a number: "))
#         num2 = float(input("Enter another number: "))
#         result = str(num1 + num2)
#         print("The answer is " + result)

#    elif user_input == "subtract":
#       ...
#    elif user_input == "multiply":
#       ...
#    elif user_input == "divide":
#       ...
#    else:
#       print("Unknown input")


# def multiply(x, y):
#    return (x * y)

# a = 4
# b = 7
# operation = multiply
# print(operation(a, b))


# import emoji

# user_input = int(input("Enter number"))
# # print('  '* (user_input) + emoji.emojize(' :heart_eyes:', use_aliases=True))
# for i in range(0,user_input+1):
#     print('  '* (user_input-i+1) + emoji.emojize(' :heart_eyes:', use_aliases=True)*(i+i))

# import random
# import sys

# random_no = random.randint(1, 10)

# # user_input = int(input('Enter valid number 1 -10 : '))
# user_input = None


# while True:
#     user_input = int(input('Enter valid number 1 -10 : '))

#     if user_input > random_no:
#         print(' high ')
#     elif user_input < random_no:
#         print('low ')
#     else:
#         print('right')
#         play_again = input('u want play again : (Y or N):')
#         play_again = play_again.lower()

#         if play_again == 'y':
#             random_no = random.randint(1, 10)

#             user_input = int(input('Enter valid number 1 -10 : '))

#         else:
#             sys.exit()


# print(random_no)



# lists 

my_list = ['red', 'blue','grey', 120 , 1 , 9 ]

get_color = my_list[len(my_list)-1]  
#cause len count 0 + till end 
print (get_color)



