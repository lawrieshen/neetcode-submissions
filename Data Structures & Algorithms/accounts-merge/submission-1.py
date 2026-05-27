class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # disjoint set union

        # emails are node, account is connections, we union them
        # Example:
        #      ["neet","neet@gmail.com","neet_dsa@gmail.com"]
        #.     we union neet and neet_dsa

        # in the final output we still need to know each union linked to which account, so we need a dict to record this information

        parents = {}
        email_to_name = {}

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parents[rootY] = rootX

        # Step 1: initialize parent and union emails in the same account
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                if email not in parents:
                    parents[email] = email
                email_to_name[email] = name
        
            for email in account[2:]:
                union(first_email, email)

        # Step 2: group union by roots
        groups = defaultdict(list)
        for email in parents:
            root = find(email)
            groups[root].append(email)

        # Step 3: build answer
        res = []
        for root, emails in groups.items():
            name = email_to_name[root]
            res.append([name] + sorted(emails))
        return res


