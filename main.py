from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import getpass

# Логин и пароль
login = input("Введите логин: ")
password = getpass.getpass("Введите пароль: ")

driver = webdriver.Firefox(executable_path='geckodriver.exe')
driver.get("https://nstu.ru")
time.sleep(1)

# найдем кнопку Войти
btn_login = driver.find_element_by_css_selector("div.header__login>a")
btn_login.click()
time.sleep(1)

# найдем ссылку Кабинет обучающегося
btn_kabinet = driver.find_element_by_xpath('//a[text() = "Кабинет обучающегося"]')
btn_kabinet.click()
time.sleep(1)

# найдем поле логина и пароля
input_login = driver.find_element_by_name('callback_0')
input_password = driver.find_element_by_name('callback_1')

# введем данные
input_login.send_keys(login)
input_password.send_keys(password)

# нажмем Enter
input_password.send_keys(Keys.RETURN)
time.sleep(2)

# найдем ссылку Информация об успеваемости
btn_uspev = driver.find_element_by_xpath('//div[text() = "Информация об успеваемости"]')
btn_uspev.click()
time.sleep(1)
btn_uspev2 = driver.find_element_by_xpath('//div[text() = "Результаты сессии"]')
btn_uspev2.click()
time.sleep(1)

tables = driver.find_elements_by_css_selector(".sysContentWithMenu>table>tbody")   
for table in tables:
    tds = table.find_elements_by_css_selector('tr.all_progress>td.tdbr:nth-child(2)')
    j = 0
    for td in tds:
        print(td.text)
    break
time.sleep(10)
driver.close()