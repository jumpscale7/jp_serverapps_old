def main(j,jp):

    import netaddr

    secret=j.application.config.get("n2n.secret")
    tracker=j.application.config.get("n2n.tracker")
    netname=j.application.config.get("n2n.netname")
    net=j.application.config.get("n2n.net")
    net2=netaddr.IPNetwork(net)
    net3=net.replace("/",":")

    if j.application.config.getBool("n2n.istracker"):
        j.system.platform.ubuntu.serviceInstall('n2ntracker', '/usr/bin/supernode',' -l %s'%85)
        j.system.platform.ubuntu.startService('n2ntracker')


    

    args='-a %s -c %s -k %s -l %s:85'%(str(net2.ip),netname,secret,tracker)
    # print args
    j.system.platform.ubuntu.serviceInstall('n2n', '/usr/sbin/edge', args)
    j.system.platform.ubuntu.startService('n2n')

    # edge -a 10.1.2.1 -c mynetwork -k encryptme -l a.b.c.d:xyw