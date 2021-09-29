# Programmers: Connor O'Brien and Reid Osborne
# Course: CS151, Prof. Mehri
# Date: September 28, 2021
# Lab Number: 2
# Program Inputs: Number of births, deaths, migrations, and years into the future
# Program Outputs: Population size


# Output purpose
print("This program will estimate the size of the current population and "
      "the future population size for a country. ")

# Ask user for number of births
births = input("Please enter the number of births per second: ")
births = float(births)

# Ask user for number of deaths
deaths = input("Please enter the number of deaths per second: ")
deaths = float(deaths)

# Ask user for number of migrations
migrations = input("Please enter the number of migrations per second: ")
migrations = float(migrations)

# Ask user for number of years into the future
years_into_the_future = input("Please enter the number of years into the future: ")
years_into_the_future = int(years_into_the_future)

# Ask user for current population size
current_population_size = input("Please enter the current population size of your country: ")
current_population_size = float(current_population_size)


seconds_per_year = 31536000

births_per_year = births*seconds_per_year
deaths_per_year = deaths*seconds_per_year
migrations_per_year = migrations*seconds_per_year

# Compute population size in desired number of years
almost_future_population = migrations_per_year+births_per_year
almost_future_population1 = almost_future_population-deaths_per_year
population = almost_future_population1*years_into_the_future
future_population_size = population+current_population_size

print("The future population size", future_population_size, )