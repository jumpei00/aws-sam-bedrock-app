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
	cp -r shared layer/python/
	pip install -r layer/python/shared/requirements.txt -t layer/python/