import pyhooker
from pyhooker.tests import import_objects
from unittest.case import TestCase

__author__ = 'sighalt'


class ImportTest(TestCase):

    def imported_id_of(self, dotted_path):
        imported_object = pyhooker.load_obj(dotted_path)

        return id(imported_object)

    def test_import_of_package_var(self):
        expected_id = id(import_objects.package_var)
        import_path = "pyhooker.tests.import_objects.package_var"
        imported_id = self.imported_id_of(import_path)

        self.assertEqual(imported_id, expected_id)

    def test_import_of_package_function(self):
        expected_id = id(import_objects.package_function)
        import_path = "pyhooker.tests.import_objects.package_function"
        imported_id = self.imported_id_of(import_path)

        self.assertEqual(imported_id, expected_id)

    def test_import_of_package_class(self):
        expected_id = id(import_objects.PackageClass)
        import_path = "pyhooker.tests.import_objects.PackageClass"
        imported_id = self.imported_id_of(import_path)

        self.assertEqual(imported_id, expected_id)

    def test_import_of_class_var(self):
        expected_id = id(import_objects.PackageClass.class_var)
        import_path = "pyhooker.tests.import_objects.PackageClass.class_var"
        imported_id = self.imported_id_of(import_path)

        self.assertEqual(imported_id, expected_id)

    def test_import_of_class_method(self):
        expected_id = id(import_objects.PackageClass.class_method)
        import_path = "pyhooker.tests.import_objects.PackageClass.class_method"
        imported_id = self.imported_id_of(import_path)

        self.assertEqual(imported_id, expected_id)

    def test_import_of_wrapped_class(self):
        expected_id = id(import_objects.PackageClass.WrappedClass)
        import_path = "pyhooker.tests.import_objects.PackageClass.WrappedClass"
        imported_id = self.imported_id_of(import_path)

        self.assertEqual(imported_id, expected_id)
