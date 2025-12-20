import pytest

from src.calculator.logic import evaluate

def test_addition():
    assert evaluate("1+1") == 2

def test_subtraction():
    assert evaluate("5-3") == 2

def test_multiplication():
    assert evaluate("2*3") == 6

def test_division():
    assert evaluate("6/3") == 2

def test_order_of_operations_parentheses():
    assert evaluate("(2+3)*4") == 20
    assert evaluate("10/(1+1)") == 5

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        evaluate("10/0")

# New tests for invalid expressions
from src.calculator.logic import InvalidExpressionError

def test_invalid_operator():
    with pytest.raises(InvalidExpressionError):
        evaluate("2^3")

def test_invalid_expression_empty():
    with pytest.raises(InvalidExpressionError):
        evaluate("")

def test_invalid_expression_malformed():
    with pytest.raises(InvalidExpressionError):
        evaluate("2+*3")

def test_mismatched_parentheses():
    with pytest.raises(InvalidExpressionError):
        evaluate("(2+3")




