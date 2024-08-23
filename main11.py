import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

url = 'https://tomsk.hh.ru/vacancies/programmist'

driver.get(url)

time.sleep(3)

vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-serp__vacancy')

parsed_data = []

for vacancy in vacancies:
    try:
        title = vacancy.find_element(By.CSS_SELECTOR, 'span.vacancy-name-wrapper--R9iuXWkZt3U_qpqlrtC5').text
        company = vacancy.find_element(By.CSS_SELECTOR, 'span.company-name-badges-container--o692jpSdR2R4SR9oXuZJ').text
        salary = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text___pbpft_3-0-13').text
        link = vacancy.find_element(By.CSS_SELECTOR, 'a.magritte-link___b4rEM_4-2-6').get_attribute('href')
    except:
        print('Ошибка при парсинге')
        continue

    parsed_data.append([title, company, salary, link])

driver.quit()

with open('hh.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'Название компании', 'Зп', 'Ссылка'])
    writer.writerows(parsed_data)

