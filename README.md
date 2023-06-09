# **“Places Remember”**
[![places-remember](https://github.com/artyom-vah/places-remember/actions/workflows/main.yml/badge.svg)](https://github.com/artyom-vah/places-remember/actions)
![coverage status](https://gist.github.com/artyom-vah/de2e181afefe9d9318af159e510c4143/raw/coverage.svg) 

## Описание
Цель: Создать веб-приложение, с помощью которого люди смогут хранить свои впечатления о посещаемых местах.

Описание задачи: Пользователь заходит на сайт и видит страницу с кратким описанием сервиса. Также, он замечает кнопки "Войти с помощью Google/VK", нажимая на которую Google/VK предлагает ему разрешить доступ к его базовой информации. Он разрешает доступ, после чего должна открыться страница. В ее шапке будет имя и фотография (информация взята из профиля Google/VK), по центру страницы надпись "У вас нет ни одного воспоминания", кнопка "Добавить воспоминание" (ее расположение на ваше усмотрение), при нажатии на которую должна открываться форма с возможностью указания места на карте, а также поле для ввода названия и поле для ввода комментария об этом месте. Далее пользователь может нажать на кнопку "Сохранить", после чего он снова попадает на домашнюю страницу со списком из этого элемента и возможностью добавлять новые места. Весь добавленный список мест будет отображаться на домашней странице. На домашней странице пользователя также есть кнопка, позволяющая ему выйти из своего аккаунта. После выхода он должен попасть на приветственную страницу сервиса без возможности видеть список посещаемых мест. При повторной авторизации через Google/VK пользователь снова видит все свои добавленные места.

## Требования к реализации
- Приложение должно быть реализовано на базе фреймворка Django.
- Оформление кода должно соответствовать стандартам (PEP8, Django coding style).
- Все используемые зависимости должны быть актуальными на момент создания проекта.
- С самого начала разработки необходимо использовать Git, а также следовать стилю коммитов: [https://chris.beams.io/posts/git-commit/](https://chris.beams.io/posts/git-commit/). Исходный код приложения должен быть размещён на GitHub.
- Основной функционал (создание впечатлений о посещаемых местах и получение их списка) должен быть покрыт юнит-тестами.
- Возможно использование любых сторонних пакетов, для стилей рекомендуется использовать Bootstrap.
- Если что-то не удалось сделать, необходимо описать проблемы в файле README.md.

### **Ссылка на  dockerhub:** 
https://hub.docker.com/repository/docker/artyomvah/places-remember/general
```
1) Cкачать образ c dockerhub: 
docker pull artyomvah/places-remember:latest

2) Запустить скаченный образ с dockerhub: 
winpty docker run --name artyomvah-places-remember -it -p 127.0.0.1:8000:8000 artyomvah/places-remember

3) Перейти в браузере на  
http://127.0.0.1:8000/
```


### **Стек:**
![python version](https://img.shields.io/badge/Python-3.10.2-green)   ![django version](https://img.shields.io/badge/Django-4.21-green)


### **Дополнительные библиотеки:**
[![django-allauth](https://img.shields.io/badge/django--allauth-0.54.0-blue?style=flat-square)](https://django-allauth.readthedocs.io/en/latest/) [![folium](https://img.shields.io/badge/folium-0.14-blue)](https://python-visualization.github.io/folium/)  [![django-smart-selects](https://img.shields.io/badge/geocoder-1.38.1-blue)](https://pypi.org/project/geocoder/) [![flake8](https://img.shields.io/badge/flake8-5.0.4-blue)](https://pypi.org/project/flake8/5.0.4/)

### **Запуск проекта в dev-режиме**
Инструкция ориентирована на операционную систему Windows и утилиту git bash.<br/>
#####Для прочих инструментов используйте аналоги команд для вашего окружения.

1. Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone https://github.com/artyom-vah/places-remember.git
```

2. Установите и активируйте виртуальное окружение
```
python -m venv venv
source venv/Scripts/activate
```
или сразу так:
```
python -m venv venv && . venv/Scripts/activate
```
3. Обновите pip 
```
python -m pip install --upgrade pip
```
4. Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```
5. Перейдите в папку project/
```
cd project/
```
6. В папке с файлом manage.py создайте и выполните миграции:
```
python manage.py makemigrations 
python manage.py migrate
```
7. Создайте суперюзера 'укажите имя пользователя, адрес электронной почты (необязательно), и Password'
```
python manage.py createsuperuser
```
8. В папке с файлом manage.py запустите сервер:
```
python manage.py runserver
```
9. Перейдите в админку
```
http://127.0.0.1:8000/admin/
```
10.  Переходим в Сайты -> Добавить
``` 
Доменное имя: http://127.0.0.1
Отображаемое имя: http://127.0.0.1
```   
11.  Переходим в социальные аккаунты -> Социальные приложения -> Добавить -> Выибираем нужный аккаунт  
```
VK или Google
```
12.  У провайдера VK, указываем имя, id клаиента, секретный ключ API, и ключ, все эти данные получаем здесь 
```
https://vk.com/dev
```
13. У провайдера Google, указываем имя, id клаиента и секретный ключ API, все эти данные получаем здесь 
```
https://console.cloud.google.com
```
14. Запуск тестов, все тесты находясь в папке с файлом manage.py выполните команду (все тесты тут places-remember\project\memories\tests\)
```
python manage.py test
coverage run --source='memories' manage.py test
coverage run --source='memories' manage.py test -v 2
coverage report
```
15. Запуск coverage_cicd.py, переходим в корневую папку places-remember\  
```
cd places-remember\  
python coverage_cicd.py
```

**Пример готового проекта**
***Вывод в браузер:***
![brows_1](https://github.com/artyom-vah/places-remember/blob/main/scrins/main_guest.jpg)
![brows_2](https://github.com/artyom-vah/places-remember/blob/main/scrins/in_google.jpg)
![brows_3](https://github.com/artyom-vah/places-remember/blob/main/scrins/in_vk.jpg)
![brows_4](https://github.com/artyom-vah/places-remember/blob/main/scrins/main_authorized_google.jpg)
![brows_5](https://github.com/artyom-vah/places-remember/blob/main/scrins/list_authorized_google.jpg)
![brows_6](https://github.com/artyom-vah/places-remember/blob/main/scrins/add_authorized_google.jpg)
![brows_7](https://github.com/artyom-vah/places-remember/blob/main/scrins/add_authorized_google_2.jpg)
![brows_8](https://github.com/artyom-vah/places-remember/blob/main/scrins/list_authorized_google-2.jpg)
![brows_9](https://github.com/artyom-vah/places-remember/blob/main/scrins/add_authorized_google_3.jpg)
![brows_10](https://github.com/artyom-vah/places-remember/blob/main/scrins/main_authorized_vk.jpg)
![brows_11](https://github.com/artyom-vah/places-remember/blob/main/scrins/list_authorized_vk.jpg)
![brows_12](https://github.com/artyom-vah/places-remember/blob/main/scrins/add_authorized_vk.jpg)

***Админка:***
![Admin_1](https://github.com/artyom-vah/places-remember/blob/main/scrins/admin_1.jpg)
![Admin_2](https://github.com/artyom-vah/places-remember/blob/main/scrins/admin_2.jpg)  
![Admin_3](https://github.com/artyom-vah/places-remember/blob/main/scrins/admin_3.jpg)
![Admin_4](https://github.com/artyom-vah/places-remember/blob/main/scrins/admin_4.jpg)
![Admin_5](https://github.com/artyom-vah/places-remember/blob/main/scrins/admin_5.jpg)





