import requests

header = 'kveola-origoassigment'


def get_available_bikes():
    available_url = 'https://gbfs.urbansharing.com/oslobysykkel.no/station_status.json'
    available_json = requests.get(available_url).json()["data"]["stations"]
    for values in available_json:
        print(values)


def get_list_of_stations():
    stations_url = 'https://gbfs.urbansharing.com/oslobysykkel.no/station_information.json'
    stations_json = requests.get(stations_url).json()
    for values in stations_json:
        print(values)


def get_available_locks():
    pass


def get_url_from_api():
    bikes_url = 'https://gbfs.urbansharing.com/oslobysykkel.no/system_information.json'
    bikes_json = requests.get(bikes_url).json()
    for values in bikes_json:
        print(values)


def main():
    # get_url_from_api()
    get_available_bikes()
    # get_list_of_stations()


if __name__ == '__main__':
    main()
