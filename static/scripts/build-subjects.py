import os
import json
from re import template

PROJECT_DIR = os.path.join(os.getenv("HOME"), "Repos", "cmgp-notes")
JSON_DIR = os.path.join(PROJECT_DIR, "data", "subjects")
GRADES_DIR = os.path.join(PROJECT_DIR, "content", "grades")
TEMPLATE_PATH = os.path.join(
    PROJECT_DIR, "static", "scripts", "template-subject.md")
TEMPLATE_INDEX_PATH = os.path.join(
    PROJECT_DIR, "static", "scripts", "template-index.md")
TEMPLATE = open(TEMPLATE_PATH).read()
TEMPLATE_INDEX = open(TEMPLATE_INDEX_PATH).read()
HTML_LAYOUT = "subject"
ALL_JSON = os.listdir(JSON_DIR)


def urlize(name: str):
    return name.lower().replace(" ", "-")


def replace_with_dict(text: str, terms: dict):
    for key in terms.keys():
        text = text.replace(key, terms[key])
    return text


print(TEMPLATE)

for filename in ALL_JSON:
    # load a grade, set related variables and set up the environment
    data = json.load(open(os.path.join(JSON_DIR, filename)))
    grade_name = data["grade"]
    grade_dir = os.path.join(GRADES_DIR, filename.replace(".json", ""))
    if not (os.path.isdir(grade_dir)):
        os.mkdir(grade_dir)
    for file in [f for f in os.listdir(grade_dir)]:
        os.remove(os.path.join(grade_dir, file))
    for subject in (data["subjects"]):
        # create a markdown file for each subject
        with open(os.path.join(GRADES_DIR, grade_dir, urlize(subject["subject"]) + ".md"), 'w') as file:
            markdown = TEMPLATE
            template_dict = {
                "[[grade]]": grade_name,
                "[[subject]]": subject["subject"],
                "[[filename]]": filename.replace(".json", ""),
                "[[layout]]": HTML_LAYOUT,
                "[[subject-lower]]": subject["subject"].lower()
            }
            markdown = replace_with_dict(markdown, template_dict)
            for topic in subject["topics"]:
                markdown += "\n" + "- [" + topic + "]" + \
                    "(" + "/topics/" + urlize(topic) + ")"
            file.write(markdown)
    with open(os.path.join(GRADES_DIR, grade_dir, "_index.md"), "w") as file:
        # create index file for each grade
        markdown = TEMPLATE_INDEX
        template_dict = {
            "[[layout]]": "subject",
            "[[grade]]": grade_name,
            "[[summary]]": "Přehled všech předmětů k ročníku:" + grade_name
        }
        markdown = replace_with_dict(markdown, template_dict)
        for subject in data["subjects"]:
            subject_name = subject["subject"]
            markdown += "\n" + "- [" + subject_name + "]" + \
                "(" + "/grades/" + "/" + urlize(grade_name) + \
                "/" + urlize(subject_name) + ")"
        file.write(markdown)


with open(os.path.join(GRADES_DIR, "_index.md"), "w") as file:
    # create index for all grades
    markdown = TEMPLATE_INDEX
    template_dict = {
        "[[layout]]": "subject",
        "[[grade]]": "Ročníky",
        "[[summary]]": "\"Přehled všech ročníků:\""
    }
    markdown = replace_with_dict(markdown, template_dict)
    for filename in ALL_JSON:
        filename = filename.replace(".json", "")
        markdown += "\n" + "- [" + filename.upper() + "]" + \
                    "(" + "/grades/" + urlize(filename) + ")"
    file.write(markdown)
