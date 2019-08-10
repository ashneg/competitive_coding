class Solution:
    def defangIPaddr(self, address: str) -> str:
        string = '[.]'.join(list(address.split('.')))
        return string
