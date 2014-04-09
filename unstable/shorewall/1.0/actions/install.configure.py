def main(j,jp):
   
    #configure the package 

    #make sure shorewall services will start
    do=j.system.process.execute
    do("sed -i 's/startup=0/startup=1/g' /etc/default/shorewall")
    do("sed -i 's/startup=0/startup=1/g' /etc/default/shorewall6")

    
