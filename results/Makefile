all : parse function_test_rest los_test wifi_one satellite_test 

wifi_one:
	$(MAKE) -C wifi1/rest

function_test_rest:
	$(MAKE) -C function_tests/rest

los_test:
	$(MAKE) -C los/rest

satellite_test:
	$(MAKE) -C satellite/rest && $(MAKE) -C satellite/nffi

parse:
	python parse.py
