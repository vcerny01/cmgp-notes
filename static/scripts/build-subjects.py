import os
import shutil
import json

PROJECT_DIR = os.path.join(os.getenv("HOME"), "Repos", "cmgp-notes")
JSON_DIR = os.path.join(PROJECT_DIR, "data", "subjects")
GRADES_DIR = os.path.join(PROJECT_DIR, "content", "grades")
TEMPLATE_PATH = "subject-template.md"
TEMPLATE = open(TEMPLATE_PATH).read()
print(TEMPLATE)

for filename in os.listdir(JSON_DIR):
    data = json.load(open(os.path.join(JSON_DIR, filename)))
    grade_name = data["grade"]
    grade_dir = os.path.join(GRADES_DIR, filename.replace(".json", ""))
    if (not os.path.isdir(grade_dir)):
        os.mkdir(grade_dir)
    shutil.rmtree(grade_dir)
    for subject in (data["subjects"]):
        markdown = TEMPLATE
        markdown = markdown.replace("[[grade]]", grade_name).replace(
            "[[subject]]", subject["subject"]).replace("[[filename]]", filename)
        with open(os.path.join(GRADES_DIR, grade_dir, subject["subject"].lower().replace(" ", "-") + ".md"), "w") as file:
            file.write(markdown)
