import pandas as pd
from pathlib import Path, PosixPath
import shutil
import csv
import argparse
import sys
import json

import generate

def prepare_output_folder():
    try:
        shutil.rmtree('output/')
    except FileNotFoundError as e:
        pass
    Path('output').mkdir()
    shutil.copytree('includes', 'output/includes')

def load_excel(filename, obj):
    file = pd.read_excel (filename, header = None)
    exhibition_list = excel_file.fillna('').iloc[1:].values.tolist()
    for row in exhibition_list:
        process_row(row, obj)

def load_csv(filename, obj):
    with open(filename) as csv_file:
        csv_file.readline() # read first line
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            process_row(row, obj)

def process_row(row, obj):
    theme = row[0]
    theme_title = row[1]
    ipad = row[2]
    item = row[3]
    language = row[4]
    title_main_character = row[5]
    main_character_description = row[6]
    short_description = row[7]
    title = row[8]
    description_1 = row[9]
    description_2 = row[10]
    pages = row[11]
    video = row[12]
    pdf = row[13]

    if theme not in obj:
        obj.update({theme: {}})
    if ipad not in obj[theme]:
        obj[theme].update({
            ipad: { "languages": {} }
        })
    if language not in obj[theme][ipad]["languages"]:
        obj[theme][ipad]["languages"].update({
            language: {
                "theme_title": theme_title,
                "items": {}
            }
        })
    language_obj = obj[theme][ipad]["languages"][language]
    if title_main_character:
        if "title_main_character" not in language_obj:
            language_obj["title_main_character"] = title_main_character
            language_obj["main_character_description"] = main_character_description
    if item not in language_obj['items']:
        language_obj['items'][item] = {
            "short_description": short_description,
            "title": title,
            "description_1": description_1,
            "description_2": description_2,
            "pages": pages,
            "video": video,
            "pdf": pdf
        }

def getOptions(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="Generate html from csv")
    parser.add_argument("-input", "--input", required=True, help="csv or xslx to process")
    options = parser.parse_args(args)
    return options

def main():
    options = getOptions()
    filename = PosixPath(options.input).expanduser()
    prepare_output_folder()
    obj = {}
    suffix = Path(filename).suffix
    if suffix == '.xlsx':
        load_excel(filename, obj)
    elif suffix == '.csv':
        load_csv(filename, obj)
    else:
        raise Exception("Unsupported file format")
    with open('output.json', 'w') as outfile:
        json.dump (obj, outfile, indent=4)
    generate.site(obj)

if __name__ == '__main__':
  main()