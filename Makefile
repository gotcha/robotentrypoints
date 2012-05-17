#!/usr/bin/make
#
options =

.PHONY: cleanall test

BUILDOUT_FILES = buildout.cfg setup.py bin/buildout

DATA_FS = var/filestorage/Data.fs

all: pybot

bin/python:
	virtualenv-2.6 --no-site-packages .

develop-eggs: bin/python bootstrap.py buildout.cfg
	./bin/python bootstrap.py

bin/buildout: develop-eggs

bin/pybot: $(BUILDOUT_FILES)
	./bin/buildout -Nvt 5 install robot
	touch $@

bin/test: $(BUILDOUT_FILES)
	./bin/buildout -Nvt 5 install test
	touch $@

cleanall:
	rm -fr bin develop-eggs downloads eggs parts .installed.cfg

test: bin/test	
	./bin/test

pybot: bin/pybot	
	./bin/pybot
