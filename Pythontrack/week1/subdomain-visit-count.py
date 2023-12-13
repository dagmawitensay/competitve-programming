class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = {}

        for domain in cpdomains:
            val, domain_val = domain.split(" ")
            subdomains = domain_val.split(".")
            for i in range(len(subdomains) - 1, -1, -1):
                curr_domain = subdomains[i: ]
                joined = ".".join(curr_domain)
                counts[joined] = counts.get(joined, 0) + int(val)


        return [" ".join([str(v), k]) for k, v in counts.items()]