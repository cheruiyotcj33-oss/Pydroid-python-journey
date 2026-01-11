#user inputs income generated
income = [250 , 500 , 1000 , 2000 , 4000]

#total income calculation
def total_income(data):
    total = 0
    for amount in data:
        total += amount
    return total
total = total_income([250 , 500 , 1000 , 2000 , 4000])
    
#average income generation
def average_income(data):
    total = total_income(data)
    count = 0
    for _ in data:
        count += 1
    return total / count
average = average_income ([250 , 500 , 1000 , 2000 , 4000])
    
#high_income days generation
def high_income_days(data , threshold):
    high_days = []
    for amount in data:
        if amount >= threshold:
            high_days.append(amount)
    return high_days
high_days = high_income_days([250 , 500 , 1000 , 2000 , 4000] , 1000)
#output generation
print("Total_income = " , total)
print("Average_income = " , average)
print("High_income_days = " , high_days)