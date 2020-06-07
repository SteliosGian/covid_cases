import re
from scrape_data import Data
from speech import speak, get_audio

URL = 'https://www.worldometers.info/coronavirus/'


def main():
    print("Started Program")
    data = Data(URL)
    END_PHRASE = "stop"
    country_list = data.get_list_of_countries()

    TOTAL_PATTERNS = {
        re.compile("total cases"): data.get_total_cases,
        re.compile("cases"): data.get_total_cases,
        re.compile(r"[\w\s]+ total [\w\s]+ cases"): data.get_total_cases,
        re.compile(r"[\w\s]+ total cases"): data.get_total_cases,
        re.compile("total deaths"): data.get_total_deaths,
        re.compile("deaths"): data.get_total_deaths,
        re.compile(r"[\w\s]+ total [\w\s]+ deaths"): data.get_total_deaths,
        re.compile(r"[\w\s]+ total deaths"): data.get_total_deaths
    }

    COUNTRY_PATTERNS = {
        re.compile(r"[\w\s]+ cases [\w\s]+"): lambda country: data.get_country_data(country)['total_cases'],
        re.compile(r"[\w\s]+ deaths [\w\s]+"): lambda country: data.get_country_data(country)['total_deaths']
    }

    while True:
        print("Listening...")
        text = get_audio()
        print(text)
        result = None

        for pattern, func in COUNTRY_PATTERNS.items():
            if pattern.match(text):
                words = set(text.split(" "))
                for country in country_list:
                    if country in words:
                        result = func(country)
                        break

        for pattern, func in TOTAL_PATTERNS.items():
            if pattern.match(text):
                result = func()
                break

        if result:
            speak(result)

        if text.find(END_PHRASE) != -1:
            print("Exit")
            break


if __name__ == "__main__":
    main()
