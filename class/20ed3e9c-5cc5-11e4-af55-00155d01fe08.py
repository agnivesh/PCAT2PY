#!/usr/bin/python
################################################################################
# 20ed3e9c-5cc5-11e4-af55-00155d01fe08
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
        self.uuid = "20ed3e9c-5cc5-11e4-af55-00155d01fe08"
        
    def check(self, cli):
        # Initialize Compliance
        self.is_compliant = True
        
        # Execute command and parse capture standard output
        stdout = cli.system("mount")
        
        # Split output lines
        self.output = stdout.split('\n')

        # Process standard output
        mount_points = []
        for line in self.output:
            if len(line.strip()) > 0:
                sub_string = (line.strip()).split(" ")
                mount_points.append(sub_string[2])
                
        stdout = ""
        for mount_point in mount_points:
            stdout += cli.system("find " + mount_point + " -xdev -type d -perm -002 \! -perm -1000")
            
        # Split output lines
        self.output = stdout.split('\n')
            
        # Process standard output
        for line in self.output:
        
            
            if len(line.strip()) > 0:
                self.is_compliant = False
                
        return self.is_compliant

    def fix(self, cli):
        # Execute command and parse capture standard output
        stdout = cli.system("mount")
        
        # Split output lines
        self.__output = stdout.split('\n')

        # Process standard output
        mount_points = []
        for line in self.__output:
            if len(line.strip()) > 0:
                sub_string = (line.strip()).split(" ")
                mount_points.append(sub_string[2])
                
        stdout = ""
        for mount_point in mount_points:
            stdout += cli.system("find " + mount_point + " -xdev -type d -perm -002 \! -perm -1000")
            
        # Split output lines
        self.__output = stdout.split('\n')
            
        # Process standard output
        for line in self.__output:
            if len(line.strip()) > 0:
                cli.system("chmod +t " + line.strip())
