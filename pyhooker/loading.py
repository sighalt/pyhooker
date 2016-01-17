import importlib

__author__ = 'sighalt'

PATH_SEPARATOR = "."


def get_deepest_module(dotted_path):
    path_parts = dotted_path.split(PATH_SEPARATOR)
    first_i = -1
    last_i = (len(path_parts) - 1) * -1

    for i in range(first_i, last_i, -1):
        deepest_module_path = PATH_SEPARATOR.join(path_parts[:i])
        remainging_path = PATH_SEPARATOR.join(path_parts[i:])

        try:
            deepest_module = importlib.import_module(deepest_module_path)
            break
        except ImportError:
            continue
    else:
        raise ImportError("Could not import by dotted path '%s'" % dotted_path)

    return deepest_module, remainging_path


def load_obj(dotted_path):

    try:
        return importlib.import_module(dotted_path)
    except ImportError:
        module, remaining_path = get_deepest_module(dotted_path)
        attribute_holder = module

        for attr in remaining_path.split(PATH_SEPARATOR):
            attribute_holder = getattr(attribute_holder, attr)

        return attribute_holder
