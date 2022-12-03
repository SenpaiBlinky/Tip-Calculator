print("Welcome to the tip calculator gang!")

bill = input("What's the bill number yo-er? ")
int_bill = float(bill)

split = input("How many peeps we splitting bud? ")
int_split = int(split)

percent_tip = input("What's the percent homie? ")
int_percent_tip = int(percent_tip) / 100 + 1

math = (int_bill / int_split) * int_percent_tip
result = "Each person should pay " + str(round(math, 2))

print(result)