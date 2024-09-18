import argparse

import logging
from get_text_from_link import get_link, extract_text_from_url
from Extraction import generate_response_new
import re
import os

from json_to_csv import json_to_csv

# Input your openai api key here
OPENAI_API_KEY = 'your-openai-api-key'
SEC_DOC_LINK_FILE = 'input/sample_8k_links.csv'
OUTPUT_DIR = 'output'


def main(input_file=SEC_DOC_LINK_FILE):

    # Ensure the output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    total_links = get_link(input_file)

    for link in total_links:
        filename = link.split('/')[-1].split('.')[0]
        text = extract_text_from_url(link)

        result = generate_response_new(text, OPENAI_API_KEY)
        # The result is natual language that includes the key information so Extract those using Regex.
        matches = re.findall(r"```json(.*?)```", result, re.DOTALL)

        result = ''
        for match in matches:
            result += match
        try:
            with open(OUTPUT_DIR + '/' + filename + '.json', 'w') as file:
                file.write(result)
            json_to_csv(OUTPUT_DIR + '/' + filename + '.json', OUTPUT_DIR + '/' + filename + '.csv')
        except Exception as e:
            logging.info(f"{e} has occurred during {filename} process")

        if os.path.getsize(OUTPUT_DIR + '/' + filename + '.json') < 1:
            total_links.append(link)




if __name__ == '__main__':

    main()

