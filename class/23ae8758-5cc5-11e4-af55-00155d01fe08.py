#!/usr/bin/python
################################################################################
# 23ae8758-5cc5-11e4-af55-00155d01fe08
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
        self.uuid = "23ae8758-5cc5-11e4-af55-00155d01fe08"
        
    def check(self, cli):
        # Initialize Compliance
        self.is_compliant = False
        
        # Execute command and parse capture standard output
        stdout = cli.system("ls -l /etc/gshadow")
        
        # Split output lines
        self.output = stdout.split('\n')

        # Process standard output
        lineNumber = 0	
        for line in self.output:
            lineNumber += 1
        
            if len(line.strip()) > 0:
                subStrings = line.split(' ')
                if "----------" in subStrings[0]:
                    self.is_compliant = True
                
        return self.is_compliant

    def fix(self, cli):
        cli.system("chmod 0000 /etc/gshadow")
