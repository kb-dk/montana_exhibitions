from jinja2 import Template

def html(obj, template_name, folder):
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
