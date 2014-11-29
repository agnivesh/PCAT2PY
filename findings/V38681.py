#!/usr/bin/python
################################################################################
# V38681
# 
# Justin Dierking
# justindierking@hardbitsolutions.com
# 
# phnomcobra@gmail.com
#
# Python implementation of PCAT by Hardbit Solutions:
#
# 06/19/2014 Original construction
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
        return "CAT III"
    
    def get_rule_id(self):
        return "SV-50482r2_rule"
    
    def get_rule_version(self):
        return "RHEL-06-000294"
    
    def get_group_id(self):
        return "V-38681"
    
    def get_group_title(self):
        return "SRG-OS-999999"
    
    def get_rule_title(self):
        return "All GIDs referenced in /etc/passwd must be defined in /etc/group"
    
    def get_vulnerability_discussion(self):
        return "Inconsistency in GIDs between /etc/passwd and /etc/group could lead to a user having unintended rights."
    
    def set_verbose(self, verbose):
        self.__verbose = bool(verbose)
        
    def check(self, cli):
        # Initialize Compliance
        self.__is_compliant = True
        
        # Execute command and parse capture standard output
        stdout = cli.system("pwck -r | grep 'no group'")
        
        # Split output lines
        self.__output = stdout.split('\n')

        # Process standard output
        line_number = 0	
        for line in self.__output:
            line_number += 1
        
            if self.__verbose:
                print("STDOUT LINE " + str(line_number) + ": " + line)	
            
            if len(line.strip()) > 0:
                self.__is_compliant = False
        
        return self.__is_compliant
    
    def get_compliance(self):
        return self.__is_compliant

    def get_posture(self):
        return "RHEL6"