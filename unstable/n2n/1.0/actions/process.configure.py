def main(j,jp):

    import netaddr

    secret=j.application.config.get("n2n.secret")
    tracker=j.application.config.get("n2n.tracker")
    netname=j.application.config.get("n2n.netname")
    net=j.application.config.get("n2n.net")
    net2=netaddr.IPNetwork(net)
    net3=net.replace("/",":")

    if j.application.config.getBool("n2n.istracker"):
        j.system.platform.ubuntu.serviceInstall('n2ntracker', '/usr/sbin/supernode',' -l %s -f'%86)
        j.system.platform.ubuntu.startService('n2ntracker')


    
    args='-a %s -c %s -k %s -l %s:86 -s 255.255.0.0 -f'%(str(net2.ip),netname,secret,tracker)
    # print args
    cmd="%s %s"%('/usr/sbin/edge', args) #actual n2n command to run
    # print cmd
    cmd="%s & pid=$!; while true; do c=1; ping 10.10.100.5 -c1 >/dev/null || c=0; if [ \"$c\" == \"0\" ]; then kill $pid; exit 1; fi; sleep 5; done"%(cmd)   # die on ping failure
    # print cmd

    print cmd

    print "stop n2n",
    j.system.platform.ubuntu.stopService('n2n')
    print "ok"
    print "stop install service n2n"
    j.system.platform.ubuntu.serviceInstall('n2n', cmd,reload=False)
    print "ok"
    print "start n2n"
    j.system.platform.ubuntu.startService('n2n')
    print "ok"

    # edge -a 10.1.2.1 -c mynetwork -k encryptme -l a.b.c.d:xyw
