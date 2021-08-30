# Basketball League

## Requirements
- Python 3.8.10
- Sqlite3

# Run project
- install requirements
```
pip install -r requirements.txt
```
- migrate the db
```
python manage.py makemigrations
python manage.py migrate
```
- import fixtures
```
python manage.py loaddata fixtures.json
```
- run server
```
python manage.py runserver
```
