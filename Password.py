#Secured password creator by Nowack
import random

numbers = "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
letters = "a", "z", "e", "r", "t", "y", "u", "i", "o", "p", "q", "s", "d", "f", "g", "h", "j", "k", "l", "m", "w", "x", "c", "v", "b", "n"
capital_letters = "A", "Z", "E", "R", "T", "U", "I", "O", "P", "Q", "S", "D", "F", "G", "H", "J", "K", "L", "M", "W", "X", "C", "V", "B", "N"
symbols = "&", "é", "(", "-", "_", "ç", ")" "=", "+", "$", "*", "^", "ù", ":", "!", ";", ",", "?"

if 1:
    lenght = int(input("How much caracters do you want in your password?: "))
    passwd = ""
    for x in range(0,lenght):
        variable = random.choice(numbers + letters + capital_letters + symbols)
        password = passwd + variable
        print(password, end='')