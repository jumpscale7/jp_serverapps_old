def main(j,jp):

    instance='$(oss.portal.instance)'

    path="$base/apps/portals/%s"%instance
    if j.system.fs.isLink(path):
        j.system.fs.unlink(path)

    jp2=j.packages.findNewest("jumpscale","portal")
    if not jp2.isInstalled(instance=instance):
        j.events.inputerror_critical("Could not find portal instance with name: %s, please install"%instance)
        # jp2.install(hrddata={"redis.name":"production","redis.port":"7768","redis.disk":"1","redis.mem":400},instance="$(cloudrobot.portal.instance)")

    j.system.fs.removeDirTree("$base/apps/portals/%s/base/test__taskmanager/"%instance)

    