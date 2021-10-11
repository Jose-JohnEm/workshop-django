./scripts/wait-for-it.sh -h db -p 5432
./manage.py makemigrations
./manage.py migrate
./manage.py runserver 0.0.0.0:8000
