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
2. Update database information in `selleraxis/settings/local.py`
3. Migrate database
   ```
   python manage.py migrate
   ```

### Launch
   ```
   python manage.py runserver 0.0.0.0:8000
   ```

## License

This project is Copyright (c) 2023 and onwards Digital Fortress. It is free software and may be redistributed under the terms specified in the [LICENSE] file.

[LICENSE]: /LICENSE
