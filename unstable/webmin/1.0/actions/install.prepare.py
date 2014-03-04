def main(j,jp):
   
    #prepare the platform before copying the files

    #install found debs they need to be in debs dir of one or more of the platforms (all relevant platforms will be used)
    #args.qp.installUbuntuDebs()
    
    #shortcut to some usefull install tools
    do=j.system.process.execute
    do("apt-get install -f -y")
    do("apt-get install libnet-ssleay-perl  libapt-pkg-perl libauthen-pam-perl libio-pty-perl -y")
    do("apt-get install -f -y")

    #configuration is not done in this step !!!!!
    #copying files from files section of jpackages is not done in this step
    
    pass