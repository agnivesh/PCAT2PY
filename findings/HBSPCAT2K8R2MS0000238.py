
#!/usr/bin/python
################################################################################
# V26544
#
# Justin Dierking
# justindierking@hardbitsolutions.com
# phnomcobra@gmail.com
#
# Python implementation of PCAT by Hardbit Solutions:
# Generated AUDITPOL finding
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
        return r"V-26544"

    def get_group_title(self):
        return ""

    def get_rule_title(self):
        return r"The system will be configured to audit ''Object Access -> File System'' failures."

    def get_vulnerability_discussion(self):
        return r"Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred as well as detecting attacks.  Audit logs are necessary to provide a trail of evidence in case the system or network is compromised.  Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior.File System auditing under Object Access is used to enable the recording of events related to the access and changing of files and directories.  Auditing must also be enabled on the specific file system objects to be audited. Detailed auditing subcategories are configured in Security Settings \ Advanced Audit Policy Configuration.   The summary level settings under Security Settings \ Local Policies \ Audit Policy will not be enforced (see V-14230).Set the policy value for Computer Configuration \ Windows Settings \ Security Settings \ Advanced Audit Policy Configuration \ System Audit Policies \ Object Access \ ''Audit File System'' with ?Failure? selected."

    def set_verbose(self, verbose):
        self.__verbose = bool(verbose)

    def check(self, cli):
        # Initialize Compliance
        self.__is_compliant = False

        # Get Auditpol Value
        enabled = cli.get_auditpol(r'File System', 'Failure')

        # Output Lines
        self.__output = [r'File System', ('Failure=' + str(enabled))]

        if self.__verbose:
            print self.__output

        if enabled:
            self.__is_compliant = True

        return self.__is_compliant

    def fix(self, cli):
        cli.set_auditpol(r'File System', 'Failure', True)

    def get_compliance(self):
        return self.__is_compliant

    def get_posture(self):
        return "2008R2MS"

    def get_hippa(self):
        return "164.312(b)"
    
    def get_pci(self):
        return "10.3.4"
    
    def get_hbs_id(self):
        return "HBSPCAT2K8R2MS0000238"
    
    def get_dod8500_2(self):
        return "ECAR-2, ECAR-3"

    def get_800_53(self):
        return "AU-2 ,AU-3,AU-8"
    
    def get_iso_27001(self):
        return "A.10.10.1, A.10.10.2, A.10.10.4, A.10.10.5, A.11.5.4, A.15.3.1, A.10.10.6, A.13.2.3"