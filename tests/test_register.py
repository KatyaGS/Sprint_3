from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random

# Тест на успешную регистрацию
def test_register_success():
    # Открыть браузер с страницей сайта
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    
    # Найти заголовок Личный кабинет и зайти
    driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()
    
    # Нажать кнопку зарегистрироваться
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/p[1]/a").click()

    # Найти поле "Имя" и заполнить его
    driver.find_element(By.NAME, "name").send_keys('ekaterina')

    # Сгенерировать случайную почту
    random_email = str(random.randint(1000000000, 9999999999)) + '@yandex.ru'
    password = '123456'

    # Найти поле "Email" и заполнить его
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(random_email)

    # Найти поле "Пароль" и заполнить его корректно
    driver.find_element(By.NAME, "Пароль").send_keys(password)

    # Найти кнопку "Зарегистрироваться" и кликнуть по ней
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

    # Явное ожидание для загрузки страницы
    WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element((By.XPATH, '//*[@id="root"]/div/main/div/h2'), 'Вход'))

    # Проверить что мы попали на правильную страницу после регистрации
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/h2').text == 'Вход'

    # Проверить что мы попали на правильную страницу после регистрации
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/h2').text == 'Вход'

    # Закрыть браузер
    driver.quit()

# Пароль меньше 6 символов
def test_register_password_less_than_6_symbols():
    # Открыть браузер с страницей сайта
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    
    # Найти заголовок Личный кабинет и зайти
    driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()
    
    # Нажать кнопку зарегистрироваться
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/p[1]/a").click()

    # Найти поле "Имя" и заполнить его
    driver.find_element(By.NAME, "name").send_keys('ekaterina')

    # Сгенерировать случайную почту
    random_email = str(random.randint(1000000000, 9999999999)) + '@yandex.ru'
    password = '12345'

    # Найти поле "Email" и заполнить его
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(random_email)

    # Найти поле "Пароль" и заполнить его
    driver.find_element(By.NAME, "Пароль").send_keys(password)

    # Найти кнопку "Зарегистрироваться" и кликнуть по ней
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

    # Найти сообщение об ошибке и проверить, что оно есть
    error_message = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p')
    assert error_message.text == 'Некорректный пароль'

    # Закрыть браузер
    driver.quit()

# Поле «Имя» должно быть не пустым
def test_register_empty_name():
    # Открыть браузер с страницей сайта
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    
    # Найти заголовок Личный кабинет и зайти
    driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()
    
    # Нажать кнопку зарегистрироваться
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/p[1]/a").click()

    # Сгенерировать случайную почту
    random_email = str(random.randint(1000000000, 9999999999)) + '@yandex.ru'
    password = '123456'

    # Найти поле "Email" и заполнить его
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(random_email)

    # Найти поле "Пароль" и заполнить его
    driver.find_element(By.NAME, "Пароль").send_keys(password)

    # Найти кнопку "Зарегистрироваться" и кликнуть по ней
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

    # Явное ожидание для загрузки страницы
    WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element((By.XPATH, '//*[@id="root"]/div/main/div/form/button'), 'Зарегистрироваться'))

    # Проверить что мы остались на той же странице
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').text == 'Зарегистрироваться'

    # Закрыть браузер
    driver.quit()

# В поле «Email» должен быть валидный email
def test_register_invalid_email():
    # Открыть браузер с страницей сайта
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    
    # Найти заголовок Личный кабинет и зайти
    driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()
    
    # Нажать кнопку зарегистрироваться
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/p[1]/a").click()

    # Найти поле "Имя" и заполнить его
    driver.find_element(By.NAME, "name").send_keys('ekaterina')

    # Сгенерировать случайную не валидную почту
    random_email = str(random.randint(1000000000, 9999999999))
    password = '123456'

    # Найти поле "Email" и заполнить его
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(random_email)

    # Найти поле "Пароль" и заполнить его
    driver.find_element(By.NAME, "Пароль").send_keys(password)

    # Найти кнопку "Зарегистрироваться" и кликнуть по ней
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

    # Явное ожидание для загрузки страницы
    WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element((By.XPATH, '//*[@id="root"]/div/main/div/form/button'), 'Зарегистрироваться'))

    # Проверить что мы остались на той же странице
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').text == 'Зарегистрироваться'

    # Закрыть браузер
    driver.quit()
