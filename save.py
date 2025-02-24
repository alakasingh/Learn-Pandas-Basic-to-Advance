# How to save the data from different-diff formate

import pandas as pd

data = {
  "name":["alaka", "radha", "madhav"],
  "age": ['20','23','30'],
  "Adress":["varansi","brsana","virndavam"]
   
}

df = pd.DataFrame(data)
print(df)   

# have a look to save the data into different-diff formate

# into csv formate 
df.to_csv("output.csv" , index = False)

# into excel formate (if occur any error to run bellow line then install required module - pip install openpyxl)
# df.to_excel("output.xlsx" , index = False)

#into json formate
# df.to_json("output.json", index=False)
