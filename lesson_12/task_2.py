class Country:
    def __init__(self, name_country="", name_continent="", population=0, country_tel_code="", name_capital="",
                 name_cities=""):
        self.__name_cities = name_cities
        self.__name_capital = name_capital
        self.__country_tel_code = country_tel_code
        self.__population = population
        self.__name_continent = name_continent
        self.__name_country = name_country

    def country_information(self):
        print(f"The name of the country is {self.__name_country}. "
              f"It is located on the continent of {self.__name_continent}. "
              f"The population of {self.__name_country} is {self.__population} people. "
              f"The capital of {self.__name_country} is {self.__name_capital}."
              f" The name of the cities: {self.__name_cities}. "
              f"The telephone code of the country is: {self.__country_tel_code}.")

    @property
    def country(self):
        return self.__name_country

    @country.setter
    def country(self, country_name):
        if 2 <= len(country_name) <= 25:
            self.__name_country = country_name
        else:
            print(ValueError("Incorrect name of the country"))

    @property
    def continent(self):
        return self.__name_continent

    @continent.setter
    def continent(self, continent_name):
        if 4 <= len(continent_name) <= 20:
            self.__name_continent = continent_name
        else:
            print(ValueError("Incorrect name of the continent"))

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, population_count):
        if 200 <= population_count <= 4000000:
            self.__population = population_count
        else:
            print(ValueError("Incorrect number of the population"))

    @property
    def code(self):
        return self.__country_tel_code

    @code.setter
    def code(self, code_number):
        if 2 <= len(code_number) <= 15:
            self.__country_tel_code = code_number
        else:
            print(ValueError("Incorrect telephone code!"))

    @property
    def capital(self):
        return self.__name_capital

    @capital.setter
    def capital(self, capital_name):
        if 2 <= len(capital_name) <= 25:
            self.__name_capital = capital_name
        else:
            print(ValueError("Incorrect capital name!"))

    @property
    def cities(self):
        return self.__name_cities

    @cities.setter
    def cities(self, cities_name):
        if 2 <= len(cities_name) <= 30:
            self.__name_cities = cities_name
        else:
            print(ValueError("Incorrect cities name!"))


country_1 = Country()
country_1.country = "Ukraine"
country_1.capital = "Kiev"
country_1.population = 2800000
country_1.code = "044"
country_1.continent = "Eurasia"
country_1.cities = "Kharkov", "Odessa", "Dnepropetrovsk"

country_1.country_information()

