import unittest
import time
from selenium import webdriver
import allure


@allure.title("Check login in hobby dn ua")
    class PythonTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("/home/p_kultchyckiy/Завантаження/chrome_driver/chromedriver")

    def test_search(self):
        driver = self.driver
        with allure.step("Open main page hobby.dn.ua"):
            driver.get("https://www.hobby.dn.ua")
        assert "Збірні" in driver.title
        time.sleep(1)
        with allure.step("Enter valid data in email and password fields"):
            driver.find_element_by_link_text("Увійти").click()
            driver.find_element_by_id("login-email").send_keys("test.mail.user.5463@gmail.com")
            driver.find_element_by_id("login-password").send_keys("test12345")
            driver.find_element_by_xpath("//form[@id='login-nav']/div[4]").click()
        time.sleep(1)
        with allure.step("Enter in search field some product name"):
            driver.find_element_by_xpath("//input[@id='search-text']").send_keys("v3000s")
            driver.find_element_by_class_name("search-button").click()
            driver.execute_script("window.scrollTo(0, 200)")
            time.sleep(2)
            driver.find_element_by_id("productGrid93455").click()
        with allure.step("Buy found product"):
            driver.find_element_by_xpath("//a[@id='addto-cart']").click()
            basket = driver.find_element_by_id("basket")
            basket.find_element_by_class_name("dropdown-toggle").click()
            time.sleep(1)
        with allure.step("Cancel order"):
            driver.find_element_by_xpath("//a[@class='close-btn']").click()
            time.sleep(1)
            driver.switch_to.alert.accept()
            time.sleep(1)
        with allure.step("Log out from the site"):
            driver.find_element_by_link_text("Ваш кабінет").click()
            time.sleep(1)
            driver.find_element_by_xpath("//ul[@id='reg-user-menu']/li[6]/a").click()
            time.sleep(1)
            driver.switch_to.alert.accept()
            driver.find_element_by_id("header-logo").click()
            time.sleep(4)

    def tearDown(self):
        self.driver.close()
