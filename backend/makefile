ROOT_DIR = ${PWD}

help:	## Show this help.
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

migration_generate:	## Generate the migration file.
	poetry run alembic revision --autogenerate -m "$(m)"

migration_apply:	## Apply the HEAD migration to the DB.
	poetry run alembic upgrade head

requirements_generation:	## Generate the requirement of project.
	poetry run sh gen_requirements.sh

run_dev:	## Run FastAPI with uvicorn server.
	poetry run uvicorn src.api:app --reload