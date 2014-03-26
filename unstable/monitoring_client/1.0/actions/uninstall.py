def main(j,jp):
	jp._uninstall()

	import subprocess
	packs="nagios-nrpe-server nagios-plugins nagios-plugins-basic nagios-plugins-standard"
	subprocess.call(["apt-get remove -y " + packs], shell=True)
