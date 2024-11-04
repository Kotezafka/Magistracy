def handler(response):
    status_code = response.status_code

    if status_code == 400:
        raise Exception(f"Неверный запрос, проверьте данные запроса: {status_code}")

    if status_code == 404:
        raise Exception(f"URL API не найден: {status_code}")
