# Extract_Voting_Reports


This project extracts vote information from the Sec 8k reports.


### How to use


Make sure your openai api key is valid in main.py file.
You can specify the link file(SEC_DOC_LINK_FILE) as well as output directory.

Set up environment

> pip install -r requirements.txt

Set openai api key
> OPENAI_API_KEY = 'your-openai-key'

Run the script

> python main.py path-to-your-link

#### Validation

> python check.py