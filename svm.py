import streamlit as st
# handle missing data (delete column in df)
newdata = pd.DataFrame(data)
del newdata['AcceptedCmp1']
del newdata['AcceptedCmp2']
del newdata['AcceptedCmp3']
del newdata['AcceptedCmp4']
del newdata['AcceptedCmp5']
del newdata['marital_Divorced']
del newdata['marital_Married']
del newdata['marital_Single']
del newdata['marital_Together']
del newdata['marital_Widow']
del newdata['education_Basic']
del newdata['education_Graduation']
del newdata['education_Master']
del newdata['education_PhD']
del newdata['MntWines']
del newdata['MntFruits']
del newdata['MntMeatProducts']
del newdata['MntFishProducts']
del newdata['MntSweetProducts']
del newdata['MntGoldProds']
del newdata['Customer_Days']
del newdata['education_2n Cycle']
del newdata['Z_CostContact']
del newdata['Z_Revenue']




# check again the null value to ensure it already drop the column
newdata.isnull().any()
