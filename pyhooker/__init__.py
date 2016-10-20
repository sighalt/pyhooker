import logging
from functools import wraps
from copy import deepcopy
from pyhooker.func_utils import build_extensive_kwargs
from pyhooker.loading import load_obj

__author__ = 'sighalt'


logger = logging.getLogger(__name__)
_registry = {}


def register(interface, implementation, auto_load=False, call=True):
    """Register an `interface` with it's concrete `implementation`.

    If the `implementation` is a dotted path to a python object you can enable
    auto loading of it with `auto_load`.

    e.g.:

        >>> import pyhooker
        >>> pyhooker.register("datetime", "datetime.datetime",
        ... auto_load=True)

    .. note::
        Pyhooker tries to call the `implementation` before storing it in the
        registry.

        This has to be done to allow convenient work with classes.

        However you can disable this behaviour by providing call=False as
        argument.

    """
    if auto_load:
        implementation = load_obj(implementation)

    if call and callable(implementation):
        implementation = implementation()

    _registry[interface] = implementation


def unregister(interface):
    try:
        del _registry[interface]
    except KeyError:
        logger.error("Could not unregister interface '%s' because it isn't already registered." % interface)


def get_implementation(interface):
    try:
        return _registry[interface]
    except KeyError:
        logger.critical("Could not get implementation '%s' because it is not registered." % interface)
        raise NotImplementedError("Interface '%s' is not registered" % interface)


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
