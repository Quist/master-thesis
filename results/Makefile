all : parse function_test_rest los_test wifi_one wifi_two cnr_test satellite_test

wifi_one:
	$(MAKE) -C wifi1/rest

cnr_test:
	$(MAKE) -C cnr/rest && $(MAKE) -C cnr/nffi

wifi_two:
	$(MAKE) -C wifi2/rest && $(MAKE) -C wifi2/nffi

function_test_rest:
	$(MAKE) -C function_tests/rest

los_test:
	$(MAKE) -C los/rest

satellite_test:
	$(MAKE) -C satellite/rest && $(MAKE) -C satellite/nffi

parse:
	python parse.py
