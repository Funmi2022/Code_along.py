import math
import sys


def example1():
    some_tuple = (1, 2, 3, 'a')
    some_variable = {
        'long': 'Long code lines should be wrapped within 79 characters.',
        'other': [
            math.pi,
            100,
            200,
            300,
            9876543210,
            'This is a long string that goes on'],
        'more': {
            'inner': 'This whole logical line should be wrapped .',
            some_tuple: [
                1,
                20,
                300,
                40000,
                500000000,
                60000000000000]}}

    is_cat_owner = True
    if is_cat_owner:
        print("OKAY")

    return (some_tuple, some_variable)


def example2(): return {'has_key() is depreciated': True}.has_key(
    {'f': 2}.has_key(''))


class Example3(object):
    def __init__(self, bar):
        if bar:
            bar += 1
            bar = bar * bar
            return bar
            else:
                somet_string = """
                                                                                Indentation in multiline strings should not be touched.
                                                                                only actual code should be reindented.
                                                                                """
                return (sys.path, somet_string)
