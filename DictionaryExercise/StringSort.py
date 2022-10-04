"""
Sort an input of characters into a specified order.

Example 1:
Input: order = "cba", s = "abcd"

Output: "cbad"

Explanation: 
"a", "b", "c" appear in order, so the order of "a", "b", "c" 
should be "c", "b", and "a". 

Since "d" does not appear in order, it can be at any position 
in the returned string. "dcba", "cdba", "cbda" are also valid 
outputs.

Example 2:
Input: order = "bca", s = "abcab"

Output: "bbcaa"
"""

def string_sort(order: str, s: str)-> str:
    sorted_string = ""

    letters = dict.fromkeys(order, 0)

    for l in s:
        if l in letters:
            letters[l] +=1
        else:
            letters[l] = 1
        

    for key, value in letters.items():
        sorted_string += key*value

    return sorted_string
    

print(string_sort(order = "cba", s = "abcd"))
print(string_sort(order = "bca", s = "abcab"))