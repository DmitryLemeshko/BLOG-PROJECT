Цей проект є простим веб-додатком у вигляді блогу, створеним на Python з використанням фреймворку Django
Основні функціональні можливості:
Реєстрація користувачів з можливістю скидання паролю.
Створення постів зареєстрованими користувачами.
Коментарі до постів від інших користувачів.
Профіль користувача, де зберігається інформація про нього.
Адміністративна панель Django для управління користувачами, постами та коментарями.
Проект побудований таким чином, щоб його можна було легко розширювати і додавати нові функції.
Використані технології
Мова програмування: Python 3.15
Веб-фреймворк: Django 5.2
База даних: SQLite 
Контроль версій: Git
Публічний репозиторій: GitHub
Редактор коду: Notepad++ 
Система запуску команд: PowerShell
blog_project/
├── accounts/           # Додаток для користувачів
│   ├── migrations/
│   ├── templates/accounts/
│   │   ├── register.html
│   │   ├── login.html
│   │   └── profile.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── posts/              # Додаток для постів
│   ├── migrations/
│   ├── templates/posts/
│   │   ├── home.html
│   │   ├── post_detail.html
│   │   └── post_form.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── blog/               # Головна конфігурація Django-проекту
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── db.sqlite3
└── .gitignore

Кроки для запуску проекту

Клонувати репозиторій:

git clone <URL_репозиторію>
cd blog_project
Встановити залежності (Django):

python -m pip install django
Застосувати міграції бази даних:

python manage.py migrate
Створити суперкористувача для адміністративної панелі:

python manage.py createsuperuser


Запустити сервер:

python manage.py runserver


Відкрити браузер і перейти на адресу:

http://127.0.0.1:8000/


Адмінка доступна за адресою:

http://127.0.0.1:8000/admin/
