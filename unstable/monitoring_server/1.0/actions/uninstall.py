def main(j,jp):
	jp._uninstall()


	import subprocess
	
	newppa="ppa:formorer/icinga"
	packs="dbconfig-common icinga icinga-idoutils mysql-server libdbd-mysql mysql-client apache2 apache2-bin apache2-data apache2-utils"
	
	subprocess.call(["add-apt-repository -r -y " + newppa], shell=True)
	
	subprocess.call(["apt-get remove -y " + packs], shell=True)
	
	
	subprocess.call(["rm", "-f", "/usr/sbin/idomod.so"])
