import json
import os
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment to run tests against（dev/stg/prd）",
    )


def load_config(env):
    config_path = os.path.join(os.path.dirname(__file__), "config", f"{env}.json")
    with open(config_path, "r") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def environment(request):
    return request.config.getoption("--env")


@pytest.fixture(scope="session")
def config(environment):
    return load_config(environment)
