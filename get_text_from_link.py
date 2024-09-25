import csv
import requests
from bs4 import BeautifulSoup
import logging


def get_link(path):
    with open(path, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        total_lines = []
        for row in csv_reader:
            for each in row:
                if "https://" in each:
                    total_lines.append(each)

    return total_lines


def extract_text_from_url(link):
    # Define headers to mimic a web browser
    # Send a GET request to the URL with headers. Typical for scrapping text.
    try:
        headers = {
            "Cookie": "ak_bmsc=E072501245094E47A5D00C83F3030696~000000000000000000000000000000"
                      "~YAAQtOIlF4jvCNaRAQAAS1vw2hkAeNQrWyTw1T4"
                      "+sRMHP3uB7eeUzyGCM7culcb2am8uDG6hbdhSmrorKAKBFlNicUtoYRVXGfuq2jSFXqULoTXH3"
                      "D1jT9TUF9aXuDZvEoXD1v8eUD52ot+wAGTuP9s8wmMYnnfWVxBMOJm7fMHU6qse2gz/7ZOWWh3hm"
                      "J137++mk3TIXKGHJBCtVZof0d5L06Q3dhNfrd5EcSapiXqbJDx/IB4XhhFKmXrJ9xCsZYqz2vWuD"
                      "9sxZ3Jcr1jDQ9yHGLKF1NBZU0M9Dxq02jf0YCuX+kxXOV/QZYdo23iyznnj5WZAO5dnRIlRnKy4tnLyXrL"
                      "/ouNYxmzoCJy61E2CwxTkUljF5UBF1cNPaD524OGQmFWqJAg555dTwC9cMagICEqckmhOasG10RDzAMXAFu"
                      "+Pg6bclAx4kW6pRKor+nOglSc3uj52z5o=",
            "sec-fetch-user": "?1",
            "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/128.0.0.0 Safari/537.36",
        }
        response = requests.get(link, headers=headers,)

    except requests.exceptions.HTTPError as err:
        return f"HTTP error occurred: {err}"
    except requests.exceptions.RequestException as e:
        return f"Error fetching the webpage: {e}"

        # Parse the webpage content if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        data = soup.get_text()
        return data
    else:
        return f"Failed to retrieve the webpage. Status code: {response.status_code}"


if __name__ == '__main__':
    url = 'https://www.sec.gov/Archives/edgar/data/320193/000114036123011192/brhc10049413_8k.htm'
    text = extract_text_from_url(url)
    logging.info(f"Result: {text}")  # Log the result instead of using print
