import csv
import json
from abc import ABC, abstractmethod
from pathlib import Path
from xml.etree.ElementTree import Element, ElementTree, SubElement


class DataSaver(ABC):
    @abstractmethod
    def save(self, student_data, file_path):
        pass


class JsonSaver(DataSaver):
    def save(self, student_data, file_path):
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(student_data.to_dict(), file, ensure_ascii=False, indent=4)


class XmlSaver(DataSaver):
    def save(self, student_data, file_path):
        data = student_data.to_dict()
        root = Element("student_data")

        student_element = SubElement(root, "student")
        for key, value in data["student"].items():
            child = SubElement(student_element, key)
            child.text = str(value)

        real_element = SubElement(root, "real_performance")
        self._fill_performance(real_element, data["real_performance"])

        desired_element = SubElement(root, "desired_performance")
        self._fill_performance(desired_element, data["desired_performance"])

        tree = ElementTree(root)
        tree.write(file_path, encoding="utf-8", xml_declaration=True)

    def _fill_performance(self, parent, data):
        subjects_element = SubElement(parent, "subjects")
        for subject in data["subjects"]:
            subject_element = SubElement(subjects_element, "subject")
            subject_element.text = subject

        grades_element = SubElement(parent, "grades")
        for grade in data["grades"]:
            grade_element = SubElement(grades_element, "grade")
            grade_element.text = str(grade)

        average_element = SubElement(parent, "average_score")
        average_element.text = str(data["average_score"])


class CsvSaver(DataSaver):
    def save(self, student_data, file_path):
        data = student_data.to_dict()

        row = {
            "full_name": data["student"]["full_name"],
            "group_number": data["student"]["group_number"],
            "birth_date": data["student"]["birth_date"],
            "address": data["student"]["address"],
            "real_subjects": "; ".join(data["real_performance"]["subjects"]),
            "real_grades": "; ".join(map(str, data["real_performance"]["grades"])),
            "real_average_score": data["real_performance"]["average_score"],
            "desired_subjects": "; ".join(data["desired_performance"]["subjects"]),
            "desired_grades": "; ".join(map(str, data["desired_performance"]["grades"])),
            "desired_average_score": data["desired_performance"]["average_score"],
        }

        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=row.keys())
            writer.writeheader()
            writer.writerow(row)


def build_file_name(student_data, work_code, extension):
    full_name = student_data.student.full_name.replace(" ", "_")
    group_number = student_data.student.group_number.replace(" ", "_")
    return f"{full_name}_{group_number}_{work_code}.{extension}"


def ensure_output_dir(base_dir):
    output_dir = Path(base_dir) / "output"
    output_dir.mkdir(exist_ok=True)
    return output_dir
