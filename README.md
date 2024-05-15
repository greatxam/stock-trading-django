# Stock Trading
***Stock Trading*** is an application for stock market trading.
User can able to place order to buy and sell stock.
And be able to upload a CSV file for bulk trades.

# Requirements
* [Debian 12.0](https://www.debian.org/releases/buster/)
* [Python 3.11](https://www.python.org/downloads/)
* [Django Framework 4.2.2](https://pypi.org/project/Django/#files/)
* [Apache HTTPD 2.4](https://httpd.apache.org/download.cgi/)
* [PostgresSQL 16.2](https://www.postgresql.org/download/)

# Starting up the application
```
docker-compose up
```

# Creating the super user
```
docker exec -it stocktrading python3 manage.py createuseruser
```

# Testing the application
Change the `core` with the module you want to test.
```
docker exec -it stocktrading python3 manage.py test core.tests
```
