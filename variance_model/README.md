# How to use variance model


<a name="folder"></a>

# Folder Structure

```bash
./variance_model
   |
   |-- README.md                                            # Contains instructions on how to use the models and adjust settings in the code.
   |
   |-- /results/                                            # directory that contains results generated by the notebooks in this directory
   |   |
   |   |-- /16u_test_run#_/                                 # runs #1 to #5 using 16 nodes
   |   |
   |   |-- /64u_test_run#_/                                 # runs #1 to #5 using 64 nodes
   |   |   
   |   |-- /test_run#_/                                     # runs #1 to #5 using 1 node
   |   |  
   |   |-- 16u_compiled_results.csv                         # compiled results for tests using 16 nodes
   |   |  
   |   |-- 64u_compiled_results.csv                         # compiled results for tests using 64 nodes
   |   |  
   |   |-- compiled_results.csv                             # compiled results for tests using 1 nodes
   |   |  
   |   |-- collated_results.csv                             # collated results for all tests
   |   
   |-- /saved_model/                                        # directory that contains trained models that can be loaded into Tensorflow
   |   |
   |   |-- /variance_fastcharge_basemodel/                  # model data for fast charge base model
   |   |
   |   |-- /variance_normalcharge_basemodel/                # model data for normal charge base model
   |   |   
   |   |-- /variance_normalcharge_transfermodel/            # model data for normal charge transfer model
   |
   |
   |-- variance_model_sklearn.ipynb                         # Building and training the Variance Model using scikit-learn library
   |
   |-- variance_model_TF.ipynb                              # Building and training the Variance Model using TensorFlow
   |
   |-- variance_model_TF_fastcharge_basemodel.ipynb         # Variance model that uses optimized settings to predict fast-charging battery lifecycle
   | 
   |-- variance_model_TF_normalcharge_basemodel.ipynb       # Variance model that uses optimized settings to predict normal-charging battery lifecycle
   |
   |-- variance_model_TF_normalcharge_transfermodel.ipynb   # Variance model uses pretrained model based on fast-charging to predict normal-charged batteries lifecycle
   |
   |-- results_compiler.ipynb                               # Compiles the data generated from the training and prediction of data in the test runs
```