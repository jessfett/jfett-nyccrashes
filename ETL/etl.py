import pandas as pd
import csv
from sqlalchemy import create_engine

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import numpy as np


file_one = "Data/2020Crashes.csv" 

crashes2020 = pd.read_csv(file_one, encoding="ISO-8859-1") 

crashes2020.head()

del crashes2020['ON STREET NAME']
del crashes2020['CROSS STREET NAME']
del crashes2020['OFF STREET NAME']
del crashes2020['CONTRIBUTING FACTOR VEHICLE 3']
del crashes2020['CONTRIBUTING FACTOR VEHICLE 4']
del crashes2020['CONTRIBUTING FACTOR VEHICLE 5']
del crashes2020['VEHICLE TYPE CODE 3']
del crashes2020['VEHICLE TYPE CODE 4']
del crashes2020['VEHICLE TYPE CODE 5']

crashes2020

crashes2020 = crashes2020[crashes2020['BOROUGH'].notna()]
crashes2020 = crashes2020[crashes2020['LATITUDE'].notna()]
crashes2020 = crashes2020[crashes2020['LONGITUDE'].notna()]

crashes2020

del crashes2020['CONTRIBUTING FACTOR VEHICLE 2']
del crashes2020['VEHICLE TYPE CODE 2']

crashes2020_df = crashes2020.rename(columns={"CRASH DATE":"CrashDate", "CRASH TIME": "CrashTime", "ZIP CODE": "ZipCode",
                                            "NUMBER OF PERSONS INJURED": "PersonsInjured", "NUMBER OF PERSONS KILLED": "PersonsKilled",
                                            "NUMBER OF PEDESTRIANS INJURED": "PedestriansInjured", "NUMBER OF PEDESTRIANS KILLED": "PedestriansKilled", 
                                            "NUMBER OF CYCLIST INJURED": "CyclistInjured", "NUMBER OF CYCLIST KILLED": "CyclistKilled",
                                            "NUMBER OF MOTORIST INJURED": "MotoristInjured", "NUMBER OF MOTORIST KILLED": "MotoristKilled",
                                            "CONTRIBUTING FACTOR VEHICLE 1": "ContributingFactor", "VEHICLE TYPE CODE 1": "VehicleType"})


crashes2020_df

crashes2020_df = crashes2020_df.rename(columns={"BOROUGH":"Borough", "LATITUDE": "Latitude", "LONGITUDE": "Longitude", 
                                                "LOCATION": "Location", "COLLISION_ID": "CollisionID"})

crashes2020_df

del crashes2020_df['Location']

crashes2020_df["CrashDate"] = pd.to_datetime(crashes2020_df["CrashDate"]).dt.strftime('%Y-%m-%d')
print(crashes2020_df)

crashes2020_df.head()

del crashes2020_df['ZipCode']

crashes2020_df

crashes2020_df=crashes2020_df.round({'Latitude': 4, 'Longitude': 4})

crashes2020_df

crashes2020_df.to_csv("Data/NYC2020crashes.csv", index=False, header=True)

crashes2020_df.to_json(r'Path to store the exported JSON file\File Name.json')

crashes2020_df

crash_count = crashes2020_df.groupby(['Borough']).count()
crash_count

crash_count = crash_count.rename(columns={"CrashDate": "CrashCount"})

del crash_count['CrashTime']
del crash_count['Latitude']
del crash_count['Longitude']
del crash_count['PersonsInjured']
del crash_count['PersonsKilled']
del crash_count['PedestriansInjured']
del crash_count['PedestriansKilled']
del crash_count['CyclistInjured']
del crash_count['CyclistKilled']
del crash_count['MotoristInjured']
del crash_count['MotoristKilled']
del crash_count['ContributingFactor']
del crash_count['CollisionID']
del crash_count['VehicleType']

crashcount = crash_count.reset_index()

crashcount.to_csv("Data/CrashCount.csv", index=False, header=True)

crash_impact = crashes2020_df.groupby(['Borough']).sum()
crash_impact

del crash_impact['Latitude']
del crash_impact['Longitude']
del crash_impact['CollisionID']

crashimpact = crash_impact.reset_index()

crashimpact.to_csv("Data/CrashImpacts.csv", index=False, header=True)

