from jinja2 import Template
from pathlib import Path, PosixPath
import shutil
import os
import json


def create_folder(path):
    try:
        Path(path).mkdir(parents=True)
    except FileExistsError as e:
        pass

def site(obj):
    # create folder structure
    for theme_name, theme in obj.items():
        for ipad_num, ipad in theme.items():
            for language_key, language_obj in ipad['languages'].items():
                path = f'output/{theme_name}/ipad{ipad_num}'
                create_folder(path)
                html(language_obj, language_key, "index", path)
                if 'title_main_character' in language_obj:
                    html(language_obj, language_key, "person-items", path)
                for item_num, item in language_obj['items'].items():
                    path = f'output/{theme_name}/ipad{ipad_num}/item{item_num}'
                    create_folder(path)
                    html(item, language_key, "text", path)
                    # Copying video.mp4 from media folder
                    if item['video'] == 'yes':
                        media_file = path.replace("output", "media")+ "/video.mp4"
                        if os.path.exists(media_file):
                            if not os.path.exists(media_file.replace("media","output")):
                                shutil.copy( media_file, path)
                        else:
                            print(media_file, " dosn't exist")
                    # Copying images.pdf from media folder
                    if item['pdf'] == 'yes':
                        media_file = path.replace("output", "media")+ "/images.pdf"
                        if os.path.exists(media_file):
                            if not os.path.exists(media_file.replace("media","output")):
                                shutil.copy( media_file, path)
                        else:
                            print(media_file, " dosn't exist")

                    # Copying book folder from media folder, generating book.html and copying book scripts
                    if item['pages'] == 'yes':
                        media_folder = path.replace("output", "media")+ "/book/pages"
                        if os.path.isdir(media_folder):
                            if not os.path.isdir(f"{path}/book"):
                                shutil.copytree( 'book', f"{path}/book") # Copy js and styling from book folder
                                # Count the number of pages in the pages folder and add it to the book template
                                pages = len ([name for name in os.listdir(media_folder) if name.endswith('jpg')])
                                book = { "pages": pages}
                                html(book, 'dk', "book", f"{path}/book")
                            if not os.path.isdir(f"{path}/book/pages"): # Not already copied
                                shutil.copytree( media_folder, f"{path}/book/pages") # Copy images (pages folder) from media folder
                        else:
                            print(media_folder, " dosn't exist")
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
