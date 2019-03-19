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
#created a filtered  Bay Area dataframe that only contains rows where companies appeared in WARN

filtered_bayarea=pd.DataFrame()

for x in range((len(commoncompany))):
    for i in range((len(bayarea))):
        #print(bayarea.iloc[i,19])
        if(type(commoncompany[x]) is str and type(bayarea.iloc[i,19]) is str):
            #print("Warn=",commoncompany[x].lower(), "||Bay=", bayarea.iloc[i,19].lower())
            if(bayarea.iloc[i,19].lower() in commoncompany[x].lower()):
                #print("match")
                filtered_bayarea = filtered_bayarea.append(bayarea.iloc[i])

print(len(filtered_bayarea))

#created a filtered WARN dataframe that only contains data of companies that appeared in Bayarea
filtered_warn=warn[warn['Company Name'].isin(commoncompany)]
print(len(filtered_warn))

#change to date format
filtered_warn['Layoff Date'] = pd.to_datetime(filtered_warn['Layoff Date'],infer_datetime_format=True)

#drop the bay area data where the person is still employed
filtered_bayarea_LayOff = filtered_bayarea[bayarea['CurrentEmployFlag'] != True]

#chage to date format
filtered_bayarea_LayOff['End Date'] = pd.to_datetime(filtered_bayarea_LayOff['End Date'],infer_datetime_format=True)

#create 3 new columns to combine WARN and bayarea datasets
filtered_bayarea_LayOff['WARN_location'] = np.nan
filtered_bayarea_LayOff['WARN_EmployeesAffected'] = np.nan
filtered_bayarea_LayOff['WARN_Layoff Date'] = np.nan

#merge the 2 datasets as long as layoff dates are less than 1 month apart
for x in range((len(filtered_warn))):
    # print("Warn=",filtered_warn.iloc[x,1].lower())
    for i in range((len(filtered_bayarea_LayOff))):

        if (type(filtered_warn.iloc[x, 1]) is str and type(filtered_bayarea_LayOff.iloc[i, 2]) is str):
            # print("Warn=",filtered_warn.iloc[x,1].lower(), "||Bay=", filtered_bayarea_LayOff.iloc[i,2].lower())
            if (filtered_bayarea_LayOff.iloc[i, 2].lower() in filtered_warn.iloc[x, 1].lower()):
                # print("match")
                # print(i)
                if ((filtered_bayarea_LayOff.iloc[i]['End Date'] - filtered_warn.iloc[x]['Layoff Date']) / np.timedelta64(1, 'M') < 1):
                    filtered_bayarea_LayOff.iloc[i]['WARN_location'] = filtered_warn.iloc[x]['Location']
                    filtered_bayarea_LayOff.iloc[i]['WARN_EmployeesAffected'] = filtered_warn.iloc[x]['Employees Affected']
                    filtered_bayarea_LayOff.iloc[i]['WARN_Layoff Date'] = filtered_warn.iloc[x]['Layoff Date']


#drop rows where the WARN data are not populated
filtered_bayarea_LayOff=filtered_bayarea_LayOff.dropna(subset=['WARN_location','WARN_EmployeesAffected','WARN_Layoff Date'],how='all')
print(len(filtered_bayarea_LayOff))

