from jinja2 import Template

def html(obj, file_path):
    with open('template/index.jinja2', 'r') as f:
        template = f.read()
    data = {
        "title": obj['theme']
    }

    j2_template = Template(template)
    html_output = j2_template.render(data)

    html_file = open(file_path, 'w')
    html_file.write(html_output)
    html_file.close()
