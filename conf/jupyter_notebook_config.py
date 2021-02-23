# Jenkins
import tempfile, os

def _run_jenkins_proxy(port):
    conf = tempfile.NamedTemporaryFile(mode='w', delete=False)
    conf.write('''
LogLevel Warning
MaxClients 5
MinSpareServers 5
MaxSpareServers 20
StartServers 10
Port {port}
ReverseOnly Yes
Upstream http localhost:8080
'''.format(port=port))
    conf.close()
    return ['tinyproxy', '-d', '-c', conf.name]

c.ServerProxy.servers = {
  'jenkins': {
    'command': _run_jenkins_proxy, # Nothing to do
    'absolute_url': True,
    'timeout': 30,
  }
}

hub_prefix = os.environ.get('JUPYTERHUB_SERVICE_PREFIX', None)
if hub_prefix is not None:
  # If this server is working under jupyterhub, we can omit authentication
  c.NotebookApp.token = ''
  c.NotebookApp.password = ''
  c.NotebookApp.base_url = hub_prefix
