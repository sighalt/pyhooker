from example_classes.car import Car
from example_classes.interfaces import ICar, IEngine, IWheel
from example_classes.driver import Driver
from example_classes.engine import OttoEngine
from example_classes.wheel import MichelinWheel
import pyhooker

__author__ = 'sighalt'

pyhooker.register(ICar, Car)
pyhooker.register(IEngine, OttoEngine)
pyhooker.register(IWheel, MichelinWheel)

driver = Driver()

print("The driver is %s\n"
      "... with its car %s\n"
      "... and engine %s\n"
      "... and wheel type %s" % (driver,
                                 driver.car,
                                 driver.car.engine,
                                 driver.car.wheel_type))
