import pandas as pd
import matplotlib.pyplot as plt
import csv


import pandas as pd
import matplotlib.pyplot as plt

from e1 import *

df_list=[]
for Year in range (1924, 2016, 4):
    Year = int(Year)


    FILE_NAME = 'Presidential_General' + line[0] + ".csv"
    header = pd.read_csv(file_name, nrows=1).dropna(axis=1)
    d=header.iloc[0].to_dict()

    df = pd.read_csv(FILE_NAME, index_col = 0, thousands = ",", skiprows = [1])

    df.rename(inplace = True, columns = d) # rename to democrat/republican
    df.dropna(inplace = True, axis = 1)    # drop empty columns
    df["Year"] = Year
    df_list.append(df[["Democratic", "Republican", "Total Votes Cast", "Year"]])

VOTES = pd.concat(df_list)
VOTES["Republican Share"] = VOTES["Republican"]/ VOTES["Total Votes Cast"]


VOTES.loc[["Accomack County"]].plot(kind="line", x="Year", y="Republican Share")
plt.savefig('accomack_county.pdf')
#albemarle_county.pdf`, `alexandria_city.pdf`, and `alleghany_county.pdf`

VOTES.loc[["Accomack County"]].plot(kind="line", x="Year", y="Republican Share")
plt.savefig('accomack_county.pdf')

VOTES.loc[["Albemarle County"]].plot(kind="line", x="Year", y="Republican Share")
plt.savefig('albemarle_county.pdf')

VOTES.loc[["Alexandria City"]].plot(kind="line", x="Year", y="Republican Share")
plt.savefig('alexandria_city.pdf')

VOTES.loc[["Alleghany County"]].plot(kind="line", x="Year", y="Republican Share")
plt.savefig('alleghany_county.pdf')

#Unable to repeat the county Republican vote share per election year - showcasing first year



#df.rename(inplace = True, columns = d) # rename to democrat/republican
#df.dropna(inplace = True, axis = 1)    # drop empty columns
#df["Year"] = 2004
