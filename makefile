-include options.mk
python = python2

.PHONY: test

test:
	PYTHONPATH=$(hayaku_path):. $(python) templates_test.py
#	PYTHONPATH=$(hayaku_path):. $(python) css_dict_test.py
