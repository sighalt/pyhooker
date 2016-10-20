.. pyhooker documentation master file, created by
   sphinx-quickstart on Fri Sep  2 14:59:09 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pyhooker's documentation!
====================================

Pyhooker intends to be a lightweight and easy-to-use dependency injection library.
It basically consists of the following two bricks.

DI-Container
------------

The dependency injection container manages all registered implementations for
the user. To add a class/object/... to the DI-container pyhooker provides the
`register` method.

.. autofunction:: pyhooker.register

Acessing the registry
---------------------

For accessing pyhooker's registry you can chose one of the following ways:

via decorator
'''''''''''''

This is the recommended way to use pyhooker. The `inject_params` decorator can
be used to inject parameters into your callables. On each call of the decorated
function or method pyhooker will lookup if the parameter to inject is already
given in the arguments (or keyword arguments) and will inject the registered
value if it doesn't find it there.

.. code-block:: python

   >>> import pyhooker
   >>> @pyhooker.inject_params(config="config")
   ... def get_current_version(config):
   ...   return config["version"]
   ...
   >>> init({"version": (1, 2, 3)}) # will not use the registry
   (1, 2, 3)
   >>> init() # will lookup the config in registry
   NotImplementedError: Interface 'config' is not registered



via function
''''''''''''

Of course you can also access the registered objects by function. Pyhooker
provides the `get_implementation` function for that.

.. code-block:: python

   >>> import pyhooker
   >>> pyhooker.register("config", dict(version=(3, 2, 1)))
   >>> pyhooker.get_implementation("config")
   (3, 2, 1)



Usage
-----

.. code-block:: python

   >>> import pyhooker
   >>> pyhooker.register("config", dict)

The `dict` class is now registered in pyhookers registry, and can easily be used
in your code to read and manipulate it.

.. code-block:: python

   >>> @pyhooker.inject_params(config="config")
   ... def init(config):
   ...   config["version"] = (3, 2, 1)
   ...
   >>> @pyhooker.inject_params(config="config")
   ... def get_current_version(config):
   ...   return config["version"]
   ...
   >>> init()
   >>> get_current_version()
   (3, 2, 1)

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

