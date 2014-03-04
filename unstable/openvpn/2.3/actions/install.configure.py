


def main(j,jp):
    from IPy import IP

    privnet = j.application.config.get("openvpn.privatenet")
    ip = IP(privnet)
    privnet = j.application.config.set("openvpn.privatenet.mask", str(ip.netmask()))
    privnet = j.application.config.set("openvpn.privatenet.net", str(ip.net()))

    # args.jp.copyFiles(subdir="easy-rsa",destination="%s/apps/easy-rsa"%j.dirs.baseDir,applyhrd=True) #  will copy files from subdir called root of platforms to root of system (carefull), will also use templateEngine for hrd
    # args.jp.copyFiles(subdir="openvpnconfig",destination="/etc/openvpn",applyhrd=True)

    # configure the package
    keydir = "%s/cfg/rsakeys" % j.dirs.baseDir
    appdir = "%s/apps/easy-rsa" % j.dirs.baseDir

    execute = j.system.process.executeWithoutPipe

    
    j.application.config.applyOnDir(appdir)

    if not j.system.fs.exists(keydir) or True:
        j.system.fs.createDir(keydir)
        j.system.fs.changeDir(appdir)

        # cmd="source %s/vars;./openvpn-build-server"%appdir
        # print execute(cmd)

        # do=e.execShellCmd

        # server certificate
        steps = []
        for i in range(18):
            steps.append([":", "\n"])
        steps.append(["y\/n\]\:", "y\n", "sign"])
        steps.append(["y\/n\]", "y\n", "confirmSign"])

        e = j.tools.expect.new("sh")

        cmd = ". %s/vars;./openvpn-build-server" % appdir
        res = e.executeSequence(steps, cmd)

        # client certificate
        steps = []
        steps.append(["client\?", "aclient\n", "client"])
        for i in range(10):
            steps.append([":", "\n"])
        steps.append(["y\/n\]\:", "y\n", "sign"])
        steps.append(["y\/n\]", "y\n", "confirmSign"])
        steps.append(["Data Base Updated", "", "done"])

        e = j.tools.expect.new("sh")

        cmd = ". %s/vars;./openvpn-build-client" % appdir
        e.executeSequence(steps, cmd)

    path = "%s/keys" % appdir
    for filter in ["*.crt", "*.key", "client_*", "dh1024.pem"]:
        for source in j.system.fs.listFilesInDir(path, recursive=False, filter=filter):
            dest = "/etc/openvpn/%s" % j.system.fs.getBaseName(source)
            j.system.fs.copyFile(source, dest)

    # cmd="iptables -t nat -A POSTROUTING -s $(rsa.privatenet) -o eth0 -j MASQUERADE"
    # execute(cmd)
    # cmd="service iptables save"
    # execute(cmd)

    # enable ip forwarding
    te = j.codetools.getTextFileEditor("/etc/sysctl.conf")
    te.replace1Line("net.ipv4.ip_forward = 1", includes=[".*net.ipv4.ip_forward.*"])
    te.save()

    cmd = "sysctl -p"
    execute(cmd)

    cmd = "openvpn --config /etc/openvpn/server.conf"

    j.tools.startupmanager.addProcess("openvpn", cmd, args="", numprocesses=1, priority=0, autostart=True, workingdir="/etc/openvpn",domain=jp.domain)
