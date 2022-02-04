# Creates a page (=markdown file with relevant frontmatter) for every subject in every grade according to subjects file

import os
import yaml
import shutil

DATA_PATH = os.path.join("data", "subjects.yaml")
GRADES_DIR = os.path.join("content", "grades")
TEMPLATE_SUBJECT_PATH = os.path.join("static", "templates", "subject.md")
TEMPALATE_GRADE_PATH = os.path.join("static", "templates", "grade-index.md")


def urlize(name: str):
    """urlize name as hugo does"""
    if not name:
        return ""
    return name.lower().replace(" ", "-")


def replace_with_dict(text: str, terms: dict):
    """build frontmatter from template"""
    for key in terms.keys():
        text = text.replace(key, terms[key])
    return text


def cleanup(grades_dir: str):
    """delete all files in grades dir to"""
    shutil.rmtree(grades_dir)
    os.mkdir(grades_dir)


def build_subjects(data: dict, grades_dir: str):
    """create all dirs and md files according to data in yaml"""
    template_subject = open(TEMPLATE_SUBJECT_PATH).read()
    template_grade = open(TEMPALATE_GRADE_PATH).read()
    for grade in data:
        grade_dir = os.path.join(grades_dir, urlize(grade["grade"]))
        os.mkdir(grade_dir)
        # write subjects
        for subject in grade["subjects"]:
            with open(os.path.join(grade_dir, urlize(subject) + ".md"), "w") as file:
                markdown = template_subject
                template_dict = {
                    "[[layout]]": "subject",
                    "[[grade]]": grade["grade"],
                    "[[subject]]": subject,
                }
                markdown = replace_with_dict(markdown, template_dict)
                file.write(markdown)
        # write index files
        with open(os.path.join(grade_dir, "_index.md"), "w") as file:
            markdown = template_grade
            template_dict = {"[[layout]]": "grade", "[[grade]]": grade["grade"]}
            markdown = replace_with_dict(markdown, template_dict)
            file.write(markdown)


if __name__ == "__main__":
    yaml_data = yaml.safe_load(open(DATA_PATH))
    print(yaml_data, type(yaml_data))
    cleanup(GRADES_DIR)
    build_subjects(yaml_data, GRADES_DIR)
