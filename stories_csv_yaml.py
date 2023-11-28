import csv
import yaml

def convert_csv_to_stories(csv_file, output_file):
    stories = {}

    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            story = row["story"]
            intent = row["intent"]
            action = row["action"]

            if story not in stories:
                stories[story] = {"steps": []}

            if intent:
                stories[story]["steps"].append({"intent": intent})

            if action:
                stories[story]["steps"].append({"action": action})

    data = {"version": "3.1", "stories": []}
    for story, steps in stories.items():
        data["stories"].append({"story": story, "steps": steps["steps"]})

    with open(output_file, "w") as file:
        yaml.dump(data, file)

csv_file = "C:\Users\ashik\Documents\Rasa\rasa_chatbot\stories.csv"
output_file = "C:\Users\ashik\Documents\Rasa\rasa_chatbot\data\stories.yml"

convert_csv_to_stories(csv_file, output_file)
