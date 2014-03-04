def main(j,jp):
   
    do=j.system.process.execute
    do("apt-get install -f -y")
    do("/etc/init.d/webmin restart")

    
    pass