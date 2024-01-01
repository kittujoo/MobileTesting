import pytest
from appium.options.common import AppiumOptions
from appium import webdriver


@pytest.fixture(scope="module")
def setup():
    appium_server_url = "http://localhost:4723/wd/hub"
    capabilities = dict(
        deviceName='Krushna',
        platformName='Android',
        appPackage='com.androidsample.generalstore',
        appActivity='com.androidsample.generalstore.SplashActivity',
    )
    driver = webdriver.Remote(appium_server_url, options=AppiumOptions().load_capabilities(capabilities))
    yield driver
    driver.close()