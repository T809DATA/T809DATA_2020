# Best Practices
To give you a slight head start for the course we have compiled a small document about best practices when it
comes to solving home assignments.

The assignments in the course are computer assignments and require at least some foundational knowledge in Python.
All the assignments are written for Python. Importantly, we will be using the Scikit-Learn Python package a lot.
We recommend using virtual environments (see below) for this. We furthermore recommend using Visual Studio Code (VS code)
as a text editor for the course. If you are more familiar with other text editors (e.g. PyCharm, Atom, vi, etc) feel free to
choose the tool you are most comfortable with.

## Scikit-learn
Scikit-learn is a very powerful machine learning toolkit and our aim is to learn how to use it and apply to real datasets.  There is only one caveat:
In connecting the theory of machine learning with practice, it is important that you get to implement to core algorithms yourself.  This is hard to do in scikit-learn since the algorithms themselves are well encapsulated in the toolbox.  We will therefore have some parts of the computer exercises where we work with the data straight with Numpy.

## Virtual Environments
We will use virtual environments to encapsulate specific python requirements from system wide requirements.
All the code in this repository is written in Python 3. To create a Python 3 virtual environment, do:
* Create the virtual environment with one of the following:
    * macOS/Linux: `python3 -m venv .env` or `virtualenv -p python3 ..env`
    * Windows: `python -m venv ./env` or `py -3 -m venv .env`
* Activate it with `source ./env/bin/activate` if you are in the project directory. Otherwise you do `source /path/to/your/environment/bin/activate`.

You can however use Python in any way you see fit and perhaps you may have all the requirements already installed system wide.

Once you have activated your virtual environment you can install requirements with e.g.: `pip install scikit-learn`.
To verify that you have installed the package you can do `pip list` to see all installed requirements in the virtual environment.

## VS Code
[VS Code](https://code.visualstudio.com/) is an open source text editor from Microsoft. It is supported on Windows,
Debian and MacOS. We recommend using it in the course.

To get the best experience make sure that your VS Code workspace is using the correct Python interpreter. If you are using a virtual environment then the workspace setting `python.pythonPath` has to be set to `/path/to/venv/bin/python`. Normally VS Code takes care of doing this for you by recognizing that there is a virtual environment in the workspace. If not:
* Make sure you have the VSC Python extension installed (search for `ms-python.python` in the extension search)
* Press the settings cog in the bottom left inside VSC and select `settings`.
* Select `Workspace`
* search for `pythonpath` and edit the value to point to your python interpreter as explained above.

You can read a more detailed document about python environments in VSC [here](https://code.visualstudio.com/docs/python/environments).

### VS Code extensions to install:
Either click the extension button on the left side in VS Code (`ctrl`+`shift`+`X`) then search and install the following extensions:
* ms-python.python
* koehlma.markdown-math


## Notebooks or not?
We have decided that all code should be turned in in normal `.py` files. This simplifies things a lot for us. Some of you might feel more comfortable with using notebooks and thats fine! If that's the case, do the following:
1. In VS Code, create a new `.ipynb` file for your notebook. The editor will ask you to install a package to edit and read notebook files. After that you can read and write notebooks in your editor
2. After finishing the assignments, port over your solution to the included `template.py` file. This will be the file you turn in.


## Git
All the assignments will be periodically released in a Github repository which we will share with you later on. I would recommend forking this
repository before starting your work. By doing that you could easily version control your own work throughout the course. The repository is a
work in progress so when important changes are made, follow [this](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork)
to update your fork according to the upstream.

This only applies if you care to keep your code in the assignment repository. You could just as well version control your code in a different repository and
then you don't have to worry about re-forking the master repository.