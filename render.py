import re
import sys
import yaml
import jinja2

    ######### get file's names from the command line ####################
if (len(sys.argv)==3):
    j2_file = sys.argv[1]
    yaml_file = sys.argv[2]
else:
    print ("   ######################################################\n")
    print ("   Syntax is:\n")
    print ("   python3 render.py template_file.j2 configuration_yaml_file.yml\n")
    print ("   ######################################################\n")
    quit()

loader = jinja2.FileSystemLoader('/tmp')
env = jinja2.Environment(autoescape=True, loader=loader)

   ######### take data from YAML file ####################
my_config=''
f = open( "./%s" % yaml_file )		
data1 = f.read()
f.close()

yaml_version = yaml.__version__

if (float(yaml_version) < 5.1):
    yaml_data = yaml.load(data1)
else:
    yaml_data = yaml.load(data1,Loader=yaml.FullLoader)

   ######### read templates from Jinja2 file ####################
f = open( "./%s" % j2_file )
data2 = f.read()
f.close()

template = env.from_string(data2)

   ######### YAML data + Jinja data -> configuration ####################
my_config = template.render(yaml_data);

# Remove blank lines:
my_config = "".join([s for s in my_config.splitlines(True) if (not re.search("^\s*$", s))])

print(my_config)
