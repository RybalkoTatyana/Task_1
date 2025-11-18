import pytest
from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum import ingredient_types
from data import Data
from praktikum.database import Database

@pytest.fixture
def bun():
    base = Data.BUNS[0]
    return Bun(base["name"], base["price"])

@pytest.fixture
def burger(bun):
    burger = Burger()
    burger.set_buns(bun)
    return burger

@pytest.fixture #создание ингредиентов
def make_ing():
    def _make_ing(
        name="ingredient",
        price=100,
        type_=ingredient_types.INGREDIENT_TYPE_FILLING
    ):
        ing = Mock()
        ing.get_name.return_value = name
        ing.get_price.return_value = price
        ing.get_type.return_value = type_
        return ing
    return _make_ing

@pytest.fixture
def database():
    return Database()
