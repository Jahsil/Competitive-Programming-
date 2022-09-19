class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)
        
        for path in paths:
            inputs = path.split()
            directory , files = inputs[0] , inputs[1:]
            
            for file in files:
                fileName , content = file.split("(")
                content = content[:-1]
                lookup[content].append(f"{directory}/{fileName}")
        result = []
        for x in lookup.values():
            if len(x) > 1:
                result.append(x)
        return result
            
            
            
