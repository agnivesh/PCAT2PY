
#!/usr/bin/python
################################################################################
# V15564
#
# Justin Dierking
# justindierking@hardbitsolutions.com
# 
# phnomcobra@gmail.com
#
# Python implementation of PCAT by Hardbit Solutions:
# Generated DWORD EQ finding
#
# 09/21/2014 Original Construction
################################################################################

class Finding:
    # Initialize compliance
    def __init__(self):
        self.__verbose = False
        self.__output = []
        self.__is_compliant = []

    def get_verbose(self):
        return self.__verbose

    def get_output(self):
        return self.__output

    def get_severity(self):
        return "CAT II"

    def get_rule_id(self):
        return ""

    def get_rule_version(self):
        return ""

    def get_group_id(self):
        return r"V-15564"

    def get_group_title(self):
        return ""

    def get_rule_title(self):
        return r"The update check interval must be configured and set to 30 days."

    def get_vulnerability_discussion(self):
        return r"Although Microsoft thoroughly tests all patches and service packs before they are published, organizations should carefully control all of the software that is installed on their managed computers. This setting specifies the update check interval, automatic installation and the default interval value, which is 30 days. If you enable this policy setting, the user will not be able to configure the update check interval, and computers will not automatically download and install updates for Internet Explorer. The update check interval must be specified. If you disable or do not configure this policy setting, the user will have the freedom to configure the update check interval. Manipulate the policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Settings -> Component Updates -> Periodic check for updates to Internet Explorer and Internet Tools -> ''Turn off configuring the update check interval (in days)'' to ?Enabled? and select ''30'' from the drop-down box."

    def set_verbose(self, verbose):
        self.__verbose = bool(verbose)

    def check(self, cli):
        # Initialize Compliance
        self.__is_compliant = False

        # Get Registry DWORD
        dword = cli.get_reg_dword(r'HKLM:\Software\Policies\Microsoft\Internet Explorer\Main', 'Update_Check_Interval')

        # Output Lines
        self.__output = [r'HKLM:\Software\Policies\Microsoft\Internet Explorer\Main', ('Update_Check_Interval=' + str(dword))]

        if self.__verbose:
            print self.__output

        if dword == 30:
            self.__is_compliant = True

        return self.__is_compliant

    def fix(self, cli):
        cli.powershell(r"New-Item -path 'HKLM:\Software\Policies\Microsoft'")
        cli.powershell(r"New-Item -path 'HKLM:\Software\Policies\Microsoft\Internet Explorer'")
        cli.powershell(r"New-Item -path 'HKLM:\Software\Policies\Microsoft\Internet Explorer\Main'")
        cli.powershell(r"Set-ItemProperty -path 'HKLM:\Software\Policies\Microsoft\Internet Explorer\Main' -name 'Update_Check_Interval' -value 30 -Type DWord")

    def get_compliance(self):
        return self.__is_compliant

    def get_posture(self):
        return "IE9"

    def get_hippa(self):
        return ""
    
    def get_pci(self):
        return ""
    
    def get_hbs_id(self):
        return "HBSPCATIE9000099"
    
    def get_dod8500_2(self):
        return "ECSC-1"

    def get_800_53(self):
        return "CM-6"
    
    def get_iso_27001(self):
        return "A.10.10.2"