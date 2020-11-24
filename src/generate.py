from jinja2 import Template

def html(obj):
    with open('template/index.jinja2', 'r') as f:
        template = f.read()
    data = {
        "title": obj['theme']
    }

    j2_template = Template(template)
    html_output = j2_template.render(data)

    html_file = open('output/index.html', 'w')
    html_file.write(html_output)
    html_file.close()
