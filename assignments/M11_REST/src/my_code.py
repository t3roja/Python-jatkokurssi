import requests
import datetime

def train_departure(train, station, date):

    ok = True
    url = "https://rata.digitraffic.fi/api/v1/trains/" + str(date) + "/" + train
    print(url)
    try:
        response = requests.get(url,
        headers={"Accept": "application/json"})
    except Exception as e:
        print(e)
        ok = False
    
    if ok:

        train_data = response.json()
        
        for train_instance in train_data:
                for time_table in train_instance.get('timeTableRows', []):
                    if time_table.get('stationShortCode') == station and time_table.get('type') == 'DEPARTURE':
                        departure_time = time_table.get('scheduledTime')
                        if departure_time:
                            return datetime.datetime.fromisoformat(departure_time.replace('Z', '+00:00'))

if __name__=='__main__':
    #Write test code here
    date=datetime.date(2021, 3, 21)
    departure=train_departure('56', 'OL', date)
    print(departure)


"""
M11 Kirjoita funktio train departure(train, station, date),
joka palauttaa annetun junan lähtöajan halutulta asemalta
tyyppinä datetime.datetime. Junaliikenteen tietoja löytyy
esimerkiksi https://www.digitraffic.fi/rautatieliikenne/.
Jos annetulta päivältä ei löydy junan tietoja asemalta, heittää
funktio (valitsemasi) poikkeuksen.
• train=junan numero merkkijonona ilman junatyypin ilmaisevaa
etukirjainta, siis esimerkiksi "56", ei "S56".
• station=asematunnus. Asematunnuksena käytetään
stationShortCode-kentän arvoa, katso
https://rata.digitraffic.fi/api/v1/metadata/stations.
• date=päivämäärä tyyppi¨a datetime.date.
Esimerkiksi junan 56 tiedot 21.3.2021 saadaan haettua kyselyllä
https://rata.digitraffic.fi/api/v1/trains/2021-03-21/56.
"""