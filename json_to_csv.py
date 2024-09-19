import json
import logging

import pandas as pd


def json_to_csv(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as file:
        json_input = json.load(file)


    # Load each section into its own DataFrame
    company_info = pd.DataFrame(json_input["company"])
    nominee_df = pd.DataFrame(json_input["nominees"])
    # nominee_df.insert(0, 'No', range(1.1, 1.1 + len(nominee_df) * 0.1, 0.1))
    # nominee_df.insert(0, 'No', range(1.1, 1.1 + len(nominee_df) * 0.1, 0.1))

    proposal_df = pd.DataFrame(json_input["proposals"])
    try:
        proposal_time_df = pd.DataFrame(json_input["proposal_time"])
    except Exception as e:
        print('There is no odd proposal in this document.', e)
    # Write each section out to the CSV file, separated by blank lines
    with open(output_path, "w", newline='') as file:
        company_info.to_csv(file, index=False)
        file.write("\n")  # Blank line to separate sections
        nominee_df.to_csv(file, index=False)
        file.write("\n")  # Blank line to separate sections
        proposal_df.to_csv(file, index=False)
        file.write("\n")  # Blank line to separate sections
        try:
            proposal_time_df.to_csv(file, index=False)
        except Exception as e:
            pass

if __name__ == '__main__':
    json_to_csv('output/tm2315877d1_8k.json', 'output/tm2315877d1_8k.csv')