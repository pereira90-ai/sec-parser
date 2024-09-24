import json
import pandas as pd


def json_to_csv(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as file:
        json_input = json.load(file)

    # Load each section into its own DataFrame
    company_info = pd.DataFrame(json_input["company"])
    nominee_df = pd.DataFrame(json_input["nominees"])
    nominee_df.insert(0, 'No', ['1.' + str(x + 1) for x in range(len(nominee_df))])
    # nominee_df.insert(0, 'No', range(1.1, 1.1 + len(nominee_df) * 0.1, 0.1))
    nominee_df['No'] = nominee_df['No'].apply(lambda x: f"{x}.")

    proposal_df = pd.DataFrame(json_input["proposals"])

    proposal_df.insert(0, 'No', list(range(2, proposal_df.__len__() + 2)))
    # Write each section out to the CSV file, separated by blank lines
    with open(output_path, "w", newline='') as file:
        company_info.to_csv(file, index=False)
        file.write("\n")  # Blank line to separate sections
        nominee_df.to_csv(file, index=False)
        file.write("\n")  # Blank line to separate sections
        proposal_df.to_csv(file, index=False)
        file.write("\n")  # Blank line to separate sections


if __name__ == '__main__':
    json_to_csv('output/tm2315877d1_8k.json', 'tm2315877d1_8k.csv')