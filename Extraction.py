import os
import logging
import time
import openai


def get_text():
    with open('input/sample_input.txt', 'r', encoding="utf-8") as input_file:
        results = input_file.readlines()
        final_text = ''
        for line in results:
            final_text += line + '\n'
    return final_text


def get_sample_output():
    with open('input/sample_output.csv', 'r', encoding="utf-8") as file:
        results = file.readlines()
        final_text = ''
        for line in results:
            final_text += line + '\n'
    return final_text


def generate_response_new(new_data, api_key):
    results = ''
    context = (("I'll give you sample input and output. Then please give me the output from the new input text."
                "Sample input: '") + get_text() + '\n"' + 'Sample Output: "' + get_sample_output()
               + '" \nAnd the input is: ')
    start_time = time.time()
    logging.info(f"Result: {start_time}")
    try:
        os.environ['OPENAI_API_KEY'] = api_key
        messages = [{"role": "user", "content": context + new_data + '\n This input is sec 8-k document. I want '
                                                                     'to extract Item 5.07 information in the '
                                                                     'format of the sample output file. '
                                                                     'Encapsulate output strings(Nominees or '
                                                                     'stockholders) with quotation'
                                                                     'mark if it includes comma. And if the count '
                                                                     'of numbers are different for each proposal, '
                                                                     'only maintain numbers linked to these '
                                                                     'column names: "for,'
                                                                     ' against, abstained, broker Non-Vote". '
                                                                     ' But you always include other numbers'
                                                                     'and I want you not to make me upset this '
                                                                     'time by providing me teh same counts of '
                                                                     'numbers for each proposal. Also use ``` for '
                                                                     'indicating the data that will'
                                                                     'be used.'}]

        openai.api_key = os.environ.get('OPENAI_API_KEY')
        response = openai.chat.completions.create(
            model="gpt-4o-2024-08-06",
            messages=messages
        )
        results = response.choices[0].message.content
        messages.append({"role": "assistant", "content": results})
        # Follow-up question to refine the result for CSV format
        follow_up_question = ('I want to make csv file from the result. So the string must be encapsulated with '
                              'quotation mark when it indicates one column.Ensure the result complies with all given '
                              'conditions, matching each number to its'
                              'corresponding column, particularly concerning "Broker non-votes". Even if column names '
                              'vary slightly, their meanings should align, so address those as well.')
        messages.append({"role": "user", "content": follow_up_question})

        response = openai.chat.completions.create(
            model='gpt-4o-2024-08-06',
            messages=messages
        )
        logging.info(f"ETA: {time.time() - start_time}")
        print(time.time() - start_time)
        results = response.choices[0].message.content
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    return results


if __name__ == '__main__':
    input_text = ("I want to extract csv file from the Item 0.57 in the given sec 8k document"
                  "I will give you the sample input and output as well as the text where I want to extract table")
    # generate_response_new(input_text)
    with open('input/sample_input.txt', 'r', encoding="utf-8") as csv:
        result = csv.readlines()
