def main(j,jp):   
    do=j.system.installtools

    allow=j.application.config.get("nfs.server.iprange.allow")

    j.system.fs.writeFile("/etc/exports", "/opt/code %s(rw,sync,no_root_squash,no_subtree_check)"%(allow))
    j.system.fs.writeFile("/etc/hosts.allow", "")
    j.system.fs.writeFile("/etc/hosts.deny", "")
    do.execute("exportfs -rav")