import time
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome(executable_path=r"C:\webdriver\chromedriver.exe")

    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    yield

    pytest.driver.quit()


def test_show_my_pets():
    # Вводим email
    pytest.driver.find_element(By.ID, 'email').send_keys('qwerty@email.com')
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'pass').send_keys('qwerty123')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    pytest.driver.get('https://petfriends.skillfactory.ru/my_pets')

    pytest.driver.implicitly_wait(10)
    names = pytest.driver.find_elements(By.CSS_SELECTOR, "#all_my_pets > table > tbody > tr > td:nth-child(2)")
    pytest.driver.implicitly_wait(10)
    age = pytest.driver.find_elements(By.CSS_SELECTOR, "#all_my_pets > table > tbody > tr > td:nth-child(4)")
    pytest.driver.implicitly_wait(10)
    poroda = pytest.driver.find_elements(By.CSS_SELECTOR, "#all_my_pets > table > tbody > tr > td:nth-child(3)")
    pytest.driver.implicitly_wait(10)
    photo = pytest.driver.find_elements(By.CSS_SELECTOR, "#all_my_pets > table > tbody > tr > th > img")




    # Присутствуют    все    питомцы.

    kolichestvo_kartochek = int(len(names))
    kolichestvo_obschee = int(len(pytest.driver.find_elements(By.CSS_SELECTOR, "#all_my_pets > table > tbody > tr")))
    wait = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#all_my_pets > table > tbody > tr"))
        )
    assert kolichestvo_kartochek == kolichestvo_obschee
    print(" \n1. Присутствуют    все    питомцы.")

    # Хотя    бы    у    половины    питомцев    есть    фото.

    count_photo = 0
    count_not_photo = 0
    for i in range(len(photo)):
        if photo[i].get_attribute('src') != '':
            count_photo = count_photo + 1
        else:
            count_not_photo = count_not_photo + 1
    assert count_photo >= count_not_photo
    print("2. Хотя    бы    у    половины    питомцев    есть    фото.")

    # У    всех    питомцев    есть    имя, возраст    и    порода.

    for i in range(len(names)):
        assert names[i].text != ''
        assert age[i].text != ''
        assert poroda[i].text != ''
    print("3. У    всех    питомцев    есть    имя, возраст    и    порода.")

    # У    всех    питомцев    разные    имена.

    vse_imena = []
    for i in range(len(names)):
        vse_imena.append(names[i].text)
    set_vse_imena = set(vse_imena)
    assert len(vse_imena) == len(set_vse_imena)
    print("4. У    всех    питомцев    разные    имена.")









