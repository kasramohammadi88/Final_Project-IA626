# Exploring datasets to better understand them 

import xport
import pandas as pd 

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
            
        if row[0] not in resp_seq.keys():
            resp_seq[row[0]] = "EC" 
        
        n += 1 
      
print("Number of EC rows:", n)
print("\n")

n = 0 
with open('datasets/BloodPressure_2017-2018_NHANES.XPT', 'rb') as f:
    for row in xport.Reader(f):
        if n == 0:
            print("Sample BP data row: ", row)
            print("type of each BP row:", type(row))
            print("Number of BP columns:", len(row))
        if row[0] not in resp_seq.keys():
            resp_seq[row[0]] = "B"  
        else: 
            resp_seq[row[0]] = "B+EC" 
        
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
        
        if row[0] not in resp_seq.keys():
            resp_seq[row[0]] = "D"  
        if row[0] in resp_seq.keys(): 
            if resp_seq[row[0]] == "B": 
                resp_seq[row[0]] = "B+D"
            if resp_seq[row[0]] == "B+EC": 
                resp_seq[row[0]] = "B+D+EC"    
            if resp_seq[row[0]] == "EC": 
                resp_seq[row[0]] = "D+EC"
                
print("Number of D rows:", n)

print("\n")
print(len(resp_seq))
45

resp_seq_vendiagram = {"B":0,"EC":0, "D":0,"B+D":0,"B+EC":0, "D+EC":0, "B+D+EC":0} 

for value in resp_seq.values(): 
    #print(value)
    resp_seq_vendiagram[value] += 1 
        
        
print(resp_seq_vendiagram)


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
        a.pop()
        ##print(a)
        ##print(len(a))
        mylist.append(a)
        i += 1 
        ##if i == 1:
        ##    break




##print(mylist)





df_ec = pd.DataFrame(mylist, columns = ["RESP#", "Mother's Age When Born", "Mother Smoked When Pregnant", \
"Weight At Birth", "Weight More/Less than 5.5lbs", "Weight More/Less than 9.0lbs"])
print(df_ec)


# Load Blood Pressure data into dataframe
'''
 
'''
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
print(df_bp)


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

print(df_d)




# Merge the datasets together 

ec_bp_merge = pd.merge(left=df_ec, right=df_bp, left_on='RESP#', right_on='RESP#', how = 'inner')

print(ec_bp_merge.shape)



