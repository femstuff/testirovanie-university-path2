import os
import requests
from dotenv import load_dotenv
import time

load_dotenv()


class GitHubAPITest:
    def __init__(self):
        self.username = os.getenv('GITHUB_USERNAME')
        self.token = os.getenv('GITHUB_TOKEN')
        self.repo_name = os.getenv('GITHUB_REPO_NAME')
        self.base_url = 'https://api.github.com'
        self.headers = {
            'Authorization': f'token {self.token}',
            'Accept': 'application/vnd.github.v3+json'
        }

    def create_repo(self):
        url = f'{self.base_url}/user/repos'
        data = {
            'name': self.repo_name,
            'description': 'Test repository created by API',
            'private': False,
            'auto_init': True
        }

        response = requests.post(url, headers=self.headers, json=data)
        if response.status_code == 201:
            print(f"Репозиторий {self.repo_name} успешно создан")
            print(response.status_code)
            time.sleep(15)
            return True
        else:
            print(f"Ошибка при создании репозитория: {response.json()}")
            return False

    def check_repo_exists(self):
        url = f'{self.base_url}/repos/{self.username}/{self.repo_name}'

        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            print(f"Репозиторий {self.repo_name} существует")
            return True
        elif response.status_code == 404:
            print(f"Репозиторий {self.repo_name} не существует")
            return False
        else:
            print(f"Ошибка при проверке репозитория: {response.json()}")
            return False

    def delete_repo(self):
        url = f'{self.base_url}/repos/{self.username}/{self.repo_name}'

        response = requests.delete(url, headers=self.headers)
        if response.status_code == 204:
            print(f"Репозиторий {self.repo_name} успешно удален")
            return True
        else:
            print(f"Ошибка при удалении репозитория: {response.json()}")
            return False

    def run_test(self):
        print("Запуск теста")

        print("\n1. Создание репозитория")
        if not self.create_repo():
            return False

        time.sleep(2)

        print("\n2. Проверка существования репозитория")
        if not self.check_repo_exists():
            return False

        print("\n3. Удаление репозитория")
        if not self.delete_repo():
            return False

        time.sleep(2)
        print("\n4. Проверка, что репозиторий удален")
        if self.check_repo_exists():
            return False

        print("\nТест успешно завершен!")
        return True


if __name__ == '__main__':
    test = GitHubAPITest()
    test.run_test()