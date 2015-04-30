"""
File: Rosko_Melvin_Gasoline.py
Author: Wade Rosko and Andrew Melvin
Description:
    Prints the pounds of carbon dioxide produced by a given number of gallons of gasoline.
"""

#ask user to input number of gallons of gasoline
gas_gallons = float(raw_input('Please enter the number of gallons of gasoline: '))

#ask user for national average
national_average = float(raw_input('Please enter the national average for the price of '
                                   '1 gallon of gasoline. (On 4/30/15 it was $2.58)  '))

#1 gallon of gasoline produces apporoximately 19.64 pounds of carbon dioxide
carbon_dioxide_pounds = gas_gallons * 19.64

print

#output the pounds of carbon dioxide produced
print gas_gallons,'gallons of gasoline produces approximately',\
      carbon_dioxide_pounds, 'pounds of carbon dioxide.'

#1 barrel of crude oil produces approximately 19 gallons of gasoline
crude_oil_barrels = gas_gallons / 19

print

#output the number of barrels of crude oil required
print crude_oil_barrels, 'barrels of crude oil produces approximately',\
       gas_gallons,'gallons of gasoline.'

print

#average cost of X gallons of gasoline in the US today
avg_cost_gas_gallons = gas_gallons * national_average


#output the average cost of X barrels of gasoline
print gas_gallons,'gallons will cost $',avg_cost_gas_gallons