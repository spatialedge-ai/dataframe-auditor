### still in an early development stage and undergoing significant changes regularly

# dataframe-auditor

[![Build Status](https://travis-ci.org/jackdotwa/dataframe-auditor.svg?branch=master)](https://travis-ci.org/jackdotwa/dataframe-auditor)
[![Coverage Status](https://coveralls.io/repos/github/jackdotwa/dataframe-auditor/badge.svg?branch=master)](https://coveralls.io/github/jackdotwa/dataframe-auditor?branch=master)

A dataframe auditor that computes a number characteristics of the data.



> [Summary](#summary)
> 
> [Installation](#installation)
>
> [Testing](#testing)
>
> [Usage](#usage)
> 
> [Contributions](#contributions)

## Summary

  [Data profiling](https://en.wikipedia.org/wiki/Data_profiling) is important in data analysis and analytics, as well as in determining characteristics of data pipelines.
  This repository aims to provide a means to extract a selection of attributes from data.
  
  It is currently focused on processing _pandas_ dataframes, but this functionality is being 
  extended to _spark_ dataframes too.
  
  Given a pandas dataframe, the extracted values are (where _object_ and _category_ types are mapped to 
  _string_, and all numerical types to _numeric_):
  
  |Type | Measure |   
  |:---|:---|
  |**String & Numeric** | Percentage null |
  |**String** | Distinct counts |
  | | Most frequent categories |
  |**Numeric** | Mean | 
  | | Standard deviation |
  | | Variance |
  | | Min value| 
  | | Max value|
  | | Range |
  | | Kurtosis |
  | | Skewness |
  | | Kullback-Liebler divergence |
  | | Mean absolute deviation |
  | | Median |
  | | Interquartile range |
  | | Percentage zero values |
  | | Percentage nan values |
     

  Naturally, many of these characteristics are not independent of one another, but some may be excluded as suits the application.
  
  The result of auditing a dataframe using this library is that a dictionary of these measures is returned for each column in the dataframe. 
  For example, if a dataframe consists of a single column, named _trivial_, where all values are `1`, then
  
  ```json
    [{
     "attr":  "trivial",
     "type": "NUMERIC",
     "median": 1.0,
     "variance": 0.0,
     "std": 0.0,
     "max": 1,
     "min": 1,
     "mad": 0.0,
     "p_zeros": 0.0,
     "kurtosis": 0,
     "skewness": 0,
     "iqr": 0.0,
     "range": 0,
     "p_nan": 0.0,
     "mean": 1.0
     }]
  ```
  
  For a dataframe with columns `["trivial", "non-trivial"]`, a list of dictionaries is returned:
  ```json
    [{
      "attr":  "trivial"
      },
     {
      "attr": "non-trivial"
     }]
```
    
  
## Installation

  * Dependencies are contained in `requirements.txt`:
      
    ```bash
    pip install -r requirements.txt
    ```
    
  * Alternatively, if you wish to install directly from github, you may use:
  
    ```bash
    pip install git+https://github.com/jackdotwa/dataframe-auditor.git
    ```
 
    
## Testing

  * Unittests may be run via:
   
  ```
    python -m unittest discover tests
  ```
  * Code coverage may be determined via:
  
  ```bash
    coverage run -m unittest discover tests && coverage report 
  ```
  

## Usage

  Many examples of using this package is:
  
  ```python
  import pandas as pd
  import dfauditor
  numeric_data = {
        'x': [50, 50, -10, 0, 0, 5, 15, -3, None, 0],
        'y': [0.00001, 256.128, None, 16.32, 2048, -3.1415926535, 111, 2.4, 4.8, 0.0],
        'trivial': [1]*10
  }
  numeric_df = pd.DataFrame(numeric_data)
  result_dict = dfauditor.audit_dataframe(numeric_df, nr_processes=3)
  ``` 
 
## Contributions
Pull requests are always welcome.
