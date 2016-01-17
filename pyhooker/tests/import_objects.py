__author__ = 'sighalt'


package_var = object()

def package_function():
    return package_function


class PackageClass(object):
    class_var = object()

    def class_method(self):
        return self.class_method

    class WrappedClass(object):
        pass

