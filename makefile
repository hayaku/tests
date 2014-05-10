-include options.mk
python = python2

tests := $(patsubst %_test.py,%.log,$(wildcard *_test.py))

all : $(tests)
	rm *.log

$(tests): %.log: %_test.py
	PYTHONPATH=$(hayaku_path):. $(python) $(shell find . -name $<)
	touch $@

.PHONY : all
