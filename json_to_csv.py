import json
import pandas as pd


def json_to_csv(input_path, output_path):
    with open(input_path, 'r') as file:
        json_input = json.load(file)


    # Load each section into its own DataFrame
    company_info = pd.DataFrame(json_input["company"])
    nominee_df = pd.DataFrame(json_input["nominees"])
    proposal_df = pd.DataFrame(json_input["proposals"])
    proposal_time_df = pd.DataFrame(json_input["proposal_time"])

    # Write each section out to the CSV file, separated by blank lines
    with open(output_path, "w", newline='') as file:
        company_info.to_csv(file, index=False)
        file.write("\n")  # Blank line to separate sections
        nominee_df.to_csv(file, index=False)
        file.write("\n")  # Blank line to separate sections
        proposal_df.to_csv(file, index=False)
        file.write("\n")  # Blank line to separate sections
        proposal_time_df.to_csv(file, index=False)