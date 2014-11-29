#!/usr/bin/python
################################################################################
# 21165e3a-5cc5-11e4-af55-00155d01fe08
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
        self.uuid = "21165e3a-5cc5-11e4-af55-00155d01fe08"
        
    def check(self, cli):
        # Initialize Compliance
        self.is_compliant = False

        # Get Registry DWORD
        dword = cli.get_reg_dword(r'HKLM:\System\CurrentControlSet\Services\Netlogon\Parameters', 'RefusePasswordChange')

        # Output Lines
        self.output = [r'HKLM:\System\CurrentControlSet\Services\Netlogon\Parameters', ('RefusePasswordChange=' + str(dword))]

        if dword == 0:
            self.is_compliant = True

        return self.is_compliant

    def fix(self, cli):
        cli.powershell(r"New-Item -path 'HKLM:\System\CurrentControlSet\Services'")
        cli.powershell(r"New-Item -path 'HKLM:\System\CurrentControlSet\Services\Netlogon'")
        cli.powershell(r"New-Item -path 'HKLM:\System\CurrentControlSet\Services\Netlogon\Parameters'")
        cli.powershell(r"Set-ItemProperty -path 'HKLM:\System\CurrentControlSet\Services\Netlogon\Parameters' -name 'RefusePasswordChange' -value 0 -Type DWord")
