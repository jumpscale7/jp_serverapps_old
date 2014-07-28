def main(j,jp):

    if j.application.sandbox:
        cmd="$base/bin/python"
    else:
        cmd="python"

    pd=j.tools.startupmanager.addProcess(\
        name='xmpprobot_$jp_instance',\
        cmd=cmd, \
        args="xmpprobot.py $(cloudrobot.xmpp.username) $(cloudrobot.xmpp.passwd)",\
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
        isJSapp=1,\
        upstart=False,\
        stats=True,\
        processfilterstr="xmpprobot.py")#what to look for when doing ps ax to find the process
    pd.start()
    