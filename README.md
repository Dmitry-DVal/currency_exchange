# Проект “Обмен валют”

## Ссылка с информацией

https://zhukovsd.github.io/python-backend-learning-course/projects/currency-exchange/

### Описание

REST API для описания валют и обменных курсов. Позволяет просматривать и редактировать списки валют и обменных курсов, и
совершать расчёт конвертации произвольных сумм из одной валюты в другую.

Веб-интерфейс для проекта не подразумевается.

### Мотивация проекта

- Знакомство с MVC
- REST API - правильное именование ресурсов, использование HTTP кодов ответа
- SQL - базовый синтаксис, создание и изменение таблиц.

Для запуска приложения - запустить app.py

### Пример возможных запросов

#### корректный POST запрос на добавление валюты в curl

curl -X POST http://localhost:8000/currencies -d "name=Albanian Lek&code=ALL&sign=L" -H "Content-Type:
application/x-www-form-urlencoded"

- GET /currencies
- GET /currency/EUR
- POST /currencies
- GET /exchangeRates
- GET /exchangeRate/USDRUB
- POST /exchangeRates
- PATCH /exchangeRate/USDRUB
- GET /exchange?from=BASE_CURRENCY_CODE&to=TARGET_CURRENCY_CODE&amount=$AMOUNT

(Подробную информацию по составлению запросов см в ссылке с информацией)

### Создание Базы данных и таблиц в ней

- перейти в dao/dataBase/..
- Запустить currenciesDataBaseCreator.py и exchangeRatesDataBaseCreator.py

### Автор

Дмитрий Валюженич
Mitya0777@gmail.com