import requests
from bs4 import BeautifulSoup


class Scrapper(object):
    """
    Описание класса
    """
    # Основные общедоступные свойства класса
    page_html = None
    soup_object = None

    # Приватные свойства класса
    __title = None
    __images = []


    def __init__(self, url):
        # Метод-конструктор класса
        # url - адрес веб страницы, которую мы загружаем
        pass

    def get_page_data(self):
        # Метод, получающий html содержимое веб-страницы
        pass

    def get_soup_object(self):
        # Метод, получающий объект BeautifulSoup, из загруженного html-документа
        pass

    @property
    def title(self):
        # Содержимое тега title
        return self.__title

    @property
    def images(self):
        # Список url картинок на странице(свойство src тегов img)
        return self.images