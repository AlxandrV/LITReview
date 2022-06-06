# LITReview

#### Require repository

```sh
git clone https://github.com/AlxandrV/LITReview.git ./
```

#### Create a virtual environnement

```sh
python -m venv env
```

#### Execute virtual env

For Windows
```sh
source env/Scripts/activate
```

For Linux
```sh
source env/bin/activate
```

#### Add requirements

```sh
pip install -r requirements.txt
```

## Django

#### Migrate models

```sh
python LITReview/manage.py makemigrations
```

```sh
python LITReview/manage.py migrate
```

#### Launch server

```sh
python LITReview/manage.py runserver
```