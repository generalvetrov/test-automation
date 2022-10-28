import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_script(link):
    browser = webdriver.Chrome()
    browser.get(link)

    # код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
    input1.send_keys("Dmytro")
    input5 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
    input5.send_keys("Victorovich")
    input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
    input2.send_keys("example@gmail.com")
    input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your phone:"]')
    input3.send_keys("103")
    input4 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your address:"]')
    input4.send_keys("Kyiv")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

    return welcome_text_elt.text


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        welcome_text = test_script(link)
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Error on test 2")

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        welcome_text = test_script(link)
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Error on test 2")


if __name__ == "__main__":
    unittest.main()
