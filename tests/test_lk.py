from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# Тест на переход по клику на «Личный кабинет»
def test_lk():
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

    # Явное ожидание для загрузки страницы
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/header/nav/a')))

    # Найти снова заголовок Личный кабинет и зайти
    driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()

    # Явное ожидание для загрузки страницы
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/nav/p')))

    # На стр появился Профиль
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/nav/p').text == 'В этом разделе вы можете изменить свои персональные данные'

    # Закрыть браузер
    driver.quit()
