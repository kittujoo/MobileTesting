from appium.webdriver.common.appiumby import AppiumBy
from Utility.BasePage import BasePage


class AddToCart(BasePage):
    drop_down_locator_country = (AppiumBy.ID, "android:id/text1")
    drop_down_locator = (AppiumBy.ID, "com.androidsample.generalstore:id/spinnerCountry")
    name_locator = (AppiumBy.ID, "com.androidsample.generalstore:id/nameField")
    radio_locator = (AppiumBy.ID, "com.androidsample.generalstore:id/radioFemale")
    text_select = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[1]")
    cart_locator = (AppiumBy.ID, "com.androidsample.generalstore:id/appbar_btn_cart")
    item_price_locator = (AppiumBy.ID, "com.androidsample.generalstore:id/productPrice")
    total_item_price_locator = (AppiumBy.ID, "com.androidsample.generalstore:id/totalAmountLbl")
    order_checkout_locator = (AppiumBy.ID, "com.androidsample.generalstore:id/btnProceed")

    def __init__(self, driver):
        super().__init__(driver)

    def add_address(self):
        self.do_click(self.drop_down_locator)
        self.swipe(348, 676, 346, 676, 500)
        self.swipe(298, 693, 298, 692, 500)
        self.do_send_keys(self.name_locator, 'Radha')
        self.do_click(self.radio_locator)
        self.swipe(240, 1524, 511, 1524, 500)
        self.swipe(348, 2054, 389, 676, 500)

    def add_to_cart(self, ORDER_ITEM):

        i = 1
        while i > 0:
            country_list = self.driver.find_elements('xpath', '//android.widget.TextView')

            for ele in country_list:
                print(ele.text)
                if ele.text == ORDER_ITEM:
                    ele.click()
                    i -= 1
                    break

            self.swipe(535, 2054, 389, 676, 500)
        self.swipe(858, 575, 898, 575, 500)
        self.do_click(self.cart_locator)

    def assert_price(self):
        item_price = self.get_price(self.item_price_locator)
        total_item_price = self.get_price(self.total_item_price_locator)
        print(f"Item price : {item_price}, Total cart price : {total_item_price}")
        assert item_price == total_item_price

    def checkout(self):
        self.swipe(90, 1676, 91, 1676, 500)
        self.do_click(self.order_checkout_locator)
