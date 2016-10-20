from unittest import TestCase
import pyhooker
from pyhooker.tests.classes import TestInterface, TestImplementation1, TestImplementation2

__author__ = 'sighalt'


class RegistryTest(TestCase):

    def setUp(self):
        self.registry = pyhooker._registry = {}
        self.test_interface = TestInterface
        self.test_implementation_1 = TestImplementation1
        self.test_implementation_2 = TestImplementation2

    def test_registry_is_initially_empty(self):
        self.assert_registry_length_equals(0)

    def test_standard_register_call(self):
        self.register_implementation_1()
        self.assert_registry_length_equals(1)

    def test_overwrite_registered_implementation(self):
        self.register_implementation_1()
        self.register_implementation_2()

        self.assert_registry_length_equals(1)
        implementation = pyhooker.get_implementation(self.test_interface)

        self.assertIsInstance(implementation, self.test_implementation_2)
        self.assertNotIsInstance(implementation, self.test_implementation_1)

    def test_unregister_of_registered_implementation(self):
        self.register_implementation_1()
        self.unregister_implementations()

        self.assert_registry_length_equals(0)

    def test_unregister_of_not_registered_implementation(self):
        self.unregister_implementations()
        self.assert_registry_length_equals(0)

    def test_get_registered_implementation_as_callable(self):
        self.register_implementation_1()
        implementation = pyhooker.get_implementation(self.test_interface)

        self.assertIsInstance(implementation, self.test_implementation_1)
        is_instantiated = (type(implementation) != type)
        assert is_instantiated

    def test_get_registered_implementation_as_scalar(self):
        test_string = "test_string"
        pyhooker.register(self.test_interface, test_string)

        implementation = pyhooker.get_implementation(self.test_interface)

        self.assertEqual(implementation, test_string)

    def test_get_not_registered_implementation(self):
        with self.assertRaises(NotImplementedError):
            pyhooker.get_implementation(self.test_interface)

    def assert_registry_length_equals(self, x):
        number_of_registered_implementations = len(self.registry)
        self.assertEqual(number_of_registered_implementations, x)

    def register_implementation_1(self):
        pyhooker.register(interface=self.test_interface,
                          implementation=self.test_implementation_1)

    def register_implementation_2(self):
        pyhooker.register(interface=self.test_interface,
                          implementation=self.test_implementation_2)

    def unregister_implementations(self):
        pyhooker.unregister(interface=self.test_interface)
