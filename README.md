# PAY
PAY = deploymen <b>P</b>alo <b>A</b>lto from <b>Y</b>aml = Palo Alto from Yaml

PAY is rather the name of the approach, than the name of the software product.

The idea is to manage the PA configuration via text files in YAML format. It allows you to
- use a simple interface for PA configuration
- think about the configuration parameters only and not about the command's syntax or GUI-navigation
- use version control systems (for example, based on git) and follow the best practices of development for network infrastructure changes control

Mostly It might be useful in two cases: 

- you have repeated operations with the same or similar command syntax, but with different parameters. In this case, the syntax can be defined using templates (jinja2), and the parameters are described in configuration files (YAML)
- during the implementation stage of the project. This approach permits you to use the best development’s practices of change management based on git and git-like applications

This project should be considered only as a set of examples. Perhaps it will meet your expectations and design, but most likely you will want something else, more or less.
And this only means that you need to change the Jinja templates (not just the YAML files), and if you understand this method, it is easy for you.

<h3>Installation</h3>

- clone this project to your local folder
- install Python3 with YAML and Jinja2 packages

<h3>Examples</h3>

Devices: Panorama and  Palo Alto Firewall.
In these examples we always configure FWs with Panorama templates or device groups except the case of initial configuration. 


- Panorama configuration 
  - device (ntp,dns,mgmt,ha,auth,proxy): folder <a href="https://github.com/nihole/PAY/tree/master/device">device</a>
  - server profiles (snmp, syslogs, tacacs), log_settings:  folder <a href="https://github.com/nihole/PAY/tree/master/panorama">panorama</a>
- Firewall configuration:
  - Initial configuration : folder <a href="https://github.com/nihole/PAY/tree/master/initial_fw">initial_fw</a>
  - log forwarding: folder <a href="https://github.com/nihole/PAY/tree/master/shared">shared</a>
  - templates (template1):
    - bgp: folder <a href="https://github.com/nihole/PAY/tree/master/template/bgp">bgp</a>
    - device: folder <a href= "https://github.com/nihole/PAY/tree/master/template/device">device</a>
    - ha: folder <a href= "https://github.com/nihole/PAY/tree/master/template/ha">ha</a>
    - interfaces: folder <a href= "https://github.com/nihole/PAY/tree/master/template/interfaces">interfaces</a>
    - shared: folder <a href= "https://github.com/nihole/PAY/tree/master/template/shared">shared</a>
    - user-id: folder <a href= "https://github.com/nihole/PAY/tree/master/template/user-id">user-id</a>
    - zone: folder <a href= "https://github.com/nihole/PAY/tree/master/template/zpne">zone</a>
  
<h3>Configuration procedure</h3>

The procedure is simple and mainly consists of three steps:

- fill in the YAML file
- generate the TXT configuration file 
- upload it to Panorama.  

You never change the Python rendering file <a href="https://github.com/nihole/PAY/blob/master/render.py">render.py</a> and generally you don't need to change Jinja2 templates.

<h3>Details</h3>

<b><em>All steps described here have already been completed. So you don't actually have to do anything, and you can just click the links and view the configuration files.</em></b>

Let's consider, for example, that we want to configure BGP sessions.

1. Go to the correspondent folder. In this case it is  <a href="https://github.com/nihole/PAY/tree/master/template/bgp">bgp</a>

There are 2 files already there: <a href="https://github.com/nihole/PAY/blob/master/template/bgp/template.j2">template.j2</a> and <a href="https://github.com/nihole/PAY/blob/master/template/bgp/bgp_tmpl.yml">bgp_tmpl.yml</a>.
- template.j2 - is Jinja2 template. You usually don't need to change it.
- bgp_tmpl.yml - this YAML file we are going to use for our YAML file creation (if it has not been done before)

2. Create a new folder (if it has not been done before). Actually you may use any folder, but it looks reasonable to create a new folder in the current one. Let's create a folder <a href="https://github.com/nihole/PAY/tree/master/template/bgp/example1">example1</a> 

```
mkdir example1
```

3. Copy file bgp_tmpl.yml (if it has not been done before) to this folder and rename it:

```
cp bgp_tmpl.yml ./example1/bgp.yml
cd ./example1/
```

4. Fill in <a href="https://github.com/nihole/PAY/blob/master/template/bgp/example1/bgp.yml">bgp.yml</a> with configuration parameters

5. Generate <a href="https://github.com/nihole/PAY/blob/master/template/bgp/example1/bgp.txt">bgp.txt</a> file for PA configuration 

```
python3 ../../render.py ../template.j2 bgp.yml > bgp.txt
```

6. Upload this file to Panorama (cut and paste for example).
