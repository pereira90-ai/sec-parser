import argparse
from get_text_from_link import get_link, extract_text_from_url
from Extraction import generate_response_new
import re
import os
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
        with open(OUTPUT_DIR + '/' + filename + '.json', 'w') as file:
            file.write(result)
        if os.path.getsize(OUTPUT_DIR + '/' + filename + '.json') < 1:
            total_links.append(link)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process a given path.")
    parser.add_argument('input_path', type=str, help='The path to your input link or file')

    args = parser.parse_args()

    main(args.input_path)
