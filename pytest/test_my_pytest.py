from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


def registration(link):

    browser = webdriver.Chrome()
    
    try:

        browser.get(link)
        browser.implicitly_wait(1)

        # код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
        input1.send_keys("Dmytro")
        input5 = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
        input5.send_keys("Victorovich")
        input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
        input2.send_keys("example@gmail.com")
        # input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your phone:"]')
        # input3.send_keys("103")
        # input4 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your address:"]')
        # input4.send_keys("Kyiv")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        # time.sleep(2)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

        return welcome_text_elt.text
    except:
        browser.quit()
    finally:
        print('done')


def test_link1():
    link = "http://suninjuly.github.io/registration1.html"
    assert registration(link) == "Congratulations! You have successfully registered!", "Error on test 1"


def test_link2():
    link = "http://suninjuly.github.io/registration2.html"
    assert registration(link) == "Congratulations! You have successfully registered!", "Error on test 2"


if __name__ == "__main__":
    pytest.main()
