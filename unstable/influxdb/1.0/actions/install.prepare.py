def main(j,jp):
    try:
        j.tools.startupmanager.stopProcess("serverapps", "influxdb")
    except Exception,e:
        pass


    cmd='dpkg -r influxdb'
    j.system.installtools.execute(cmd,dieOnNonZeroExitCode=False,ignoreErrorOutput=True, useShell=True,outputToStdout=False)

    cmd='dpkg -P influxdb'
    j.system.installtools.execute(cmd,dieOnNonZeroExitCode=False,ignoreErrorOutput=True, useShell=True,outputToStdout=False)


    j.system.fs.createDir("$vardir/influxdb/data/db")
    j.system.fs.createDir("$vardir/influxdb/data/wal")
    j.system.fs.createDir("$vardir/influxdb/data/raft")
    j.system.fs.createDir("$vardir/influxdb/logs")