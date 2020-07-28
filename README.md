Copyright Tecnalia 2020

This project has been created in Python to calculate the System Usability Scale (SUS) questionnaire score for different participants and the mean of the different participants' scores.

`sus_process_class.py` calculates the SUS score in percentage for each participant and the average score for all the participants, by reading the data provided in a `csv` file.

The 'csv' file will contain:

* first row with questions or questions numbers.
  This first line will be excluded for the process.
* first column with the users IDs.
  This information will be used to give the results for each user.
- each participants' answers must be distributed in rows: one value for each question.
  if any answer is missing, it will be replaced with a '3' according to Bangor et al., 2009 to calculate the final score
  Used delimitator for `csv` file must be `;`.

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



