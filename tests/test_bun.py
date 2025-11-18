from test_data import Data

class TestBun:

    def test_bun_initialization(self, bun):
        assert bun.name == Data.BUNS[0]["name"]
        assert bun.price == Data.BUNS[0]["price"]

    def test_bun_get_name(self, bun):
        assert bun.get_name() == Data.BUNS[0]["name"]

    def test_bun_get_price(self, bun):
        assert bun.get_price() == Data.BUNS[0]["price"]
