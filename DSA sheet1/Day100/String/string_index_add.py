# A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.
#
# A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.
#
# For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
# Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.



def index_add(str):
    list_data=str.split(" ")
    res_data=[]
    sn=0
    for i  in (list_data):
        data=f"{i}{sn}"
        sn+=1
        res_data.append(data)
    # sort_list=sorted(res_data,reverse=True)
    start=0
    end=len(res_data)-1
    while start < end:
        res_data[start],res_data[end]=res_data[end],res_data[start]
        start =start + 1
        end =end - 1
    ans=" ".join(res_data)
    return ans
word="The quick brown fox jumps over the lazy dog"
print(index_add(word))