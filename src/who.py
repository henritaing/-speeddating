import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px


data = pd.read_csv("res\\Speed Dating Data.csv", encoding="ISO-8859-1", sep=',')


# Gender distribution

gender_column = data.loc[:, 'gender']

nb_participants = gender_column.count()
nb_men = gender_column[gender_column == 1].count()  
nb_women = (nb_participants - nb_men)
gender_values = [nb_men/nb_participants, nb_women/nb_participants]
genders = ['Men', 'Women']

plt.pie(gender_values, labels = genders, wedgeprops=dict(width=0.6), startangle=-90, 
        colors=['lightpink', 'palegreen'], autopct='%1.1f%%', labeldistance=1.1, pctdistance=0.7)
plt.show()


# Race distribution

races_column = data.loc[:, 'race']

races_values = data.groupby('race').size().reset_index(name='count') 
races_values['count'] = races_values['count']/nb_participants 
races = ['Black/African American', 'European/Caucasian-American', 'Latino/Hispanic American', 
         'Asian/Pacific Islander/Asian-American', 'Other']

plt.pie(races_values['count'], labels = races, wedgeprops=dict(width=0.6), startangle=-90, 
        colors=['azure', 'gold','lightblue', 'pink', 'salmon'], autopct='%1.0f%%', labeldistance=1.1, 
        pctdistance=0.7)
plt.show()


# Most represented field of study/work?

field_cd_column = data['field_cd']

field_cd = field_cd_column.dropna()
field = field_cd.value_counts()
field = field.reset_index()
top = field.head(5)
top_5 = ['Business/Econ/Finance', 'Bio/Chemistry/Physics', 'Engineering', 'Politics', 'Sociology']
top_5_values_in_percent = list((top['count']/nb_participants))
rounded_values = [str(int(round(value, 2)*100)) + "%" for value in top_5_values_in_percent]

fig, ax = plt.subplots()
bars = ax.bar(top_5, top_5_values_in_percent, 
              color=['k', 'darkslategrey', 'teal', 'lightseagreen', 'mediumaquamarine'])
plt.xticks(rotation = 35)

for bar, value in zip(bars, rounded_values):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height()/2, f'{value}', ha='center', 
             va='bottom', fontsize = 12, fontweight='bold', color='white')

plt.show()