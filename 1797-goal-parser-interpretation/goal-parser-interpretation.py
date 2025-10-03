class Solution:
    def interpret(self, command: str) -> str:
        definition={'G':'G','()':'o','(al)':'al'}
        empty=''
        final=''
        for char in command:
            empty+=char
            if empty in definition:
                final += definition.get(empty)
                empty=''
        return final

        