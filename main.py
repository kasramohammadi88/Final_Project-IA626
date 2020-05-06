"""
##########################

INTIAL PACKAGE IMPORTATION

##########################

"""




import xport
import pandas as pd 
import re
import numpy as np
from decimal import *
import matplotlib.pyplot as plt
"""
############################

PRELIMINARY DATA EXPLORATION

############################
"""

"""

print("\n")
# Early Childhood dataset 
n = 0 
resp_seq = {}
with open('datasets/EarlyChildhood_2017-2018_NHANES.XPT', 'rb') as f:
    for row in xport.Reader(f):
        if n == 0:
            print("Sample EC data row: ", row)
            print("type of each EC row:", type(row))
            print("Number of EC columns:", len(row))
            
        ##if row[0] not in resp_seq.keys():
        ##    resp_seq[row[0]] = "EC" 
        
        n += 1 
##print(resp_seq)
 
print("Number of EC rows:", n)
print("\n")

n = 0 
with open('datasets/BloodPressure_2017-2018_NHANES.XPT', 'rb') as f:
    for row in xport.Reader(f):
        if n == 0:
            print("Sample BP data row: ", row)
            print("type of each BP row:", type(row))
            print("Number of BP columns:", len(row))
        ##if row[0] not in resp_seq.keys():
        ##    resp_seq[row[0]] = "B"  
        ##else: 
        ##    resp_seq[row[0]] = "B+EC" 
        
        n += 1 
     
print("Number of BP rows:", n)







print("\n")
n = 0 
with open('datasets/Demographics_2017-2018_NHANES.XPT', 'rb') as f:
    for row in xport.Reader(f):
        if n == 0:
            print("Sample D data row: ", row)
            print("type of each D row:", type(row))
            print("Number of D columns:", len(row))
        n += 1 
        
        ##if row[0] not in resp_seq.keys():
        ##    resp_seq[row[0]] = "D"  
        ##if row[0] in resp_seq.keys(): 
        ##   if resp_seq[row[0]] == "B": 
        ##        resp_seq[row[0]] = "B+D"
        ##    if resp_seq[row[0]] == "B+EC": 
        ##        resp_seq[row[0]] = "B+D+EC"    
        ##    if resp_seq[row[0]] == "EC": 
        ##        resp_seq[row[0]] = "D+EC"
                
print("Number of D rows:", n)

print("\n")
##print(len(resp_seq))


##resp_seq_vendiagram = {"B":0,"EC":0, "D":0,"B+D":0,"B+EC":0, "D+EC":0, "B+D+EC":0} 

##for value in resp_seq.values(): 
    #print(value)
    ##resp_seq_vendiagram[value] += 1 
        
        
##print(resp_seq_vendiagram)
"""
"""
############################

COLLECTING CODED DICTIONARIES

############################

"""

# Collecting Coded dictionary from Early Childhood dataset 

f = open("Datasets/EC_2017-2018_NHANES_Doc.htm", 'r')
file = f.read()
f.close() 

lines = file.split('\n')
parse = False           

tn = 0 
tr = 0 
td = 0

EC_codes = []  
table_codes = {} 
i = 0
# for loop to create coded dictionary 
for item in lines: 
    if "Codebook and Frequencies" in item: 
        parse = True
    if parse == True and '<table class="values">' in item: 
        ##print(table_codes)
        if table_codes != {}:
            EC_codes.append(table_codes)
            ##print("append worked")
            
        table_codes = {} 
        tn += 1 
        tr = 0 
        td = 0
        ##print(table_number)
        ##print(item)
        #print(item, tn, tr, td)
    if parse == True and '<tr>' in item: 
        tr += 1
        #print(item, tn, tr, td)
    if parse == True and '<td' in item: 
        td += 1 
        #print(item, tn, tr, td)
    
    # locating the row with the value of interest
    if '<td scope="row" class="values"' in item: 
        key = re.split('<|>', item)[2]
        #print(key)
        value = re.split('<|>', lines[i+1])[2]
        #print(value)
        
        table_codes[key] = value 
        
        
        #print(item)
        #print(lines[i+1])
        #print('\n')
       ## if td == 2 and td == 1:
       ## if td == 2 and td == 2: 
       ## if td
    
        
        
    i += 1 
# appending the last table of codes collected from the above loop    
EC_codes.append(table_codes)
##print(len(EC_codes))

##print(EC_codes)

##for item in EC_codes:
##        print(item)
i = 0 
# replace a 'range' datatype for coded keys that are correspond to a range of values rather than
# an exact number 
for dic in EC_codes:
    ##if i == 1:
        ##break
    for key in dic.keys(): 
        ##if i == 1:
        ##    break
        if 'to' in key:
            # spliting string where there is a numerical range involved
            a = key.split('to')
            # removing leading and trailing white spaces from the list values 
            a = [x.strip(' ') for x in a]
            # replace the range values in the string with a 'range' datatype variable
            num_range = range(int(a[0]), int(a[1]) + 1)
            ##print("before:", dic)
            dic[num_range] = dic[key]
            del dic[key]
            ##print("after:", dic)
            ##print(num_range)
            ##print(a)
            ##i += 1 
      
      
      

##for item in EC_codes:
##        print(item)


# Collecting Coded dictionary from Blood Pressure dataset  

f = open("Datasets/BP_2017-2018_NHANES_Doc.htm", 'r')
file = f.read()
f.close() 

lines = file.split('\n')
parse = False           

tn = 0 
tr = 0 
td = 0

BP_codes = []  
table_codes = {} 
i = 0
# for loop to create coded dictionary 
for item in lines: 
    if "Codebook and Frequencies" in item: 
        parse = True
    if parse == True and '<table class="values">' in item: 
        ##print(table_codes)
        if table_codes != {}:
            BP_codes.append(table_codes)
            ##print("append worked")
            
        table_codes = {} 
        tn += 1 
        tr = 0 
        td = 0
        ##print(table_number)
        ##print(item)
        #print(item, tn, tr, td)
    if parse == True and '<tr>' in item: 
        tr += 1
        #print(item, tn, tr, td)
    if parse == True and '<td' in item: 
        td += 1 
        #print(item, tn, tr, td)
    
    # locating the row with the value of interest
    if '<td scope="row" class="values"' in item: 
        key = re.split('<|>', item)[2]
        #print(key)
        value = re.split('<|>', lines[i+1])[2]
        #print(value)
        
        table_codes[key] = value 
        
        
        #print(item)
        #print(lines[i+1])
        #print('\n')
       ## if td == 2 and td == 1:
       ## if td == 2 and td == 2: 
       ## if td
    
        
        
    i += 1 
# appending the last table of codes collected from the above loop    
BP_codes.append(table_codes)
##print("number of collected coded dictionaries for blood pressure:", len(BP_codes))
##print('\n')

##print(EC_codes)
i = 0 
# replace a 'range' datatype for coded keys that are correspond to a range of values rather than
# an exact number 
for dic in BP_codes:
    ##if i == 1:
        ##break
    for key in dic.keys(): 
        ##if i == 1:
        ##    break
        if 'to' in key:
            # spliting string where there is a numerical range involved
            a = key.split('to')
            # removing leading and trailing white spaces from the list values 
            a = [x.strip(' ') for x in a]
            # replace the range values in the string with a 'range' datatype variable
            num_range = range(int(a[0]), int(a[1]) + 1)
            ##print("before:", dic)
            dic[num_range] = dic[key]
            del dic[key]
            ##print("after:", dic)
            ##print(num_range)
            ##print(a)
            ##i += 1 
      
      
      

##for item in EC_codes:
##        print(item.keys())  
##        print(type(item.values()))

# removing coded columns dictionaries we don't need and keeping the rest 

BP_codes_new = [] 
for num,dic in enumerate(BP_codes, start = 1):
    if num == 3 or num == 4 or num == 6 or num == 7 or num == 15 or num == 16: 
        BP_codes_new.append(dic)
        
##print("new coded dictionary list:\n", BP_codes_new)
##print("number of dictionaries in new coded list: ", len(BP_codes_new))
  

BP_codes = BP_codes_new 

##print(BP_codes)

##print(len(BP_codes))  
"""

##for num, dic in enumerate(BP_codes):
    ##print('index #:', num)
    ##print('coded dictionary for index: ', dic)
    ##print('\n')
"""



# Collecting Coded dictionary from Demographics dataset  

f = open("Datasets/D_2017-2018_NHANES_Doc.htm", 'r')
file = f.read()
f.close() 

lines = file.split('\n')
parse = False           

tn = 0 
tr = 0 
td = 0

D_codes = []  
table_codes = {} 
i = 0
# for loop to create coded dictionary 
for item in lines: 
    if "Codebook and Frequencies" in item: 
        parse = True
    if parse == True and '<table class="values">' in item: 
        ##print(table_codes)
        if table_codes != {}:
            D_codes.append(table_codes)
            ##print("append worked")
            
        table_codes = {} 
        tn += 1 
        tr = 0 
        td = 0
        ##print(table_number)
        ##print(item)
        #print(item, tn, tr, td)
    if parse == True and '<tr>' in item: 
        tr += 1
        #print(item, tn, tr, td)
    if parse == True and '<td' in item: 
        td += 1 
        #print(item, tn, tr, td)
    
    # locating the row with the value of interest
    if '<td scope="row" class="values"' in item: 
        key = re.split('<|>', item)[2]
        #print(key)
        value = re.split('<|>', lines[i+1])[2]
        #print(value)
        
        table_codes[key] = value 
        
        
        #print(item)
        #print(lines[i+1])
        #print('\n')
       ## if td == 2 and td == 1:
       ## if td == 2 and td == 2: 
       ## if td
    
        
        
    i += 1 
# appending the last table of codes collected from the above loop    
D_codes.append(table_codes)
##print("\n number of collected coded dictionaries for demographics:", len(D_codes))
##print('\n')

##print("\n collected dictionaries for demographics: ", D_codes)
i = 0 
# replace a 'range' datatype for coded keys that are correspond to a range of values rather than
# an exact number 
for dic in D_codes:
    ##if i == 1:
        ##break
        
    for key in dic.keys(): 
        ##if i == 1:
        ##    break
        if 'to' in key:
            # spliting string where there is a numerical range involved
            a = key.split('to')
            # removing leading and trailing white spaces from the list values 
            a = [x.strip(' ') for x in a] 
            # replace the range values in the string with a 'range' datatype variable
            ##print(
            ##print(a[1], len(a[1]))
            if '.' in a[0] or '.' in a[1]:
                ##print("detecting non-integer values in: ", a)
                if len(a[0]) == 4 or len(a[1]) == 4:
                    ##print(float(a[1]))
                    step = Decimal(str(0.01)).quantize(Decimal('.01'))
                    ##print("type of step:", type(step))
                    beg_range = Decimal(a[0]).quantize(Decimal('.01'))
                    end_range = Decimal(a[1]).quantize(Decimal('.01'))
                    num_range = np.arange(beg_range, end_range + step, step)
                    # need to convert to tuple to make it 'hashable' for the dictionary key designation
                    #print("numpy array version of range:", num_range)
                    num_range = tuple(num_range)
                    #print("tuple version of range:", num_range)
                    ##print(num_range)
                    ##print("detecting the Ratio of Family of Income poverty rate dictionary:", a)
                else:
                    ##print("detected non-integer value but not relevant column; skipping to next dictionary iteration:", a)
                    continue 
            else: 
                num_range = range(int(a[0]), int(a[1]) + 1)
            #print("before:", dic)
            dic[num_range] = dic[key]
            del dic[key]
            #print("after:", dic)
            ##print(num_range)
            ##print("range values:", a)
            ##print('\n')
            ##i += 1 
##print(num_range)

##if Decimal('4.98') in num_range:
##    print("FOUND IT!")
     

##for item in D_codes:
##        print(item.keys())  
##        print(type(item.values()))

# removing coded columns dictionaries we don't need and keeping the rest 
#print('\n')
#print("Demographic codes: \n \n", D_codes)
#print("number of dictionaries in old coded list: ", len(D_codes))
D_codes_new = [] 
for num,dic in enumerate(D_codes, start = 1):
    if num == 3 or num == 4 or num == 7 or num == 10 or num == 11 or num == 12 or num == 15 or num == 16 or num == 17 or num == 45: 
        D_codes_new.append(dic)
        
#print('\n')     
#print("new coded dictionary list:\n", D_codes_new)
#print("number of dictionaries in new coded list: ", len(D_codes_new))
  

D_codes = D_codes_new 

##print("after fixing range keys: \n", D_codes)

##print(len(D_codes))  
"""

##for num, dic in enumerate(D_codes):
    ##print('index #:', num)
    ##print('coded dictionary for index: ', dic)
    ##print('\n')
"""



"""

################################

LOADING DATASETS INTO DATAFRAMES

################################ 


"""






# Load Early-Childhood data into dataframe
'''
Looking at the dataset, it was determined that only the first 6 datafields are interesting/relevant to use for the 
analysis, thus only these fields will be loaded in the main dataframe 
'''
i = 0
mylist = []



with open('datasets/EarlyChildhood_2017-2018_NHANES.XPT', 'rb') as f:
    for row in xport.Reader(f):
        a = list(row)
        ##print(a)
        # remove unwanted data fields for the row 
        a.pop()
        a.pop()
        a.pop()
        ##print(a)
        ##print(len(a))
        mylist.append(a)
        i += 1 
        ##if i == 1:
        ##    break




##print(mylist)

##print(len(mylist[0]))



df_ec = pd.DataFrame(mylist, columns = ["RESP#", "Mother's Age When Born", "Mother Smoked When Pregnant", \
"Weight At Birth Lbs", "Weight At Birth Ozs", "Weight More/Less than 5.5lbs", "Weight More/Less than 9.0lbs"])
##print(df_ec)

# replacing all NaN fields with '.', which will help the conversion of the numerical code values 
# downstream 
df_ec = df_ec.fillna("123456789")

##print(df_ec)





# Load Blood Pressure data into dataframe


i = 0
mylist = []


with open('datasets/BloodPressure_2017-2018_NHANES.XPT', 'rb') as f:
    for row in xport.Reader(f):
        a = list(row)
        ##print(a)
        # remove unwanted data fields for the row 
        a = a[0:1] + a[3:5] + a[6:8] + a[15:17]
        ##print(a)
        ##print(len(a))
        ##print(len(a))
        mylist.append(a)
        i += 1 
        ##if i == 1:
        ##    break




##print(mylist)
"""


"""


df_bp = pd.DataFrame(mylist, columns = ["RESP#", "Arm Selected", "Coded Cuff Size", \
"Pulse Regular Or Irregular", "Pulse Type", "Systolic (3rd Rdg)", "Diastolic (3rd Rdg)"])
##print(df_bp)

# replacing all NaN fields with arbitrary'ZZZ', which will help the conversion of the numerical code values 
# downstream 
df_bp = df_bp.fillna("123456789")
##print(df_bp)

# Load Demographics data into dataframe
'''
 
'''
i = 0
mylist = []


with open('datasets/Demographics_2017-2018_NHANES.XPT', 'rb') as f:
    for row in xport.Reader(f):
        a = list(row)
        ##print(len(a))
        ##print(a)
        
        # remove unwanted data fields for the row 
        a = a[0:1] + a[3:5] + a[7:8] + a[10:13] + a[15:18] + a[45:46]
        
        ##print(a)
        ##print(len(a))
        mylist.append(a)
        i += 1 
        ##if i == 1:
        ##    break




##print(mylist)

df_d = pd.DataFrame(mylist, columns = ["RESP#", "Gender", "Age In Years", \
"Race", "Served in U.S. Armed Forces", "Serviced In Foreign Armed Forces", "Country Of Birth", \
"Education Ages 6-19", "Education Ages 20+", "Marital Status", "Ratio Of HH Income To Poverty"])

# replacing all NaN fields with arbitrary string'123456789', which will help the conversion of the numerical code values 
# downstream 
df_d = df_d.fillna("123456789")

#print(df_d)

"""

#####################################################################################

TRANSFORM DATASETS FROM NUMERICALLY CODED VERSION TO SEMANTICALLY DESCRIPTIVE VERSION

#####################################################################################

"""

# Transforming Early-Childhood dataset from coded version to semantically descriptive version 

# Converting coded numbers for descriptive field per collected coding semantic 

##print(df_ec)
##print(df_ec.dtypes)

# change all values to 'int32' to remove decimal points off the numeric values
df_ec = df_ec.astype({"RESP#":'int32', "Mother's Age When Born":'int32', "Mother Smoked When Pregnant":'int32', \
"Weight At Birth Lbs":'int32', "Weight At Birth Ozs":'int32', "Weight More/Less than 5.5lbs":'int32', \
"Weight More/Less than 9.0lbs":'int32' })

##print("after int32 change: \n", df_ec)
##print(df_ec.dtypes)

# change all values to 'str' so as to allow the replace() method to work seemlessly with the coded dictionary values 
df_ec = df_ec.astype({"RESP#":'str', "Mother's Age When Born":'str', "Mother Smoked When Pregnant":'str', \
"Weight At Birth Lbs":'str', "Weight At Birth Ozs":'str', "Weight More/Less than 5.5lbs":'str', \
"Weight More/Less than 9.0lbs":'str'})


##print("after str change: \n",df_ec)
##print(df_ec.dtypes)

# replace assigned 0 values with the appropriate '.' string which will aid in the coding transformation process
df_ec = df_ec.replace('123456789','.')

##print("after 0 to . replacement: \n",df_ec)
##print(df_ec)

##print(df_ec.dtypes)
##print(EC_codes)
#df_ec = df_ec.replace(      

##for row in df_ec["Mother's Age When Born"]: 
##    print(row)


#print(len(EC_codes))

##print (df_ec.iloc[:,1])

change_num = 0 
range_values = 0 
flag = 0 

flag_list = [] 

# collect list of column names to reference later when cycling through different columns 
# when transforming datafields from coded version to semantically descriptive version
col_names  = []
for col in df_ec.columns:
    col_names.append(col)
# indexes of columns of interest for the Early Childhood data. This index will be used in the FOR loop below to cycle 
# through specific columns of interest only 

distinct_values_list = [] 
#print(col_names)
#print(type(col_names[0]))   

# iteration count for the column names list 
col_i = 0
for col in col_names:
    distinct_dic = {} 
    i = 0
    ##print('\n')
    ##print("column iteration number starts as", col_i)
    ##if col_i == 4:
    ##    print("break loop when starting on column 4!")
    ##    break
    if col == 'RESP#':
        ##print("skip RESP# column")
        col_i += 1 
        continue
    
    ##print('\n')
    ##print("column name:", col)
    ##print("corresponding codes: ", EC_codes[col_i-1])
    ##print('\n')
    for row_value in df_ec[col]:
        # for non-range key values in the coded dictionary
        ##print(row_value)
        ##if i % 500 == 0:
            ##print(row_value, i)
        if row_value in EC_codes[col_i-1].keys():
            ##print('\n')
            ##print("non range row value in dataframe", df_ec[col_names[col_i]][i])
            ##print("non range key: ", row_value)
            ##print("non range corresponding key-value in Coded dictionary: ", EC_codes[col_i-1][row_value])
            ##print(i)
            ##print("Before non-range change: ", df_ec[col_names[1]][i])
            df_ec[col_names[col_i]][i] = EC_codes[col_i-1][row_value]
            ##df_ec.iloc[i:1] = EC_codes[0][row_value]
            ##print("After non-range change: ", df_ec[col_names[1]][i])
            ##print("\n")
            
            ##print(df_ec["Mother's Age When Born"][i])
            ##print('\n')
            change_num += 1 
            if df_ec[col_names[col_i]][i] in distinct_dic.keys():
                distinct_dic[df_ec[col_names[col_i]][i]] += 1 
            else: 
                distinct_dic[df_ec[col_names[col_i]][i]] = 1 
            
            
            
            
        # for range key values in the coded dictionary 
        else: 
            if df_ec[col_names[col_i]][i] in distinct_dic.keys():
                distinct_dic[df_ec[col_names[col_i]][i]] += 1 
            else: 
                distinct_dic[df_ec[col_names[col_i]][i]] = 1 
            ##print("NOW in range mode")
            for key in EC_codes[col_i-1]:
                ##print(type(key))
                ##print(type(key) == range)
                ##print(row_value in key)
                if type(key) == range:
                    ##print("row value: ", row_value)
                    ##print("Found range key:", key)
                    if int(row_value) in key:
                        ##print("row value identified in range key")
                        range_values += 1 
                    else: 
                        flag += 1 
                        flag_dic = {'row number':i, 'row value': row_value, 'range key': key}
                        flag_list.append(flag_dic)
                    ##print('\n')
                    
                    
        
        i += 1 
    distinct_values_list.append(distinct_dic)    
    col_i += 1 
##print(col_names[col_i-1])
##for row_value in df_ec[col_names[col_i-1]]:
##    print(row_value)

"""
print('\n')
print("number of changes to columns in total: ", change_num)
print("number of range values in columns in total:", range_values)
print("sum total of detected and dealt with values for all columns: ", change_num + range_values)
print("number of rows datafields for all columns: ", len(df_ec)*6)
print("number of flags raised for range values for all columns: ", flag)
print("list of flags for range for all columns: ", flag_list)

for index, dic in enumerate(distinct_values_list, start = 1):
    print('\n')
    print("column name:", col_names[index])
    print('unique values:', dic)
"""   
    

##print('\n')
##print(df_ec)
    



# Transforming Blood Pressure dataset from coded version to semantically descriptive version 





# Converting coded numbers for descriptive field per collected coding semantic 

##print(df_bp)
##print(df_bp.dtypes)

# change all values to 'int32' to remove decimal points off the numeric values
df_bp = df_bp.astype({"RESP#":'int32', "Arm Selected":'int32', "Coded Cuff Size":'int32', \
"Pulse Regular Or Irregular":'int32', "Pulse Type":'int32', "Systolic (3rd Rdg)":'int32', \
"Diastolic (3rd Rdg)":'int32' })


##print("after int32 change: \n", df_bp)
##print(df_bp.dtypes)

# change all values to 'str' so as to allow the replace() method to work seemlessly with the coded dictionary values 
df_bp = df_bp.astype({"RESP#":'str', "Arm Selected":'str', "Coded Cuff Size":'str', \
"Pulse Regular Or Irregular":'str', "Pulse Type":'str', "Systolic (3rd Rdg)":'str', \
"Diastolic (3rd Rdg)":'str' })



##print("after str change: \n",df_bp)
##print(df_bp.dtypes)

# replace assigned 0 values with the appropriate '.' string which will aid in the coding transformation process
df_bp = df_bp.replace('123456789','.')

##print("after 123456789 to . replacement: \n \n",df_bp)
##print(df_bp)

##print(df_bp.dtypes)
##print(BP_codes)
#df_bp = df_bp.replace(      

##for row in df_bp["Mother's Age When Born"]: 
##    print(row)


#print(len(BP_codes))

##print (df_bp.iloc[:,1])

change_num = 0 
range_values = 0 
flag = 0 

flag_list = [] 

# collect list of column names to reference later when cycling through different columns 
# when transforming datafields from coded version to semantically descriptive version
col_names  = []
for col in df_bp.columns:
    col_names.append(col)
# indexes of columns of interest for the Early Childhood data. This index will be used in the FOR loop below to cycle 
# through specific columns of interest only 

distinct_values_list = [] 
#print(col_names)
#print(type(col_names[0]))   

# iteration count for the column names list 
col_i = 0
for col in col_names:
    distinct_dic = {} 
    i = 0
    ##print('\n')
    ##print("column iteration number starts as", col_i)
    ##if col_i == 4:
    ##    print("break loop when starting on column 4!")
    ##    break
    if col == 'RESP#':
        ##print("skip RESP# column")
        col_i += 1 
        continue
    
    ##print('\n')
    ##print("column name:", col)
    ##print("corresponding codes: ", BP_codes[col_i-1])
    ##print('\n')
    for row_value in df_bp[col]:
        # for non-range key values in the coded dictionary
        ##print(row_value)
        ##if i % 500 == 0:
            ##print(row_value, i)
        if row_value in BP_codes[col_i-1].keys():
            ##print('\n')
            ##print("non range row value in dataframe", df_bp[col_names[col_i]][i])
            ##print("non range key: ", row_value)
            ##print("non range corresponding key-value in Coded dictionary: ", BP_codes[col_i-1][row_value])
            ##print(i)
            ##print("Before non-range change: ", df_bp[col_names[1]][i])
            df_bp[col_names[col_i]][i] = BP_codes[col_i-1][row_value]
            ##df_bp.iloc[i:1] = BP_codes[0][row_value]
            ##print("After non-range change: ", df_bp[col_names[1]][i])
            ##print("\n")
            
            ##print(df_bp["Mother's Age When Born"][i])
            ##print('\n')
            change_num += 1 
            if df_bp[col_names[col_i]][i] in distinct_dic.keys():
                distinct_dic[df_bp[col_names[col_i]][i]] += 1 
            else: 
                distinct_dic[df_bp[col_names[col_i]][i]] = 1 
            
            
            
            
        # for range key values in the coded dictionary 
        else: 
            if df_bp[col_names[col_i]][i] in distinct_dic.keys():
                distinct_dic[df_bp[col_names[col_i]][i]] += 1 
            else: 
                distinct_dic[df_bp[col_names[col_i]][i]] = 1 
            ##print("NOW in range mode")
            for key in BP_codes[col_i-1]:
                ##print(type(key))
                ##print(type(key) == range)
                ##print(row_value in key)
                if type(key) == range:
                    ##print("row value: ", row_value)
                    ##print("Found range key:", key)
                    if int(row_value) in key:
                        ##print("row value identified in range key")
                        range_values += 1 
                    else: 
                        flag += 1 
                        flag_dic = {'row number':i, 'row value': row_value, 'range key': key}
                        flag_list.append(flag_dic)
                    ##print('\n')
                    
                    
        
        i += 1 
    distinct_values_list.append(distinct_dic)    
    col_i += 1 
##print(col_names[col_i-1])
##for row_value in df_bp[col_names[col_i-1]]:
##    print(row_value)

"""
print('\n')
print("number of changes to columns in total: ", change_num)
print("number of range values in columns in total:", range_values)
print("sum total of detected and dealt with values for all columns: ", change_num + range_values)
print("number of rows datafields for all columns: ", len(df_bp)*6)
print("number of flags raised for range values for all columns: ", flag)
print("list of flags for range for all columns: ", flag_list)

for index, dic in enumerate(distinct_values_list, start = 1):
    print('\n')
    print("column name:", col_names[index])
    print('unique values:', dic)
   
    

##print('\n')
print("blood pressure dataframe AFTER FULL transformation process: \n", df_bp)
"""







# Transforming DEMOGRAPHICS dataset from coded version to semantically descriptive version 

# Converting coded numbers for descriptive field per collected coding semantic 


"""
df_d = pd.DataFrame(mylist, columns = ["RESP#", "Gender", "Age In Years", \
"Race", "Served in U.S. Armed Forces", "Serviced In Foreign Armed Forces", "Country Of Birth", \
"Education Ages 6-19", "Education Ages 20+", "Marital Status", "Ratio Of HH Income To Poverty"])
"""


##print("Before transformation")
##print(df_d)
##print(df_d.dtypes)
##print('\n')

# change all values to 'int32' to remove decimal points off the numeric values
df_d = df_d.astype({"RESP#":'int32', "Gender":'int32', "Age In Years":'int32', \
"Race":'int32', "Served in U.S. Armed Forces":'int32', "Serviced In Foreign Armed Forces":'int32', \
"Country Of Birth":'int32', "Education Ages 6-19":'int32', "Education Ages 20+":'int32', "Marital Status":'int32', \
"Ratio Of HH Income To Poverty":'int32'})


##print("after int32 change: \n", df_d)
##print(df_d.dtypes)

# change all values to 'str' so as to allow the replace() method to work seemlessly with the coded dictionary values 

df_d = df_d.astype({"RESP#":'str', "Gender":'str', "Age In Years":'str', \
"Race":'str', "Served in U.S. Armed Forces":'str', "Serviced In Foreign Armed Forces":'str', \
"Country Of Birth":'str', "Education Ages 6-19":'str', "Education Ages 20+":'str', "Marital Status":'str', \
"Ratio Of HH Income To Poverty":'str'})


##print("after str change: \n",df_d)
##print(df_d.dtypes)

# replace assigned '123456789' values with the appropriate '.' string which will aid in the coding transformation process
df_d = df_d.replace('123456789','.')

##print("after 123456789 to . replacement:\n",df_d)
##print(df_d)

##print(df_d.dtypes)
##print(BP_codes)
##df_d = df_d.replace(      

##for row in df_d["Mother's Age When Born"]: 
##    print(row)


##print(len(BP_codes))

##print (df_d.iloc[:,1])

change_num = 0 
range_values = 0 
flag = 0 

flag_list = [] 

# collect list of column names to reference later when cycling through different columns 
# when transforming datafields from coded version to semantically descriptive version
col_names  = []
for col in df_d.columns:
    col_names.append(col)
# indexes of columns of interest for the Early Childhood data. This index will be used in the FOR loop below to cycle 
# through specific columns of interest only 

distinct_values_list = [] 
#print(col_names)
#print(type(col_names[0]))   

# iteration count for the column names list 
col_i = 0
for col in col_names:
    distinct_dic = {} 
    i = 0
    ##print('\n')
    ##print("column iteration number starts as", col_i)
    ##if col_i == 4:
    ##    print("break loop when starting on column 4!")
    ##    break
    if col == 'RESP#':
        ##print("skip RESP# column")
        col_i += 1 
        continue
    
    ##print('\n')
    ##print("column name & col_i index:", col, col_i)
    ##print("corresponding codes: ", D_codes[col_i-1])
    ##print('\n')
    for row_value in df_d[col]:
        # for non-range key values in the coded dictionary
        ##print(row_value)
        ##if i % 500 == 0:
            ##print(row_value, i)
        if row_value in D_codes[col_i-1].keys():
            ##print('\n')
            ##print("non range row value in dataframe", df_d[col_names[col_i]][i])
            ##print("non range key: ", row_value)
            ##print("non range corresponding key-value in Coded dictionary: ", D_codes[col_i-1][row_value])
            ##print(i)
            ##print("Before non-range change: ", df_d[col_names[1]][i])
            df_d[col_names[col_i]][i] = D_codes[col_i-1][row_value]
            ##df_d.iloc[i:1] = BP_codes[0][row_value]
            ##print("After non-range change: ", df_d[col_names[1]][i])
            ##print("\n")
            
            ##print(df_d["Mother's Age When Born"][i])
            ##print('\n')
            change_num += 1 
            if df_d[col_names[col_i]][i] in distinct_dic.keys():
                distinct_dic[df_d[col_names[col_i]][i]] += 1 
            else: 
                distinct_dic[df_d[col_names[col_i]][i]] = 1 
            
            
            
            
        # for range key values in the coded dictionary 
        else: 
            if df_d[col_names[col_i]][i] in distinct_dic.keys():
                distinct_dic[df_d[col_names[col_i]][i]] += 1 
            else: 
                distinct_dic[df_d[col_names[col_i]][i]] = 1 
            ##print("NOW in range mode")
            for key in D_codes[col_i-1]:
                ##print(type(key))
                ##print(type(key) == range)
                ##print(row_value in key)
                if type(key) == range or type(key) == tuple:
                    ##print("row value: ", row_value)
                    ##print("Found range key:", key)
                    if int(row_value) in key:
                        ##print("row value identified in range key")
                        range_values += 1 
                    else: 
                        flag += 1 
                        flag_dic = {'row number':i, 'row value': row_value, 'range key': key}
                        flag_list.append(flag_dic)
                    ##print('\n')
                    
                    
        
        i += 1 
    distinct_values_list.append(distinct_dic)    
    col_i += 1 
##print(col_names[1])
##for row_value in df_d[col_names[1]]:
##    print(row_value)

"""
print('\n')
print("number of changes to columns in total: ", change_num)
print("number of range values in columns in total:", range_values)
print("sum total of detected and dealt with values for all columns: ", change_num + range_values)
print("number of rows datafields for all columns: ", len(df_d)*10)
print("number of flags raised for range values for all columns: ", flag)
print("list of flags for range for all columns: ", flag_list)

"""

##for index, dic in enumerate(distinct_values_list, start = 1):
##    print('\n')
##    print("column name & index:", col_names[index], index)
##    print('unique values:', dic)
  


##print('\n')


##print("demographics dataframe AFTER FULL transformation process: \n", df_d)

"""

"""

"""
###########################

MERGE THE DATASETS TOGETHER

########################### 
"""


# Merge the datasets together 

ec_bp_merge = pd.merge(left=df_ec, right=df_bp, left_on='RESP#', right_on='RESP#', how = 'inner')

##print(ec_bp_merge)

ec_bp_d_merge = pd.merge(left=ec_bp_merge, right=df_d, left_on='RESP#', right_on='RESP#', how = 'inner')

#print(ec_bp_d_merge)


two_dimension_array = {} 

for index, row in enumerate(ec_bp_d_merge["Mother's Age When Born"]): 
    # if it is an acceptable data row
    if (row != 'Refused' and row != "Don't know" and row != "Missing" and row != '45 years or older' and row !=  '14 years or younger') and ec_bp_d_merge["Coded Cuff Size"][index] != 'Missing':
        # see if it is an integer acceptable value 
        try:
            a = int(row)
            two_dimension_array[a] = ec_bp_d_merge["Coded Cuff Size"][index]
            ##print("Integer accepted row:", row)
        except:
            
            two_dimension_array[row] = ec_bp_d_merge["Coded Cuff Size"][index]
            ##print("Not accepted integer row", row)
    
    
    
sorted_array = {} 


labels = ['Child (9X17)', 'Adult (12X22)', 'Large (15X32)', 'Thigh (18X35)'] 


for label in labels: 
    for key in two_dimension_array.keys():
        if two_dimension_array[key] == label:
            sorted_array[key] = label

print(sorted_array)
print(len(sorted_array))

##print(two_dimension_array)
##print(len(two_dimension_array))
    ##print(row)
    ##print(index)



##for row in ec_bp_d_merge["Served in U.S. Armed Forces"]:
##    print(row)
##    print("column name & index:", col_names[index], index)
##    print('unique values:', dic)

"""
###########################

DATA ANALYSIS 

########################### 
"""

fig, ax = plt.subplots()
    
##ax.scatter(ec_bp_d_merge['Served in U.S. Armed Forces'], ec_bp_d_merge['Pulse Regular Or Irregular'])

##ax.hist(ec_bp_d_merge['Gender'])
##plt.show()

ax.scatter(sorted_array.keys(), sorted_array.values())
plt.show()








"""

# testing for unique respondent numbers in the merged data frame

## confirmed that all respondent values in the fully merged inner join dataframe are unique 

# collecting column of respondent numbers into 'test' series datatype 
i = 0 
for column in ec_bp_d_merge:
    resp_col = ec_bp_d_merge[column]
    #print(column, resp_col)
    i += 1 
    if i == 1:
        break

seq = {} 
for item in resp_col: 
    if item not in seq.keys():
        seq[item] = 1 
    else: 
        seq[item] += 1 
        
#print(seq)        
#print(len(seq))

"""