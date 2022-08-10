# django-drf-postgres-musicapp

first create your virtualenv

`$ python3 -m venv venv`

activate venv

`$ source venv/bin/activate`

then install requeriments

`$ pip install -r requirements.txt`

install postgresql, login and create the database

`CREATE DATABASE <yourDBname;`

create a .env file in the root folder

`$ touch .env`

and add your postgresql credentials and the app SECRET_KEY to .env file

>ENV_SECRET_KEY="{add a secret key like bhajfbkjhawbdkjhabdjh}"\
ENV_NAME='{yourDBname}'\
ENV_HOST='{your host or localhost}'\
ENV_PORT='{your db port or 5432}'\
ENV_USER='{your db user}'\
ENV_PASSWORD='{your db password}'

run the command:

`python manage.py migrate`

finally the project run with: 

`$ python manage.py runserver`

open your browser in: 

`localhost:8000/artist`\
`localhost:8000/artist/new`\
`localhost:8000/artist/<int:id>`\
`localhost:8000/artist/put/<int:id>`\
`localhost:8000/artist/del/<int:id>`\
`localhost:8000/album`\
`localhost:8000/album/new`\
`localhost:8000/album/<int:id>`\
`localhost:8000/album/put/<int:id>`\
`localhost:8000/album/del/<int:id>`\
`localhost:8000/song`\
`localhost:8000/song/new`\
`localhost:8000/song/<int:id>`\
`localhost:8000/song/put/<int:id>`\
`localhost:8000/song/del/<int:id>`\
`localhost:8000/songs`


