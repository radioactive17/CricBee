# Cricbee

Introducing a website designed exclusively for cricket fans worldwide! Stay up-to-date with the latest rankings, fixtures, and news from around the world of cricket. This website also features a unique blog section where you can share your thoughts and opinions about recent events in the world of cricket with fellow fans.

But that's not all! This website also offers a comprehensive module where you can learn about the various events that changed the course of the game, deepening your understanding and appreciation of this beloved sport. Whether you're a die-hard cricket fan or a casual observer, our website is the ultimate destination for everything cricket. Join our community today and experience the excitement of cricket like never before!

## Install Dependencies
Go to the directory containing requirements.txt 
```bash
pip install -r requirements.txt
```

## Setup Database
You code wont be executed until you set up your database.
Following are the steps to setup your database for PostgreSQL. 
1. Create a database named Cricbee in the PostgreSQL
2. Change the settings.py file in Cricbee directory accordingly. 
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Cricbee',
        'USER': 'your username',
        'PASSWORD': 'your password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```
Note: Different Databases require differnet setup. Pleae setup your database accordingly.

## Run the program
After installing the dependencies and setting up the database you should be good to go and execute the program.  
Make sure you are in the directory containing manage.py file and Run the following command line to bring up the sever 
```bash
python manage.py runserver
```
If everything went smoothly, you should see the below screen.
![cmd](https://github.com/radioactive17/Cricbee/blob/main/Readme%20images/cmd.png?raw=true)

If you run into errors. Please look online for solutions

## Developer-Owner
Jignesh Kirti Nagda
