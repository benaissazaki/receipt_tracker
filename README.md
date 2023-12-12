# Receipt Tracker
A Django app for tracking receipts. Made as a practical assignment for a job candidacy.

## Installation
### Dependencies
```
pip install -r requirements.txt
```
or if using poetry
```
poetry install
``` 

### Environment variables
Create a .env file in the root folder (same folder as `settings.py`) with the following variables:

#### Development:
```
SECRET_KEY=
DEBUG=True
```

#### Production:
```
SECRET_KEY=
DEBUG=False

ALLOWED_HOSTS=

DATABASE_URL=
PGDATABASE=
PGUSER=
PGPASSWORD=
PGHOST=
PGPORT=
```

You can manually generate a secret key using [Djecrety](https://djecrety.ir).

### Migrate changes to the Database
```
python ./manage.py migrate
```
or if using poetry
```
poetry run python ./manage.py migrate
```

### Running:
```
python ./manage.py runserver
```
or if using poetry
```
poetry run python ./manage.py runserver
```

## Reasoning behind some choices

### Comments
I avoid commenting just for the sake of it. 

Considering that 90% of the code is just reusing Django generics and overriding their functions, there rarely was a need to explain something, as any Django developer understanding the core concepts will have no problem understanding it.


### Tests
Same thing for tests, it would make little sense to test Django built-ins.

I didn't write tests for the Receipt model because it's a basic one. Generally I test models whenever I add some custom methods to them, since there are none, there is no test.

Similarly, for views, I only tested the custom logic like access permission and redirection. It would be a waste of time to test, for example, if the generic LogoutView would log out the user.

