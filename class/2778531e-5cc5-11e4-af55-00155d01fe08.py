#!/usr/bin/python
################################################################################
# 2778531e-5cc5-11e4-af55-00155d01fe08
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
        self.uuid = "2778531e-5cc5-11e4-af55-00155d01fe08"
        
    def check(self, cli):
        # Initialize Compliance
        self.is_compliant = False
        
        # Execute command and parse capture standard output
        stdout = cli.system("grep password /etc/grub.conf")
        
        # Split output lines
        self.output = stdout.split('\n')

        # Process standard output
        for line in self.output:
            if len(line.strip()) > 0:
                if "password --encrypted" in line:
                    self.is_compliant = True
        
        return self.is_compliant
