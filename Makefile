add:
	poetry add $(package)
dev-add:
	poetry add $(package) --dev
install:
	poetry install
shell:
	poetry shell