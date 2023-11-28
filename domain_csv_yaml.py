import csv
import yaml

def convert_csv_to_domain(csv_file, output_file):
    intents = []
    responses = {}
    session_config = {}

    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row

        for row in reader:
            section = row[0]
            key = row[1]
            value = row[2]

            if section == "intents":
                intents.append(value.strip("'"))
            elif section == "responses":
                if key not in responses:
                    responses[key] = []
                responses[key].append({"text": value})
            elif section == "session_config":
                session_config[key] = value

    data = {
        "version": "3.1",
        "intents": intents,
        "responses": responses,
        "session_config": session_config,
    }

    with open(output_file, "w") as file:
        yaml.dump(data, file)



csv_file = "C:\Users\ashik\Documents\rasa_chatbot\domain.csv"
output_file = "C:\Users\ashik\Documents\rasa_chatbot\domain.yml"

convert_csv_to_domain(csv_file, output_file)


