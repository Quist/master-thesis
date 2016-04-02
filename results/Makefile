all : parse function_test_rest los_test satellite_test

function_test_rest:
	$(MAKE) -C function_tests/rest

los_test:
	$(MAKE) -C los/rest

satellite_test:
	$(MAKE) -C satellite/rest && $(MAKE) -C satellite/nffi

parse:
	python parse.py
