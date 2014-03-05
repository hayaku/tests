.PHONY: test

test:
	PYTHONPATH=. python ./test/templates_test.py
	PYTHONPATH=. python ./test/css_dict_test.py
	PYTHONPATH=. python ./test/segmentation_test.py
