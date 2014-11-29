
#!/usr/bin/python
################################################################################
# V17570
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
        return r"V-17570"

    def get_group_title(self):
        return ""

    def get_rule_title(self):
        return r"Object Model Prompt behavior for accessing User Property Formula must be configured."

    def get_vulnerability_discussion(self):
        return r"A custom form in Outlook could be used to gain access to sensitive address book data and potentially to change that data. By default, when a user tries to bind an address information field to a combination or formula custom field in a custom form, Outlook relies on the setting configured in the ''Programmatic Access'' section of the Trust Center. This setting determines whether Outlook will warn users about programmatic access attempts: * Only when antivirus software is out of date or not running (the default setting)* Every time* Not at allIf the ''Not at all'' option is selected, Outlook will silently grant programmatic access to any program that requests it, which could allow a malicious program to gain access to sensitive information.Note: This described default functionality assumes that the ''Outlook Security Mode'' Group Policy setting to ensure that Outlook security settings are configured by Group Policy has not been followed. If Group Policy security settings are used for Outlook, the ''Programmatic Access'' section of the Trust Center is not used. In this situation, the default is to prompt users based on computer security, which is the equivalent of the ''Only when antivirus software is out of date or not running'' option in the Trust Center, and the user experience is not affected. Set the policy value for: User Configuration \ Administrative Templates \ Microsoft Outlook 2013 \ Security \ Security Form Settings \ Programmatic Security ''Configure Outlook object model prompt When accessing the Formula property of a UserProperty object'' to ''Enabled (Automatically Deny)''."

    def set_verbose(self, verbose):
        self.__verbose = bool(verbose)

    def check(self, cli):
        # Initialize Compliance
        self.__is_compliant = False

        # Get Registry DWORD
        dword = cli.get_reg_dword(r'HKCU:\Software\Policies\Microsoft\Office\15.0\outlook\security', 'PromptOOMFormulaAccess')

        # Output Lines
        self.__output = [r'HKCU:\Software\Policies\Microsoft\Office\15.0\outlook\security', ('PromptOOMFormulaAccess=' + str(dword))]

        if self.__verbose:
            print self.__output

        if dword == 0:
            self.__is_compliant = True

        return self.__is_compliant

    def fix(self, cli):
        cli.powershell(r"New-Item -path 'HKCU:\Software\Policies\Microsoft\Office\15.0'")
        cli.powershell(r"New-Item -path 'HKCU:\Software\Policies\Microsoft\Office\15.0\outlook'")
        cli.powershell(r"New-Item -path 'HKCU:\Software\Policies\Microsoft\Office\15.0\outlook\security'")
        cli.powershell(r"Set-ItemProperty -path 'HKCU:\Software\Policies\Microsoft\Office\15.0\outlook\security' -name 'PromptOOMFormulaAccess' -value 0 -Type DWord")

    def get_compliance(self):
        return self.__is_compliant

    def get_posture(self):
        return "Office2013Outlook"

    def get_hippa(self):
        return ""
    
    def get_pci(self):
        return ""
    
    def get_hbs_id(self):
        return "HBSIDOf13Out0015"
    
    def get_dod8500_2(self):
        return "ECSC-1"

    def get_800_53(self):
        return "CM-6"
    
    def get_iso_27001(self):
        return "A.10.10.2"