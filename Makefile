## -----------------------------------------------------------------------
## This Makefile contains a targets for test framework installation, development and running.
## Available targets listed below:
## -----------------------------------------------------------------------

# Versions
PYTHON_MINIMAL_VERSION = 3.8

# Paths
CUR_PATH = $(shell pwd)
ALLURE_PATH = $(CUR_PATH)/allure_report
VIRTUAL_ENV ?= $(CUR_PATH)/.venv
VENV_ACTIVATE = $(VIRTUAL_ENV)/bin/activate

# Check Python
PYTHON_MINIMAL_MAIN_VERSION = $(shell echo $(PYTHON_MINIMAL_VERSION) | cut -f1 -d.)
PYTHON_MINIMAL_MAJ_VERSION = $(shell echo $(PYTHON_MINIMAL_VERSION) | cut -f2 -d.)
PYTHON_CUR_VERSION = $(strip $(shell python3 -V 2>&1 | grep -Po '(?<=Python )(.+)'))
PYTHON_CUR_MAIN_VERSION = $(shell echo $(PYTHON_CUR_VERSION) | cut -f1 -d.)
PYTHON_CUR_MAJ_VERSION = $(shell echo $(PYTHON_CUR_VERSION) | cut -f2 -d.)
CHECK_PYTHON_VERSION := $(shell [ $(PYTHON_CUR_MAIN_VERSION) -ge $(PYTHON_MINIMAL_MAIN_VERSION) -a $(PYTHON_CUR_MAJ_VERSION) -ge $(PYTHON_MINIMAL_MAJ_VERSION) ] && echo true)

# Other
SHELL = /bin/bash

# Update PATH to work via virtual environment
export PATH := $(VIRTUAL_ENV)/bin:$(PATH)

all: help


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Help
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Check if virtual environment exist
$(VENV_ACTIVATE):
ifeq ($(CHECK_PYTHON_VERSION), )
	$(error [ERROR] Python$(PYTHON_MINIMAL_VERSION) or higher expected!)
endif
	python3 -m venv $(VIRTUAL_ENV)

## help                 : Show this message
help: Makefile
	@sed -n 's/^##//p' $<

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Targets
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

## install              : Install requirements
install: $(VENV_ACTIVATE)
	pip install poetry
	poetry config virtualenvs.create false
	poetry install


## test                 : Run pytest
test: clear-allure-report
	pytest tests --alluredir=$(ALLURE_PATH) -p no:cacheprovider

## allure-report        : Generate and open HTML allure report in GoogleChrome
allure-report:
	allure generate $(ALLURE_PATH) --report-dir $(ALLURE_PATH)/html
	google-chrome --disable-web-security --user-data-dir="$(ALLURE_PATH)/chrome_files" $(ALLURE_PATH)/html/index.html

## clear-allure-report  : Remove all files form ./allure_report folder
clear-allure-report:
	rm -rf $(ALLURE_PATH)/*

## black                : Style code with Black
black:
	cd $(CUR_PATH) && black . --line-length 120


## black-diff           : Show code style diff with colored diff
black-diff:
	cd $(CUR_PATH) && black . --line-length 120 --diff --color

## -----------------------------------------------------------------------
