
#!/usr/bin/python
################################################################################
# V40884
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
        return r"V-40884"

    def get_group_title(self):
        return ""

    def get_rule_title(self):
        return r"Roaming settings must be stored locally and not synchronized to the Microsoft Office roaming settings web service."

    def get_vulnerability_discussion(self):
        return r"Microsoft Office includes the ability to roam settings for specific Office features amongst devices by storing this data in the cloud. This data includes user activity such as the list of most recently used documents as well as user preferences such as the Office theme. This policy setting controls whether this data is allowed to be stored in the cloud. If this policy setting is enabled, roaming settings are only stored locally and not synchronized to the Microsoft Office roaming settings web service. If this policy setting is disabled or not configured, roaming settings are synchronized with the Microsoft Office roaming settings web service and users can access their data from other devices. Existing data in the cloud is not affected by this policy. Set the policy value for: User Configuration \ Administrative Templates \ Microsoft Office 2013 \ Services \ ''Disable Roaming Office User Settings'' to ''Enabled''."

    def set_verbose(self, verbose):
        self.__verbose = bool(verbose)

    def check(self, cli):
        # Initialize Compliance
        self.__is_compliant = False

        # Get Registry DWORD
        dword = cli.get_reg_dword(r'HKCU:\software\policies\Microsoft\office\15.0\common\roaming', 'roamingsettingsdisabled')

        # Output Lines
        self.__output = [r'HKCU:\software\policies\Microsoft\office\15.0\common\roaming', ('roamingsettingsdisabled=' + str(dword))]

        if self.__verbose:
            print self.__output

        if dword == 1:
            self.__is_compliant = True

        return self.__is_compliant

    def fix(self, cli):
        cli.powershell(r"New-Item -path 'HKCU:\software\policies\Microsoft\office\15.0'")
        cli.powershell(r"New-Item -path 'HKCU:\software\policies\Microsoft\office\15.0\common'")
        cli.powershell(r"New-Item -path 'HKCU:\software\policies\Microsoft\office\15.0\common\roaming'")
        cli.powershell(r"Set-ItemProperty -path 'HKCU:\software\policies\Microsoft\office\15.0\common\roaming' -name 'roamingsettingsdisabled' -value 1 -Type DWord")

    def get_compliance(self):
        return self.__is_compliant

    def get_posture(self):
        return "Office2013OfficeSystem"

    def get_hippa(self):
        return ""
    
    def get_pci(self):
        return ""
    
    def get_hbs_id(self):
        return "HBSIDOf13OS0045"
    
    def get_dod8500_2(self):
        return "ECSC-1"

    def get_800_53(self):
        return "CM-6"
    
    def get_iso_27001(self):
        return "A.10.10.2"