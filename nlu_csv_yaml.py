import csv

def generate_nlu_file(csv_file, output_file):
    intents = {}
    
    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            intent = row["intent"]
            example = row["examples"]
            if intent in intents:
                intents[intent].append(example)
            else:
                intents[intent] = [example]
    
    with open(output_file, "w") as file:
        file.write("version: '3.1'\n\n")
        file.write("nlu:\n")
        for intent, examples in intents.items():
            file.write(f"- intent: {intent}\n")
            file.write("  examples: |\n")
            for example in examples:
                file.write(f"    - {example}\n")

csv_file = "/Users/indrajanambiar/Documents/semester4/internship/rasa_final_files/rasa_final/nlu.csv"
output_file = "/Users/indrajanambiar/Documents/semester4/internship/rasa_final_files/rasa_final/data/nlu.yml"
generate_nlu_file(csv_file, output_file)
