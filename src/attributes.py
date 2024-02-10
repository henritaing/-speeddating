import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px


data = pd.read_csv("res\\Speed Dating Data.csv", encoding="ISO-8859-1", sep=',')

data_eval = data.loc[:, ['gender', 'attr1_1', 'sinc1_1', 'intel1_1', 'fun1_1', 'amb1_1', 'shar1_1', 
                         'attr2_1', 'sinc2_1', 'intel2_1', 'fun2_1', 'amb2_1', 'shar2_1', 'attr3_1', 
                         'sinc3_1', 'intel3_1', 'fun3_1', 'amb3_1', 'attr4_1', 'sinc4_1', 'intel4_1', 
                         'fun4_1', 'amb4_1', 'shar4_1', 'attr5_1', 'sinc5_1', 'intel5_1', 'fun5_1', 'amb5_1']]
data_men = data_eval[data_eval['gender'] == 1]
data_women = data_eval[data_eval['gender'] == 0]
qualities = ['Attractive', 'Sincere', 'Intelligent', 'Fun', 'Ambitious', 'Shared Interests']
data_men_avg = data_men.mean()
data_women_avg = data_women.mean()


# Comparison 1: women vs men - What do they look for?

data_men_1 = [data_men_avg['attr1_1'], data_men_avg['sinc1_1'], data_men_avg['intel1_1'], 
              data_men_avg['fun1_1'], data_men_avg['amb1_1'], data_men_avg['shar1_1']]
criterias1 = ['attr1_1', 'sinc1_1', 'intel1_1', 'fun1_1', 'amb1_1', 'shar1_1']
data_women_1 = [data_women_avg[column] for column in criterias1]

df1_men = pd.DataFrame({'qualities': qualities, 'r': data_men_1})
df1_men = pd.concat([df1_men, df1_men.iloc[[0]]], ignore_index=True)
df1_women = pd.DataFrame({'qualities': qualities, 'r': data_women_1})
df1_women = pd.concat([df1_women, df1_women.iloc[[0]]], ignore_index=True)

fig = go.Figure()
fig.add_trace(go.Scatterpolar(r=df1_men['r'], theta=df1_men['qualities'], fill='toself', 
                              fillcolor='rgba(255, 182, 193, 0.5)', line=dict(color='pink'), name='men'))
fig.add_trace(go.Scatterpolar(r=df1_women['r'], theta=df1_women['qualities'], fill='toself', 
                              fillcolor='rgba(173, 216, 230, 0.5)', line=dict(color='lightblue'), name='women'))
fig.update_layout(polar=dict(radialaxis=dict(range=[0, 40])))
fig.show()


# Comparison 2 - What do men look for ? What do they think their fellow men look for? And what do they think the opposite sex look for? 

criterias4 = ['attr4_1', 'sinc4_1', 'intel4_1', 'fun4_1', 'amb4_1', 'shar4_1']     # fellow
data_men_4 = [data_men_avg[column] for column in criterias4]
df4_men = pd.DataFrame({'qualities': qualities, 'r': data_men_4})
df4_men = pd.concat([df4_men, df4_men.iloc[[0]]], ignore_index=True)

criterias2 = ['attr2_1', 'sinc2_1', 'intel2_1', 'fun2_1', 'amb2_1', 'shar2_1']     # opposite
data_men_2 = [data_men_avg[column] for column in criterias2]
df2_men = pd.DataFrame({'qualities': qualities, 'r': data_men_2})
df2_men = pd.concat([df2_men, df2_men.iloc[[0]]], ignore_index=True)

fig = go.Figure()
fig.add_trace(go.Scatterpolar(r=df1_men['r'], theta=df1_men['qualities'], fill='toself', 
                              fillcolor='rgba(255, 182, 193, 0.5)', line=dict(color='pink'), name='men'))
fig.add_trace(go.Scatterpolar(r=df4_men['r'], theta=df4_men['qualities'], fill='toself', 
                              fillcolor='rgba(255, 105, 180, 0.3)', line=dict(color='violet'), name='fellow men'))
fig.add_trace(go.Scatterpolar(r=df2_men['r'], theta=df2_men['qualities'], fill='toself', 
                              fillcolor='rgba(255, 30, 150, 0.3)', line=dict(color='red'), name='opposite sex looks for'))
fig.update_layout(polar=dict(radialaxis=dict(range=[0, 40])))
fig.show()


# Comparison 3 - What do women look for ? What do they think their fellow women look for? And what do they think the opposite sex look for?

data_women_4 = [data_women_avg[column] for column in criterias4]     # fellow
df4_women = pd.DataFrame({'qualities': qualities, 'r': data_women_4})
df4_women = pd.concat([df4_women, df4_women.iloc[[0]]], ignore_index=True)

data_women_2 = [data_women_avg[column] for column in criterias2]     # opposite
df2_women = pd.DataFrame({'qualities': qualities, 'r': data_women_2})
df2_women = pd.concat([df2_women, df2_women.iloc[[0]]], ignore_index=True)

fig = go.Figure()
fig.add_trace(go.Scatterpolar(r=df1_women['r'], theta=df1_women['qualities'], fill='toself', 
                              fillcolor='rgba(173, 216, 230, 0.5)', line=dict(color='lightblue'), name='women'))
fig.add_trace(go.Scatterpolar(r=df4_women['r'], theta=df4_women['qualities'], fill='toself', 
                              fillcolor='rgba(0, 102, 204, 0.4)', line=dict(color='blue'), name='fellow women'))
fig.add_trace(go.Scatterpolar(r=df2_women['r'], theta=df2_women['qualities'], fill='toself', 
                              fillcolor='rgba(0, 76, 153, 0.2)', line=dict(color='darkslategray'), 
                              name='opposite sex looks for'))
fig.update_layout(polar=dict(radialaxis=dict(range=[0, 40]))) 
fig.show()


# Comparison 4 - What do men think they look for (before the event)? What do they chose in reality (halfway)? What's the result at the end (after)?

data_s = data.loc[:, ['gender', 'attr1_s', 'sinc1_s', 'intel1_s', 'fun1_s', 'amb1_s', 'shar1_s']]     # Halfway
data_s_men = data_s[data_s['gender'] == 1]
df_s_men = data_s_men.dropna()
data_men_avg_s = df_s_men.mean()
values_s_men = list(data_men_avg_s)
values_s_men.pop(0) 
df_s_men = pd.DataFrame({'qualities': qualities, 'r': values_s_men})
df_s_men = pd.concat([df_s_men, df_s_men.iloc[[0]]], ignore_index=True)

data_after = data.loc[:, ['gender', 'attr7_2', 'sinc7_2', 'intel7_2', 'fun7_2', 'amb7_2', 'shar7_2']]     # After
data_m_avg_after = data_after[data_after['gender'] == 1]
data_m_avg_after = list(data_m_avg_after.dropna().mean())
data_m_avg_after.pop(0)
dfs_after_men = pd.DataFrame({'qualities': qualities, 'r': data_m_avg_after})
dfs_after_men = pd.concat([dfs_after_men, dfs_after_men.iloc[[0]]], ignore_index=True)

fig = go.Figure()
fig.add_trace(go.Scatterpolar(r=df1_men['r'], theta=df1_men['qualities'], fill='toself', 
                              fillcolor='rgba(255, 182, 193, 0.5)', line=dict(color='pink'), name='men'))
fig.add_trace(go.Scatterpolar(r=df_s_men['r'], theta=df_s_men['qualities'], fill='toself', 
                              fillcolor='rgba(255, 182, 193, 0.5)', line=dict(color='violet'), name='reality'))
fig.add_trace(go.Scatterpolar(r=dfs_after_men['r'], theta=dfs_after_men['qualities'], fill='toself', 
                              fillcolor='rgba(255, 150, 171, 0.5)', line=dict(color='purple'), name='after man'))
fig.update_layout(polar=dict(radialaxis=dict(range=[0, 40])))
fig.show()


# Comparison 5 - What do women think they look for (before the event)? What do they chose in reality (halfway)? What's the result at the end (after)?

data_s_women = data_s[data_s['gender'] == 0]     # Halfway
df_s_women = data_s_women.dropna()
data_women_avg_s = df_s_women.mean()
values_s_women = list(data_women_avg_s)
values_s_women.pop(0) 
df_s_women = pd.DataFrame({'qualities': qualities, 'r': values_s_women})
df_s_women = pd.concat([df_s_women, df_s_women.iloc[[0]]], ignore_index=True)

data_after_w = data_after[data_after['gender'] == 0]     # After
data_after_w = data_after_w.dropna()
data_w_avg_after = data_after_w.mean()
values_after_women = list(data_w_avg_after)
values_after_women.pop(0) 
dfs_after_women = pd.DataFrame({'qualities': qualities, 'r': values_after_women})
dfs_after_women = pd.concat([dfs_after_women, dfs_after_women.iloc[[0]]], ignore_index=True)
fig = go.Figure()

fig.add_trace(go.Scatterpolar(r=df1_women['r'], theta=df1_women['qualities'], fill='toself', 
                              fillcolor='rgba(173, 216, 230, 0.5)', line=dict(color='lightblue'), name='women'))
fig.add_trace(go.Scatterpolar(r=df_s_women['r'], theta=df_s_women['qualities'], fill='toself', 
                              fillcolor='rgba(0, 102, 204, 0.4)', line=dict(color='blue'), name='reality'))
fig.add_trace(go.Scatterpolar(r=dfs_after_women['r'], theta=dfs_after_women['qualities'], fill='toself', 
                              fillcolor='rgba(0, 76, 153, 0.2)', line=dict(color='darkslategray'), name='after'))
fig.update_layout(polar=dict(radialaxis=dict(range=[0, 40])))
fig.show()


# Comparison 6 - Men vs Women after the event

fig = go.Figure()
fig.add_trace(go.Scatterpolar(r=dfs_after_men['r'], theta=dfs_after_men['qualities'], fill='toself', 
                              fillcolor='rgba(255, 150, 171, 0.5)', line=dict(color='violet'), name='after man'))
fig.add_trace(go.Scatterpolar(r=dfs_after_women['r'], theta=dfs_after_women['qualities'], fill='toself', 
                              fillcolor='rgba(0, 76, 153, 0.2)', line=dict(color='darkslategray'), name='after woman'))
fig.update_layout(polar=dict(radialaxis=dict(range=[0, 40])))
fig.show()


# Comparison 7 - Men's decision after the event and what women thought men looked for

fig = go.Figure()
fig.add_trace(go.Scatterpolar(r=dfs_after_men['r'], theta=dfs_after_men['qualities'], fill='toself', 
                              fillcolor='rgba(255, 150, 171, 0.5)', line=dict(color='violet'), name='after man'))
fig.add_trace(go.Scatterpolar(r=df2_women['r'], theta=df2_women['qualities'], fill='toself', 
                              fillcolor='rgba(0, 76, 153, 0.2)', line=dict(color='darkslategray'), name='(men) opposite sex looks for'))
fig.update_layout(polar=dict(radialaxis=dict(range=[0, 40])))
fig.show()