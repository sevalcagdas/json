import json
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def browser():
    # Selenium WebDriver'ını başlat
    driver = webdriver.Chrome()
    yield driver
    # WebDriver'ı kapat
    driver.quit()

def test_login_with_valid_credentials(browser):
    # JSON dosyasından kullanıcı adı ve şifreyi al
    with open("data/data.json") as f:
        credentials = json.load(f)

    username = credentials['username']
    password = credentials['password']

    # Siteye git
    browser.get('https://www.saucedemo.com/')

    # Kullanıcı adı ve şifre girişi
    browser.find_element(By.ID, 'user-name').send_keys(username)
    browser.find_element(By.ID, 'password').send_keys(password)
    browser.find_element(By.ID, 'login-button').click()

    # Girişin başarılı olup olmadığını kontrol etmek için bekleyin
    WebDriverWait(browser, 20).until(EC.url_to_be('https://www.saucedemo.com/inventory.html'))

    # Başarılı girişin doğruluğunu assert ile kontrol edin
    assert "inventory.html" in browser.current_url
