#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(length):
        hash_table_insert(ht, weights[i], i)

    for i in range(length):
        compare = hash_table_retrieve(ht, (limit - weights[i]))

        if compare:
            if compare > i:
                return [compare, i]
            else:
                return [i, compare]

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


# def normalHtAnswer(weights, length, limit):
#     diff={}
#     for w in weights:
#         if diff[limit-w] in diff:
#             diff[limit-w] +=1
#         else:
#             diff[limit-w] = 1

#     ans=[]
#     for x in weights:
#         if diff[x]:
#             ans.append(diff[x])
#         if len(ans)<2:
#             return None
#         else:
#             ans.sort()
#             return ans

# print(normalHtAnswer([4,6,10,15,16], 5, 21))
