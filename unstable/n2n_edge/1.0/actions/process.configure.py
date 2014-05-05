def main(j,jp):

    import netaddr

    secret=j.application.config.get("n2n.secret")
    tracker=j.application.config.get("n2n.tracker")
    netname=j.application.config.get("n2n.netname")
    net=j.application.config.get("n2n.net")
    net2=netaddr.IPNetwork(net)

    args='-a %s -c %s -k %s -l %s:86 -s 255.255.0.0 -f'%(str(net2.ip),netname,secret,tracker)
    # print args
    cmd="%s %s"%('$bindir/edge', args) #actual n2n command to run
    # print cmd
    cmd="%s & pid=$!; while true; do c=1; ping 10.10.100.5 -c1 >/dev/null || c=0; if [ \"$c\" == \"0\" ]; then kill $pid; exit 1; fi; sleep 5; done"%(cmd)   # die on ping failure
    # print cmd

    j.tools.startupmanager.addProcess('n2n_edge', cmd, '', jpackage=jp, isJSapp=0, upstart=True, processfilterstr='$bindir/edge', domain='serverapps')
