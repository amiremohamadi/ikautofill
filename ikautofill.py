from model.person import Person
from utills.core import Core
from sys import argv

try:
    _file = argv[1]
    _person = Person(_file)
    _core = Core()
    _core.fill(_person)

except IndexError:
    print('ERROR: no input files')
    print('usage: python ikaoutfill.py [file.json]')
