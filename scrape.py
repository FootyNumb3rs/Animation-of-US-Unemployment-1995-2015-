import pandas as pd

url = 'https://www.bls.gov/lau/laucnty{}.xlsx'
dfs = []

urls = [url.format(str(dig)[2:]) for dig in range(1990,2017)]

for u in urls:
    #print(pd.read_excel(u)[5:])
    dfs.append(pd.read_excel(u)[5:])

print(pd.concat(dfs))
