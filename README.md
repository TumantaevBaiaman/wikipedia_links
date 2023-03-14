# Wikipedia Links
***
#Логика приложении 
- path: wikipedia/logic.py

Код написан на языке Python и имеет следующую логику:
1. Создается список пустых строк path длиной 4 элемента и 
базовая настройка логгирования.
2. Создается функция p_links, которая принимает список 
списков и возвращает новый список, содержащий все элементы 
из входного списка.
3. Создается функция get_links, которая принимает 
HTML-страницу и возвращает список уникальных URL-адресов 
вики-страниц, на которые имеются ссылки внутри тегов <p> 
на данной странице.
4. Создается функция create_graph, которая принимает 
две вики-страницы и возвращает список из двух или 
трех URL-адресов вики-страниц, образующих путь между 
ними (если путь был найден) или None (если путь не был найден).
5. Создается функция new_data, которая принимает список 
из двух или трех URL-адресов вики-страниц и возвращает 
словарь с тремя ключами, каждый из которых содержит 
тексты и ссылки на вики-страницы, которые были найдены 
в процессе перехода по пути из одной вики-страницы в другую.
6. Создается функция main, которая принимает два 
URL-адреса вики-страниц и возвращает словарь, 
содержащий информацию о текстах и ссылках на 
вики-страницы, которые были найдены в процессе перехода 
по кратчайшему пути между двумя заданными страницами.


# Django
1. Установите Git на свой компьютер. Вы можете скачать Git с официального сайта: https://git-scm.com/downloads
2. Откройте командную строку/терминал и перейдите в каталог, в который вы хотите клонировать проект.
3. https://github.com/TumantaevBaiaman/wikipedia_links
4. cd wikipedia_links
5. python -m venv venv
6. venv/Scripts/activate.bat
7. pip install -r requirements.txt
8. python manage.py runserver

# Docker
1. $ docker-compose up -d --build


# host & port
***
- http://127.0.0.1:8000/

# Imges Project
![Image alt](https://github.com/TumantaevBaiaman/wikipedia_links/raw/master/images_project/p1.png)
![Image alt](https://github.com/TumantaevBaiaman/wikipedia_links/raw/master/images_project/p2.png)
![Image alt](https://github.com/TumantaevBaiaman/wikipedia_links/raw/master/images_project/p3.png)
![Image alt](https://github.com/TumantaevBaiaman/wikipedia_links/raw/master/images_project/p4.png)
![Image alt](https://github.com/TumantaevBaiaman/wikipedia_links/raw/master/images_project/p5.png)

