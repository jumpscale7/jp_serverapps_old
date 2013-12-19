def main(j,jp):
   
    #See http://docs.kolab.org/installation-guide/ubuntu.html for details

    ver = j.system.platform.ubuntu.getVersion()[3]
    if ver not in ["12.04", "12.10", "13.04", "13.10"]:
        raise Exception("Unknown ubuntu version %s"%ver)

    j.system.installtools.writefile('/etc/apt/sources.list.d/kolab.list', "deb http://obs.kolabsys.com:82/Kolab:/3.1/Ubuntu_%s/ ./\ndeb http://obs.kolabsys.com:82/Kolab:/3.1:/Updates/Ubuntu_%s/ ./"%(ver,ver))

    j.system.installtools.execute("wget http://obs.kolabsys.com:82/Kolab:/3.1/Ubuntu_%s/Release.key -O /tmp/Release.key"%ver,dieOnNonZeroExitCode=False,ignoreErrorOutput=True, useShell=True)
    j.system.installtools.execute("apt-key add /tmp/Release.key",dieOnNonZeroExitCode=False,ignoreErrorOutput=True, useShell=True)
    j.system.installtools.execute("rm -rf /tmp/Release.key",dieOnNonZeroExitCode=False,ignoreErrorOutput=True, useShell=True)
    j.system.installtools.execute("wget http://obs.kolabsys.com:82/Kolab:/3.1:/Updates/Ubuntu_%s/Release.key -O /tmp/Release.key"%ver,dieOnNonZeroExitCode=False,ignoreErrorOutput=True, useShell=True)
    j.system.installtools.execute("apt-key add /tmp/Release.key",dieOnNonZeroExitCode=False,ignoreErrorOutput=True, useShell=True)
    j.system.installtools.execute("rm -rf /tmp/Release.key",dieOnNonZeroExitCode=False,ignoreErrorOutput=True, useShell=True)

    j.system.installtools.writefile('/etc/apt/preferences.d/kolab', "Package: *\nPin: origin obs.kolabsys.com\nPin-Priority: 501")

    j.system.platform.ubuntu.updatePackageMetadata()
    j.system.platform.ubuntu.install('kolab')

