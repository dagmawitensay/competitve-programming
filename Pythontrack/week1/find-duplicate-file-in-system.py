class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        counts = {}

        for path in paths:
            path = path.split(" ")
            for i in range(1, len(path)):
                content = path[i].split(".")[1][4: -1]
                if content not in counts:
                    counts[content] = []

                counts[content].append(path[0] + "/" + path[i].split("(")[0])
        

        return [val for val in counts.values() if len(val) > 1]