
#!/usr/bin/python
################################################################################
# V36738
#
# Justin Dierking
# justindierking@hardbitsolutions.com
# phnomcobra@gmail.com
#
# Python implementation of PCAT by Hardbit Solutions:
# Generated MANUAL finding
#
# 09/30/2014 Original Construction
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
        return r"V-36738"

    def get_group_title(self):
        return ""

    def get_rule_title(self):
        return r"The Windows 8 Games app must be removed from the system."

    def get_vulnerability_discussion(self):
        return r"Some Windows 8 default apps provide links to external services and must be removed from the system. Remove the Games app from the system.Open a command prompt as an administrator.Enter ''dism /online /Get-ProvisionedAppxPackages''.Make note of the PackageName (e.g., Microsoft.XboxLIVEGames_1.0.927.0_x64__8wekyb3d8bbwe)Enter the following to remove the app package from the system: ''dism /online /Remove-ProvisionedAppxPackage /PackageName:packagename'' substituting ''packagename'' noted from the previous step.Uninstall the application from any user profiles provisioned prior to this."

    def set_verbose(self, verbose):
        self.__verbose = bool(verbose)

    def get_posture(self):
        return "Win8"

    def get_hippa(self):
        return "164.312( c)(1)"
    
    def get_pci(self):
        return "2.2.4"
    
    def get_hbs_id(self):
        return "HBSPCATWIN8000356"
    
    def get_dod8500_2(self):
        return "ECSC-1"

    def get_800_53(self):
        return "CM-6"
    
    def get_iso_27001(self):
        return "A.10.10.2"