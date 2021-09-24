from aws_cdk import (
    Stack,
    aws_lambda as _lambda
)
from constructs import Construct

class ExampleTestStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda1 = _lambda.Function(
            scope=self,
            id="test-lambda",
            function_name="test-lambda",
            code=_lambda.Code.from_asset("lambda_fns"),
            handler="lambda1.handler",
            runtime=_lambda.Runtime.PYTHON_3_9
        )
