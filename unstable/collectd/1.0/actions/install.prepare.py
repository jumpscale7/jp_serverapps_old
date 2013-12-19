def main(j,jp):
   

    j.system.platform.ubuntu.install("collectd")
       
    do=j.system.installtools

    do.execute("/etc/init.d/collectd stop")

    j.system.fs.remove("/etc/init.d/collectd")

    
    pass