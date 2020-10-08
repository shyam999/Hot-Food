# Hot-Food
> Food Delivery Website built with Django and Bootstrap
## Installation:

**1.Clone the Repo & Setup Virtualenv**
```sh
git clone https://github.com/shyam999/Hot-Food.git
virtualenv env
source env/bin/activate
```
**2.Install Requirements**
```sh
cd requirements.txt
pip install -r requirements.txt
```
**3.Set Up RabbitMQ Server**
```sh
sudo apt-get install rabbitmq-server
service rabbitmq-server start
```
**4.Migrate Database**
```sh
python manage.py makemigrations
python manage.py migrate
```
**5.Start Server**
```sh
python manage.py runserver
```
# Screenshots:
## Homepage:
![](demo/home.png)
## Product Page:
![](demo/product.png)
