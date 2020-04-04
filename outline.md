# Outline of Final Project 

## **General Description:** 

For this project, I will looking at datasets derived from the National Health and Nutrition Examination Survey (NHANES) public program, set forth by the Center of Disease Control (CDC). These datasets are dervied from *https://wwwn.cdc.gov/nchs/nhanes/*. The data is collected yearly from people across the United States for the purpose of better informing public health policy, among other uses. Specifically, I've decided to hone in on three particular datasets from the 2017-2018 NHANES data, namely datasets on *Blood Pressure*, *Demographics*, and *Early Childhood*. I chose to look at the datasets from those particular years because the combination of recent and interesting was deemed to best be sourced from those years. Using these datasets, I'll be processing the *join* of the three separate datasets using a **Respondent Sequence Number**, which is a person identifier number for the individual being examined contained within each of the three datasets. In addition, I'll be using the three datasets to draw interesting and useful analysis outputs, partly in the form of visualization.

## **Key Points:**

* Three datasets from NHANES: Blood Pressure, Demographics, Early Childhood 
  * file formats: *XPT* - Binary file format 
* *join* will be done on the **Respondent Sequence Number** field (person identifier number) 
* The three datasets are each accompanied by a *.HTM* file which describes the dataset, along with giving descriptions for the coded data field values. Since the datasets are all numeric, a web-scrapping code of the *.HTM* files will be created to create a *Code-Conversion* JSON dictionary, which will be used to properly populate a joined set of the three datasets, fully converted from the numeric coded version of the data to a de-coded self-descriptive version, which will be easier to use downstream in the analysis.
* Analysis output, in the form of derived data and visualization, will be created from the joined datasets. The specifics of the analysis and visualization to be made is still TBD 
* Fields of interest:
  * *for Blood Pressure*: Arm Selected, Pulse Type, Systolic, Diasystolic
  * *for Demographics*: Gender, Race, Marital Status, Age, Education Level, No. of people in HH, Ratio of family income to poverty 
  * *for Early Childhood*: Mother's age when born, Mother smoked when pregnant, weight at birth 



