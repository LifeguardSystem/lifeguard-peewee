deps:
	pip3 install -r requirements.txt
	pip3 install -r requirements.dev.txt

test:
	nose2 -v --with-coverage --coverage-report html --coverage-report term

black:
	black lifeguard_peewee
	black tests

clean:
	find . -iname "*.pyc" | xargs rm
