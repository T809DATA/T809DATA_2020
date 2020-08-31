# T-809-DATA exercises

This repository contains exercises and supporting code for the course T-809-SPST at Reykjavik University. The assignments in the course are computer assignments and require at least some foundational knowledge in Python. All the assignments are written for Python and together require only one _virtual environment_ for requirements. See the installation section for more information on that and best practices.


## Modules
The repository contains the followorkng modules:
* Assignment 0: [Introduction](00_introduction/README.md)
* Assignment 1: [Decision Trees](01_decision_trees/README.md)
* Assignment 2: [K-Nearest Neighbors](02_nearest_neighbours/README.md)
* Assignment 3: [Sequential Estimation](03_sequential_estimation/README.md)
* Assignment 4: [Classification Based on Probability](04_classification/README.md)
* Assignment 5: [The Back-propagation Algorithm](05_backprop/README.md)
* Assignment 6: [Applying Neural Networks](06_neural_networks/README.md)
* Assignment 7: [Linear Models For Regression](07_linear_models/README.md)
* Assignment 8: [Support Vector Machines](08_SVM/README.md)
* Assignment 9: [Random Forests](09_random_forests/README.md)
* Assignment 10: [Boosting](010_boosting/README.md)
* Assignment 11: [K-Means and Gaussian Mixtures](011_k_means/README.md)
* Assignment 12: [Principal Component Analysis](012_PCA/README.md)

## Installation

### Installing Requirements
All the code in this repository is written in Python and **requires Python 3.6.9+**. The recommended approach is to create a python virtual environment:
* Create the virtual environment with one of the following:
    * macOS/Linux: `python3 -m venv env` or `virtualenv -p python3 ..env`
    * Windows: `python -m venv ./env` or `py -3 -m venv .env`
    * Note: Make sure that `python3` or `python` points to Python3.7+ interpreter. You can run `python3 --version` to see which version you are running. All python installations should be listed by running e.g. `ls usr/bin/python`. You can also use VS Code to discover all python interpreters on your OS, see the next section.
* Activate it with `source /env/bin/activate` if you are in the project directory. Otherwise you do `source /path/to/your/environment/bin/activate`.

You can however use Python in any way you see fit and perhaps you may have all the requirements already installed system wide.

Install Python requirements with `pip install -r requirements.txt`. You can of course install any additional python requirements using `pip`, just make sure you have your virtual environment activated when you do.

## Using VS Code + Python (Optional)
To get the best experience make sure that your VS Code workspace is using the correct Python interpreter. If you are using a virtual environment then the workspace setting `python.pythonPath` has to be set to `/path/to/venv/bin/python`. Normally VS Code takes care of doing this for you by recognizing that there is a virtual environment in the workspace. If not:
* Make sure you have the VSC Python extension installed (search for `ms-python.python` in the extension search)
* Press the settings cog in the bottom left inside VSC and select `settings`.
* Select `Workspace`
* search for `pythonpath` and edit the value to point to your python interpreter as explained above.

You can additionally see in the bottom toolbar of VS Code which python interpreter is running (it should say e.g. `Python 3.6.9 64-bit ('env': virtualenv)`. By clicking that (or entering `ctrl`+`shift`+`p` and enter `python interpreter` in the prompt) you can select the python interpreter for the work space.

You can read a more detailed document about python environments in VSC [here](https://code.visualstudio.com/docs/python/environments).


## Using this repository
Assignments are separated into folders. Each assignment folder contains the following files:
* `README.md`: The assignment description. For the best experience, open the file in VSC and press either `ctrl`+`K` `V` or the small magnifier glass icon on the right side in the header to _Open preview to the side_.
* `template.py`: Contains a template for you to fill in with your own code. This is the file to submit.

Each directory might also contain:
* `example.py`: Example code that is relevant to the assignment. Examples from this file are often referenced from the `README.md`
* `tools.py` : Sometimes we supply some helper functions for you to use. They will be found in this file.
* Directories that contain image, text or any other type of data relevant to the assignment.

## How to turn in the assignments
All your code should be turned in as a python script, i.e.
* A single file with a `.py` ending. Although you can use a  notebook in your development and then port your code over to `template.py` if that suits you.
* The file should contain all the functions with **exactly** the same function names as listed in the assignment description below
* Use the supplied `template.py` file to fill in your code
* Plots should be turned in as well. The naming convention for submitted plots is as follows: The Z-th plot under Section X.Y should be turned in as `X_Y_Z.png`

## Bonus questions
Some assignments will have *bonus sections*. In those assignments, the assignment itself counts 80% towards the assignment grade and the bonus section 20%. The idea behind the bonus questions is to allow you to use your intuition to add relevant insight to your assignment without clear instructions. Examples of this could be for example:
* Test your assignment code on a different dataset.
* Compare performance across different parameter configurations.
* Expand your model according to some hypothesis and compare performance to base model
* Test your model on different amount of training data and comment on difference in performance
* etc.

[Assignment 1](01_decision_trees/README.md) and [Assignment 2](02_nearest_neighbors/README.md) have *pre-formulated bonus sections*. Here the bonus questions have already been formulated to give you an idea about what is suitable for the bonus sections in future assignments.
TODO: Add notes about what should be returned for the bonus section, i.e. code, example of running, plots, text etc.
