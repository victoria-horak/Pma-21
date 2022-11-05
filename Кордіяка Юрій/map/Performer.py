from NotPresentException import *


class Performer:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def is_element_present_full_name(self, name):
        full_name = ''
        for key, value in self.dictionary.items():
            if name.lower() == key.lower():
                full_name = value
        if full_name != '':
            print(full_name)
        else:
            raise NotPresentException('element is not present')

    def is_element_present_abbreviation(self, name):
        abbreviation = ''
        for key, value in self.dictionary.items():
            if name.lower() == value.lower():
                abbreviation=key
        if abbreviation != '':
            print(abbreviation)
        else:
            raise NotPresentException('element is not present')
