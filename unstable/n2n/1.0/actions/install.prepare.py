def main(j,jp):
   
    j.system.platform.ubuntu.stopService('n2n')
    j.system.platform.ubuntu.stopService('n2ntracker')
    j.system.process.execute("killall edge",dieOnNonZeroExitCode=False)
    j.system.process.execute("killall supernode",dieOnNonZeroExitCode=False)
    j.system.fs.remove("/usr/bin/supernode")
    j.system.fs.remove("/usr/sbin/supernode")
    j.system.fs.remove("/usr/sbin/edge")
    j.system.fs.remove("/usr/bin/edge")
