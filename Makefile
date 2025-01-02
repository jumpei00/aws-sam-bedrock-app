add:
	poetry add $(package)
dev-add:
	poetry add $(package) --dev
install:
	poetry install
shell:
	poetry shell
generate-types:
	poetry run python scripts/generate_types.py
test:
	poetry run pytest tests/unit
validate:
	sam validate
generate-layer:
	mkdir -p layer/python/shared/
	cp -r shared/* layer/python/shared/