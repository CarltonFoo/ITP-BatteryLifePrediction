# ITP-BatteryLifePrediction

## Requirements
Python 3.10+
## Setup
1. Clone this repository
2. Create a folder named "Data" in the root of the project folder.
3. Download the datasets from [here](https://data.matr.io/1/projects/5c48dd2bc625d700019f3204).
> Scroll down to the bottom to see the section titled "Batches" with three dates.  
> Navigate to each of the three batches and for each one, scroll down until you see "Matlab Struct File" with a download icon.  
> Note that the server hosting the files will throttle downloads to around 96-128 kBps. Expect download time of about 3 days.
4. Save the .mat dataset files to the "Data" folder previously created.
5. In the root of the project folder, create a Python Virtual Enviroment
> Depending on how Python is installed on your computer, commands may differ; it may be any of the following:  
> `python3 -m venv .venv` *OR*  
> `python -m venv .venv` *OR*  
> `c:\Python310\python -m venv c:\path\to\project\folder\.venv`  
6. Open the jupyter notebooks for the respective models, DischargeModel or VarianceModel, in your preferred IDE. **We recommend VSCode**
7. In the upper right corner of the notebook, select the environment as ".venv" if it is currently something else like "Python 3.10 64 bit"
8. Click "Run All" at the top. The notebook should check and install required dependencies into the virtual environment.
9. Scroll and observe the results.

## Notes
Signature Errors, not available in python (must use MATLAB):
finaldata_4
finaldata_6and8
finaldata_all

Testable mat files (via h5py):
2018-08-28_batchdata_updated_struct_errorcorrect
2018-04-03_varcharge_batchdata_updated_struct_errorcorrect

Credits for h5py code setup:
https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation
