#!/usr/bin/python
################################################################################
# 20cb92a6-5cc5-11e4-af55-00155d01fe08
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
        self.uuid = "20cb92a6-5cc5-11e4-af55-00155d01fe08"
        
    def check(self, cli):
        # Initialize Compliance
        self.is_compliant = True

        # Get Accounts
        usernames = cli.get_secedit_account('NewAdministratorName')

        # Output Lines
        self.output = [("NewAdministratorName=")] + usernames
	
	# Banned Usernames
	banned_usernames = ("Administrator")

	for user in usernames:
	    if user.lower().strip('"') in banned_usernames.lower():
	        self.is_compliant = False

        return self.is_compliant
