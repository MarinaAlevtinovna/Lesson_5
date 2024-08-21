from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.get('https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')

assert 'Википедия' in browser.title

search_box = browser.find_element(By.ID, "searchInput")
user_request = input('Введите запрос: ')
search_box.send_keys(user_request)
search_box.send_keys(Keys.RETURN)
time.sleep(3)
a = browser.find_element(By.LINK_TEXT, user_request)
a.click()

while True:
    enter = input('Выберете варианты действий:\n'
            '1. Листать текущую страницу.\n'
            '2. Перейти на одну из статей.\n'
            '3. Выйти из программы.\n')
    print(enter)

    if enter == '1':
        paragraphs = browser.find_elements(By.TAG_NAME, 'p')
        for paragraph in paragraphs:
            print(paragraph.text)
            action = input("\nНажмите Enter для продолжения или введите 'q' для выхода в меню: ")
            if action.lower() == 'q':
                break

    elif enter == '2':
        links = browser.find_elements(By.TAG_NAME, 'a')
        links = [link for link in links if link.get_attribute('href') and 'wikipedia.org' in link.get_attribute('href')]

        for i, link in enumerate(links[:10]):
            print(f'{i + 1}. {link.text} - {link.get_attribute("href")}')

        try:
            link_choice = int(input('Введите номер ссылки для перехода: '))
            if 1 <= link_choice <= len(links):
                chosen_link = links[link_choice - 1]
                time.sleep(3)
                chosen_link.click()
                time.sleep(3)
            else:
                print("Ошибка: неверный номер ссылки.")
        except ValueError:
            print("Ошибка: введите число.")

    elif enter == '3':
        print('Досвидание...')
        browser.quit()
        break

    else:
        print("Ошибка ввода. Пожалуйста, выберите 1, 2 или 3.")