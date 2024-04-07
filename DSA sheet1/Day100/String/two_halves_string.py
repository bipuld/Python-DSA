# You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.
#
# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.
#
# Return true if a and b are alike. Otherwise, return false.


def half_str(value):
   data=[char.lower() for char in value]
   mid=len(data)//2
   first=data[:mid]

   second=data[mid:]
   vowels='aeiou'
   c1=0
   c2=0
   print(first)
   for char in first:
       for vowel in vowels:
           if char == vowel:
               c1 += 1
   print(second)
   for char in second:
       for vowel in vowels:
           if char == vowel:
               c2 += 1

   if c1 == c2:
       return True
   return False

value="aAaAaAaAaAaAaAaA"
print((half_str(value)))