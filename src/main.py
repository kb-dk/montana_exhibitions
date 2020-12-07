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
            short_description = row[5]
            title = row[6]
            if theme not in obj:
                obj.update({theme: {}})
            if ipad not in obj[theme]:
                obj[theme].update({
                    ipad: {},
                    "theme_title": {}
                })
            if language not in obj[theme]["theme_title"]:
                obj[theme]["theme_title"].update({ language: theme_title })
            if item not in obj[theme][ipad]:
                obj[theme][ipad].update({
                    item: {
                        "short_description": {},
                        "title": {}
                    }
                })
            if language not in obj[theme][ipad][item]["short_description"]:
                obj[theme][ipad][item]["short_description"].update({ language: short_description })
            if language not in obj[theme][ipad][item]["title"]:
                obj[theme][ipad][item]["title"].update({ language: title })

            #obj[theme][ipad].update({ 
            #obj['short_description'] = row[5]
            #obj['title'] = row[6]
            #obj['description_1'] = row[7]
            #obj['description_2'] = row[8]
            #obj['image'] = row[9]
            #obj['video'] = row[10]
            # create_file(obj)
        print(json.dumps(obj, indent = 3))
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