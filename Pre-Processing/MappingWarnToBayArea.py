import pandas as pd
import numpy as np

#Storing data
bayarea=pd.read_csv(r"C:\Users\whatr\BayArea\bay_area.csv", sep = "\t",nrows=10000)
warn=pd.read_csv(r"C:\Users\whatr\BayArea\warn_bay_area.csv")
colnames=['ID', 'Birth Year', 'Gender Flag', 'Skillset1', 'Skillset1 Weight', 'Skillset2', 'Skillset2 Weight', 'City of profile','Country of profile','Education','Elite Institution', 'Start Date', 'StartFlag','End Date', 'EndFlag', 'CurrentEmployFlag','Length','Role','Dept','Company','Company_Norm','Ticker','Exchange','PublicFlag','Location','Industry','EducationFlag','DegreeType','EliteFlag','Dummy1','Dummy2','Dummy3','Dummy4']
bayarea.columns=colnames
#If skillset weight1 and weight2 are empty, then remove the row
listdrop=[]
for i in range(len(bayarea)):
    if(bayarea.iloc[i,3]=='-1') and (bayarea.iloc[i,5]=='-1'):
        listdrop.append(i)

bayarea=bayarea.drop(bayarea.index[[listdrop]])
#Converting company names to list
bay_area_company=bayarea['Company']
bay_area_company=bay_area_company.tolist()
warn_company=warn['Company Name']
warn_company=warn_company.tolist()

#cleaning strings in bay_area_company to make it easier to compare
temp=bay_area_company
for x in range(len(temp)):
    if(type(temp[x]) is str):
        temp[x]=temp[x].lower()
        temp[x]=temp[x].lstrip()
        temp[x]=temp[x].rstrip()

commoncompany=[]
for x in range((len(warn_company))):
    for y in range((len(temp))):
        if(type(warn_company[x]) is str and type(temp[y]) is str):
            if(warn_company[x].lower() in temp[y] or temp[y] in warn_company[x].lower()):
                commoncompany.append(warn_company[x])

#only store unique values in commoncompany
output = []
for x in commoncompany:
    if x not in output:
        output.append(x)
print(output)


####################################
#only keep rows where companies appeared in WARN

listkeep=[]

for i in range((len(bayarea))):
    for x in range((len(commoncompany))):
        if(type(commoncompany[x]) is str and type(bayarea.iloc[i,19]) is str):
            if(bayarea.iloc[i,19].lower() in commoncompany[x].lower()):
                listkeep.append(i)


#only keep unique index
listkeep = list(set(listkeep))
listkeep.sort()
bayarea=bayarea.iloc[listkeep,:]


#drop the bay area data where the person is still employed
bayarea = bayarea[bayarea['CurrentEmployFlag'] != True]
print(len(bayarea))

#chage to date format
bayarea['End Date'] = pd.to_datetime(bayarea['End Date'],infer_datetime_format=True)


#created a filtered WARN dataframe that only contains data of companies that appeared in Bayarea
filtered_warn=warn[warn['Company Name'].isin(commoncompany)]
print(len(filtered_warn))

#change to date format
filtered_warn['Layoff Date'] = pd.to_datetime(filtered_warn['Layoff Date'],infer_datetime_format=True)


#create 3 new columns to combine WARN and bayarea datasets
bayarea['WARN_location'] = np.nan
bayarea['WARN_EmployeesAffected'] = np.nan
bayarea['WARN_LayoffDate'] = np.nan

#merge the 2 datasets as long as layoff dates are less than 1 month apart
for i in range((len(bayarea))):
    for x in range((len(filtered_warn))):
        if (type(filtered_warn.iloc[x, 1]) is str and type(bayarea.iloc[i, 19]) is str):
            if (bayarea.iloc[i, 19].lower() in filtered_warn.iloc[x, 1].lower()):
                if (abs((bayarea.iloc[i]['End Date'] - filtered_warn.iloc[x]['Layoff Date']) / np.timedelta64(1,'M')) < 1):
                    bayarea.WARN_location.iloc[[i]] = filtered_warn.iloc[x]['Location']
                    bayarea.WARN_EmployeesAffected.iloc[[i]] = filtered_warn.iloc[x]['Employees Affected']
                    bayarea.WARN_LayoffDate.iloc[[i]] = filtered_warn.iloc[x]['Layoff Date']

#drop rows where the WARN data are not populated
bayarea=bayarea.dropna(subset=['WARN_location','WARN_EmployeesAffected','WARN_LayoffDate'],how='all')
print(len(bayarea))

