import pandas as pd
warn = pd.read_csv('../Data/WARN/warn.csv')
warn.isna().sum()
#Source: https://www.bizdetail.com/list-of-bay-area-cities-copy-paste/
bay_area_cities = ["Alameda",
"Albany",
"American Canyon",
"Antioch",
"Atherton",
"Belmont",
"Belvedere",
"Benicia",
"Berkeley",
"Brisbane",
"Burlingame",
"Campbell",
"Clayton",
"Colma",
"Concord",
"Corte Madera",
"Cupertino",
"Daly City",
"Danville",
"Dublin",
"East Palo Alto",
"El Cerrito",
"Emeryville",
"Fairfax",
"Foster City",
"Fremont",
"Gilroy",
"Half Moon Bay",
"Hayward",
"Healdsburg",
"Hercules",
"Hillsborough",
"Lafayette",
"Larkspur",
"Livermore",
"Los Altos",
"Los Altos Hills",
"Los Gatos",
"Martinez",
"Menlo Park",
"Mill Valley",
"Millbrae",
"Milpitas",
"Moraga",
"Morgan Hill",
"Mountain View",
"Newark",
"Novato",
"Oakland",
"Oakley",
"Orinda",
"Pacifica",
"Palo Alto",
"Petaluma",
"Piedmont",
"Pinole",
"Pittsburg",
"Pleasanton",
"Redwood City",
"Richmond",
"Rohnert Park",
"Ross",
"Helena",
"San Anselmo",
"San Bruno",
"San Carlos",
"San Francisco",
"San Jose",
"San Leandro",
"San Mateo",
"San Pablo",
"San Rafael",
"San Ramon",
"Santa Clara",
"Santa Rosa",
"Saratoga",
"Sausalito",
"Sebastopol",
"Sonoma",
"South San Francisco",
"Suisun City",
"Sunnyvalle",
"Tiburon",
"Union City",
"Vallejo",
"Walnut Creek",
"Windsor",
"Woodside"]

bay_area_cities = [x.upper() for x in bay_area_cities]
warn['Location'] = [i.upper() for i in warn['Location']]
warn_bay_area = warn.loc[warn['Location'].isin(bay_area_cities)]
print("Number of unique company names: ", len(warn_bay_area["Company Name"].unique()))

#warn_bay_area.to_csv('../Data/WARN/warn_bay_area.csv')

# Summing  # of employees across different branches
summary_w_date = warn_bay_area.groupby(['Company Name', 'Layoff Date']).sum().reset_index()
summary_w_date.head(10)
#summary_w_date.to_csv('../Data/WARN/summary_w_date.csv')

import string
# Group the number of laid off employees acorss different branches under different layoff events from the same company
summary_wo_date = summary_w_date.groupby(['Company Name']).sum().reset_index()
summary_wo_date.head(10)
