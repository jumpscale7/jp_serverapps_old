def main(j,jp):

	#configure the package 

	import subprocess
	
	packs="openssl nagios-nrpe-server nagios-plugins nagios-plugins-basic nagios-plugins-standard"
	nrpe_configfile="/etc/nagios/nrpe.cfg"

	def checkStatus(x):
	    if x != 0:
	        exit(x)
	
	exitcode = subprocess.call(["apt-get install -y " + packs], shell=True)
	checkStatus(exitcode)
	nrpe_config ="server_address=" + raw_input("\nPlease insert the monitoring server Hostname/IP: \n")
	f = open(nrpe_configfile,'a')
	f.write(nrpe_config)
	f.close()
	
	def serviceRestart(s):
		subprocess.call(["service " + s + " restart"], shell=True)

	serviceRestart("nagios-nrpe-server")
	
	pass
