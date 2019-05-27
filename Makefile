.PHONY: requirements clean migrate

define PROJECT_HELP_MSG

Usage:
    make help                   	show this message
    make clean                  	remove intermediate files

    make requirements 		 	install dev requirements
    make requirements_live 		install live requirements

    make migrate 			run migrate on dev environment
    make migrate_live			run migrate on live environment

endef
export PROJECT_HELP_MSG

help:	# Show help message
	echo "$$PROJECT_HELP_MSG"

requirements: # Install dev requirements
	pip install -r requirements/dev.txt

requirements_live: # Install live requirements
	pip install -r requirements/base.txt

clean:
	find . -name "*.pyc" -print0 | xargs -0 rm -rf
	-rm -rf htmlcov
	-rm -rf .coverage
	-rm -rf build
	-rm -rf dist
	-rm -rf src/*.egg-info

migrate: # Run migrate on dev environment
	. pyenv/bin/activate; \
	python src/manage.py migrate

migrate_live: # Run migrate on dev environment
	. pyenv/bin/activate; \
	python src/manage.py migrate --settings=djlibrary.settings.live
