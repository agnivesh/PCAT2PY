#!/usr/bin/python
################################################################################
# 2112e476-5cc5-11e4-af55-00155d01fe08
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
        self.uuid = "2112e476-5cc5-11e4-af55-00155d01fe08"
        
    def check(self, cli):
        # Initialize Compliance
        self.is_compliant = True
        
        # Execute command and parse capture standard output
        stdout = cli.system("rpm -V audit | grep '^.....U'")
        
        # Split output lines
        self.output = stdout.split('\n')

        # Process standard output
        for line in self.output:
            if len(line.strip()) > 0:
                self.is_compliant = False
                 
        return self.is_compliant

    def fix(self, cli):
        cli.system("rpm --setugids audit")
