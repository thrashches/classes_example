# Задание на тему классы, объекты, веб-скраппинг

На основе наброска в файле ```scrapper.py``` создать класс, который загружает указанную веб-страницу в память и выдергивает из нее заголовок и картинки. В данном примере мы будем использовать библиотеку ```requests``` для выполнения http-запросов. Библиотеку BeautifulSoup4 для парсинга полученных страниц.

---

В качестве примера предлагаю попробовать сайт 

> https://serpantin-shop.ru/. 

Можно взять страницу:

> https://serpantin-shop.ru/catalog/velosipedy/shosseynye/

и вытащить с нее фотографии велосипедов с карточек товаров. Нужны именно ссылки на картинки. Их необходимо записать в приватное свойство класса ```__images```.

В свойство ```__title``` нужно записать заголовок страницы, записанный в теге ```<title></title>```.

---

По итогу полученный класс должен запускаться примерно следующим образом:
```python

scrapper = Scrapper('https://serpantin-shop.ru/catalog/velosipedy/shosseynye/')
print(scrapper.title)
print(scrapper.images)

```

### Дополнительное задание

Добавить метод класса, который скачивает все фотографии из ```__images``` на жесткий диск компьютера.


## Подготовка директории проекта

Самый простой вариант подготовки директории проекта - склонировать его средствами pycharm из этого репозитория в новую папку проекта. Но если хочется прокачаться в работе с консолью, то рекомендую попробовать следующее:

1. Клонируем папку с проектом(репозиторий можно форкнуть к себе):

```bash
git clone <адрес репозитория>
```

2. Перемещаемся в эту папку с помощью PowerShell:

```bash
cd <Путь к папке проекта>
```

3. Создаем виртуальное окружение и активируем его. На новой строке слева должно появиться ```(venv)```.

```bash
python -m venv venv
.\venv\Scripts\activate.ps1
```

4. Устанавливаем зависимости:

```
pip install -r requirements.txt
```

5. Далее открываем папку в pycharm и можем работать.

### Что почитать/посмотреть

Про классы:
https://www.youtube.com/watch?v=esSIFatS6kM

Про декоратор ```@property```:
https://tirinox.ru/useful-decorators/

Документация BeautifulSoup4: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

Документация requests: https://docs.python-requests.org/en/latest/