
#!/usr/bin/python
################################################################################
# V40864
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
        return r"V-40864"

    def get_group_title(self):
        return ""

    def get_rule_title(self):
        return r"The prompt to save to SkyDrive must be disabled."

    def get_vulnerability_discussion(self):
        return r"SkyDrive is a cloud based storage feature that introduces the capability for users to save documents to locations outside of protected enclaves. This feature introduces the risk that FOUO and PII data, as well as other protected data, may be inadvertently stored in a nonsecure location.  This setting, which will prompt the user to sign in to SkyDrive while performing a file save operation, must be disabled. Set the policy value for: User Configuration \ Administrative Templates \ Microsoft Office 2013 \ Miscellaneous \ ''Show SkyDrive Sign In'' to ''Disabled''."

    def set_verbose(self, verbose):
        self.__verbose = bool(verbose)

    def check(self, cli):
        # Initialize Compliance
        self.__is_compliant = False

        # Get Registry DWORD
        dword = cli.get_reg_dword(r'HKCU:\software\policies\Microsoft\office\15.0\common\general', 'skydrivesigninoption')

        # Output Lines
        self.__output = [r'HKCU:\software\policies\Microsoft\office\15.0\common\general', ('skydrivesigninoption=' + str(dword))]

        if self.__verbose:
            print self.__output

        if dword == 0:
            self.__is_compliant = True

        return self.__is_compliant

    def fix(self, cli):
        cli.powershell(r"New-Item -path 'HKCU:\software\policies\Microsoft\office\15.0'")
        cli.powershell(r"New-Item -path 'HKCU:\software\policies\Microsoft\office\15.0\common'")
        cli.powershell(r"New-Item -path 'HKCU:\software\policies\Microsoft\office\15.0\common\general'")
        cli.powershell(r"Set-ItemProperty -path 'HKCU:\software\policies\Microsoft\office\15.0\common\general' -name 'skydrivesigninoption' -value 0 -Type DWord")

    def get_compliance(self):
        return self.__is_compliant

    def get_posture(self):
        return "Office2013OfficeSystem"

    def get_hippa(self):
        return ""
    
    def get_pci(self):
        return ""
    
    def get_hbs_id(self):
        return "HBSIDOf13OS0038"
    
    def get_dod8500_2(self):
        return "ECSC-1"

    def get_800_53(self):
        return "CM-6"
    
    def get_iso_27001(self):
        return "A.10.10.2"