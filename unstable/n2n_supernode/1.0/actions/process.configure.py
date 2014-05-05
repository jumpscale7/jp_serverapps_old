def main(j,jp):
    cmd = '/usr/local/bin/supernode'
    args = ' -l %s -f'%86
    j.tools.startupmanager.addProcess('n2n_supernode', cmd, args, jpackage=jp, isJSapp=0, upstart=True, processfilterstr=cmd, domain='serverapps')
