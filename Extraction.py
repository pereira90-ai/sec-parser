import os
import logging
import time
import openai

def get_sample_output():
    with open('input/sample_output.txt', 'r', encoding="utf-8") as file:
        results = file.readlines()
        final_text = ''
        for line in results:
            final_text += line + '\n'
    return final_text


def generate_response_new(new_data, api_key):
    results = ''
    context = get_sample_output()

    try:
        os.environ['OPENAI_API_KEY'] = api_key
        messages = [{"role": "user", "content": new_data + context}]

        openai.api_key = os.environ.get('OPENAI_API_KEY')
        start_time = time.time()
        logging.info(f"Start Time: {start_time}")
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        results = response.choices[0].message.content
        print(time.time() - start_time)
        logging.info(f"ETA: {time.time() - start_time}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
    return results


if __name__ == '__main__':
    input_text = ("I want to extract csv file from the Item 0.57 in the given sec 8k document"
                  "I will give you the sample input and output as well as the text where I want to extract table")

