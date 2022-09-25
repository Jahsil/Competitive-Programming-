class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        newArr = [(n , h) for n ,h in zip(names , heights)]
        return [x for x , y in sorted(newArr , key = lambda i : -i[1])]
