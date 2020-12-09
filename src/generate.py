from jinja2 import Template
from pathlib import Path, PosixPath

import json


def create_folder(path):
    try:
        Path(path).mkdir(parents=True)
    except FileExistsError as e:
        pass

def site(obj):
    #print(json.dumps(obj, indent = 3))

    # create folder structure
    for theme_name, theme in obj.items():
        for ipad_num, ipad in theme.items():
            for language_key, language_obj in ipad['languages'].items():
                path = f'output/{theme_name}/ipad{ipad_num}'
                create_folder(path)
                html(language_obj, language_key, "index", path)
                for item_num, item in language_obj['items'].items():
                    path = f'output/{theme_name}/ipad{ipad_num}/item{item_num}'
                    create_folder(path)
                    html(item, language_key, "text", path)

def html(obj, language, template_name, path):
    with open(f"template/{template_name}.jinja2", 'r') as f:
        template = f.read()

    obj["language"] = language
    j2_template = Template(template)
    html_output = j2_template.render(obj)

    if language == 'dk':
        extension = f".html"
    else:
        extension = f"-{language}.html"
    file_path = f"{path}/{template_name}{extension}"

    html_file = open(file_path, 'w')
    html_file.write(html_output)
    html_file.close()
