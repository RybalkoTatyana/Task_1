from test_data import Data

class TestDatabase:

    def test_available_buns(self, database):
        buns = database.available_buns()
        assert len(buns) == len(Data.BUNS)
        for bun, expected in zip(buns, Data.BUNS):
            assert bun.get_name() == expected["name"]
            assert bun.get_price() == expected["price"]

    def test_available_ingredients(self, database):
        ingredients = database.available_ingredients()
        assert len(ingredients) == len(Data.INGREDIENTS)
        for ing, expected in zip(ingredients, Data.INGREDIENTS):
            assert ing.get_name() == expected["name"]
            assert ing.get_price() == expected["price"]
            assert ing.get_type() == expected["type"]
