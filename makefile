-include options.mk
python = python2

.PHONY: test segmentation_test

test: segmentation_test
	PYTHONPATH=$(hayaku_path):. $(python) templates_test.py
	PYTHONPATH=$(hayaku_path):. $(python) css_dict_test.py

segmentation_test:
	PYTHONPATH=$(hayaku_path):. $(python) segmentation_test.py
