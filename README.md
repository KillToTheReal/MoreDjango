# MoreDjango
Изучение фреймворка Django

### Создать venv. для пакета python команда ``` python -m venv venv ```
### Активировать venv. Для windows команда ``` .\venv\Scripts\activate ```. Для линукса ```source /venv/bin/activate```  Для выхода набрать ``` deactivate ```

#### Если powershell не даёт выполнить активацию, [решение](https://zawindows.ru/%D1%80%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D1%8B-%D0%BD%D0%B5%D0%B2%D0%BE%D0%B7%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE-%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7/) 
#### https://pypi.org/ - Сайт для просмотра и поиска пакетов питона

### Скачать Django. Из (venv) ``` pip install Django ```
### Создать проект ``` django-admin startproject {Имя проекта} ```
### Накатить сервер. Из папки {Имя проекта} ``` python manage.py runserver ```
### Разделение логики внутри сайта(проекта) происходит по приложениям. Для создания соответственно ``` python manage.py startapp {Название приложения} ```

### Добавить Vue CLI в проект ``` npm install -g @vue/cli ```
#### В Django MVC === MTV(?). Где
- Model == Model 
- View == Template 
- Controller == View
