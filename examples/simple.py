import pyhooker

__author__ = 'sighalt'

# wheel.py

class IWheel(object):
    pass


class MichelinWheel(IWheel):
    pass

pyhooker.register(IWheel, MichelinWheel)

# engine.py

class IEngine(object):
    pass


class OttoEngine(IEngine):
    pass

pyhooker.register(IEngine, OttoEngine)


# car.py

class ICar(object):
    pass


class Car(ICar):

    @pyhooker.inject_params(engine=IEngine, wheel_type=IWheel)
    def __init__(self, engine, wheel_type):
        self.engine = engine
        self.wheel_type = wheel_type

pyhooker.register(ICar, Car)

# driver.py

class Driver(object):

    @pyhooker.inject_params(car=ICar)
    def __init__(self, car):
        self.car = car

driver = Driver()

print("The driver is %s\n... with its car %s\n... and engine %s\n... and wheel type %s" % (driver,
                                                      driver.car,
                                                      driver.car.engine,
                                                      driver.car.wheel_type))
