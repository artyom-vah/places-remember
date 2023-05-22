поправить
### **“Places Remember”**
```
Цель:
Создать веб-приложение, с помощью которого люди смогут хранить свои впечатления о посещаемых
местах.

Описание задачи:
Пользователь заходит на сайт и видит страницу с кратким описанием сервиса. Также, он замечает
кнопки “Войти с помощью Google/VK”, нажимая на которую Google/VK предлагает ему разрешить доступ
к его базовой информации.
Он разрешает доступ, после чего должна открыться страница. В ее шапке будет имя и фотография
(информация взята из профиля Google/VK), по центру страницы надпись “У вас нет ни одного
воспоминания”, кнопка “Добавить воспоминание” (ее расположение на ваше усмотрение), при нажатии
на которую должна открываться форма с возможностью указания места на карте, а также поле для
ввода названия и поле для ввода комментария об этом месте.
Далее пользователь может нажать на кнопку “Сохранить”, после чего он снова попадает на домашнюю
страницу со списком из этого элемента и возможностью добавлять новые места. Весь добавленный
список мест будет отображаться на домашней странице.
На домашней странице пользователя также есть кнопка, позволяющая ему выйти из своего аккаунта.
После выхода он должен попасть на приветственную страницу сервиса без возможности видеть список
посещаемых мест. При повторной авторизации через Google/VK пользователь снова видит все свои
добавленные места.

Требования к реализации:
● Приложение должно быть реализовано на базе фреймворка Django.
● Оформление кода должно соответствовать стандартам (PEP8, Django coding style)
● Все используемые зависимости должны быть актуальными на момент создания проекта.
● С самого начала разработки необходимо использовать git, а также следовать стилю коммитов:
https://chris.beams.io/posts/git-commit/. Исходный код приложения должен быть размещён на
github.
● Основной функционал (создание впечатлений о посещаемых местах и получение их списка)
должен быть покрыт юнит-тестами.
● Возможно использование любых сторонних пакетов, для стилей рекомендуется использовать
bootstrap.
● Если что-то не удалось сделать, необходимо описать проблемы в файле README.md


```


### **Стек:**
![python version](https://img.shields.io/badge/Python-3.10-green)


### **Дополнительные библиотеки:**
[![django-extensions](https://img.shields.io/badge/django--extensions-3.2.1-purple)](https://github.com/django-extensions/django-extensions)  
[![django-smart-selects](https://img.shields.io/badge/django--smart--selects-1.6.0-yellow)](https://github.com/jazzband/django-smart-selects)


### **Запуск проекта в dev-режиме**
Инструкция ориентирована на операционную систему Windows и утилиту git bash.<br/>
Для прочих инструментов используйте аналоги команд для вашего окружения.

1. Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone https://github.com/artyom-vah/places-remember.git
```

2. Установите и активируйте виртуальное окружение
```
python -m venv venv
``` 
```
source venv/Scripts/activate
```

3. Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```

4. В папке с файлом manage.py выполните миграции:
```
python manage.py migrate
```

5. Создайте суперюзера, зайдите в админку
```
python manage.py createsuperuser
```

6. В папке с файлом manage.py запустите сервер, выполнив команду:
```
python manage.py runserver
```

7. Перейдите в админку и добавьте дивизионы, предприятия и вопросы(также можете их добавить через основную форму подачи вопроса http://127.0.0.1:8000/)
```
http://127.0.0.1:8000/admin/
```

**Пример готового проекта**

***Админка:***
![Admin_1](https://github.com/artyom-vah/director-s-day/blob/main/screens/admin_1.jpg)
![Admin_2](https://github.com/artyom-vah/director-s-day/blob/main/screens/admin_2.jpg)
![Admin_3](https://github.com/artyom-vah/director-s-day/blob/main/screens/admin_3.jpg)
***Вывод в браузер:***
![brows_1](https://github.com/artyom-vah/director-s-day/blob/main/screens/brows_1.jpg)
![brows_2](https://github.com/artyom-vah/director-s-day/blob/main/screens/brows_2.jpg)



