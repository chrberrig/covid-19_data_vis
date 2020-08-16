#!/bin/python

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

confirmed_df = pd.read_csv("COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
deaths_df = pd.read_csv("COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")

countries_list = ["Denmark","Sweden"]
filt = confirmed_df["Country/Region"].isin(countries_list) # & ~ confirmed_df["Province/State"].isnull()
 
def clean_df(df):
	# state_filt = ~ df["Province/State"].isnull()
	# df["Area"] = np.where(state_filt, df["Country/Region"] + " (" + df["Province/State"] + ")", df["Country/Region"])
	# df.drop(columns=["Country/Region", "Province/State"], inplace=True)
	df.drop(columns=["Lat", "Long"], inplace=True)
	return df.groupby(["Country/Region"])

# print(confirmed_df.columns)
# print(confirmed_df.loc[filt, "Country/Region"])
country_grp = clean_df(confirmed_df)
print(country_grp["Province/State"].head(10))
# print(country_grp.get_group("Denmark"))
# print(country_grp.apply(lambda x: x.sum()).loc["Denmark"])
# print(confirmed_df.columns)
# print(confirmed_df.index)
# print(confirmed_df.loc[filt, "Area"])

