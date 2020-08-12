# T-809-DATA exercises

This repository contains excercises and supporting code for the course T-809-DATA at Reykjavik University. The assignments in the course are computer assignments and require at least some foundational knowledge in Python. All the assignments are written for Python and together require only one _virtual environment_ for requirements. See the installation section for more information on that and best practices.

Right now, this repository is **a Work In Progress (wip)**.

## Modules
The repository contains the following modules (modules will be added during the semester):
* Assignment 0: [Introduction](00_introduction/README.md)


## Installation

### Installing Requirements
All the code in this repository is written in Python 3. The recommended approach is to create a python virtual environment:
* Create the virtual environment with one of the following:
    * macOS/Linux: `python3 -m venv .env` or `virtualenv -p python3 ..env`
    * Windows: `python -m venv ./env` or `py -3 -m venv .env`
* Activate it with `source ./env/bin/activate` if you are in the project directory. Otherwise you do `source /path/to/your/environment/bin/activate`.

You can however use Python in any way you see fit and perhaps you may have all the requirements already installed system wide.

Install Python requirements with `pip install -r requirements.txt`. You can of course install any additional python requirements using `pip`, just make sure you have your virtual environment activated when you do.

## Using VS Code + Python (Optional)
To get the best experience make sure that your VS Code workspace is using the correct Python interpreter. If you are using a virtual environment then the workspace setting `python.pythonPath` has to be set to `/path/to/venv/bin/python`. Normally VS Code takes care of doing this for you by recognizing that there is a virtual environment in the workspace. If not:
* Make sure you have the VSC Python extension installed (search for `ms-python.python` in the extension search)
* Press the settings cog in the bottom left inside VSC and select `settings`.
* Select `Workspace`
* search for `pythonpath` and edit the value to point to your python interpreter as explained above.

You can read a more detailed document about python environments in VSC [here](https://code.visualstudio.com/docs/python/environments).


## Using this repository
Assignments are seperated into folders. Each assignment folder contains the following files:
* `README.md`: The assignment description. For the best experience, open the file in VSC and press either `ctrl`+`K` `V` or the small magnifier glass icon on the right side in the header to _Open preview to the side_.
* `template.py`: Contains a template for you to fill in with your own code. This is the file to submit.
* `template.ipynb` The same as `template.py` but in a notebook format. __This file should not be turned in__.

Each directory might also contain:
* `example.py`: Example code that is relevant to the assignment. Examples from this file are often referenced from the `README.md`
* `tools.py` : Sometimes we supply some helper functions for you to use. They will be found in this file.
* Directories that contain image, text or any other type of data relevant to the assignment.

## How to turn in the assignments
All your code should be turned in as a python script, i.e.
* A single file with a `.py` ending. Although you can use the `template.ipynb` notebook in your development and then port your code over to `template.py` if that suits you.
* The file should contain all the functions with **exactly** the same function names as listed in the assignment description below
* Use the supplied `template.py` file to fill in your code
* Plots should be turned in as well. The naming convention for submitted plots is as follows: The Z-th plot under Part X.Y should be turned in as `X_Y_Z.png`
* Store your plots in a seperate directory called `plots`
* Turn these files in as a `.zip` file.



