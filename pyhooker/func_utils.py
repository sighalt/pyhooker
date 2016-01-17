import sys
import inspect

__author__ = 'sighalt'


def build_extensive_kwargs(func, args, kwargs):
    """
    Return a dictionary of the merged args list and kwargs dictionary.

    This method will chose the right method of merging based on the python version.
    :rtype: dict
    """

    if sys.version_info >= (3, 3):
        return _build_extensive_kwargs_with_signature(func, args, kwargs)
    else:
        return _build_extensive_kwargs_with_getargspec(func, args, kwargs)


def _build_extensive_kwargs_with_signature(func, args, kwargs):
    """
    Return a dictionary of the merged args list and kwargs dictionary by using inspect.signature().

    This method only works in python >= 3.3.

    :rtype: dict
    """
    function_signature = inspect.signature(func)
    extensive_kwargs = function_signature.bind_partial(*args, **kwargs)

    return extensive_kwargs.arguments


def _build_extensive_kwargs_with_getargspec(func, args, kwargs):
    """
    Return a dictionary of the merged args list and kwargs dictionary by using inspect.getargspec().

    This method is deprecated in python >= 3.3.

    :rtype: dict
    """
    args = list(args)
    obj_arguments = inspect.getargspec(func).args
    extensive_kwargs = {}

    for argument_name in obj_arguments:
        try:
            # try to provide this argument from args
            extensive_kwargs[argument_name] = args.pop(0)
        except IndexError:
            # try to provide this argument from kwargs
            try:
                extensive_kwargs[argument_name] = kwargs[argument_name]
            except KeyError:
                continue

    return extensive_kwargs
