class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False

        if self.rank[pv] > self.rank[pu]:
            pu, pv = pv, pu
        
        self.parent[pv] = pu
        self.rank[pu] += self.rank[pv]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU(len(accounts))
        email_to_acc = {} # email -> account

        for i, account_data in enumerate(accounts):
            for email in account_data[1:]:
                if email not in email_to_acc:
                    email_to_acc[email] = i # neet@gamil -> 0
                else:
                    dsu.union(i, email_to_acc[email]) # neet@gmail -> 2 # dsu.find(0) === 1
        
        # reconstruct account -> email
        acc_to_emails = defaultdict(list)
        for email, account_idx in email_to_acc.items():
            resolved_account_idx = dsu.find(account_idx)
            acc_to_emails[resolved_account_idx].append(email)

        # sub acc name with id
        res = []
        for account_idx, emails in acc_to_emails.items():
            account_name = accounts[account_idx][0]
            res.append([account_name] + sorted(set(emails)))
        
        return res

                
            
