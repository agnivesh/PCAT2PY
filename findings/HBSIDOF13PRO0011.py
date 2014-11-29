
#!/usr/bin/python
################################################################################
# V40888
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
        return r"V-40888"

    def get_group_title(self):
        return ""

    def get_rule_title(self):
        return r"Add-ins to Office applications must be signed by a Trusted Publisher."

    def get_vulnerability_discussion(self):
        return r"Office 2013 applications do not check the digital signature on application add-ins before opening them.  Disabling or not configuring this setting may allow an application to load a dangerous add-in.  As a result, malicious code could become active on user computers or the network. Set the policy value for: User Configuration \ Administrative Templates \ Microsoft Project 2013 \ Project Options \ Security \  Trust Center \ ''Require that application add-ins are signed by Trusted Publisher'' to ''Enabled''."

    def set_verbose(self, verbose):
        self.__verbose = bool(verbose)

    def check(self, cli):
        # Initialize Compliance
        self.__is_compliant = False

        # Get Registry DWORD
        dword = cli.get_reg_dword(r'HKCU:\software\policies\Microsoft\office\15.0\ms project\security', 'requireaddinsig')

        # Output Lines
        self.__output = [r'HKCU:\software\policies\Microsoft\office\15.0\ms project\security', ('requireaddinsig=' + str(dword))]

        if self.__verbose:
            print self.__output

        if dword == 1:
            self.__is_compliant = True

        return self.__is_compliant

    def fix(self, cli):
        cli.powershell(r"New-Item -path 'HKCU:\software\policies\Microsoft\office\15.0'")
        cli.powershell(r"New-Item -path 'HKCU:\software\policies\Microsoft\office\15.0\ms project'")
        cli.powershell(r"New-Item -path 'HKCU:\software\policies\Microsoft\office\15.0\ms project\security'")
        cli.powershell(r"Set-ItemProperty -path 'HKCU:\software\policies\Microsoft\office\15.0\ms project\security' -name 'requireaddinsig' -value 1 -Type DWord")

    def get_compliance(self):
        return self.__is_compliant

    def get_posture(self):
        return "Office2013Project"

    def get_hippa(self):
        return ""
    
    def get_pci(self):
        return ""
    
    def get_hbs_id(self):
        return "HBSIDOf13Pro0011"
    
    def get_dod8500_2(self):
        return "ECSC-1"

    def get_800_53(self):
        return "CM-6"
    
    def get_iso_27001(self):
        return "A.10.10.2"