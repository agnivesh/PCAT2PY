#!/usr/bin/python
################################################################################
# 21584eee-5cc5-11e4-af55-00155d01fe08
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
        self.uuid = "21584eee-5cc5-11e4-af55-00155d01fe08"
        
    def check(self, cli):
        # Initialize Compliance
        self.is_compliant = False

        # Get Registry DWORD
        dword = cli.get_reg_dword(r'HKLM:\System\CurrentControlSet\Control\Session Manager\Memory Management', 'ClearPageFileAtShutdown')

        # Output Lines
        self.output = [r'HKLM:\System\CurrentControlSet\Control\Session Manager\Memory Management', ('ClearPageFileAtShutdown=' + str(dword))]

        if dword == 0:
            self.is_compliant = True

        return self.is_compliant

    def fix(self, cli):
        cli.powershell(r"New-Item -path 'HKLM:\System\CurrentControlSet\Control'")
        cli.powershell(r"New-Item -path 'HKLM:\System\CurrentControlSet\Control\Session Manager'")
        cli.powershell(r"New-Item -path 'HKLM:\System\CurrentControlSet\Control\Session Manager\Memory Management'")
        cli.powershell(r"Set-ItemProperty -path 'HKLM:\System\CurrentControlSet\Control\Session Manager\Memory Management' -name 'ClearPageFileAtShutdown' -value 0 -Type DWord")
