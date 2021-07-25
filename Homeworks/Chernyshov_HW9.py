"""Чернышов Алексей HW9"""

from datetime import datetime
import webbrowser
from math import floor

"""Задание №1
Создайте класс "животное". Наполните его данными и методами на свое усмотрение.
Пропишите в методах класса докстринги с описанием метода"""


class Animals:
    animal_type = None
    animal_habitat = None
    animal_date_of_birth = None

    def __init__(self, a_type: str, a_habitat: str, a_date: tuple):
        """This constructor created to collect correct data from each attribute, whatever the user enters"""
        all_types = 'mammal', 'amphibian', 'reptile', 'bird', 'fish'
        all_habitats = 'ocean', 'forest', 'mountain', 'desert', 'jungle'
        try:
            a_type = str(a_type)
            a_habitat = str(a_habitat)
            a_date = datetime(*a_date).date()
        except:
            return

        if a_type.lower() in all_types:
            self.animal_type = a_type.lower()
        if a_habitat.lower() in all_habitats:
            self.animal_habitat = a_habitat.lower()
        self.animal_date_of_birth = a_date

    def tell_me_about_type(self):
        """This function will give you all information about your animal's type"""
        if self.animal_type == 'mammal':
            print(
                'Mammals are a group of vertebrate animals constituting the class Mammalia (/məˈmeɪliə/), and '
                'characterized by the presence \nof mammary glands which in females produce milk for feeding (nursing) '
                'their young, a neocortex (a region of the brain), \nfur or hair, and three middle ear bones.')
        elif self.animal_type == 'amphibian':
            print(
                'Amphibians are ectothermic, tetrapod vertebrates of the class Amphibia. All living amphibians belong '
                'to the group Lissamphibia. \nThey inhabit a wide variety of habitats, with most species living within '
                'terrestrial, fossorial, \narboreal or freshwater aquatic ecosystems.')
        elif self.animal_type == 'reptile':
            print(
                'Reptiles, as most commonly defined, are the animals in the class Reptilia /rɛpˈtɪliə/, a paraphyletic'
                ' grouping comprising all \namniotes except synapsids (mammals and their extinct relatives) and '
                'Aves (birds). The class comprises turtles, \ncrocodilians, snakes, amphisbaenians, lizards, '
                'tuatara, and their extinct relatives.')
        elif self.animal_type == 'bird':
            print(
                'Birds are a group of warm-blooded vertebrates constituting the class Aves /ˈeɪviːz/, characterised '
                'by feathers, toothless beaked jaws, \nthe laying of hard-shelled eggs, a high metabolic rate, a '
                'four-chambered heart, and a strong yet lightweight skeleton.')
        elif self.animal_type == 'fish':
            print(
                'Fish are aquatic, craniate, gill-bearing animals that lack limbs with digits. They form a sister '
                'group to the tunicates, together forming the olfactores. \nIncluded in this definition are the living '
                'hagfish, lampreys, and cartilaginous and bony fish as well as various extinct related groups. ')
        else:
            print('Sorry, but we have no information about this type. Maybe animal\'s data is incorrect.')

    def tell_me_about_habitat(self):
        """This function will give you all information about your animal's habitat, and if you wish, it will show you
        the picture of one"""
        pictures = input('Do you want to see a pictures? *Browser will be opened* (y/else=no): ')
        if pictures == 'y':
            pictures = True
        else:
            pictures = False
        if self.animal_habitat == 'ocean':
            print(
                'The ocean (also the sea or the world ocean) is the body of salt water which covers approximately 71% '
                'of the surface of the Earth and contains 97% of Earth\'s water.')
            if pictures:
                webbrowser.open('https://wallpapercave.com/wp/wp4273133.jpg')
        elif self.animal_habitat == 'forest':
            print(
                'A forest is an area of land dominated by trees. Hundreds of definitions of forest are used '
                'throughout the world, \nincorporating factors such as tree density, tree height, land use, '
                'legal standing and ecological function.')
            if pictures:
                webbrowser.open('https://images2.alphacoders.com/103/thumb-1920-1036023.jpg')
        elif self.animal_habitat == 'mountain':
            print(
                'A mountain is an elevated portion of the Earth\'s crust, generally with steep sides that show '
                'significant exposed bedrock.')
            if pictures:
                webbrowser.open('https://wallpapershome.ru/images/wallpapers/gori-1920x1080-nebo-4k-5k-zakat-android'
                                '-oboi-11473.jpg')
        elif self.animal_habitat == 'desert':
            print(
                'A desert is a barren area of landscape where little precipitation occurs and, \nconsequently, '
                'living conditions are hostile for plant and animal life.')
            if pictures:
                webbrowser.open('https://wallpapercave.com/wp/wp3329848.jpg')
        elif self.animal_habitat == 'jungle':
            print('A jungle is land covered with dense forest and tangled vegetation, usually in tropical climates.')
            if pictures:
                webbrowser.open('https://images3.alphacoders.com/691/thumb-1920-691924.jpg')
        else:
            print('Sorry, but we have no information about this area. Maybe animal\'s data is incorrect.')

    def tell_me_about_age(self):
        """This function return actual age of animal"""
        try:
            age_of_animal_years = floor((datetime.now().date() - self.animal_date_of_birth).days / 365)
        except:
            return print('Something went wrong. Maybe animal\'s data is incorrect.')
        if not age_of_animal_years:
            age_of_animal_days = (datetime.now().date() - self.animal_date_of_birth).days
            print(f'Your animal\'s age is ~{age_of_animal_days} days.')
        else:
            print(f'Your animal\'s age is ~{age_of_animal_years} years.')


white_shark = Animals('Fish', 'Ocean', (2010, 10, 10))
king_cobra = Animals('Reptile', 'Jungle', (2018, 2, 20))
african_elephant = Animals('Mammal', 'Desert', (2008, 12, 15))
peregrine_falcon = Animals('Bird', 'Mountain', (2016, 8, 9))
wood_frog = Animals('Amphibian', 'Forest', (2020, 10, 27))
natures_mistake = Animals(123, False, ['1', {None: None}, 99.99])

"""Задание №2
Почитайте про Диаграммы класса. Опишите с помощью классов кухонную технику в виде диаграммы. Продумайте классы, 
их назначение и взаимосвязи. Реализовать с описанием свойств и методов."""
# Plan is here>>>   https://ibb.co/pdKPhWh
"""Задание №3
Описать все то же с помощью питона.

Моделируем ситуацию, когда покупатель пришел в магазин, и хочет выбрать подходящую технику."""


class Appliances:
    """Technology parameters, base class"""
    name = None
    price = None
    weight = None

    def __init__(self, name: str, price: int, weight: int):
        try:
            name = str(name)
            price = int(price)
            weight = int(weight)
        except:
            return

        self.name = name
        self.price = price
        self.weight = weight

    def turn(self, on_or_off):
        """This function turning on and off the device"""
        if not self.name:
            return print('Something went wrong. Data may be incorrect')
        if on_or_off.lower() == 'on':
            print(f'{self.name} is turned on!')
        elif on_or_off.lower() == 'off':
            print(f'{self.name} is turned off!')
        else:
            print('Incorrect data')

    def can_i_lift_it(self, your_maximum: int):
        """If user want to transport an item, this function will say, if it possible or not"""
        if not self.weight:
            return print('Something went wrong. Data may be incorrect')
        if your_maximum > self.weight:
            print('You can do it!')
        elif your_maximum == self.weight:
            print('You can do it, but be careful. Can I ask someone to help you?')
        else:
            print(f'The {self.name} is too heavy! The weight of one is {self.weight}kg !!')

    def i_have_no_dollars(self):
        """If user has no $ this function will convert the price in any currency"""
        if not self.price:
            return print('Something went wrong. Data may be incorrect')
        users_currency = input('Enter your currency (eur/uah/rub): ').upper()
        if users_currency == 'EUR':
            return print(f'Price of {self.name} is', str(round(self.price / 1.18, 2)) + ' EUR')
        elif users_currency == 'UAH':
            return print(f'Price of {self.name} is', str(round(self.price / 0.037, 2)) + ' UAH')
        elif users_currency == 'RUB':
            return print(f'Price of {self.name} is', str(round(self.price / 0.014, 2)) + ' RUB')
        else:
            print('Sorry, but we don\'t accept this currency.')

    def define_it(self):
        """This function will describe the whole class"""
        print('Kitchen appliances exist to make life easier and automate processes in your house.')


"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
dict_of_masses = {'apple': 126,
                  'watermelon': 6000,
                  'melon': 3500,
                  'lemon': 150,
                  'grapefruit': 450,
                  'water': 1000,
                  'chocolate': 50,
                  'grape': 320}


class Heating_device(Appliances):
    """Heating devices have new parameter as power, that will be used in calculating speed of work of device"""
    power = None

    def __init__(self, name: str, price: int, weight: int, power: int):
        try:
            power = int(power)
        except:
            return
        self.power = power
        super().__init__(name, price, weight)

    def how_fast_it_will_be(self):
        """Calculating the speed of working on some types of kitchen stuff."""
        if not self.power:
            return print('Something went wrong. Data may be incorrect')
        heating_item = input(f'Which item you want to heat in: {self.name}? (power = {self.power}W)'
                             f'\n(apple/watermelon/melon/lemon/grapefruit/water/chocolate/grape)\n: ')
        if heating_item.lower() in dict_of_masses:
            res_in_minutes = int(dict_of_masses.get(heating_item.lower()) / (self.power / 10))
            if not res_in_minutes:
                return print(f'It need less then a minute to heat: {heating_item.capitalize()}')
            return print(f'It need {res_in_minutes} minutes to heat: {heating_item.capitalize()}')
        else:
            return print('We haven\'t this item in our base.')

    def i_have_no_dollars(self):
        print('Sorry but you can pay for it only in dollars.')

    def define_it(self):
        print('The heating technique exists to cook delicious hot food, and it also kills a parasites.')


class Cooling_device(Appliances):
    power = None

    def __init__(self, name: str, price: int, weight: int, power: int):
        try:
            power = int(power)
        except:
            return
        self.power = power
        super().__init__(name, price, weight)

    def how_fast_it_will_be(self):
        if not self.power:
            return print('Something went wrong. Data may be incorrect')
        freezing_item = input(f'Which item you want to freeze in: {self.name}? (power = {self.power}W)'
                              f'\n(apple/watermelon/melon/lemon/grapefruit/water/chocolate/grape)\n: ')
        if freezing_item.lower() in dict_of_masses:
            res_in_minutes = int(dict_of_masses.get(freezing_item.lower()) / (self.power / 10))
            if not res_in_minutes:
                return print(f'It need less then a minute to freeze: {freezing_item.capitalize()}')
            return print(f'It need {res_in_minutes} minutes to freeze: {freezing_item.capitalize()}')
        else:
            return print('We haven\'t this item in our base.')

    def define_it(self):
        print('Cooling technique is used to store cooled food and keep it fresh for some time.')


class Washing_device(Appliances):
    def __init__(self, name: str, price: int, weight: int):
        super().__init__(name, price, weight)

    def define_it(self):
        print('Washing devices helps us to keep our dishes clean and eliminates the need for washing dishes.')


"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""


class Microwave(Heating_device):
    size = None

    def __init__(self, name: str, price: int, weight: int, power: int, size: int):
        try:
            size = int(size)
        except:
            return
        self.size = size
        super().__init__(name, price, weight, power)

    def show_me_size(self):
        """"This function will return the capacity of device"""
        if not self.size:
            return print('Something went wrong. Data may be incorrect')
        return print(f'Size of {self.name} is {self.size}l.')

    def define_it(self):
        print('Microwaves are used to quickly heat any food or liquid.')


class Cooker(Heating_device):
    def __init__(self, name: str, price: int, weight: int, power: int):
        super().__init__(name, price, weight, power)

    def define_it(self):
        print('The cooker is used for cooking different types of dishes.')


dishwasher_bosch = Washing_device('Dishwasher \'Bosch\'', 100, 30)
refrigerator_gorenje = Cooling_device('Refrigerator \'Gorenje\'', 150, 50, 100)
refrigerator_toshiba = Cooling_device('Refrigerator \'Toshiba\'', 200, 60, 200)
microwave_samsung = Microwave('Microwave \'Samsung\'', 50, 5, 800, 5)
microwave_lg = Microwave('Microwave \'LG\'', 65, 7, 1000, 10)
cooker_tefal = Cooker('Cooker \'Tefal\'', 110, 15, 20)
interceptor_3000 = Heating_device([1.2, 1.3, '111'], False, "Zz123Zz", {None: 'dict'})
