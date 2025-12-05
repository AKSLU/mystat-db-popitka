# mystat-db-popitka

---

## Требования

* Python 3.10+
* `requests`, `psycopg2`
* PostgreSQL с таблицей:

```sql
CREATE TABLE IF NOT EXISTS executer (
    id SERIAL PRIMARY KEY,
    attempt INT NOT NULL,
    data JSONB NOT NULL
);
```

---

## Настройка

1. Установить зависимости:

```bash
pip install requests psycopg2
```

2. В `app.py` указать свои данные:

```python
conn = psycopg2.connect(
    dbname="base",
    user="postgres",
    password="ВАШ_ПАРОЛЬ",
    host="localhost",
    port="5432"
)

headers = {"Authorization": "ВАШ_API_КЛЮЧ"}
url = "https://mapi.itstep.org/v1/mystat/aqtobe/schedule/get-existing-schedule?date_filter=2025-07-01"
```

---

## Запуск

```bash
python app.py
```

Вывод:

```
Сохронено попытка: <номер>
```

Данные сохраняются в PostgreSQL в формате JSON. Каждый запуск увеличивает попытку на 1.
