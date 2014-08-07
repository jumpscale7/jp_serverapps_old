def main(j,jp):

    if j.application.sandbox:
        cmd="$base/bin/python"
    else:
        cmd="python"

    services=jp.hrd_instance.getList("cloudrobot.services")

    if "mail" in services:
        pd=j.tools.startupmanager.addProcess(\
            name='mailrobot',\
            cmd="%s mailrobot.py"%cmd, \
            args="$jp_instance",\
            env={},\
            numprocesses=1,\
            priority=100,\
            shell=False,\
            workingdir='$base/apps/cloudrobot',\
            jpackage=jp,\
            domain=jp.domain,\
            ports=[25],\
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
            processfilterstr="mailrobot.py")#what to look for when doing ps ax to find the process
        
        pd.start()

    if "http" in services:
        pd=j.tools.startupmanager.addProcess(\
            name='httprobot',\
            cmd=cmd, \
            args="httprobot.py $jp_instance",\
            env={},\
            numprocesses=1,\
            priority=100,\
            shell=False,\
            workingdir='$base/apps/cloudrobot',\
            jpackage=jp,\
            domain=jp.domain,\
            ports=[8099],\
            autostart=0,\
            reload_signal=0,\
            user="root",\
            log=True,\
            stopcmd=None,\
            check=True,\
            timeoutcheck=20,\
            isJSapp=1,\
            upstart=False,\
            stats=True,\
            processfilterstr="httprobot.py")#what to look for when doing ps ax to find the process
        pd.start()

    pd=j.tools.startupmanager.addProcess(\
        name='filerobot',\
        cmd=cmd, \
        args="filerobot.py $jp_instance",\
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
        processfilterstr="filerobot.py")#what to look for when doing ps ax to find the process
    pd.start()

    if "xmpp" in services:
        pd=j.tools.startupmanager.addProcess(\
            name='xmpprobot',\
            cmd=cmd, \
            args="xmpprobot.py $jp_instance",\
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
            processfilterstr="filerobot.py")#what to look for when doing ps ax to find the process
        pd.start()