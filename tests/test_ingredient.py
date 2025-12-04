import pytest
from praktikum.ingredient import Ingredient
from data import Data


@pytest.mark.parametrize("item", Data.INGREDIENTS)
def test_ingredient_initialization(item):
    ingredient = Ingredient(item["type"], item["name"], item["price"])
    
    assert ingredient.type == item["type"]
    assert ingredient.name == item["name"]
    assert ingredient.price == item["price"]
    
    assert ingredient.get_type() == item["type"]
    assert ingredient.get_name() == item["name"]
    assert ingredient.get_price() == item["price"]
