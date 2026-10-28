import pytest
from app import Figure

def test_figure_angles_square():
    fig = Figure("квадрат", 5)
    assert fig.get_angles == 4

def test_figure_angles_triangle():
    fig = Figure("трикутник", 5)
    assert fig.get_angles == 3

def test_figure_invalid_length():
    with pytest.raises(ValueError):
        Figure("квадрат", -1)