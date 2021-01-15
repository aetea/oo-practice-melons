############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""
    ## creating attributes for this class
    # code = None
    # first_harvest = 0

    def __init__(self, name, code, first_harvest, color, is_seedless, is_bestseller):
        """Initialize a melon."""

        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller

        self.pairings = []


    # def __repr__(self):
    #     print(f'this melon is called {self.name} with the code {self.code}.')
    #     print(f'first harvest is {self.first_harvest} and bestseller is {self.is_bestseller}')
    #     print(f'it is {self.color}, seedless {self.is_seedless} and pairs well with:')
    #     print(f'{self.pairings}')
    #     return "---"

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType("Muskmelon", "musk", 1998, "green", True, True)
    muskmelon.add_pairing("mint")

    casaba = MelonType("Casaba", "cas", 2003, "orange", False, False)
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")

    crenshaw = MelonType("Crenshaw", "cren", 1996, "green", False, False)
    crenshaw.add_pairing("proscuitto")

    yellow = MelonType("Yellow Watermelon", "yw", 2013, "yellow", False, True)
    yellow.add_pairing("ice cream")

    all_melon_types.extend([muskmelon, casaba, crenshaw, yellow])

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon_type in melon_types:
        print(f"{melon_type.name} pairs with")
        for pairing in melon_type.pairings:
            print(f"- {pairing}")
        print()

    return None


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_codes = {melon_type.code: melon_type for melon_type in melon_types}
    return melon_codes

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



