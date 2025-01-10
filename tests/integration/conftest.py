import boto3
import pytest


@pytest.fixture(scope="session")
def api_gateway_url(config):
    if config["environment"] == "dev":
        return config["api_gateway"]["base_url"]

    stack_name = config["stack_name"]
    client = boto3.client("cloudformation", region_name=config["region"])

    try:
        response = client.describe_stacks(StackName=stack_name)
    except Exception as e:
        raise Exception(
            f"Cannot find stack {stack_name} \n"
            f'Please make sure a stack with the name "{stack_name}" exists'
        ) from e

    stack_outputs = response["Stacks"][0]["Outputs"]
    api_outputs = [
        output for output in stack_outputs if output["OutputKey"] == "APIGateway"
    ]

    if not api_outputs:
        raise KeyError(f"HelloWorldAPI not found in stack {stack_name}")

    return api_outputs[0]["OutputValue"]
