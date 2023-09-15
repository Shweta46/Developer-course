# from math import *
# print(sqrt(334))
# print('hi')
# name = input('Input your name: ')
# age = int(input('Input your age: '))
# print('You name is ' + name + ' and this is good')   

# sentence = input('Enter your sentence: ')
# print("Your sentence is: ", sentence)
# word1 = input('Enter the word to replace: ')
# word2 = input('Enter the word to replace with: ')
# print(sentence.replace(word1, word2))

# try:
#     x = int(input('Input an integer: '))
#     print(x)
# except ValueError:
#     print('Value not an integer.')
# else:
#     print('Nothing went wrong.')


try:
    x = int(input('Input an integer: '))
    print(x)
except:
    print('Something went wrong.')
finally:
    print('try except failed.')

