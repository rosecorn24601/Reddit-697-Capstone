# Capstone-697-TeamAugury
Capstone Project for SIADS 697-698

Project Augury: Predicting which Investing posts on Reddit are likely to become popular
 * GitHub Repository: https://github.com/erlan321/Capstone-697-TeamAugury
 * Blog Post: [https://share.streamlit.io/erlan321/capstone-697-teamaugury/main/streamlit_blog_app.py](https://erlan321-capstone-697-teamaugury-spring22.streamlit.app)

Authors:
 * Antoine Wermenlinger (awerm@umich.edu)
 * Chris Lynch (cdlynch@umich.edu)
 * Erik Lang (eriklang@umich.edu)

Note about our database: The code has credentials for an AWS database that is not public. The schema is in the blog above if you want to replicate it. 

Note about the blog: in the event that you cannot access the blog on the web, you will be able to view a version of it on your local machine by cloning this Git repository to your machine, and in a terminal go to the main folder and run "streamlit run streamlit_blog_app.py".  This should open a browswer window locally that contains our blog post.

**File Descriptions in the Main Folder:**

Exploratory Data Analysis (EDA)
* EDA.ipynb : contains most of the retained EDA analyses
* dow.ipynb : quick verification on day of week / hour of day correlation
* feat_imp.ipynb : feature importance calculation based on models
* svm_feat_imp.ipynb: exploration of model feature importances

Supervised Learning Pipeline
* baseline_models.py : calculates the baseline models results (both train/validate) for model selection in the Hyperparameter tuning phase
* hyperparameter_tuning_* : python files to generate the csv results of the gridsearched cross-validation per model
* hyperparameter_viz_*: Vizualisations of our outputs from the hyperparameter tuning.


Final model selection
* final_model.py : generates the final model as a pickled file based on the hyperparameter 
tuning
* final_LR_baseline.py: generates the LR HPT model
* final_GBT_doublecheck.py: generates the GBDT HPT model
* final_results.py : featurizes the unseen data and predicts wit the final model reporting accuracy and f1 scores

Blog and Production Prediction Model
 * streamlit_blog_app.py : the main script for our blog to function

Miscellaneous files
* vanilla_models_pkl.py: creates pickled files of the vanilla (non-hpt) models to create the feature importances analysis
* requirements.txt : contains the requirements for both our analysis and for our blog. *Note that our blog is dependent on this file and should not be altered*

**File Folder Descriptions:**

aws_scraping_code : folder containing the scripts on our AWS instance for the scraping of Reddit data and storage in our Database:
 * lambda_function.py : the main AWS Lambda instance file that uses the following two helper functions
 * submission_list.py : creates a list of both new posts from Reddit and old posts we are still tracking in our database
 * praw_scrape7.py : useing the submission_list.py gathers all required data from Reddit

functions: folder containing supporting functions named Team_Augury_*
* blog_praw_functions.py: functions to be used in the streamlit blog post to scrape live Reddit data and run our feature engineering and prediction process
* feature_functions.py: functions for feature extraction from raw dataframes, either from our database or live data from Reddit
* Iterate.py: function for the baseline_models.py iteration
* load_transform_saved.py: loads a stored version of pre-processed data and returns an output identical to what is fed to clf
* SQL_func.py: returns raw data from SQL using timestamps as entrants

Other Folders
* blog_assets: files for the streamlit blog post, mainly visuals
* models: saved trained models
* saved_work: storage for csv files or other saved work
* sample_csv_data: small csv files (only 10 records each) to illustrate the raw data from our database and the feature-transformed data that flows into our analysis.
