import logging
from functools import wraps
from copy import deepcopy
from pyhooker.func_utils import build_extensive_kwargs

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
        raise NotImplementedError("Interface '%s' is not registered" % interface)
    else:
        if callable(obj):
            return obj()
        else:
            return obj


def inject_params(**injected_parameters):
    """
    Inject the parameters given in params/kwargs

    :param injected_parameters: the paramters to inject in the form {"parameter_name": InterfaceClass}
    :return: the decorator function
    """

    def decorator(obj):
        """
        The decorator for the object, since decorators take just one argument.

        :param obj: the decorated object
        :return: the wrapped object
        """

        @wraps(obj)
        def wrapper(*args, **kwargs):
            """
            Wraps the object and inject the parameters given in params into the kwargs if they are not set.

            :param args: arguments
            :param kwargs: keyword arguments
            :return: whatever obj return
            """
            kwargs_to_inject = deepcopy(injected_parameters)
            final_kwargs = build_extensive_kwargs(obj, args, kwargs)

            for parameter_to_inject, interface in kwargs_to_inject.items():

                if parameter_to_inject not in final_kwargs:
                    final_kwargs[parameter_to_inject] = get_implementation(interface)

            return obj(**final_kwargs)

        return wrapper

    return decorator
