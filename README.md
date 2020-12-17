# Starbucks-Passive-Customer-Detection Project repository structure:
The 'src' directory consists of the python programs run via jupyter notebooks.
* Datasets_Preprocessing contains code for data cleansing and basic feature extraction for experiment-1.
* Input_data_visualiation is our initial analysis of the input data set.
* Passive_Customer_Detection code contains the experiment-1 results for RandomForestClassifier, GradientBosstingClassifier, AdaBoostClassifier and Logistic Regression.
* SVM and k_NN files also contain experiment-1 results using the respective models.
* K_means_Clustering code is for the clustering experiement-2 using K-means algorithm.
* Mean_Shift and DBSCAN codes consist of the experiment-2 results obtained using the respective clustering methods.

The 'org_datasets' directory contains the original dataset downloaded from kaggle.

The 'processed_datasets' directory contains the datasets after cleansed and preprocessed with required features extracted from all the files.
* files with the prefix 'cln_' are the cleansed files of their respective datasets from Kaggle.
* total_dist.csv is the file that contains the complete joint information of the transcript data with both portfolio and profile files.
* xtr_profile.csv contains all of the features that are obtained and will be used for feature selection.

Poster.pdf contains is poster presented for the poster session.

Report.pdf is the final report submitted for the CMPT726 Project.
