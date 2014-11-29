
#!/usr/bin/python
################################################################################
# V1121
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
        return "CAT I"

    def get_rule_id(self):
        return ""

    def get_rule_version(self):
        return ""

    def get_group_id(self):
        return r"V-1121"

    def get_group_title(self):
        return ""

    def get_rule_title(self):
        return r"Installed FTP server will not be configured to allow access to the system drive."

    def get_vulnerability_discussion(self):
        return r"The FTP service allows remote users to access shared files and directories which could provide access to system resources and compromise the system, especially if the user can gain access to the root directory of the boot drive. Set the system to prevent an FTP service from allowing access to the system drive."

    def set_verbose(self, verbose):
        self.__verbose = bool(verbose)

    def get_posture(self):
        return "2012MS"

    def get_hippa(self):
        return "164.312(e)(2)(i)"
    
    def get_pci(self):
        return "2.2.2, 2.2.3"
    
    def get_hbs_id(self):
        return "HBSPCAT12MS0000026"
    
    def get_dod8500_2(self):
        return "ECCD-1, ECCD-2"

    def get_800_53(self):
        return "AC-3, AC-3(3), AC-3(4)"
    
    def get_iso_27001(self):
        return "A.7.2.2, A.10.6.1, A.10.7.3, A.10.7.4, A.10.8.1 A.10.9.1, A.10.9.2, A.10.9.3, A.11.2.2, A.11.5.4, A.11.6.1, A.12.4.3, A.15.1.3"