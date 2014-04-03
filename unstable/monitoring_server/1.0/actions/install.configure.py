def main(j,jp):

	#configure the package 

	import subprocess
	import os
	
	#newppa="ppa:formorer/icinga"
	packs="dbconfig-common icinga icinga-idoutils mysql-server libdbd-mysql mysql-client apache2 apache2-bin apache2-data apache2-utils"
	ido_configfile="/etc/icinga/modules/idoutils.cfg"
	icinga_configfile="/etc/default/icinga"
	ido_config='''\
	define module{
	        module_name     idomod
	        module_type     neb
	        path            /usr/lib/icinga/idomod.so
	        args            config_file=/etc/icinga/idomod.cfg
	        }
	'''
	icinga_config='''\
	# /etc/default/icinga
	
	# location of the icinga configuration file
	ICINGACFG="/etc/icinga/icinga.cfg"
	
	# location of the CGI configuration file
	CGICFG="/etc/icinga/cgi.cfg"
	
	# nicelevel to run icinga daemon with
	NICENESS=5
	
	# start ido2db daemon (no/yes)
	IDO2DB=yes
	
	# if you use pam_tmpdir, you need to explicitly set TMPDIR:
	#TMPDIR=/tmp
	'''
	def checkStatus(x):
	    if x != 0:
	        exit(x)
	
	#exitcode = subprocess.call(["add-apt-repository -y " + newppa], shell=True)
	#checkStatus(exitcode)
	exitcode = subprocess.call(["apt-get install -y " + packs], shell=True)
	checkStatus(exitcode)
	
	f = open(ido_configfile,'w')
	f.write(ido_config)
	f.close()
	
	f = open(icinga_configfile,'w')
	f.write(icinga_config)
	f.close()
	
	subprocess.call(["ln", "-s", "/usr/lib/icinga/idomod.so", "/usr/sbin/"])
	
	def serviceRestart(s):
    		subprocess.call(["service " + s + " restart"], shell=True)

	serviceRestart("ido2db")
	serviceRestart("icinga")

	if os.path.exists('/etc/icinga/objects/vscalers.cfg'):
		os.system('cp updatenagiosconf.py /etc/icinga')
		os.system('python /etc/icinga/updatenagiosconf.py')
	else:
		os.system('touch /etc/icinga/objects/vscalers.cfg')
                os.system('cp updatenagiosconf.py /etc/icinga')
                os.system('python /etc/icinga/updatenagiosconf.py')
	serviceRestart("icinga")
	f = open('/etc/crontab', 'a')
	f.write('*/5 *	* * * root  python /etc/icinga/updatenagiosconf.py')
	f.close()
	pass
