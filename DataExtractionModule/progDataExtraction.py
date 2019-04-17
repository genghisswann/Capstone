#THIS MODULE WILL PROGRAMMATICALLY DOWNLOAD AND SAVE ALL FITBIT DATA
#SECOND MODULE PLOTS DATA TAKEN FROM HR

import fitbit
import gather_keys_oauth2 as Oauth2
import pandas as pd
import numpy as np
import datetime
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import matplotlib.dates as mdates

#Establish a standard date format
yesterday = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y%m%d"))
yesterday2 = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
today = str(datetime.datetime.now().strftime("%Y%m%d"))
today2 = str(datetime.datetime.now().strftime("%Y-%m-%d"))

def accessAPI():

    #Client ID & Secret is given to us from the FitBit website
    CLIENT_ID = r'22DFZ8'
    CLIENT_SECRET = r'9e72de768392860b178fe36968c788e3'

    #Establish authentication with Fitbit
    server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
    server.browser_authorize()

    #Save these if new access or refresh is needed
    ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
    REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])

    #Connection
    auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

    #calls data and saves into dataframe
    fit_statsHR = auth2_client.intraday_time_series('activities/heart', base_date=today2, detail_level='1min')

    #reads the dictionary format and iterates through the dictionary values
    time_list = []
    val_list = []

    for i in fit_statsHR['activities-heart-intraday']['dataset']:
        val_list.append(i['value'])
        time_list.append(i['time'])

    heartdf = pd.DataFrame({'HR':val_list,'Time':time_list})

    UI = input("\nWould you like to write data file out? y / n: ")

    if UI == 'y' or UI == 'Y':
        heartdf.to_csv('data/rawHR/' + 'HR_' + today + '.csv', columns=['Time','HR'], header=True, index = False)
        print("File saved")


    else:
        print("File called for but not saved.\n")

def plotting():
    thisFile = ('data/rawHR/' + 'HR_' + today + '.csv')
    print ("\nThis file is: ", thisFile)

    df = pd.read_csv(thisFile)

    plt.figure(figsize=(16,6))
    plt.step(df.Time, df.HR)
    plt.ylabel('Heart Rate (BPM)')
    plt.xlabel('Time')

    plt.show()


if __name__ == "__main__":
    #accessAPI()
    plotting()