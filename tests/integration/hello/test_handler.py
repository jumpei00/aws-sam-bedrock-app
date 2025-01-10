import requests


class TestHelloIntegration:
    def test_api_gateway(self, api_gateway_url):
        response = requests.get(api_gateway_url + "/hello")

        assert response.status_code == 200
        assert response.json() == {"message": "hello world"}
