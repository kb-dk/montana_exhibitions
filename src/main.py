from pathlib import Path, PosixPath
import shutil
import csv
import argparse
import sys

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
                        "theme_title": {},
                        "items": {}
                    }
                })
            obj[theme][ipad]["theme_title"].update({ language: theme_title })
            if title_main_character:
                if "title_main_character" not in obj[theme][ipad]:
                    obj[theme][ipad]["title_main_character"] = {}
                    obj[theme][ipad]["main_character_description"] = {}
                obj[theme][ipad]["title_main_character"].update({ language: title_main_character })
                obj[theme][ipad]["main_character_description"].update({ language: main_character_description })
            if item not in obj[theme][ipad]['items']:
                obj[theme][ipad]['items'][item] = {
                    "texts": {
                        "dk": {},
                        "uk": {},
                        "kid": {}
                    }
                    #"short_description": {},
                    #"title": {},
                    #"description_1": {},
                    #"description_2": {},
                    #"pages": pages,
                    #"video": video,
                    #"pdf": pdf
                }
            if short_description not in obj[theme][ipad]["items"][item]["texts"][language]:
                obj[theme][ipad]["items"][item]["texts"][language]["short_description"] = short_description
                obj[theme][ipad]["items"][item]["texts"][language]["title"] = title
                obj[theme][ipad]["items"][item]["texts"][language]["description_1"] = description_1
                obj[theme][ipad]["items"][item]["texts"][language]["description_2"] = description_2

        return obj

def getOptions(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="Generate html from csv")
    parser.add_argument("-c", "--csv", required=True, help="csv to process")
    options = parser.parse_args(args)
    return options

def main():
    options = getOptions()
    filename = PosixPath(options.csv).expanduser()
    prepare_output_folder()
    obj = load_csv(filename)
    generate.site(obj)

if __name__ == '__main__':
  main()