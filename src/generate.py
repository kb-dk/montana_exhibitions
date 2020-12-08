from jinja2 import Template
from pathlib import Path, PosixPath

import json


def create_folder(path):
    try:
        Path(path).mkdir(parents=True)
    except FileExistsError as e:
        print(e)

def site(obj):
    print(json.dumps(obj, indent = 3))
    exit(0)

    # create folder structure
    for theme_name, theme in obj.items():
        for ipad_num, ipad in theme.items():
            for item_num, item in ipad['items'].items():
                path = f'output/{theme_name}/ipad{ipad_num}/item{item_num}'
                create_folder(path)
                print(path)
    # create templates
    for theme_name, theme in obj.items():
        for ipad_num, ipad in theme.items():
            try:
                ipad_folder = f'output/{theme_name}/ipad{ipad_num}'
                #for language in ipad['theme_title']
                html(ipad, "index", ipad_folder)
            except Exception as e:
                print(e)
            
            #for item_num, item in ipad['items'].items():

    exit(0)

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

def html(obj, template_name, folder):
    print(obj)
    exit(0)
    with open(f"template/{template_name}.jinja2", 'r') as f:
        template = f.read()

    j2_template = Template(template)
    html_output = j2_template.render(obj)

    if obj['language'] == 'dk':
        extension = f".html"
    else:
        extension = f"-{obj['language']}.html"
    file_path = f"{folder}/{template_name}{extension}"

    html_file = open(file_path, 'w')
    html_file.write(html_output)
    html_file.close()
