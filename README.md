## Getting Started <a name="getting_started"></a>
The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/sumit5529/invoice
$ cd invoice
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ pip install virtualenv
$virtualenv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements
```


Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd invoice
(env)$ python manage.py runserver and go to `http://127.0.0.1:8000/admin`
(env)$ python manage.py test 
```
And navigate to `http://127.0.0.1:8000`.
