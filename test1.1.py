import pandas as pd
df={
"mpg":[18,15,18,16,17],"cylinders":[8,8,6,4,8],"displacement":[307,350,318,304,302],
"horsepower":[130,165,150,150,140],"weigth":[3504,3693,3436,3433,3449],
"acceleration":[12.0,11.5,11.0,12.0,10.5],"model year":[70,71,70,80,70],
"origin":[1,1,1,1,1],"car name":["cheverlot","buick","plymoth","amc","ford"]
}
dp=pd.DataFrame(df)
sa=dp.describe()
ei=dp[dp["cylinders"]==8]
ye = dp.groupby('model year')["model year"].count()
print("Satistical:\n",sa)
print("\n8 cylinders:\n",ei)
print("\nBy year:\n",ye)
