# Напишите программу, которая находит все числа, делящиеся на 7, но при этом не делящиеся на 5 в диапазоне между 2000 и 3200 
#(оба конца интервала включены в перебор). Верните ответ в виде строки, где все такие числа соединены запятой.

def solve():
        solution = ""
        for i in range(2000,3201):
                if i%7==0 and i%5!=0:
                        solution=solution + "%s," % (i)
        return solution
print(solve()[:-1])
