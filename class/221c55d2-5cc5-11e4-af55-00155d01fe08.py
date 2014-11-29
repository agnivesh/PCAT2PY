#!/usr/bin/python
################################################################################
# 221c55d2-5cc5-11e4-af55-00155d01fe08
#
# Justin Dierking
# justindierking@hardbitsolutions.com
# phnomcobra@gmail.com
#
# 10/24/2014 Original Construction
################################################################################

class Finding:
    def __init__(self):
        self.output = []
        self.is_compliant = False
        self.uuid = "221c55d2-5cc5-11e4-af55-00155d01fe08"
        
    def check(self, cli):
        # Initialize Compliance
        self.is_compliant = False

        # Get Registry DWORD
        dword = cli.get_reg_dword(r'HKCU:\Software\Policies\Microsoft\Internet Explorer\Control Panel', 'FormSuggest PW Ask')

        # Output Lines
        self.output = [r'HKCU:\Software\Policies\Microsoft\Internet Explorer\Control Panel', ('FormSuggest PW Ask=' + str(dword))]

        if dword == no:
            self.is_compliant = True

        return self.is_compliant

    def fix(self, cli):
        cli.powershell(r"New-Item -path 'HKCU:\Software\Policies\Microsoft'")
        cli.powershell(r"New-Item -path 'HKCU:\Software\Policies\Microsoft\Internet Explorer'")
        cli.powershell(r"New-Item -path 'HKCU:\Software\Policies\Microsoft\Internet Explorer\Control Panel'")
        cli.powershell(r"Set-ItemProperty -path 'HKCU:\Software\Policies\Microsoft\Internet Explorer\Control Panel' -name 'FormSuggest PW Ask' -value no -Type DWord")
