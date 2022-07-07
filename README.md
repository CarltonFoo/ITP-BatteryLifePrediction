# Battery Lifetime Prediction with Advanced Machine Learning
### ICT3111 Integrated Team Project, Team 19
This objective of this project is to develop data-driven models to predict the cycle life of commercial lithium iron phosphate (LFP)/graphite battery cells using early-cycle data, with no prior knowledge of degradation mechanisms within batteries.
To do this we will:
- Extract the needed features from our dataset
- Build 2 early-prediction models using feature-based approach
- Benchmark performance of models against prior research
- Identify and experiment with degradation modes, to understand and analyze the impact of cycles on the batteries.

This repository will go through the first two steps for this project.

<br />

# Table of Contents  
- [Requirements](#requirements)
- [Code-base Structure](#codebase)
- [Setup and Data Preparation](#setup)
- [Data Structure](#data)
- [Usage](#usage)
- [Additional Notes](#notes)


<a name="requirements"></a>

<br />

# Requirements

Python 3.10+

An environment to open and run Jupyter Notebooks

<br />

<a name="codebase"></a>

# Code-base Structure

```bash
< PROJECT ROOT >
   |
   |-- Data/
   |    |
   |    |-- 2017-05-12_batchdata_updated_struct_errorcorrect.mat    
   |    |   # pre-processed batchdata from 2017-05-12
   |    |
   |    |-- 2017-06-30_batchdata_updated_struct_errorcorrect.mat    
   |    |   # pre-processed batchdata from 2017-06-30
   |
   |-- ExportFeatures.ipynb         # extracts the features needed from the batchdata to train our models
   |
   |-- VQlinspace2.ipynb            # function that returns a linearly-spaced V vs Q curve. used to extract QDiffLinVar in ExportFeatures.csv
   |
   |-- features_combined.csv        # dataset containing the features we need to train our models. to be generated by ExportFeatures.ipynb
   |
   |-- DischargeModel.ipynb         # Building and training the Discharge Model using scipy
   |
   |-- DischargeModelTF.ipynb       # Building and training the Discharge Model using TensorFlow
   |
   |-- VarianceModel.ipynb          # Building and training the Variance Model using scipy
   |
   |-- VarianceModelTF.ipynb        # Building and training the Variance Model using TensorFlow
   |
   |-- loaddataset.py               # Contains functions to load *.mat data into memory, or read its data directly
   |
```

<br />

<a name="setup"></a>

# Setup and Data Preperation
In this step we will download our dataset and extract its features.

1. Clone this repository
2. Download the `2017-05-12_batchdata_updated_struct_errorcorrect.mat` and `2017-06-30_batchdata_updated_struct_errorcorrect.mat` datasets from [here](https://data.matr.io/1/projects/5c48dd2bc625d700019f3204).
    1. Scroll down to the bottom to see the section titled "Batches" with three dates.
    2. Navigate to each of the three batches and for each one, scroll down until you see "Matlab Struct File" with a download icon.
    3. Note that the server hosting the files will throttle downloads to around 96-128 kBps. Expect download time of about 3 days.
3. Save the .mat dataset files to the `/Data` folder in the root of the project folder.
4. In the root of the project folder, create a Python Virtual Enviroment
    1. Depending on how Python is installed on your computer, commands may differ; it may be any of the following:  
        ```python
        python3 -m venv .venv   # OR  
        python -m venv .venv    # OR  
        c:\Python310\python -m venv c:\path\to\project\folder\.venv  
        ```
5. Open the jupyter notebook file `./ExportFeatures.ipynb`, in your preferred IDE. **We recommend VSCode**
6. In the upper right corner of the notebook, select the environment as `.venv` if it is currently something else like `Python 3.10 64 bit`.
7. Click "Run All" at the top. The notebook should check and install required dependencies into the virtual environment, then read the MATLAB data files and extract their flattened features to a new file in the Data folder called `./features_combined.csv`.

<br />

<a name="data"></a>

# Data
Structure of `./featres_combined.csv`. All values are type `int`, except `policy` and `barcode`, which are type `string`.
Column          | Description
--------------- | -------------
policy          | Charing policy the battery used
barcode         | Unique identifier for a battery
cycle_life      | Number of cycles for the battery to reach its end-of-life
QD2             | Discharge capacity, cycle 2
QD(Max-2)       | Difference between max discharge capacity and cycle 2
QD100           | Discharge capacity, cycle 100
QDiffMin        | Minimum change in discharge voltage curve between cycle 10 and 100
QDiffMean       | Mean change in discharge voltage curve between cycle 10 and 100
QDiffVar        | Variance of the change in discharge voltage curve between cycle 10 and 100
QDiffSkew       | Skewness of the change in discharge voltage curve between cycle 10 and 100
QDiffKurtosis   | Kurtosis of the change in discharge voltage curve between cycle 10 and 100
QDiffStart      | First value of the change in discharge voltage curve between cycle 10 and 100
R3Coef          | Slope of the linear fit to capacity fade curve, cycles 2 to 100
R3Intercept     | Intercept of the linear fit to capacity fade curve, cycles 2 to 100
R1Coef          | Slope of the linear fit to capacity fade curve, cycles 91 to 100
R1Intercept     | Intercept of the linear fit to capacity fade curve, cycles 91 to 100
QDiffLinVar     | Linearly Interpolated Var(QD100-QD10)

<br />

<a name="usage"></a>

# Usage
1. Open the jupyter notebooks for the respective models, DischargeModel or VarianceModel. Ensure the environment is `venv`, and click `Run All` at the top; these notebooks will read from the `./features_combined.csv` file for training data.
2. Scroll and observe the results. Further explaination of the model can be found within the jupyter notebook as comments. 

<br />

<a name="notes"></a>

# Additional Notes
ExportFeatures.ipynb:
> matFilename should be edited according to your filename and file path with the content of the "Data" folder.  
> E.g. matFilename = './Data/filename.mat'

Signature Errors, not available in python (must use MATLAB):
> finaldata_4  
> finaldata_6and8  
> finaldata_all

Credits for h5py code setup:
> https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation
