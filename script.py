from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader
from json import load

template_env = Environment(loader=FileSystemLoader(searchpath='./template'))
template = template_env.get_template('template.html')

with open('content.md') as markdown_file:
    article = markdown(markdown_file.read())

with open('template/content.json') as config_file:
    config = load(config_file)

with open('public/index.html', 'w') as output_file:
    output_file.write(
        template.render(
            title=config['title'],
            article=config['article']
        )
    )