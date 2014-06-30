def main(j,jp):

    if j.application.sandbox:
        cmd="$base/bin/python"
    else:
        cmd="python"

    pd=j.tools.startupmanager.addProcess(\
        name=jp.name,\
        cmd="/etc/init.d/postfix stop;%s mailrobot.py"%cmd, \
        args="",\
        env={},\
        numprocesses=1,\
        priority=100,\
        shell=False,\
        workingdir='$base/apps/cloudrobot',\
        jpackage=jp,\
        domain=jp.domain,\
        ports=[],\
        autostart=1,\
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

    pd=j.tools.startupmanager.addProcess(\
        name='httprobot',\
        cmd=cmd, \
        args="httprobot.py",\
        env={},\
        numprocesses=1,\
        priority=100,\
        shell=False,\
        workingdir='$base/apps/cloudrobot',\
        jpackage=jp,\
        domain=jp.domain,\
        ports=[],\
        autostart=1,\
        reload_signal=0,\
        user="root",\
        log=True,\
        stopcmd=None,\
        check=True,\
        timeoutcheck=20,\
        isJSapp=0,\
        upstart=False,\
        stats=True,\
        processfilterstr="httprobot.py")#what to look for when doing ps ax to find the process
    pd.start()
