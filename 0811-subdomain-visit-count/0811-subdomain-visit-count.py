class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visitCount = defaultdict(int)
        for data in cpdomains:
            visit, domain = data.split(" ")
            subdomain = domain.split(".")
            for i in range(len(subdomain)):
                dom = ".".join(subdomain[i:])
                visitCount[dom] += int(visit)
        output = []
        for domain, visitor in visitCount.items():
            output.append(f"{visitor} {domain}")
        return output