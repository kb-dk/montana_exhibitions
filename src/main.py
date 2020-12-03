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
            ipad = row[2]
            item = row[3]
            language = row[4]
            obj.update({theme: {}})
            #print(theme + " " + ipad)
            obj[theme].update({ ipad: {}})
            #obj[theme][ipad].update({ language: []})
            #obj[theme][ipad][language].append(item)
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