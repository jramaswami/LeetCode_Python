"""
LeetCode :: September 2021 Challenge :: Unique Email Addresses
jramaswami
"""

class Solution:

    def numUniqueEmails(self, emails):

        def plus_rule(local_name):
            """
            If you add a plus '+' in the local name, everything after the first
            plus sign will be ignored. This allows certain emails to be
            filtered. Note that this rule does not apply to domain names.
            """
            # Find first plus sign and remove the rest.
            i = local_name.find('+')
            if i >= 0:
                return local_name[:i]
            return local_name


        def dot_rule(local_name):
            """
            If you add periods '.' between some characters in the local name
            part of an email address, mail sent there will be forwarded to the
            same address without dots in the local name. Note that this rule
            does not apply to domain names.
            """
            return "".join(c for c in local_name if c != '.')

        canonical_emails = set()
        for email_address in emails:
            local_name, domain_name = email_address.split('@')
            local_name = dot_rule(plus_rule(local_name))
            canononical = "@".join((local_name, domain_name))
            canonical_emails.add(canononical)
        return len(canonical_emails)


def test_1():
    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    expected = 2
    assert Solution().numUniqueEmails(emails) == expected


def test_2():
    emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
    expected = 3
    assert Solution().numUniqueEmails(emails) == expected
