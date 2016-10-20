from __future__ import print_function
from example_classes.interfaces import ICar, IEngine, IWheel
from example_classes.driver import Driver
import pyhooker

__author__ = 'sighalt'

pyhooker.register(ICar, "example_classes.car.Car", auto_load=True)
pyhooker.register(IEngine, "example_classes.engine.OttoEngine", auto_load=True)
pyhooker.register(IWheel, "example_classes.wheel.MichelinWheel", auto_load=True)

driver = Driver()

print("The driver is %s\n"
      "... with its car %s\n"
      "... and engine %s\n"
      "... and wheel type %s" % (driver,
                                 driver.car,
                                 driver.car.engine,
                                 driver.car.wheel_type))
