import time
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import re

if __name__ == '__main__':
    appium_server_url = "http://localhost:4723/wd/hub"
    capabilities = dict(
        deviceName='Krushna',
        platformName='Android',
        appPackage='com.androidsample.generalstore',
        appActivity='com.androidsample.generalstore.SplashActivity',
    )
    drop_down_locator_country = (AppiumBy.ID, "android:id/text1")
    drop_down_locator = (By.ID, "com.androidsample.generalstore:id/spinnerCountry")
    name_locator = (AppiumBy.ID, "com.androidsample.generalstore:id/nameField")
    radio_locator = (AppiumBy.ID, "com.androidsample.generalstore:id/radioFemale")
    text_select = (AppiumBy.XPATH,
                   f"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[1]")
    driver = webdriver.Remote(appium_server_url, options=AppiumOptions().load_capabilities(capabilities))
    time.sleep(3)
    driver.find_element(*drop_down_locator).click()
    driver.swipe(348, 676, 346, 676, 500)  # 196,703,287,711

    cart_locator = (AppiumBy.ID, "com.androidsample.generalstore:id/appbar_btn_cart")
    # i = 1
    # while i > 0:
    #     country_list = driver.find_elements('xpath', '//android.widget.TextView')
    #
    #     for ele in country_list:
    #         print(ele.text)
    #         if ele.text == 'India':
    #             ele.click()
    #             i -= 1
    #             break
    #
    #     driver.swipe(535, 2054, 389, 676, 500)

    driver.find_element(*name_locator).send_keys("Krushna")
    time.sleep(1)
    driver.find_element(*radio_locator).click()
    time.sleep(1)
    driver.swipe(240, 1524, 511, 1524, 500)  # 196,703,287,711
    # 240, 1524, 511, 1524
    time.sleep(1)
    ORDER_ITEM = 'Converse All Star'
    driver.swipe(348, 2054, 389, 676, 500)

    i = 1
    while i > 0:
        country_list = driver.find_elements('xpath', '//android.widget.TextView')

        for ele in country_list:
            print(ele.text)
            if ele.text == ORDER_ITEM:
                ele.click()
                i -= 1
                break

        driver.swipe(535, 2054, 389, 676, 500)
        # driver.find_element(By.T)
    time.sleep(2)
    driver.swipe(858, 575, 898, 575, 500)
    time.sleep(2)
    driver.find_element(*cart_locator).click()
    time.sleep(2)
    item_price_locator = (AppiumBy.ID, "com.androidsample.generalstore:id/productPrice")
    total_item_price_locator = (AppiumBy.ID, "com.androidsample.generalstore:id/totalAmountLbl")

    item_price = str(driver.find_element(*item_price_locator).text)
    total_item_price = str(driver.find_element(*total_item_price_locator).text)

    print(f"Item price : {item_price}, Total cart price : {total_item_price}")

    assert item_price == total_item_price.replace(' ','')

    driver.swipe(90, 1676, 91, 1676, 500)
    time.sleep(2)
    order_checkout_locator = (AppiumBy.ID, "com.androidsample.generalstore:id/btnProceed")
    driver.find_element(*order_checkout_locator).click()
    time.sleep(10)
