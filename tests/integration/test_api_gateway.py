import boto3
import pytest
import requests


class TestApiGateway:

    @pytest.fixture()
    def api_gateway_url(self):
        stack_name = "sam-bedrock-app"
        client = boto3.client("cloudformation", region_name="ap-northeast-1")

        try:
            response = client.describe_stacks(StackName=stack_name)
        except Exception as e:
            raise Exception(
                f"Cannot find stack {stack_name} \n"
                f'Please make sure a stack with the name "{stack_name}" exists'
            ) from e

        stacks = response["Stacks"]
        stack_outputs = stacks[0]["Outputs"]
        api_outputs = [
            output for output in stack_outputs if output["OutputKey"] == "APIGateway"
        ]

        if not api_outputs:
            raise KeyError(f"HelloWorldAPI not found in stack {stack_name}")

        return api_outputs[0]["OutputValue"]

    def test_api_gateway(self, api_gateway_url):
        """Call the Hello API"""
        response = requests.get(api_gateway_url + "/hello")

        assert response.status_code == 200
        assert response.json() == {"message": "hello world"}
