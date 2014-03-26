def main(j,jp):

	import subprocess

	repofile = "/etc/apt/sources.list.d/reverbrain.list"
	repoconfig = '''\
	deb http://repo.reverbrain.com/precise/ current/amd64/
	deb http://repo.reverbrain.com/precise/ current/all/
	'''
	prerequisite = "curl"
	repokey = "http://repo.reverbrain.com/REVERBRAIN.GPG"
	package = "elliptics"
	
	f = open(repofile,'w')
	f.write(repoconfig)
	f.close()
	
	def checkStatus(x):
	    if x != 0:
	        exit(x)
	
	exitcode = subprocess.call(["apt-get install -y " + prerequisite], shell=True)
	checkStatus(exitcode)
	
	exitcode = subprocess.call(["curl " + repokey + " | apt-key add -"], shell=True)
	checkStatus(exitcode)
	
	exitcode = subprocess.call(["apt-get update"], shell=True)
	checkStatus(exitcode)
	
	exitcode = subprocess.call(["apt-get install -y " + package], shell=True)
	checkStatus(exitcode) 

	pass
    
