import json

from functions.hello import app


def test_lambda_handler(apigw_event, lambda_context):

    ret = app.lambda_handler(apigw_event, lambda_context)
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "message" in ret["body"]
    assert data["message"] == "Hello, World!!"
