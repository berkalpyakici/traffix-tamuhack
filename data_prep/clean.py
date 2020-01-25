'''
Lucas Atayde, Alp Burke

File responsible for cleaning up our data pipeline. This will prepare our API to query the
data.
'''

import pandas as pd

usaa = pd.read_csv("data_prep/raw/US_Accidents_Dec19.csv", skiprows=range( int(2974335 * .01), 2974335))
# usaa = pd.read_csv("data_prep/raw/US_Accidents_Dec19.csv")

# Step 1: Convert accident ids to integers
usaa["ID"] = usaa["ID"].apply(lambda id: int(id[2:]))

# Drop unnecessary data. Makes computation slower and adds noise
usaa = usaa.drop(columns="Source")




