import logging
from copy import deepcopy

__author__ = 'sighalt'


logger = logging.getLogger(__name__)
_registry = {}


def register(interface, implementation):
    _registry[interface] = implementation


def unregister(interface):
    try:
        del _registry[interface]
    except KeyError:
        logger.error("Could not unregister interface '%s' because it isn't already registered." % interface)


def get_implementation(interface):
    try:
        obj = _registry[interface]
    except KeyError:
        logger.critical("Could not get implementation '%s' because it is not registered." % interface)
        raise Exception("Interface '%s' is not registered" % interface)
    else:
        return obj() if callable(obj) else obj


def inject_params(**params):
    """
    Inject the parameters given in params/kwargs

    :param params: the paramters to inject in the form {"parameter_name": InterfaceClass}
    :return: the decorator function
    """

    def decorator(obj):
        """
        The decorator for the object, since decorators take just one argument.

        :param obj: the decorated object
        :return: the wrapped object
        """

        def wrapper(*args, **kwargs):
            """
            Wraps the object and inject the parameters given in params into the kwargs if they are not set.

            :param args: arguments
            :param kwargs: keyword arguments
            :return: whatever obj return
            """
            nonlocal params
            defaults = deepcopy(params)
            defaults = {param_name: get_implementation(interface) for param_name, interface in defaults.items()}
            defaults.update(**kwargs)

            return obj(*args, **defaults)

        return wrapper

    return decorator
