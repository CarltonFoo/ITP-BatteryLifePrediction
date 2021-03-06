# How to use discharge model
`DischargeModel.ipynb` must be run first in its entirety to auto-install dependencies and generate base model files. The other two notebooks may be run afterwards in either order.  
When running `model_tester.ipynb`, you may need to adjust the value of `N_CPUS` so that it is no more than half the number of physically installed CPU cores. The default value of 2 should suffice for the large majority of processors, which usually have at least 4 cores.  

<a name="folder"></a>

# Folder Structure

```bash
./discharge_model/
   |
   |-- README.md                       # Contains instructions on how to use the models and adjust settings in the code.
   |-- /results/                       # directory that contains results generated by the model_tester notebook
   |   |-- runs.csv                    # RMSE of runs #1 to #10 using layering and fine-tuning transfer learning techniques 
   |   |
   |   |-- statistics.csv              # collated statistics from the 10 runs e.g. standard deviation
   |
   |-- /saved_model/                   # directory that contains trained TensorFlow base models
   |   |
   |   |-- /DischargeModelFastTF/      # model data for fast charge model
   |   |
   |   |-- /DischargeModelNormTF/      # model data for normal charge model
   |
   |-- DischargeModel.ipynb            # Building and training the Discharge Model using scikit-learn library.
   |                                   # Also generates and saves the 'fast-charging' and 'normal-charging' base models.
   |
   |-- DischargeModelTransfer.ipynb    # Transfer Learning Experimentation of Discharge Model using TensorFlow
   |
   |-- Training.py                     # contains helper functions to enable multi-threaded parallel training of multiple models
   |
   |-- model_tester.ipynb              # automatically re-runs the model building and training process 10 times for transfer models to observe run-to-run variation
```
