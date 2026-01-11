#income values 
income = [250 , 500 , 1000 , 2000 , 4000]

#income levels amount
def income_levels(amount):
    if amount < 500:
        return "Low"
    elif amount < 1500:
         return "medium"
    else:
          return "high"
          
#income levels classify
def classify_income(data):
    category = []
    for amount in data:
        category.append(income_levels(amount))
    return category
    
#income action levels
def income_action(level):
    if level == "low":
        return "Reduce expenses"
    elif level == "medium":
         return "save & invest"
    elif level == "high":
         return "Scale income"
         
#process
levels = classify_income(income)

actions = []
for level in levels:
    actions.append(income_action(level))

#results
print("income values = " , income)
print("Income level = " , levels)
print("Action: " , actions)