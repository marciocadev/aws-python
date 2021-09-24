from lambda_fns.lambda1 import handler
from unittest import TestCase


class TestLambda1(TestCase):
    
    def test_lambda1(self):
        result = handler({}, {})
        self.assertDictEqual(result, {"statusCode": 200})