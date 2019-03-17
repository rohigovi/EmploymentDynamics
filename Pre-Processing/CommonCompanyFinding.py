
import pandas as pd
#Storing data
bayarea=pd.read_csv(r"C:\Users\Rohit\Desktop\RequiredData\bay_area.csv", sep = "\t",nrows=10000)
warn=pd.read_csv(r"C:\Users\Rohit\Desktop\RequiredData\warn_bay_area.csv")
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
