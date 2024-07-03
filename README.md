## Click tracker

# Installation instructions 
For beginning you have to install Python3+

Firstly you need to create .env file(Search for example in .env_sample file).\
Set all environment variables for postgresql database and secret key(Generate your key [here](https://djecrety.ir))

In terminal write down following command:
```shell
git clone https://github.com/Lebwa1337/Click_tracker.git
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
