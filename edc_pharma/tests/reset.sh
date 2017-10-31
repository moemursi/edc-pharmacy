echo "Rest migrations and drop/create DB? Cannot be undone! (Hit CTRL-C to cancel)"
mysql -u root -p -Bse 'drop database edc_pharma; create database edc_pharma character set utf8;'
rm -rf edc_pharma/migrations/
# rm db.sqlite3
# mysql -u root -p -Bse 'create database edc_pharma character set utf8;'
python manage.py makemigrations edc_pharma
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

