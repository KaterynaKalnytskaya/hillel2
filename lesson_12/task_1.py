class City:
    def __init__(self, name_city="", region="", name_country="", population=0, city_index="", city_tel_code=""):
        self.__name_city = name_city
        self.__region = region
        self.__name_country = name_country
        self.__population = population
        self.__city_index = city_index
        self.__city_tel_code = city_tel_code

    def city_information(self):
        print(f"The city of {self.__name_city} is located in {self.__name_country}, in the {self.__region} region. "
              f"The city's population is {self.__population}. The city's postal code is {self.__city_index}. "
              f"The city's telephone code is {self.__city_tel_code}\n")

    @property
    def name_city(self):
        return self.__name_city

    @name_city.setter
    def name_city(self, city_name):
        if 2 <= len(city_name) <= 15:
            self.__name_city = city_name
        else:
            print(Exception("Incorrect name of the city"))

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, name_region):
        if 2 <= len(name_region) <= 15:
            self.__region = name_region
        else:
            print(Exception("Incorrect name of the region"))

    @property
    def name_country(self):
        return self.__name_country

    @name_country.setter
    def name_country(self, country_name):
        if 2 <= len(country_name) <= 15:
            self.__name_country = country_name
        else:
            print(Exception("Incorrect name of the country"))

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, city_population):
        if 100 < city_population < 4000000:
            self.__population = city_population
        else:
            print(Exception("Incorrect number of population"))

    @property
    def city_index(self):
        return self.__city_index

    @city_index.setter
    def city_index(self, index_city):
        if 2 <= len(index_city) <= 6:
            self.__city_index = index_city
        else:
            print(Exception("Incorrect index number"))

    @property
    def city_tel_code(self):
        return self.__city_tel_code

    @city_tel_code.setter
    def city_tel_code(self, telephone_code):
        if 1 <= len(telephone_code) <= 7:
            self.__city_tel_code = telephone_code
        else:
            print(Exception("Incorrect telephone code."))


city1 = City()
city1.name_city = "Kiev"
city1.region = "Kiev"
city1.name_country = "Ukraine"
city1.population = 2800000
city1.city_index = "01000"
city1.city_tel_code = "044"

city2 = City()
city2.name_city = "Kharkov"
city2.region = "Kharkov"
city2.name_country = "Ukraine"
city2.population = 1400000
city2.city_index = "61000"
city2.city_tel_code = "057"

city3 = City()
city3.name_city = "Odessa"
city3.region = "Odessa"
city3.name_country = "Ukraine"
city3.population = 1010537
city3.city_index = "65000"
city3.city_tel_code = "48"

print("City:", city1.name_city)

city_1 = City("Kharkov", "Kharkov", "Ukraine", 1400000, "61000", "057")
city_1.city_information()

city_2 = City("Odessa", "Odessa", "Ukraine", 1010537, "65000", "48")
city_2.city_information()

city_3 = City("Kiev", "Kiev", "Ukraine", 2000000, "1234", "1234")
city_3.city_information()
