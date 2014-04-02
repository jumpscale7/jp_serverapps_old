def main(j,jp):
   
    cmd="cd /tmp/kernel;dpkg -i linux-headers-3.13.6-*.deb linux-image-3.13.6-*.deb"
    j.system.process.executeWithoutPipe(cmd)
    
