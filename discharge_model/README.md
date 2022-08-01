# How to use discharge model


<a name="folder"></a>

# Folder Structure

```bash
./discharge_model/
   |
   |-- README.md                       # Contains instructions on how to use the models and adjust settings in the code.
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
```