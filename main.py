from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
import getpass

# Логин и пароль
login = input("Введите логин: ")
password = getpass.getpass("Введите пароль: ")

driver = webdriver.Firefox(executable_path='geckodriver.exe')
driver.get("https://nstu.ru")
time.sleep(2)

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
time.sleep(2)

# получение список
'''html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
div = soup.find('table', class_='tdall')
trs = div.find_elements_by_css_selector('tbody>tr.all_progress')

for tr in trs:
    #tds = tr.find_all('td:nth-child(2)')
    #print(tds[1].text.strip())
    print(tr)
    print('----')
   '''
trs = driver.find_elements_by_css_selector("table.tdall:first-child>tbody>tr.all_progress>td:nth-child(2)")   
for tr in trs:
    print(tr.text)
time.sleep(10)
driver.close()