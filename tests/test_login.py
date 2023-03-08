from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# Вход по кнопке «Войти в аккаунт» на главной странице
def test_login():
    # Открыть браузер с страницей сайта
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    
    # Найти заголовок "Войти в аккаунт" и зайти
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()
    
    # Найти поле "Email" и заполнить его
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('ekaterinagashibayazova777@yandex.ru')
    
    # Найти поле "Пароль" и заполнить его
    driver.find_element(By.NAME, "Пароль").send_keys(123456789)
    
    # Найти кнопку "Войти" и кликнуть по ней
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

    # Явное ожидание для загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')))

    # Кнопка Войти изменилась на кнопку Оформить заказ
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').text == 'Оформить заказ'
    
    # Закрыть браузер
    driver.quit()

# Вход через кнопку «Личный кабинет»
def test_login_lk():
    # Открыть браузер с страницей сайта
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Найти кнопку Личный кабинет и кликнуть по ней
    driver.find_element(By.XPATH, './/a[@href="/account"]').click()

    # Найти поле "Email" и заполнить его
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys(
        'ekaterinagashibayazova777@yandex.ru')

    # Найти поле "Пароль" и заполнить его
    driver.find_element(By.NAME, "Пароль").send_keys(123456789)

    # Найти кнопку "Войти" и кликнуть по ней
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

    # Явное ожидание для загрузки страницы
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')))

    # Кнопка Войти изменилась на кнопку Оформить заказ
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').text == 'Оформить заказ'

    # Закрыть браузер
    driver.quit()

# Вход через кнопку в форме регистрации
def test_login_register_page():
    # Открыть браузер с страницей сайта
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Найти кнопку Личный кабинет и кликнуть по ней
    driver.find_element(By.XPATH, './/a[@href="/account"]').click()

    # Найти кнопку зарегистрироваться
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/p[1]/a").click()

    # Найти кнопку Войти
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p/a').click()

    # Найти поле "Email" и заполнить его
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys(
        'ekaterinagashibayazova777@yandex.ru')

    # Найти поле "Пароль" и заполнить его
    driver.find_element(By.NAME, "Пароль").send_keys(123456789)

    # Найти кнопку "Войти" и кликнуть по ней
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

    # Явное ожидание для загрузки страницы
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')))

    # Кнопка Войти изменилась на кнопку Оформить заказ
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').text == 'Оформить заказ'

    # Закрыть браузер
    driver.quit()

# Вход через кнопку в форме восстановления пароля
def test_login_password_recovery_page():
    # Открыть браузер с страницей сайта
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    
    # Найти кнопку Личный кабинет и кликнуть по ней
    driver.find_element(By.XPATH, './/a[@href="/account"]').click()
    
    # Найти кнопку Восстановить пароль и кликнуть по ней
    driver.find_element(By.XPATH, './/a[@href="/forgot-password"]').click()

    # Найти кнопку Войти и кликнуть по ней
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p/a').click()

    # Найти поле "Email" и заполнить его
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('ekaterinagashibayazova777@yandex.ru')
    
    # Найти поле "Пароль" и заполнить его
    driver.find_element(By.NAME, "Пароль").send_keys(123456789)
    
    # Найти кнопку "Войти" и кликнуть по ней
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

    # Явное ожидание для загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')))

    # Кнопка Войти изменилась на кнопку Оформить заказ
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').text == 'Оформить заказ'

    # Закрыть браузер
    driver.quit()
