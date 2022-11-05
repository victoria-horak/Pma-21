from Performer import *
from NotPresentException import NotPresentException

dictionary = {
    'Гідроген': 'H',
    'Гелій': 'He',
    'азот': 'N',
    'актиній': 'Ac',
    'алюміній': 'Al'
}
try:
    e = Performer(dictionary)
    e.is_element_present_full_name('Гідроген')
    e.is_element_present_abbreviation('He')
except NotPresentException as exception:
    print(exception)
