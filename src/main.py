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

def load_csv(filename):
    with open(filename) as csv_file:
        obj = {}
        csv_file.readline() # read first line
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
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
                    ipad: {
                        "theme_title": {}
                        }
                })
            obj[theme][ipad]["theme_title"].update({ language: theme_title })
            if title_main_character:
                if "title_main_character" not in obj[theme][ipad]:
                    obj[theme][ipad]["title_main_character"] = {}
                    obj[theme][ipad]["main_character_description"] = {}
                obj[theme][ipad]["title_main_character"].update({ language: title_main_character })
                obj[theme][ipad]["main_character_description"].update({ language: main_character_description })
            if item not in obj[theme][ipad]:
                obj[theme][ipad].update({
                    item: {
                        "short_description": {},
                        "title": {},
                        "description_1": {},
                        "description_2": {},
                        "pages": pages,
                        "video": video,
                        "pdf": pdf
                    }
                })
            obj[theme][ipad][item]["short_description"].update({ language: short_description })
            obj[theme][ipad][item]["title"].update({ language: title })
            obj[theme][ipad][item]["description_1"].update({ language: description_1 })
            obj[theme][ipad][item]["description_2"].update({ language: description_2 })

            #create_file(obj)
        print(json.dumps(obj, indent = 3))
        with open('test.json', 'w') as outfile:
            json.dump(obj, outfile, indent = 3)
        exit(0)

def create_file(obj):
    try:
        ipad_folder = f"output/{obj['theme']}/iPad{obj['ipad']}"
        folder = f"{ipad_folder}/{obj['item']}"
        Path(folder).mkdir(parents=True)
    except FileExistsError as e:
        pass
    try:
        generate.html(obj, "index", ipad_folder)
        generate.html(obj, "text", folder)
    except Exception as e:
        print(e)


def getOptions(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="Generate html from csv")
    parser.add_argument("-c", "--csv", required=True, help="csv to process")
    options = parser.parse_args(args)
    return options

def main():
    options = getOptions()
    filename = PosixPath(options.csv).expanduser()
    prepare_output_folder()
    load_csv(filename)

if __name__ == '__main__':
  main()