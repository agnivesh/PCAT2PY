
#!/usr/bin/python
################################################################################
# V2906
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
        return r"V-2906"

    def get_group_title(self):
        return ""

    def get_rule_title(self):
        return r"Ensure a complex password filter is installed and configured to enforce password complexity requirements."

    def get_vulnerability_discussion(self):
        return r"Weak passwords are easily broken with readily available hacker tools.  They can give an intruder access to the system with the privileges of the account whose password was broken. Install and configure a complex password filter to enforce password complexity requirements."

    def set_verbose(self, verbose):
        self.__verbose = bool(verbose)

    def get_posture(self):
        return "2008DC"

    def get_hippa(self):
        return "164.308(a)(5)(ii)(D)"
    
    def get_pci(self):
        return "8.2.3"
    
    def get_hbs_id(self):
        return "HBSPCAT2K8DC00000192"
    
    def get_dod8500_2(self):
        return "IAIA-1"

    def get_800_53(self):
        return "IA-2, IA-4(2), IA-5, IA-5(1), IA-5(3), IA-5(5), IA-5(6), IA-5(7)"
    
    def get_iso_27001(self):
        return "A.10.9.1, A.10.9.2, A.11.4.2, A.11.5.1, A.11.5.2 ,A.11.2.1, A.11.2.3, A.11.3.1, A.11.5.3"