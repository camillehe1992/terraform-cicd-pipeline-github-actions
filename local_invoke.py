# pylint: disable=wrong-import-position
# pylint: disable=unused-import
# pylint: disable=wrong-import-order
import json
from dotenv import load_dotenv

load_dotenv(override=True)
from aws_lambda_powertools.utilities.typing import LambdaContext

from frontend.app import main


def get_mock_lambda_context():
    context = LambdaContext()
    context._function_name = "test"
    context._memory_limit_in_mb = "test"
    context._invoked_function_arn = "test"
    context._aws_request_id = "test"
    return context


def test_frontend_lambda_function(path) -> dict:
    with open(path, encoding="utf-8") as my_file:
        response = main.lambda_handler(
            json.loads(my_file.read()), get_mock_lambda_context()
        )
        return json.loads(response["body"])


if __name__ == "__main__":
    # files = os.listdir("tests/data/")
    files = ["get_pet_by_id.json"]
    for file in files:
        print(
            f"\n************************************************** {file} ****************************************************\n"
        )
        filepath = f"tests/data/{file}"
        result = test_frontend_lambda_function(filepath)
        print(result)
