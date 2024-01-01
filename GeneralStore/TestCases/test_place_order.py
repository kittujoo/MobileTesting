from POM_Page.place_order import AddToCart


class TestPlaceOrder:
    ORDER_ITEM = 'Converse All Star'

    def test_fill_address(self, setup):
        global all_in_one

        all_in_one = AddToCart(setup)
        all_in_one.add_address()

    def test_add_to_cart(self):
        all_in_one.add_to_cart(ORDER_ITEM='Converse All Star')

    def test_assert_price(self):
        all_in_one.assert_price()

    def test_checkout(self):
        all_in_one.checkout()
