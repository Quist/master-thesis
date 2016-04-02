all : parse function_test_rest satellite_test_rest

function_test_rest: parse
	$(MAKE) -C function_tests/rest

satellite_test_rest:
	$(MAKE) -C satellite/rest

parse:
	python parse.py
