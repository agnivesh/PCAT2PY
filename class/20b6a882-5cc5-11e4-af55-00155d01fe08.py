#!/usr/bin/python
################################################################################
# 20b6a882-5cc5-11e4-af55-00155d01fe08
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
        self.uuid = "20b6a882-5cc5-11e4-af55-00155d01fe08"
        
    def check(self, cli):
        # Initialize Compliance
        self.is_compliant = False

        # Get Registry DWORD
        sz = cli.get_reg_sz(r'HKLM:\Software\Policies\Microsoft\Windows\TCPIP\v6Transition', '6to4_State')

        # Output Lines
        self.output = [r'HKLM:\Software\Policies\Microsoft\Windows\TCPIP\v6Transition', ('6to4_State=' + sz)]

        if sz == "Disabled":
            self.is_compliant = True

        return self.is_compliant

    def fix(self, cli):
        cli.powershell(r"New-Item -path 'HKLM:\Software\Policies\Microsoft\Windows'")
        cli.powershell(r"New-Item -path 'HKLM:\Software\Policies\Microsoft\Windows\TCPIP'")
        cli.powershell(r"New-Item -path 'HKLM:\Software\Policies\Microsoft\Windows\TCPIP\v6Transition'")
        cli.powershell(r"Set-ItemProperty -path 'HKLM:\Software\Policies\Microsoft\Windows\TCPIP\v6Transition' -name '6to4_State' -value Disabled")
