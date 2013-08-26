#Assign the price of a meal

meal = float(raw_input("How much does your meal cost by itself?"))
tax_rate = 5
tip = 18
tax = tax_rate / 100.0
tax_value = meal * tax 
meal_with_tax = meal + tax_value
tip_value = meal * tip / 100.0

total = meal_with_tax + tip_value

print "The cost of your meal is {:0.2f}." .format(meal)
print "The cost of the tax is %0.2f" % tax_value 
print "Here's the amount of tip you'll need to pay: {tip_value:0.2f}".format(tip_value=tip_value)
print "Total amount: %0.2f" % total 