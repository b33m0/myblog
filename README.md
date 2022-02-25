# CSE330
Usage:

1. go to the directory of the blog

cd blog

2. install required modules

pip install -r requirements.txt

3. migrate data for db

python manage.py makemigrations

python manage.py migrate

4. run the server

python manage.py runserver

5. access the website

http://127.0.0.1:8000/article/article-list/