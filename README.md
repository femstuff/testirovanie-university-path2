# Тестирование GitHub API
## Требования

- Python 3.7+
- Учетная запись GitHub
- Personal Access Token (PAT) с правами repo

## Установка

1. Клонируйте репозиторий:

```bash
git clone git@github.com:femstuff/testirovanie-university-path2.git
cd testirovanie-university-path2
```

2. Создание виртуального окружения (рекомендуется)

```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
```


3. Установка зависимостей
bash
```
pip install -r requirements.txt
```


4. Настройка переменных окружения

    1) Переименуйте .env.example в .env

    2) Заполните файл своими данными:
```
GITHUB_USERNAME=ваш_username_на_GitHub
GITHUB_TOKEN=ваш_персональный_токен
GITHUB_REPO_NAME=тестовый-репозиторий
```


Как получить токен?

    Перейдите в Settings → Developer settings → Personal access tokens → Generate new token 
    Выберите разрешение repo

Запуск теста


```python main.py```