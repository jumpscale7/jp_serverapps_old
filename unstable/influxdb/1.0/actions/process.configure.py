def main(j,jp):
    name = "influxdb"
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'influxdb')
    cmd = "./influxdb"
    cfgfile = j.system.fs.joinPaths(j.dirs.cfgDir, 'influxdb', 'config.toml')
    args = "-config=%s" % cfgfile
    startstoptimeout = 60
    processfilterstr = "influxdb"
    j.tools.startupmanager.addProcess(name, cmd, args=args, domain="serverapps",jpackage=jp,ports=[],priority=1,\
        check=True,timeoutcheck=startstoptimeout,isJSapp=0,processfilterstr=processfilterstr,stats=True,upstart=False)