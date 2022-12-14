def findNotationByName(dictionary, name):
    return dictionary.get(name, "There is no such name!")

def findNameByNotation(dictionary, notation):
    allValues = dictionary.values()
    if notation not in allValues:
        return "There is no such notation!"
    return list(dictionary.keys())[list(allValues).index(notation)]

dictionary = {
    "Actinium" : "Ac",
    "Aluminum" : "Al",
    "Americium" : "Am",
    "Antimony" : "Sb",
    "Argon" : "Ar",
    "Arsenic" : "As",
    "Astatine" : "At",
    "Barium" : "Ba",
    "Berkelium" : "Bk",
    "Beryllium" : "Be",
    "Bismuth" : "Bi",
    "Bohrium" : "Bh",
    "Boron" : "B",
    "Bromine" : "Br",
    "Cadmium" : "Cd",
    "Calcium" : "Ca",
    "Californium" : "Cf",
    "Carbon" : "C",
    "Cerium" : "Ce",
    "Cesium" : "Cs",
    "Chlorine" : "Cl",
    "Chromium" : "Cr",
    "Cobalt" : "Co",
    "Copper" : "Cu",
    "Curium" : "Cm",
    "Darmstadtium" : "Ds",
    "Dubnium" : "Db",
    "Dysprosium" : "Dy",
    "Einsteinium" : "Es",
    "Erbium" : "Er",
    "Europium" : "Eu",
    "Fermium" : "Fm",
    "Fluorine" : "F",
    "Francium" : "Fr",
    "Gadolinium" : "Gd",
    "Gallium" : "Ga",
    "Germanium" : "Ge",
    "Gold" : "Au",
    "Hafnium" : "Hf",
    "Hassium" : "Hs",
    "Helium" : "He",
    "Holmium" : "Ho",
    "Hydrogen" : "H",
    "Indium" : "In",
    "Iodine" : "I",
    "Iridium" : "Ir",
    "Iron" : "Fe",
    "Krypton" : "Kr",
    "Lanthanum" : "La",
    "Lawrencium" : "Lr",
    "Lead" : "Pb",
    "Lithium" : "Li",
    "Lutetium" : "Lu",
    "Magnesium" : "Mg",
    "Manganese" : "Mn",
    "Meitnerium" : "Mt",
    "Mendelevium" : "Md",
    "Mercury" : "Hg",
    "Molybdenum" : "Mo",
    "Neodymium" : "Nd",
    "Neon" : "Ne",
    "Neptunium" : "Np",
    "Nickel" : "Ni",
    "Niobium" : "Nb",
    "Nitrogen" : "N",
    "Nobelium" : "No",
    "Oganesson" : "Uuo",
    "Osmium" : "Os",
    "Oxygen" : "O",
    "Palladium" : "Pd",
    "Phosphorus" : "P",
    "Platinum" : "Pt",
    "Plutonium" : "Pu",
    "Polonium" : "Po",
    "Potassium" : "K",
    "Praseodymium" : "Pr",
    "Promethium" : "Pm",
    "Protactinium" : "Pa",
    "Radium" : "Ra",
    "Radon"  : "Rn",
    "Rhenium" : "Re",
    "Rhodium" : "Rh",
    "Roentgenium" : "Rg",
    "Rubidium" : "Rb",
    "Ruthenium" : "Ru",
    "Rutherfordium" : "Rf",
    "Samarium" : "Sm",
    "Scandium" : "Sc",
    "Seaborgium" : "Sg",
    "Selenium" : "Se",
    "Silicon" : "Si",
    "Silver" : "Ag",
    "Sodium" : "Na",
    "Strontium" : "Sr",
    "Sulfur" : "S",
    "Tantalum" : "Ta",
    "Technetium" : "Tc",
    "Tellurium" : "Te",
    "Terbium" : "Tb",
    "Thallium" : "Tl",
    "Thorium" : "Th",
    "Thulium" : "Tm",
    "Tin" : "Sn",
    "Titanium" : "Ti",
    "Tungsten" : "W",
    "Ununbium" : "Uub",
    "Ununhexium" : "Uuh",
    "Ununpentium" : "Uup",
    "Ununquadium" : "Uuq",
    "Ununseptium" : "Uus",
    "Ununtrium" : "Uut",
    "Uranium" : "U",
    "Vanadium" : "V",
    "Xenon" : "Xe",
    "Ytterbium" : "Yb",
    "Yttrium" : "Y",
    "Zinc": "Zn",
    "Zirconium": "Zr"
}

isEntering = True
while isEntering:
    choice = input('Menu:\n[0] - find notation by name\n[1] - find name by notation\n[any other key] - EXIT\nEnter : ')
    if(choice == '0'):
        print('Notation searching : ' + findNotationByName(dictionary, input('Enter element name : ')))
    elif(choice == '1'):
        print('Name searching : ' + findNameByNotation(dictionary, input('Enter element notation : ')))
    else:
        isEntering = False
