ROOT_DIR = ${PWD}

help:	## Show this help.
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

migration_generate:	## Generate the migration file.
	poetry run alembic revision --autogenerate -m "$(m)"

migration_apply:	## Apply the HEAD migration to the DB.
	poetry run alembic upgrade head

generate_requirements:	## Generate the requirement of project.
	poetry run sh gen_requirements.sh

run_dev:	## Run FastAPI with uvicorn server.
	poetry run uvicorn src.api:app --reload

run_tests:	## Run all Pytest tests.
	poetry run pytest

pyright:	## Run pyright check.
	poetry run pyright .

before_commit:	## Run pyright, update requirements/* and run tests.
	echo `--- [ RUN PYRIGHT ] ---` && make pyright && \
	echo '--- [ RUN TESTS ] ---' && make run_tests && \
	echo '--- [ GENERATE REQUIREMENTS ] ---' && make generate_requirements