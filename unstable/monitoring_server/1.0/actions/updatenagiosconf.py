#!/usr/bin/env python

# Fetches the latest config and compares it to running
# Reloads icinga service if needed

import requests
import subprocess
import getpass


cloudbrokerip = raw_input("Please insert CloudBroker IP/Hostname: ")
username = raw_input("Please insert Username: ")
#password = 'm09m23458kVx0p12sFtr'
password = getpass.getpass(prompt="Please insert Password: \n",stream=None)
conffile = "/etc/icinga/objects/vscalers.cfg"

def getLatestConfig(cloudbrokerip, username, password):
	res = ""

	session = requests.Session()

	# Log in
	session.post("http://%s:81"%(cloudbrokerip), {'user_login_': username, 'passwd': password})

	# Fetch nodes list
	nodes = session.get("http://192.198.94.5:81/restmachine/system/gridmanager/getNodes").json()

	# Create the hostgroup
	res += """
define hostgroup {
	hostgroup_name		vscalers
}
"""

	# Create the services
	res += """
define service{
	use			generic-service
	hostgroup_name		vscalers
	service_description	Disk Space
	check_command		check_all_disks!20%!10%
}

define service{
	use			generic-service
	hostgroup_name		vscalers
	service_description	Current Users
	check_command		check_users!20!50
}

define service{
	use			generic-service
	hostgroup_name		vscalers
	service_description	Total Processes
	check_command		check_procs!250!400
}

define service{
	use			generic-service
	hostgroup_name		vscalers
	service_description	Current Load
	check_command		check_load!5.0!4.0!3.0!10.0!6.0!4.0
}
"""

	for node in nodes:
		#print node.keys()

		# Monitor only nodes that are marked 'active'
		if node.get('active'):
			name = node.get('name')
			#print name
			ips = node.get('ipaddr')
			for ip in ips:
				# Only use ip's in the mgmt network
				if "172.16.128.0" <= ip <= "172.16.135.255":
					#print ip

					# If we got here, we should have all needed data
					res += """
define host {
	use		generic-host
	host_name	%s
	address		%s
	hostgroups	vscalers
}
"""%(name, ip)

	return res


# Fetch new config
newConf = getLatestConfig(cloudbrokerip, username, password)

# Fetch currently running config
f = open(conffile, 'r')
oldConf = f.read()
f.close()

# Only update if anything changed
if newConf != oldConf:
	print "Updated icinga config."

	f = open(conffile, 'w')
	f.write(newConf)
	f.close()

	#Reload icinga daemon
	if subprocess.call(["/etc/init.d/icinga", "reload"]) != 0:
		# something went wrong
		exit(1)

	exit(0)
