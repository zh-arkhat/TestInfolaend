import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Список ссылок для параметризации
links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]

@pytest.mark.parametrize('link', links)
def test_stepik_feedback(link):
    # Инициализация браузера с автоподбором драйвера
    browser = webdriver.Chrome(ChromeDriverManager().install())
    wait = WebDriverWait(browser, 10)

    try:
        # Открываем страницу
        browser.get(link)

        # Авторизация (замените на свои логин/пароль)
        login_button = wait.until(EC.element_to_be_clickable((By.ID, "ember33")))
        login_button.click()

        email_input = wait.until(EC.presence_of_element_located((By.ID, "id_login_email")))
        email_input.send_keys("zh.arkhat2001@gmail.com")
        password_input = browser.find_element(By.ID, "id_login_password")
        password_input.send_keys("Ar!@#$%Rau2016")
        submit_button = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
        submit_button.click()

        # Ввод ответа
        answer_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[name='answer']")))
        answer_input.clear()
        answer = str(math.log(int(time.time())))
        answer_input.send_keys(answer)

        # Отправка ответа
        submit_button = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
        submit_button.click()

        # Ожидаем фидбек
        feedback = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "pre.smart-hints__hint")))
        feedback_text = feedback.text

        # Проверяем фидбек
        assert feedback_text == "Correct!", f"Фидбек для {link} не совпадает: {feedback_text}"

    finally:
        browser.quit()
