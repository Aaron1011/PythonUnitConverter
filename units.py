# Do you want to use Python Unit Converter's functionality in
# your own application? This file makes it easy to include unit conversion
# in your own Python application. This file will explain the steps to
# implement the Python Unit Converter API.

# First, you will need to include the 'from units import *' statement in the
# beginning of your application. This allows you to access all of the unit-
# conversion function available in Python Unit Converter. Remember to put the
# modules directory in the same folder as this file.

import modules

class UnitConverter():
    # The 'convert' method takes three arguments: the name of the unit
    # to be converted, the quantity of that unit, and the unit to convert to.
    # Example: UnitConverter.convert('centimeters','kilometers',12)
    # The function returns the converted number of units.
    def convert(self, unit1, unit2, q):
        a = getattr(modules, unit1 + '_' + unit2)
        return a(q, api=True)
    # The 'exists' method takes two arguments: the name of the unit to be
    # converted, and the name of the unit to be converted to. If Python
    # Unit Converter has the hapability, it returns True. Otherwise, it returns
    # False.
    def exists(self, unit1, unit2):
        try:
            getattr(modules, unit1 + '_' + unit2)
        except AttributeError:
            return False
        else:
            return True
