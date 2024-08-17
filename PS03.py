from bs4 import BeautifulSoup
import requests
from googletrans import Translator

def get_english_words():
    url = 'https://randomword.com/'
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        english_words = soup.find('div', id='random_word').text.strip()
        word_definition = soup.find('div', id='random_word_definition').text.strip()

        return {
            'english_words': english_words,
            'word_definition': word_definition
        }
    except:
        print('Ошибка')
        return None

def word_game():
    print('Добро пожаловать в игру!')

    while True:
        word_dict = get_english_words()
        word = word_dict.get('english_words')
        word_definition = word_dict.get('word_definition')
        translator = Translator()
        result = translator.translate(f'{word_definition}', dest='ru')
        word_ru = translator.translate(f'{word}', dest='ru')

        print(f'Значение слова - {result.text}')
        user = input('Что это за слово? ')
        if user == word_ru:
            print('Ответ верный!')
        else:
            print(f'Неверно, это - {word_ru.text}')

        play_again = input('Хотите сыграть еще раз? y / n ')
        if play_again != 'y':
            print('Спасибо за игру!')
            break

word_game()