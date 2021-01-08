from jinja2 import FileSystemLoader, Environment
import sys

secret, tag = sys.argv[1:3]

content={"secret": secret, "tag": tag}
env = Environment(loader=FileSystemLoader('./'))
template = env.get_template('wx-alert-smoke-test-pipeline.jinja')
ren = template.render(content)
print(ren)

with open('wx-alert-smoke-test-pipeline.yml', 'w+') as f:
    f.write(ren)
