# Load Covid-19 CSV from URL
import numpy as np

def getCovidAttr(c19attr):
    from urllib.request import urlopen
    url = f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-{c19attr}.csv'
    raw_data = urlopen(url)
    df={'names': ('Location', 'Country', c19attr),'formats': ('S128', 'S128', 'i')}
    dataset = np.loadtxt(raw_data, dtype=df, delimiter=",", skiprows=1, usecols=(0, 1, -1))
    return dataset[c19attr].sum()


def getCovidAttr3(c19attr):
    import requests
    c19url = f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-{c19attr}.csv'
    df={'names': ('Location', 'Country', c19attr),'formats': ('S128', 'S128', 'i')}
    with requests.get(c19url, headers={'Accept': 'application/text'}) as url:
        if 200 == url.status_code:
            dataset = np.loadtxt(url.content.decode('utf-8').splitlines(), dtype=df, delimiter=",", skiprows=1, usecols=(0, 1, -1))
            return dataset[c19attr].sum()
    return -1


for attr in ('Confirmed','Recovered','Deaths'):
    print(attr,getCovidAttr(attr))
    print(attr,getCovidAttr3(attr))



