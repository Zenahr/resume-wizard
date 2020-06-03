from jinja2 import Environment, FileSystemLoader
from json import load
import yaml

template_env = Environment(loader=FileSystemLoader(searchpath='./template'))
template = template_env.get_template('template.html')

with open('template/config.yaml', 'r') as config_file:
    config = yaml.load(config_file)
    config = config['content']

with open('public/index.html', 'w') as output_file:
    output_file.write(
        template.render(
            firstName=config['firstName'],
            lastName=config['lastName']
        )
    )