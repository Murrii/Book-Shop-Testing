from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_goods_card_add_to_busket_btn_exist(browser):
    browser.get(link)

    # sleep(30)

    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "btn-add-to-basket")))

    try:
        browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        assert True
    except NoSuchElementException:
        return False, "Web element not found"
