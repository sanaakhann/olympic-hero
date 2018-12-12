# --------------
#Code starts here
best=data[data['Country_Name']==best_country]

best=best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar(stacked=True)

plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


# --------------
#Code starts here
top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries=top_countries.drop(top_countries.index[len(top_countries)-1])

def top_ten(top_countries,Cols):
    country_list=[]
    tp=top_countries.nlargest(10,Cols)
    country_list=list(tp.iloc[:,0])
    return country_list
   



top_10_summer=top_ten(top_countries,'Total_Summer')
top_10_winter=top_ten(top_countries,'Total_Winter')
top_10=top_ten(top_countries,'Total_Medals')

common=list(set(top_10_summer) & set(top_10_winter) & set(top_10))
type(common)


# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here

#Reading the file
data=pd.read_csv(path)

#Renaming a column
data.rename(columns={'Total':'Total_Medals'},inplace=True)

#Printing the first five columns
print(data.head(10))




# --------------
#Code starts here
import numpy as np
import pandas as pd

Summer_or_Winter=np.where(data['Total_Summer']>=data['Total_Winter'],'Summer','Winter')

data['Better_Event']=np.where(data['Total_Summer']==data['Total_Winter'],'Both',Summer_or_Winter)

print(data['Better_Event'].value_counts())

better_event='Summer'


# --------------
#Code starts here
import matplotlib.pyplot as plt

summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]

c_name=summer_df.iloc[:,0]
sum_medal=summer_df.loc[:,'Total_Summer']
plt.xlabel('Country Names')
plt.ylabel('Total Medals')
plt.title('For Summer Events')
plt.bar(c_name,sum_medal)
plt.xticks(rotation=90)


c1_name=winter_df.iloc[:,0]
sum1_medal=winter_df.loc[:,'Total_Winter']
plt.xlabel('Country Names')
plt.ylabel('Total Medals')
plt.title('For Winter Events')
plt.bar(c1_name,sum1_medal)
plt.xticks(rotation=90)


c2_name=top_df.iloc[:,0]
sum2_medal=top_df.loc[:,'Total_Medals']
plt.xlabel('Country Names')
plt.ylabel('Total Medals')
plt.title('For Top Events')
plt.bar(c2_name,sum2_medal)
plt.xticks(rotation=90)




# --------------
#Code starts here
#for summer_df
summer_df['Golden_Ratio']=summer_df.loc[:,'Gold_Summer']/summer_df.loc[:,'Total_Summer']
#print(summer_df['Golden_Ratio'])
summer_max_ratio=summer_df['Golden_Ratio'].max()
print(summer_max_ratio)
#in simple form
summer_country_gold='China'
print(summer_country_gold)
#using code
#summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'] == summer_max_ratio, 'Country_Name']


#for winter_df

winter_df['Golden_Ratio']=winter_df.loc[:,'Gold_Winter']/winter_df.loc[:,'Total_Winter']
#print(winter_df['Golden_Ratio'])
winter_max_ratio=winter_df['Golden_Ratio'].max()
print(winter_max_ratio)
#in simple
winter_country_gold='Soviet Union'
print(winter_country_gold)
#using code
#winter_country_gold=winter_df.loc[winter_df['Golden_Ratio'] == winter_max_ratio,'Country_Name']



#for top_df

top_df['Golden_Ratio']=top_df.loc[:,'Gold_Total']/top_df.loc[:,'Total_Medals']
#print(top_df['Golden_Ratio'])
top_max_ratio=top_df['Golden_Ratio'].max()
print(top_max_ratio)
#in simple
top_country_gold='China'
print(top_country_gold)
#using code
#top_country_gold=top_df.loc[top_df['Golden_Ratio'] == top_max_ratio,'Country_Name']



# --------------
#Code starts here
#dropping last row of data
data_1=data.drop(data.index[len(data)-1])
#print(data_1)

#including new column and calculating points
data_1['Total_Points']=(data_1.loc[:,'Gold_Total']*3)+(data_1.loc[:,'Silver_Total']*2)+(data_1.loc[:,'Bronze_Total']*1)

most_points=data_1['Total_Points'].max()

#found country name with the help of code
#best_country=data_1.loc[data_1.Total_Points == most_points].Country_Name.values

#in simple form
best_country='United States'




