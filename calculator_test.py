import pytest 
import calculator

def test_addition(): 
    assert calculator.addition(7,8) == 14

def test_subtraction(): 
    assert calculator.subtraction(8,8) == 0

def test_multiplication(): 
    assert calculator.multiplication(7,8) == 56

def test_division(): 
    assert calculator.addition(7,70) == 10