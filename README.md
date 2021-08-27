# AQA Sandbox

Sandbox project to practice Automation Testing.

---

---

## Requirements
* `Python3.8` or higher - https://www.python.org/
* `virtualenv` - https://pypi.org/project/virtualenv/

---

---

## Project initialization

---

### Ubuntu / MacOS
Use `Make` file from project. 

Just `cd` to the project folder and run `make` command. It will show help message with available commands.

> `make install` - for creating virtual environment and installing all dependencies.
>
> `make test` - to run all the tests.

---

### Windows

Sorry, but you have to install environment manually =,(

In the command line `cd` to the project folder.

> `python3 -m venv .venv` - to create virtual environment
> 
> `python3 -m venv .venv` - to create virtual environment 
>
> `.\venv\Scripts\activate` - to activate virtual environment
>
> `pip install poetry` - to install python package manager
>
> `poetry install` - to install all the dependencies.

---

---

## PyCharm settings

Set Python interpreter from installed .venv
> * Open `settings -> project -> python interpreter`
> 
> * Open dropdown
> 
> * Select `Show all`
> 
> * Hit `+` to add new interpreter
> 
> * Pick `Existing environment`
> 
> * Hit `...` to select folder and select installed interpreter `PROJECT_PATH/.venv/bin/python`

Set testrunner
> * Open `settings -> Tools -> python integrated tools -> Testing` and select `pythest` from dropdown

Prevent pytest cache folder creation
> In run/debug configuration `Edit configuration templates -> python tests -> pytest` add to Additional Arguments `-p no:cacheprovider`

---

---

