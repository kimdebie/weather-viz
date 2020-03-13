import requests
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta

def knmi_data():

    # define start and end date
    enddate = date.today().strftime("%Y%m%d")
    startdate = (date.today() - relativedelta(years=30)).strftime("%Y%m%d")

    # read in data from KNMI API
    url = 'http://projects.knmi.nl/klimatologie/daggegevens/getdata_dag.cgi'
    params = {'stns': 235, 'start': startdate, 'end': enddate, 'inseason': 'Y', 'vars': 'tg'}
    file = requests.post(url, data=params).text
    data = file.splitlines()

    # data cleaning: remove lines starting with #
    clean_data = []
    for line in data:
        if not line[0] == '#':
            line = line.split(',')
            clean_data.append(line)

    # read data into pandas dataframe
    cols = ['station', 'date', 'temp']
    df = pd.DataFrame(clean_data, columns=cols)

    # remove whitespace
    for col in cols:
        df[col] = df[col].str.strip()

    df = df.astype('int32')

    final_data = df.to_dict('records')

    return final_data
