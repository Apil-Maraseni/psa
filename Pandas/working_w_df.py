import pandas as pd

data = {
    'name':['Bart','Lisa','Homer','Marge'],
    'age':[10,8,39,36],
    'phone_number':['939-555-0113','939-555-0114','939-555-0115','939-555-0116'],
    'astrological_sign':['Taurus','Vigro','Taurus','Pisces']
}

df = pd.DataFrame(data)
print(df)