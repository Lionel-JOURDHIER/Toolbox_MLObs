import pytest

from app.modules.mon_module import add, square, sub


@pytest.mark.parametrize("a, b, expected", [(3, 5, 8), (-1, 1, 0), (100, 200, 300)])
def test_add_parametrized(a, b, expected):
    """Test the add function with multiple sets of inputs and expected outputs.

    Args :
        a (int) : first integer
        b (int) : second integer
        expected (int) : expected result of the addition
    Assert :
        The result of add(a, b) should be equal to expected
    """
    assert add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(10, 4, 6), (0, 5, -5), (10, 10, 0)])
def test_sub_parametrized(a, b, expected):
    """Test the sub function with multiple sets of inputs and expected outputs.

    Args :
        a (int) : first integer
        b (int) : second integer
        expected (int) : expected result of the substraction

    Assert :
        The result of sub(a, b) should be equal to expected
    """
    assert sub(a, b) == expected


@pytest.mark.parametrize(
    "input_val, expected", [(9, 3.0), (16, 4.0), (0, 0.0), (25, 5.0)]
)
def test_square_parametrized(input_val, expected):
    """Test the square function with multiple sets of inputs and expected outputs.

    Args :
        input_val (int) : number to be squared
        expected (float) : expected result of the square function

    Assert :
        The result of square(input_val) should be equal to expected
    """
    assert square(input_val) == expected


def test_square_negative_value():
    """Test the square function with a negative input to ensure it raises a ValueError.

    Args :
        None

    Assert :
        The square function should raise a ValueError when given a negative input
    """
    # Vérifie que l'exception est bien levée pour les nombres négatifs
    # Attention : assure-toi d'utiliser 'raise ValueError' dans ton module
    with pytest.raises(ValueError):
        square(-1)
