from .interfaces import ICar, IWheel, IEngine
import pyhooker

__author__ = 'sighalt'


class Car(ICar):
    @pyhooker.inject_params(engine=IEngine, wheel_type=IWheel)
    def __init__(self, engine, wheel_type):
        self.engine = engine
        self.wheel_type = wheel_type
