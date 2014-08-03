def main(j,jp):
   
    j.application.config.applyOnDir("$cfgdir/influxdb")
    j.dirs.replaceFilesDirVars("$cfgdir/influxdb")
    
