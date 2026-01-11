#a function "is_even" is defined
def is_even(n):
    if n % 2 == 0:
        return "Even"
    else:
         return "Odd"
even_results = is_even(6)

def check_score(score):
    if score >= 50:
        return "Pass"
    else:
        return "Fail"
score = check_score(60)

def calculate(a , b , op):
    if op == "-":
        return a - b
    elif op == "+":
        return a + b
results = calculate(4 , 6 , "-")

print("Number is" , even_results)
print(score)
print(results)