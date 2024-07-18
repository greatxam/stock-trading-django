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

# Configuration
You must provide values for the environment variables in your `.env` file.

## Environment Variables
| NAME              | TYPE    | REQUIRED | DEFAULT          | DESCRIPTION                             |
|-------------------|---------|----------|------------------|-----------------------------------------|
| POSTGRES_HOST     | String  | True     | None             | Database hostname.                      |
| POSTGRES_PORT     | Number  | True     | None             | Database port.                          |
| POSTGRES_DB       | String  | True     | None             | Database name.                          |
| POSTGRES_USER     | String  | True     | None             | Database username.                      |
| POSTGRES_PASSWORD | String  | True     | None             | Database password.                      |
| POSTGRES_PASSWORD | String  | True     | None             | Database password.                      |
| SECRET_KEY        | String  | True     | None             | Secret key for hashing sensitive data.  |
| HOST              | String  | False    | localhost        | Application hostname.                   |
| CORS              | List    | False    | http://localhost | List of allowed urls. (Comma separated) |
| DEBUG             | Boolean | False    | False            | Enable debugging.                       |

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

# Registering your OAuth application
Go to the URL below and create a new application.

```
http://localhost:8080/api/v1/auth/applications/
```

- **Name:** *The name of you OAuth application*
- **Client Type:** confidential
- **Authorization Grant Type:** Resource owner password-based

Copy the **Client Secret** original value, it will be hash later.

For more information about *[Django OAuth Toolkit](https://django-oauth-toolkit.readthedocs.io/en/latest/rest-framework/getting_started.html)* follow the link.
