import pandas as pd
import plotly.express as px 


#reading files df = data frame
df=pd.read_csv("Covid.csv")
fig=px.scatter(df, x ='date',y='cases',color="country")
fig.show()