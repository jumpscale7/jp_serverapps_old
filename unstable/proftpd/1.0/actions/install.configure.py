def main(j,jp):
   
    do = j.system.installtools
    passwd = "$(proftpd.password)"

    def initJumpscaleUser(passwd):
        home = "/home/jumpscale"
        name = "jumpscale"
        import JumpScale.baselib.remote.cuisine 

        j.remote.cuisine.fabric.env["password"]=passwd
        
        homeexists = j.system.fs.exists(home)

        j.system.platform.ubuntu.createUser(name, passwd, home=home)
        c = j.remote.cuisine.api

        if not homeexists:
            c.dir_ensure(home, owner=name, group=name, mode=770, recursive=True)

        # if j.system.fs.exists("/root/.hgrc"):
        #     C = j.system.fs.fileGetContents("/root/.hgrc")
        #     C2 = ""

        #     for line in C.split("\n"):
        #         if line.find("[trusted]") <> -1:
        #             break
        #         C2 += "%s\n" % line

        #     C2 += "[trusted]\n"
        #     C2 += "users = jumpscale\n\n"

        #     j.system.fs.writeFile("/root/.hgrc", C2)

    initJumpscaleUser(passwd)

    

    j.system.fs.createDir("/opt/jpackagesftp")

    C = """

ServerName          "ProFTPD Default Installation"
ServerType          standalone
DefaultServer       on
Port                21
Umask               022
MaxInstances        30

RequireValidShell   no

User                proftpd
Group               proftpd

#DefaultRoot /opt/jpackagesftp

#TransferLog /var/log/proftpd/xferlog
SystemLog   /var/log/proftpd/proftpd.log

DefaultRoot                    ~

<Directory />

AllowOverwrite  on

<Limit WRITE STOR MKD RMD DELE RNTO>
    DenyUser ftp
</Limit>

</Directory>


"""
    j.system.fs.writeFile("/etc/proftpd/proftpd.conf", C)

    import JumpScale.baselib.remote.cuisine

    c = j.remote.cuisine.api

    ftphome = "/opt/jpackagesftp"
    ftpname = "jpackages"

    j.system.platform.ubuntu.createUser(ftpname, passwd, home=ftphome)
    j.system.platform.ubuntu.createUser("proftpd", "$(jpackageserver.password)")
    j.system.platform.ubuntu.createGroup("proftpd")
    j.system.platform.ubuntu.addUser2Group("proftpd", "proftpd")
    j.system.platform.ubuntu.addUser2Group(ftpname, "jumpscale")
    j.system.platform.ubuntu.addUser2Group(ftpname, "ftp")
    j.system.platform.ubuntu.addUser2Group(ftpname, "proftpd")
    j.system.platform.ubuntu.addUser2Group("jumpscale", "proftpd")
    j.system.platform.ubuntu.addUser2Group("jumpscale", "ftp")

    c.dir_ensure(ftphome, owner=ftpname, group=ftpname, mode=770, recursive=True)

    do.execute("/etc/init.d/proftpd restart")

    # do.createdir("/opt/code")
    # do.createdir("$(jumpscale.paths.base)")

    # def symlink(src, dest):
    #     try:
    #         j.system.fs.remove(dest)
    #     except Exception, e:
    #         if str(e).find("could not be removed") <> -1:
    #             cmd = "umount %s" % dest
    #             try:
    #                 do.execute(cmd)
    #             except:
    #                 pass

    #     j.system.fs.createDir(dest)
    #     cmd = "mount --bind %s %s" % (src, dest)
    #     do.execute(cmd)

    # symlink("/opt/code", "/home/jumpscale/code")
    # symlink("$(jumpscale.paths.base)", "/home/jumpscale/jumpscale")
    # symlink("/opt/jpackagesftp", "/home/jumpscale/jpackages")
    # symlink("/opt/jpackagesftp", "/home/ftp/jpackages")
    # symlink("/opt/jpackagesftp", "/home/jpackages/jpackages")
