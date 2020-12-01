from pathlib import Path, PosixPath
import csv
import argparse
import sys

import generate


def load_csv(filename):
    with open(filename) as csv_file:
        csv_file.readline() # read first line
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            obj = {}
            obj['theme'] = row[0]
            obj['ipad'] = row[1]
            obj['item'] = row[2]
            obj['language'] = row[3]
            obj['short_description'] = row[4]
            create_file(obj)

def create_file(obj):
    try:
        ipad_folder = f"output/iPad{obj['ipad']}"
        folder = f"{ipad_folder}/{obj['item']}"
        if obj['language'] == 'dk':
            file = f"index.html"
        else:
            file = f"index-{obj['language']}.html"
        Path(folder).mkdir(parents=True)
    except FileExistsError as e:
        pass
    try:
        generate.html(obj, folder + '/' + file)
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
    load_csv(filename)

if __name__ == '__main__':
  main()