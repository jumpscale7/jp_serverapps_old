def main(j,jp):
   
    cmd = 'source /opt/rq-dashboard/bin/activate;cd /opt/rq-dashboard/bin;rq-dashboard -P 7768'
    args = ''
    workingdir = ""
    name = 'rqdb'
    domain = "serverapps"
    ports = [9181]
    j.tools.startupmanager.addProcess(name=name, cmd=cmd, args=args, env={}, numprocesses=1, priority=2, \
       shell=False, workingdir=workingdir,jpackage=jp,domain=domain,ports=ports)


    pass
