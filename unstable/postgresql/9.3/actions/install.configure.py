def main(j,jp):
   
    passwd=j.application.config.get("system.superadmin.passwd")
    j.system.platform.ubuntu.createUser(name="postgres", passwd=passwd, home="/home/postgres", creategroup=True)

    datadir="$vardir/postgresql"
    j.system.fs.removeDirTree(datadir)
    j.system.fs.createDir(datadir)

    j.system.fs.chown(datadir,"postgres")
    j.system.fs.chmod(datadir,0777)

    cmd="su -c '$base/apps/postgresql/bin/initdb -D %s' postgres"%datadir
    j.system.process.executeWithoutPipe(cmd)

    def replace(path,newline,find):
        lines=j.system.fs.fileGetContents(path)
        out=""
        found=False
        for line in lines.split("\n"):
            if line.find(find)<>-1:
                line=newline
                found=True
            out+="%s\n"%line
        if found==False:
            out+="%s\n"%newline
        j.system.fs.writeFile(filename=path,contents=out)

    replace("$vardir/postgresql/pg_hba.conf","host    all             all             0.0.0.0/0               md5","0.0.0.0/0")





    
