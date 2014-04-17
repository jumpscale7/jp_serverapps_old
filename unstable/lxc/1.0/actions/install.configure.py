def main(j,jp):
   
    import JumpScale.baselib.codetools

    editor=j.codetools.getTextFileEditor("/etc/ssh/ssh_config")
    editor.replace1Line("    GSSAPIAuthentication no",includes=["GSSAPIAuthentication*"],excludes=["#"])
    editor.save()
    
