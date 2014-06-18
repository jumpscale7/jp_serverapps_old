def main(j,jp):

    if j.application.sandbox:
        cmd="$base/bin/python"
    else:
        cmd="python"

    pd=j.tools.startupmanager.addProcess(\
        name=jp.name,\
        cmd=cmd, \
        args="mailrobot.py",\
        env={},\
        numprocesses=1,\
        priority=100,\
        shell=False,\
        workingdir='$base/apps/mailrobot',\
        jpackage=jp,\
        domain=jp.domain,\
        ports=[],\
        autostart=False,\
        reload_signal=0,\
        user="root",\
        log=True,\
        stopcmd=None,\
        check=True,\
        timeoutcheck=20,\
        isJSapp=0,\
        upstart=False,\
        stats=True,\
        processfilterstr="mailrobot.py")#what to look for when doing ps ax to find the process
    
    pd.start()