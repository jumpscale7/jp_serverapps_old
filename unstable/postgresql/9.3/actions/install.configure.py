def main(j,jp):
   
    j.system.platform.ubuntu.createUser(name="postgres", passwd="$(system.superadmin.passwd)", home="/home/postgres", creategroup=True)

    datadir="$vardir/postgresql"

    j.system.fs.chown(datadir,"postgres")
    j.system.fs.chmod(datadir,0700)
    
