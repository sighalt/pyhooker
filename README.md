# pyhooker

Lightweight and easy-to-use python dependency injection library

Pyhooker is ready to use for Python >=2.7 and >=3.2

[![Build Status](https://travis-ci.org/sighalt/pyhooker.svg?branch=master)](https://travis-ci.org/sighalt/pyhooker)


## Installation

```
pip install git+https://github.com/sighalt/pyhooker.git
```

## Usage

```python
import pyhooker


# wheel.py

class IWheel(object):
    pass


class MichelinWheel(IWheel):
    pass

# engine.py

class IEngine(object):
    pass


class OttoEngine(IEngine):
    pass


# car.py

class ICar(object):
    pass


class Car(ICar):

    @pyhooker.inject_params(engine=IEngine, wheel_type=IWheel)
    def __init__(self, engine, wheel_type):
        self.engine = engine
        self.wheel_type = wheel_type

# driver.py

class Driver(object):

    @pyhooker.inject_params(car=ICar)
    def __init__(self, car):
        self.car = car

# __init__.py

pyhooker.register(ICar, Car)
pyhooker.register(IEngine, OttoEngine)
pyhooker.register(IWheel, MichelinWheel)

driver = Driver()

print("The driver is %s\n... with its car %s\n... and engine %s\n... and wheel type %s" % (driver,
                                                      driver.car,
                                                      driver.car.engine,
                                                      driver.car.wheel_type))
```
