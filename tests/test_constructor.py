from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# Тест на переход к разделам: «Булки»
def test_bread():
    # Открыть браузер с страницей сайта
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Найти заголовок "Войти в аккаунт" и зайти
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()

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

    # Отображается раздел Булки
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[1]').text == 'Булки'

    # Закрыть браузер
    driver.quit()

# Тест на переход к разделам: «Соусы»
def test_sauces():
    # Открыть браузер с страницей сайта
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Найти заголовок "Войти в аккаунт" и зайти
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()

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

    # Нажать на раздел Соусы
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]').click()

    # Отображается раздел Соусы
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[2]').text == 'Соусы'

    # Закрыть браузер
    driver.quit()

# Тест на переход к разделам: «Начинки»
def test_filling():
    # Открыть браузер с страницей сайта
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Найти заголовок "Войти в аккаунт" и зайти
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()

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

    # Нажать на раздел Начинки
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]').click()

    # Отображается раздел Начинки
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[3]').text == 'Начинки'

    # Закрыть браузер
    driver.quit()
