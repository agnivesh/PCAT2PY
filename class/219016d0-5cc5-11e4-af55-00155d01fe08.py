#!/usr/bin/python
################################################################################
# 219016d0-5cc5-11e4-af55-00155d01fe08
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
        self.uuid = "219016d0-5cc5-11e4-af55-00155d01fe08"
        
    def check(self, cli):
        # Initialize Compliance
        self.is_compliant = False
        
        # Execute command and parse capture standard output
        stdout = cli.system("service postfix status")
        
        # Split output lines
        self.output = stdout.split('\n')

        # Process standard output
        for line in self.output:
            if "is running" in line:
                self.is_compliant = True
        
        return self.is_compliant

    def fix(self, cli):
        cli.system("chkconfig postfix on")
        cli.system("service postfix start")
