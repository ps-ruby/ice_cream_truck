# Ice Cream Truck

## Setup

The first thing to do is to clone the repository:

```sh
git clone https://github.com/ps-ruby/ice_cream_truck.git
cd ice_cream_truck
```

Create a virtual environment to install dependencies in and activate it:

```sh
python3 -m virtualenv env
source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip3 install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ bash migrate_and_seed.sh
(env)$ python3 manage.py runserver
```

### API Endpoints
1. `http://127.0.0.1:8000/api/trucks/`: List all ice creams truck
2. `http://127.0.0.1:8000/api/food-items/`: List all food items from all truck
3. `http://127.0.0.1:8000/api/orders/`: List all orders of a user
