class City:
    def __init__(self, name_city, region, name_country, population, city_index, city_tel_code):
        self.__city_tel_code = city_tel_code
        self.__region = region
        self.__city_index = city_index
        self.__name_country = name_country
        self.__name_city = name_city
        self.__population = population

    def city_information(self):
        print(f"The city of {self.__name_city} is located in {self.__name_country}, in the {self.__region} region. "
              f"The city's population is {self.__population}. The city's postal code is {self.__city_index}. "
              f"The city's telephone code is {self.__city_tel_code}\n")

    @property
    def name(self):
        return self.__name_city

    @name.setter
    def name(self, city_name):
        if 2 <= len(city_name) <= 15:
            self.__name_city = city_name
        else:
            raise ValueError("Incorrect name of the city")

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, name_region):
        if 2 <= len(name_region) <= 15:
            self.__region = name_region
        else:
            raise ValueError("Incorrect name of the region")

    @property
    def country(self):
        return self.__name_country

    @country.setter
    def country(self, country_name):
        if 2 <= len(country_name) <= 15:
            self.__name_country = country_name
        else:
            raise ValueError("Incorrect name of the country")

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, city_population):
        if 100 < city_population < 2000000:
            self.__population = city_population
        else:
            raise ValueError("Incorrect number of population")

    @property
    def index(self):
        return self.__city_index

    @index.setter
    def index(self, index_city):
        if 4 <= len(index_city) <= 6:
            self.__city_index = index_city
        else:
            raise ValueError("Incorrect index number")

    @property
    def tel_code(self):
        return self.__city_tel_code

    @tel_code.setter
    def tel_code(self, telephone_code):
        if 2 <= telephone_code <= 6:
            self.__city_tel_code = telephone_code
        else:
            raise ValueError("Incorrect telephone code.")


city_1 = City("Kharkov", "Kharkov", "Ukraine", 1400000, "61000", "057")
city_1.city_information()

city_2 = City("Odessa", "Odessa", "Ukraine", 1010537, "65000", "48")
city_2.city_information()

city_3 = City("Kiev","Kiev", "Ukraine", "2000000", "1234", "1234")
city_3.city_information()

