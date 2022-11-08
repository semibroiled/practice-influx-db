import numpy as np
import pandas as pd
import pytest
import random

#Practicing building in test
#TODO: Practice raising and resolving errors as well as novel stratagems and documentation

def divisible_by_fifteen(number):
    if number == int(number):
        print('Number is integer')
    else:
        raise TypeError
    if ((number) % 15) == 0:
        return '15'
    elif ((number) % 5) == 0:
        return '5'
    elif ((number) % 3) == 0:
        return '3'

def test_fifteen():
    assert divisible_by_fifteen(35) == '5'
    assert divisible_by_fifteen(30) == '15'
    assert divisible_by_fifteen(33) != '5'


