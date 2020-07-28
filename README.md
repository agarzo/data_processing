Copyright Tecnalia 2020

This a script for the SUS (Sytem Usability Scale) questionnaire process implemented in Python.

`SUS_process_class.py` measures the SUS score in percentage for each participant and the average score for all the participants, by reading the data provided in a `csv` file.
The 'csv' file will contain:

* first row with questions or questions numbers.
  This first line will be excluded for the process.
* first column with the users IDs.
  This information will be used to give the results for each user.
* each user answers must be distributed in rows.
  `csv` information will be divided with ;`.

# Installation

### using Conda
Requires the following packages (install with 'conda'): unicodecsv, easygui, statistics

And then run the following commands:

**[source, shell]**

    conda install -c conda-forge pip
    pip install virtualenv
    *create virtual environment*
    virtualenv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt


### using pip

**[source, shell]**

    sudo -H pip install virtualenv
    *create virtual environment*
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

# Usage

**[source, shell]**

    python sus_questionnaire/sus_process_class.py

An example file of input [testdata] `csv` file are provided in `sus_questionnaire/test/`

The result of the data process is provided on the `sus_questionnaire/test/testresult.csv` file



