'''
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. 
Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Note: The characters in the array beyond the returned length do not matter and should be ignored.
'''

class Solution:
    def compress(self, chars: List[str]) -> int:
            stack = []
            while chars != []:
                counter = 1
                last = chars.pop()
            
                while chars != [] and last == chars[-1]:
                    chars.pop()
                    counter += 1
                if counter != 1:
                    stack.append(counter)
                    counter = 1
                stack.append(last)
            output = 0
            while stack != []:
                last = str(stack.pop())
                if last.isnumeric():
                    for el in last:
                        chars.append(el)
                        output += 1
                else:
                    chars.append(last)
                    output += 1
            return output