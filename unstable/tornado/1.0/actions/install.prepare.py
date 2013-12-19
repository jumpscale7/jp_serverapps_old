
def main(j,jp):
    # pypackages = ['circus','circus-web','chaussette']
    # pypackages = ['tomako','tornadio2']
    pypackages=[]

    toremove = ['tornado','tornadio2','tomako'] 
    j.system.platform.python.remove(toremove)

    for pp in pypackages:
        # do.execute("pip uninstall %s" % pp)
        j.system.platform.python.install(pp)

    jp.copyPythonLibs()
   
