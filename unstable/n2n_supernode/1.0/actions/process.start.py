def main(j,jp):
   
    #start the application (only relevant for server apps)
    jp.log("start n2n_supernode")
    j.tools.startupmanager.startJPackage(jp)
    jp.waitUp(timeout=20)

