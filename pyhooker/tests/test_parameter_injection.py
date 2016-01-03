from unittest import TestCase
import pyhooker
from pyhooker.tests.classes import TestInterface, TestImplementation1

__author__ = 'sighalt'


class TestParameterInjection(TestCase):

    def setUp(self):
        pyhooker._registry = {}
        self.test_interface = TestInterface
        self.test_implementation_1 = TestImplementation1
        pyhooker.register(self.test_interface, self.test_implementation_1)

    @pyhooker.inject_params(implementation=TestInterface)
    def test_valid_parameter_injection(self, implementation):
        self.assertIsInstance(implementation, self.test_interface)

    def test_typeerror_on_non_existent_parameter_injection(self):
        with self.assertRaises(TypeError):
            self.non_existent_parameter_injection()

    @pyhooker.inject_params(implementation=TestInterface)
    def non_existent_parameter_injection(self):
        pass

    def test_overwrite_injected_parameter(self):
        test_object = object()
        self.assert_equal_after_injection(injected=test_object, expected=test_object)

    def test_overwrite_injected_parameter_via_args(self):
        """
        Test if we can overwrite an injected parameter with the args instead of kwargs argument.
        """
        test_object = object()
        self.assert_equal_after_injection(test_object, expected=test_object)

    @pyhooker.inject_params(injected=TestInterface)
    def assert_equal_after_injection(self, injected, expected):
        self.assertEqual(injected, expected)
