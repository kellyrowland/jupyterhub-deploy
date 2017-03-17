import os
c.JupyterHub.authenticator_class = 'gsiauthenticator.auth.GSIAuthenticator'

#c.JupyterHub.ssl_key = '/certs/wild.nersc.gov.key'
#c.JupyterHub.ssl_cert = '/certs/wild.nersc.gov.crt'

IP='127.0.0.1'
c.JupyterHub.hub_ip = '0.0.0.0'

c.JupyterHub.hub_port = 8082

c.JupyterHub.proxy_api_ip = IP

c.JupyterHub.proxy_api_port = 8001

#c.JupyterHub.spawner_class = 'jupyterhub.spawner.GSISpawner'

c.Spawner.cmd = ['/global/homes/c/canon/bin/jupyterhub-singleuser']
c.Spawner.cmd = ['/global/common/cori/software/python/3.5-anaconda/bin/jupyterhub-singleuser']

c.Spawner.ip = '0.0.0.0'

c.GSIAuthenticator.server='nerscca.nersc.gov'

# Same initial setup as the previous example
c.JupyterHub.spawner_class = 'batchspawner.ProfilesSpawner'
c.Spawner.http_timeout = 300

# The notebook directory for the single-user server
c.Spawner.notebook_dir = '/'
c.Spawner.default_url = '/tree/global/homes/%u/%U'
#------------------------------------------------------------------------------
# BatchSpawnerBase configuration
#   Providing default values that we may omit in the profiles
#------------------------------------------------------------------------------
#c.BatchSpawnerBase.req_host = 'edison01-eth5.nersc.gov'
c.BatchSpawnerBase.req_runtime = '12:00:00'
c.BatchSpawnerBase.launcher = '/srv/jupyterhub/gsisshwrap -l {username} {host} '
c.BatchSpawnerBase.start_timeout = 300
c.Spawner.start_timeout = 300

if 'APIPORT' in os.environ:
  hub_api_url="http://jupyter-dev.nersc.gov:%s/hub/api"%os.environ['APIPORT']

if 'HUBURL' in os.environ:
  hub_api_url=os.environ['HUBURL']

c.BatchSpawnerBase.hub_api_url=hub_api_url
c.SSHSpawner.hub_api_url=hub_api_url
c.SSHSpawner.path = '/global/common/edison/software/python/3.5-anaconda/bin:/global/common/edison/das/jupyterhub/:/usr/common/usg/bin:/usr/bin:/bin:/usr/bin/X11:/usr/games:/usr/lib/mit/bin:/usr/lib/mit/sbin'
c.SSHSpawner.remote_port_command = '/global/common/cori/das/jupyterhub/get_port.py'

c.BatchSpawnerBase.tunnel = "/srv/jupyterhub/tunnel.sh"

#c.SlurmSpawner.state_exechost_exp = r'\1'
#------------------------------------------------------------------------------
# ProfilesSpawner configuration
#------------------------------------------------------------------------------
# List of profiles to offer for selection. Signature is:
#   List(Tuple( Unicode, Unicode, Type(Spawner), Dict ))
# corresponding to profile display name, unique key, Spawner class,
# dictionary of spawner config options.
# 
# The first three values will be exposed in the input_template as {display},
# {key}, and {type}
#
c.ProfilesSpawner.profiles = [
   ('Edison - 1 Node debug', 'debug', 'batchspawner.SlurmSpawner',
      dict(req_nodes='1', req_host='edison01-eth5.nersc.gov',req_partition='debug', req_runtime='0:30:00', req_memory='4gb')),
   ('Cori -1 Node debug', 'coridebug', 'batchspawner.SlurmSpawner',
      dict(req_nodes='1', req_host='cori19-224.nersc.gov',req_partition='debug', req_runtime='0:30:00',req_options='-C haswell')),
   ('Cori -3 Node debug', 'coridebug3', 'batchspawner.SlurmSpawner',
      dict(req_nodes='3', req_host='cori19-224.nersc.gov',req_partition='debug', req_runtime='0:30:00',req_options='-C haswell')),
   ('Cori Spark -3 Node debug', 'coridebugspark3', 'batchspawner.SlurmSpawner',
      dict(req_nodes='3', req_host='cori19-224.nersc.gov',req_partition='debug', req_runtime='0:30:00',req_options='-C haswell',
           req_precmd='/global/common/shared/das/jupyterhub/spark.sh')),
   ('Cori Spark -32 Node debug', 'coridebugspark32', 'batchspawner.SlurmSpawner',
      dict(req_nodes='32', req_host='cori19-224.nersc.gov',req_partition='debug', req_runtime='0:30:00',req_options='-C haswell',
           req_precmd='/global/common/shared/das/jupyterhub/spark.sh')),
   ('Cori Spark - 3 Node Regular', 'corispark3', 'batchspawner.SlurmSpawner',
      dict(req_nodes='3', req_host='cori19-224.nersc.gov',req_partition='regular', req_runtime='1:00:00',req_options='--reservation=jupyterdemo -Adasrepo -C haswell -c 64',
           req_precmd='/global/common/shared/das/jupyterhub/spark.sh')),
   ('Cori iPyParallel -1 Node debug', 'coridebugipy1', 'batchspawner.SlurmSpawner',
      dict(req_nodes='1', req_host='cori19-224.nersc.gov',req_partition='debug', req_runtime='0:30:00',req_options='-C haswell',
           req_precmd='/global/common/shared/das/jupyterhub/parallel.sh')),
   ('Cori iPyParallel -3 Node debug', 'coridebugipy3', 'batchspawner.SlurmSpawner',
      dict(req_nodes='3', req_host='cori19-224.nersc.gov',req_partition='debug', req_runtime='0:30:00',req_options='-C haswell',
           req_precmd='/global/common/shared/das/jupyterhub/parallel.sh')),
   ('Cori iPyParallel -16 Node Regular', 'coridebugipy16', 'batchspawner.SlurmSpawner',
      dict(req_nodes='16', req_host='cori19-224.nersc.gov',req_partition='regular', req_runtime='1:00:00',req_options='--reservation=jupyterdemo -Adasrepo -C haswell -c 64',
           req_precmd='/global/common/shared/das/jupyterhub/parallel.sh')),
   ( "Cori19 server",'cori19', 'sshspawner.sshspawner.SSHSpawner', 
       dict(remote_host='cori19-224.nersc.gov',ssh_command='gsissh',remote_port='2222', use_gsi=True) )
   ]


