def main(j,jp):
   
    #configure the application to no longer autostart
    
    jp.log("remove autostart n2n_supernode")
    jp.kill()
    j.tools.startupmanager.removeProcess(jp.name)


