from get_text_from_link import get_link, extract_text_from_url
from Extraction import generate_response_new
import re
import os
# Input your openai api key here
OPENAI_API_KEY = 'your-openai-api-key'
SEC_DOC_LINK_FILE = 'input/sample_8k_links.csv'
OUTPUT_DIR = 'output'


def main():

    # Ensure the output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    total_links = get_link(SEC_DOC_LINK_FILE)

    for link in total_links:
        filename = link.split('/')[-1].split('.')[0]
        text = extract_text_from_url(link)

        result = generate_response_new(text, OPENAI_API_KEY)
        # The result is natual language that includes the key information so Extract those using Regex.
        matches = re.findall(r"```(.*?)```", result, re.DOTALL)

        csv = ''
        for match in matches:
            csv += match
        with open('output/' + filename + '.csv', 'w') as file:
            file.write(csv)
        if os.path.getsize('output/' + filename + '.csv') < 1:
            total_links.append(link)


if __name__ == '__main__':
    main()
