import pytest
from praktikum.burger import Burger
from data import Data
from praktikum import ingredient_types

class TestBurger:

    def test_init(self):
        burger = Burger()
        assert burger.bun is None and burger.ingredients == []

    def test_set_buns(self, bun):
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun is bun

    def test_add_remove_move(self, burger, make_ing):
        first = make_ing()
        second = make_ing()
        
        burger.add_ingredient(first)
        burger.add_ingredient(second)
        burger.move_ingredient(0, 1)
        burger.remove_ingredient(0)
        
        assert burger.ingredients == [first]

    @pytest.mark.parametrize(
        "ingredient_prices, expected",
        [
            ([100, 200], Data.BUNS[0]["price"] * 2 + 300),
            ([], Data.BUNS[0]["price"] * 2),
        ]
    )
    def test_get_price(self, burger, make_ing, ingredient_prices, expected):
        for price in ingredient_prices:
            burger.add_ingredient(make_ing(price=price))
        assert burger.get_price() == expected

    @pytest.mark.parametrize(
        "names, types_, expected_lines",
        [
            (
                ["chili sauce", "dinosaur"],
                [ingredient_types.INGREDIENT_TYPE_SAUCE,
                 ingredient_types.INGREDIENT_TYPE_FILLING],
                ["= sauce chili sauce =", "= filling dinosaur ="]
            ),
            ([], [], []),
        ]
    )
    def test_get_receipt(self, burger, make_ing, names, types_, expected_lines):
        for name, type_ in zip(names, types_):
            burger.add_ingredient(make_ing(name=name, type_=type_))
        receipt = burger.get_receipt()
        assert all(line in receipt for line in expected_lines)

    def test_remove_invalid_index(self, burger):
        with pytest.raises(IndexError):
            burger.remove_ingredient(999)

    def test_move_invalid_index(self, burger, make_ing):
        burger.add_ingredient(make_ing())
        with pytest.raises(IndexError):
            burger.move_ingredient(999, 0)

    def test_get_price_no_bun(self):
        burger = Burger()
        with pytest.raises(AttributeError):
            burger.get_price()

    def test_get_receipt_no_bun(self):
        burger = Burger()
        with pytest.raises(AttributeError):
            burger.get_receipt()
