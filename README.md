# spa-care backend

## Prerequisites
- [Python](https://www.python.org/) v3.12
- [PostgreSQL](https://www.postgresql.org/)

## Setup

### Setup environment

1. Install dependencies
   ```
   pip install -r requirements.txt
   ```
2. Update database information in `spacare/settings.py`
3. Migrate database
   ```
   python manage.py migrate
   ```

### Launch
   ```
   python manage.py runserver 0.0.0.0:8000
   ```