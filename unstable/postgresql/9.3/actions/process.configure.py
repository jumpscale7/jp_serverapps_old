def main(j,jp):

    import time
   
    #configure the application to autostart
    
    # jp.log("set autostart $(jp.name)")


    #numprocesses: if more than 1 process, will be started in tmux as $name_$nr
    #ports: tcpports
    #autostart: does this app start auto
    #stopcmd: if special command to stop
    #check: check app to see if its running
    #stats: gather statistics by process manager
    #timeoutcheck: how long do we wait to see if app active
    #isJSapp: to tell system if process will self register to redis (is jumpscale app)

    import os

    ospath=os.environ["PATH"]

    env={}
    env["PGDATA"]="$vardir/postgresql"
    env["PGHOME"]="$base/apps/postgresql"
    env["PATH"]="$base/apps/postgresql/bin:%s"%ospath
    env["LD_LIBRARY_PATH"]="$base/apps/postgresql/lib:\$LD_LIBRARY_PATH"
    env["PGUSER"]="postgres"
    env["PGDATABASE"]="postgres"
    env["PGPORT"]="5432"

    pd=j.tools.startupmanager.addProcess(\
        name=jp.name,\
        cmd="./postgres", \
        args="",\
        env=env,\
        numprocesses=1,\
        priority=100,\
        shell=False,\
        workingdir='$base/apps/postgresql/bin',\
        jpackage=jp,\
        domain=jp.domain,\
        ports=[5432],\
        autostart=True,\
        reload_signal=0,\
        user="postgres",\
        log=True,\
        stopcmd=None,\
        check=True,\
        timeoutcheck=10,\
        isJSapp=False,\
        upstart=False,\
        stats=True,\
        processfilterstr="postgresppppp")#what to look for when doing ps ax to find the process
    
    pd.start()

    passwd=j.application.config.get("system.superadmin.passwd")

    j.system.net.waitConnectionTest("localhost", 5432, 5)
    print "postgresql tcp port responded."

    time.sleep(1)

    cmd="cd $base/apps/postgresql/bin;./psql -U postgres template1 -c \"alter user postgres with password '%s';\" -h localhost"%passwd
    j.system.process.execute(cmd)

    print "installed"

    # def sql(sql):
    #     cmd='$base/apps/postgresql/bin/psql -U postgres -h localhost -c "%s"'%sql
    #     print cmd
    #     j.system.process.executeWithoutPipe(cmd)

    # sql("ALTER USER postgres WITH PASSWORD '%s';"%passwd)
