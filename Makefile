add:
	poetry add $(package)
dev-add:
	poetry add $(package) --dev
update:
	poetry update $(package)
delete:
	poetry remove $(package)
install:
	poetry install
shell:
	poetry shell
test:
	poetry run pytest tests/unit
validate:
	sam validate
generate-layer:
	cp -r shared layer/
	mv layer/shared/requirements.txt layer/
start-api:
	sam local start-api --port=3000