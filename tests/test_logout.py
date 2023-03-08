from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# Выход по кнопке «Выйти» в личном кабинете
def test_logout():
    # Открыть браузер с страницей сайта
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Найти заголовок Личный кабинет и зайти
    driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()

    # Найти поле "Email" и заполнить его
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys(
        'ekaterinagashibayazova777@yandex.ru')

    # Найти поле "Пароль" и заполнить его
    driver.find_element(By.NAME, "Пароль").send_keys(123456789)

    # Найти кнопку "Войти" и кликнуть по ней
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

    # Найти заголовок Личный кабинет и зайти
    driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()

    # Явное ожидание для загрузки страницы
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button')))

    # Нажать на кнопку Выход
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button').click()

    # Явное ожидание для загрузки страницы
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/h2')))

    # Переход на стр Вход
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/h2').text == 'Вход'

    # Закрыть браузер
    driver.quit()
