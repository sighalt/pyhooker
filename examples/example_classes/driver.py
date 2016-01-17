from .interfaces import ICar
import pyhooker

__author__ = 'sighalt'


class Driver(object):
    @pyhooker.inject_params(car=ICar)
    def __init__(self, car):
        self.car = car
