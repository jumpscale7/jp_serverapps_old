def main(j,jp):
   
    jp2=j.packages.findNewest("jumpscale","portal")
    if not jp2.isInstalled(instance='$(cloudrobot.portal.instance)'):
        j.events.inputerror_critical("Could not find portal instance with name: $(cloudrobot.portal.instance), please install")
        # jp2.install(hrddata={"redis.name":"production","redis.port":"7768","redis.disk":"1","redis.mem":400},instance="$(cloudrobot.portal.instance)")

    j.system.fs.removeDirTree("$base/apps/portals/$(cloudrobot.portal.instance)/base/test__taskmanager/")

    