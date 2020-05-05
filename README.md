# FinalProject-IA626
***
 
## General Description:
***

For this project, I will looking at datasets derived from the National Health and Nutrition Examination Survey (NHANES) public program, set forth by the Center of Disease Control (CDC). These datasets are dervied from https://wwwn.cdc.gov/nchs/nhanes/. The data is collected yearly from people across the United States for the purpose of better informing public health policy, among other uses. Specifically, I've decided to hone in on three particular datasets from the 2017-2018 NHANES data, namely datasets on Blood Pressure, Demographics, and Early Childhood. I chose to look at the datasets from those particular years because the combination of recent and interesting was deemed to best be sourced from those years. Using these datasets, I'll be processing the join of the three separate datasets using a Respondent Sequence Number, which is a person identifier number for the individual being examined contained within each of the three datasets. In addition, I'll be using the three datasets to draw interesting and useful analysis outputs, partly in the form of visualization.

## Coding Outlines: 
***

To tackle this coding problem, I've divided the coding efforts into broad sections as follows: 

1. **Data Exploration**  
> Pre-liminary exploration of data attributes such as size, type, distinct values, etc. 
2. **Creating Coded Dictionaries **
> The datasets from NHANES contain numerically coded datafields. In order to have the datafields be self-descriptive, a coded dictionary for each dataset is web-scraped from the corresponding .htm file of each dataset, and then used *section 4* to transform the dataset to a semantically descriptive version 
3. **Loading Data**
> Loading the data from its orginal source to a pandas dataframe, to be able to begin doing work on it 
4. **Transforming Data**
> Transforming and cleaning the dataset as need be, and altering the dataset from a numerical coded version to a semantically descriptive version, through the use of the created coded dictionary in *section 2*
5. **Merging Data**
> Merging the three datasets into one combined dataset, joining appropriately using their shared Respondent Sequence Numbers (aka person identifier)
6. **Data Analysis** 
> Performing various data analysis scripts to find out interesting results from the collected data

### 1. Data Exploration 
***

The three datasets of interest were downloaded as .xpt files from the NHANES website. We want to better understand the attributes of the datasets. Therefore, we first want to explore the datasets and see what they look like. 

The code looks like this for the Early Childhood data (and will be repeated for the other two datasets exactly):
```python
with open('datasets/EarlyChildhood_2017-2018_NHANES.XPT', 'rb') as f:
    for row in xport.Reader(f):
        if n == 0:
            print("Sample EC data row: ", row)
            print("type of each EC row:", type(row))
            print("Number of EC columns:", len(row))
``` 

With the results, we see the following from the 3 datasets: 
```
Sample EC data row:  (93703.0, 35.0, 2.0, 8.0, 11.0, nan, nan, 3.0, 2.0, nan)
type of each EC row: <class 'tuple'>
Number of EC columns: 10
Number of EC rows: 3093


Sample BP data row:  (93703.0, nan, 120.0, nan, nan, nan, 1.0, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan)
type of each BP row: <class 'tuple'>
Number of BP columns: 21
Number of BP rows: 8704


Sample D data row:  (93703.0, 10.0, 2.0, 2.0, 2.0, nan, 5.0, 6.0, 2.0, 27.0, nan, nan, 1.0, 1.0, nan, nan, nan, nan, nan, 1.0, 1.0, 2.0, 1.0, 2.0, 2.0, nan, nan, nan, nan, 5.0, 5.0, 3.0, 0.0, 0.0, 1.0, 2.0, 3.0, 1.0, 3.0, 9246.491864820517, 8539.7313482887, 2.0, 145.0, 15.0, 15.0, 5.0)
type of each D row: <class 'tuple'>
Number of D columns: 46
Number of D rows: 9254
```

Now we have an idea of what the dataset looks like, seeing a sample row of the datasets, understanding the datatype (i.e. tuple), and size of each dataset. This will inform us in how to proceed down the line. 

### 1. Created Coded Dictionary 
***

### 1. Loading Data
***

### 1. Transforming Data 
***

### 1. Merging Data 
***

### 1. Data Analysis  
***
