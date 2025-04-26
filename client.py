import requests
import json
#

class AuthClient:
    def __init__(self, base_url="https://ekranstroy.ru/api/v1/"):
        self.base_url = base_url
        self.token = None

    def login(self, username, password):
        """
        Авторизует пользователя и сохраняет токен.

        Args:
            username (str): Имя пользователя.
            password (str): Пароль пользователя.

        Returns:
            str: Токен доступа при успешной авторизации, None в случае ошибки.
        """
        url = self.base_url + "login/"
        headers = {"Content-Type": "application/json"}
        data = {"username": username, "password": password}

        try:
            response = requests.post(url, headers=headers, data=json.dumps(data))
            response.raise_for_status()  # Вызывает исключение для кодов ошибок 4xx и 5xx

            response_data = response.json()
            self.token = response_data.get("token")
            return self.token

        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе: {e}")
            if response.status_code == 401:
                print("Неверные учетные данные")
            elif response.status_code == 400:
                print("Неверный запрос")
            return None
        except json.JSONDecodeError as e:
            print(f"Ошибка при декодировании JSON: {e}")
            return None

    def get_headers(self):
        """
        Возвращает заголовки с токеном авторизации.

        Returns:
            dict: Заголовки с токеном, если пользователь авторизован, иначе пустой словарь.
        """
        if self.token:
            return {"Authorization": f"Token {self.token}"}
        else:
            return {}


# Пример использования:
if __name__ == "__main__":
    client = AuthClient()

    # Вход в систему
    token = client.login("vsp44", "abs1ebd23")  # Замените на свои учетные данные
    if token:
        print(f"Успешная авторизация. Токен: {token}")
