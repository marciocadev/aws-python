import aws_cdk as cdk
from example_test.example_test_stack import ExampleTestStack
import pytest
from unittest import TestCase


class TestLambda(TestCase):

    @pytest.fixture(autouse=True)
    def init(self):
        # GIVEN
        self.app = cdk.App()
        # WHEN
        ExampleTestStack(scope=self.app, construct_id="Test")
        # THEN
        self.template = self.app.synth().get_stack_by_name("Test").template
        self.functions = [ \
            resource for resource in self.template['Resources'].values() \
            if resource['Type'] == 'AWS::Lambda::Function']

    def test_lambda_count(self):
        self.assertEqual(len(self.functions), 1)

    def test_lambda_name(self):
        for funtion in self.functions:
            if funtion['Properties']['FunctionName'] == 'test-lambda':
                assert True
                return
        assert False
