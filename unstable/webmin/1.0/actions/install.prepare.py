def main(j,jp):
   
    #prepare the platform before copying the files

    # can happen by e.g. installing a debian package e.g. by
    packages='libnet-ssleay-perl  libapt-pkg-perl libauthen-pam-perl libio-pty-perl'
    for packagename in packages.split(" "):
        print "install %s"%packagename
        packagename=packagename.strip()
        if packagename<>"":
            j.system.platform.ubuntu.install(packagename)
       
    #install found debs they need to be in debs dir of one or more of the platforms (all relevant platforms will be used)
    #args.qp.installUbuntuDebs()
    
    #shortcut to some usefull install tools
    do=j.system.installtools
    do.execute("apt-get install -f -y")

    #configuration is not done in this step !!!!!
    #copying files from files section of jpackages is not done in this step
    
    pass