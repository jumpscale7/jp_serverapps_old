def main(j,jp):
    name = "influxdb"
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'influxdb')
    cmd = "./influxdb"
    cfgfile = j.system.fs.joinPaths(j.dirs.cfgDir, 'influxdb', 'config.toml')
    args = "-config=%s" % cfgfile
    startstoptimeout = 60
    processfilterstr = "./influxdb -config"
    j.tools.startupmanager.addProcess(name, cmd, workingdir=workingdir, args=args, domain="serverapps",jpackage=jp,ports=[8086,8090,8083],priority=1,\
        check=True,timeoutcheck=startstoptimeout,isJSapp=0,processfilterstr=processfilterstr,stats=True,upstart=False)