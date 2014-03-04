def main(j,jp):
   
    #prepare the platform before copying the files

    # can happen by e.g. installing a debian package e.g. by
    ## j.system.platform.ubuntu.install(packagename)
       
    #install found debs they need to be in debs dir of one or more of the platforms (all relevant platforms will be used)
    #args.qp.installUbuntuDebs()
    
    #shortcut to some usefull install tools
    # do=j.system.installtools
    do=j.system.process.execute
    do("add-apt-repository ppa:guacamole/stable -y")
    do("apt-get update")
    do("apt-get install libguac-client-ssh0 libguac-client-rdp0 -y")
    do("apt-get install guacamole-tomcat -y")

    #configuration is not done in this step !!!!!
    #copying files from files section of jpackages is not done in this step
    
    pass