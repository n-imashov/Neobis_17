import json


def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4)


new_data = {
    "Student`s name": "Armin Arlert",
    "Age": "15 y.o.",
    "Gender": "male",
    "Height": "163 cm",
    "Weight": "56 kg",
    "Birthday": "November 3rd",
    "Birthplace": "Shiganshina District",
    "Affiliation": "Survey Corps",
}

write(new_data, 'data.json')
