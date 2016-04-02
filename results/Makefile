all : parse function_test_rest satellite_test

function_test_rest: parse
	$(MAKE) -C function_tests/rest

satellite_test:
	$(MAKE) -C satellite/rest && $(MAKE) -C satellite/nffi

parse:
	python parse.py
