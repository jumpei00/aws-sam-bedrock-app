from datamodel_code_generator import InputFileType, generate
from pathlib import Path


def generate_types():
    input_path = Path("openapi/schema.yaml")
    output_dir = Path("shared/types")
    output_file = output_dir / "models.py"

    generate(
        input_=input_path,
        input_file_type=InputFileType.OpenAPI,
        output=output_file,
    )


if __name__ == "__main__":
    generate_types()
