import json
from typing import Dict, Any
from shared.types.models import Hello


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    try:
        response = Hello(message="hello world!!!!")
        return {"statusCode": 200, "body": json.dumps(response.model_dump())}
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps(
                {
                    "error": json.dumps(str(e)),
                }
            ),
        }
