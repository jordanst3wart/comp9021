# Uses Heath Nutrition and Population statistics, avalaible at
# http://datacatalog.worldbank.org, stored in the file HNP_Data.csv,
# assumed to be stored in the working directory.
# Prompts the user for an Indicator Name. If it exists and is associated with
# a numerical value for some countries or categories, for some the years 1960-2015,
# then finds out the maximum value, and outputs:
# - that value;
# - the years when that value was reached, from oldest to more recents years;
# - for each such year, the countries or categories for which that value was reached,
#   listed in lexicographic order.
# 
# Written by Jordan Stewart and Eric Martin for COMP9021


import sys
import os
import csv


# TODO not print .0
# TODO does not always print the right answer
# TODO broken  check why this isn't working Newborns protected against tetanus (%)
# TODO fixed   Number of neonatal deaths    with a .0 fix
# TODO fixed   Age population, age 12, female, interpolated     .0 fix
def return_values(filename,indicator_of_interest, first_year, number_of_years, countries_for_max_value_per_year):
    max_value = -1
    temp_value = 0
    with open(filename, 'rt') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',') # could use csv.reader()
        for row in reader:
            #print(row)
            if indicator_of_interest == row["Indicator Name"]:
                temp_value = get_max_in_row(row, max_value, first_year, number_of_years)
                #print("temp_value: ", temp_value)
                # if max_value greater than current max populate countries
                if float(temp_value) > float(max_value):
                    #print("Overriding ", float(max_value), " with ", float(temp_value))
                    max_value = float(temp_value)
                    #print("in if, max value is: ", temp_value)
                    countries_for_max_value_per_year = {}   # reset value
                    countries_for_max_value_per_year = populate_country_list(countries_for_max_value_per_year, max_value, row,first_year, number_of_years)
                elif temp_value == max_value:
                    countries_for_max_value_per_year = populate_country_list(countries_for_max_value_per_year, max_value,row,first_year, number_of_years)
                    #print('in elif, temp value: ', temp_value)
    # print(max_value)
    return [max_value, countries_for_max_value_per_year]


def get_max_in_row(row, max_value, first_year, number_of_years):
    last_year = first_year + number_of_years
    year = first_year
    while year <= last_year:
        if str(year) in row and len(row[str(year)]) > 3:
            #print("here 11111111")
            # errors with value on the year being empty
            if float(row[str(year)]) >= max_value:
                max_value = float(row[str(year)])
                #print("here 222222222")
        year += 1
    return max_value


def populate_country_list(countries_for_max_value_per_year, max_value,row, first_year, number_of_years):
    last_year = first_year + number_of_years
    year = first_year
    country = row["Country Name"]
    # append and stuff
    while year <= last_year:
        if str(year) in row and len(row[str(year)]) > 3:
            if float(row[str(year)]) == max_value:
                if str(year) in countries_for_max_value_per_year:
                    #if isinstance(countries_for_max_value_per_year[str(year)], list):
                    countries_for_max_value_per_year[str(year)].append(country)
                else:
                    countries_for_max_value_per_year[str(year)] = [country]
        year += 1
    return countries_for_max_value_per_year


filename = 'HNP_Data.csv'
if not os.path.exists(filename):
    print('There is no file named {} in the working directory, giving up...'.format(filename))
    sys.exit()

indicator_of_interest = input('Enter an Indicator Name: ')

first_year = 1960
number_of_years = 56
max_value = None
countries_for_max_value_per_year = {}

[max_value, countries_for_max_value_per_year] = return_values(filename, indicator_of_interest, first_year, number_of_years, countries_for_max_value_per_year)
# countries or categories for that year
            
if max_value == -1:
    print('Sorry, either the indicator of interest does not exist or it has no data.')
else:
    print('The maximum value is:', ('%f' % max_value).rstrip('0').rstrip('.'))
    #print('The maximum value is: {0:g}'.format(max_value))
    print('It was reached in these years, for these countries or categories:')
    for year in sorted(countries_for_max_value_per_year):
        print('    {}: {}'.format(year, countries_for_max_value_per_year[year]))
