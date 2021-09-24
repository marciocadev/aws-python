import aws_cdk as cdk
from example_test.example_test_stack import ExampleTestStack
from unittest import TestCase


class TestLambdas(TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        # GIVEN
        cls.app = cdk.App()
        # WHEN
        ExampleTestStack(scope=cls.app, construct_id="Test")
        # THEN
        cls.template = cls.app.synth().get_stack_by_name("Test").template
        cls.functions = [ \
            resource for resource in cls.template['Resources'].values() \
            if resource['Type'] == 'AWS::Lambda::Function']

    def test_lambda_count(self):
        self.app = cdk.App()
        ExampleTestStack(scope=self.app, construct_id="Test")
        self.template = self.app.synth().get_stack_by_name("Test").template
        self.functions = [ \
            resource for resource in self.template['Resources'].values() \
            if resource['Type'] == 'AWS::Lambda::Function']
        self.assertEqual(len(self.functions), 1)

    def test_lambda_name(self):
        for funtion in self.functions:
            if funtion['Properties']['FunctionName'] == 'test-lambda':
                assert True
                return
        assert False
