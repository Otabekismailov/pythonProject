# class Node:
#     def __init__(self, val, next=None) -> None:
#         self.val = val
#         self.next = next
#
#
#
# def __iter__(self):
#     node = self.head
#     while node is not None:
#         yield node
#         node = node.next
# class Node:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
#
#
# l1 = [2, 4, 3]
# l2 = [5, 6, 4]
# head = Node(0)
# tmp = head
# while tmp:
#     print(tmp.val)
#     tmp = tmp.next
import collections
#
# def append_(head , value):
#     tmp = head.next
#     n6 = Node(value)
#     while tmp.next:
#         tmp = tmp.next
#     tmp.next = n6
#     return head
#
# head = append_(head , 10)
#
# def insert_(head , index , value):
#     tmp = head.next
#     c = 0
#     n_new = Node(value)
#     while tmp:
#         if c+1 == index:
#             n_new.next = tmp.next
#             tmp.next = n_new
#
#         tmp = tmp.next
#         c += 1
#     return head


# head = insert_(head , 1 , 20)
# head = insert_(head , 4 , 30)


# tmp = head.next
# while tmp:
#     print(tmp.val , end= ' ')
#     tmp = tmp.next
# def sotr(nums1: list, nums2: list) -> float:
#     nums3 = nums1 + nums2
#     for i in sorted(nums3):
#         nums3.reverse()
#     nums3 = set(nums3)
#     nums3 = list(nums3)
#     if len(nums3) == 1:
#         s = 0
#         for i in nums3:
#             s += i
#         return float(s)
#     elif len(nums3) == 3:
#         s = 0
#         for i in nums3:
#             s += i
#             if s == 0:
#                 return float(s)
#
#             else:
#                 return float(s)
#     else:
#         s = len(nums3) // 2
#         c = len(nums3)
#         a = nums3[0:s]
#         b = nums3[s:c]
#         p = a[-1] + b[0]
#         return float(p) / 2


# nums1 = [0, 0, 0, 0, 0]
# nums2 = [-1, 0, 0, 0, 0, 0, 1]
#
# s = sotr(nums1, nums2)
# print(s)
from collections import Counter

# def tas(a):
#     s = Counter(a).values()
#     r = 0
#     for i in s:
#         if i == 1:
#             return -1
#         else:
#             r += i // 3 + bool(i % 3)
#     return r
#
#
from collections import Counter, deque


# def nums(a, b, c):
#     return list(set(list(set(a) & set(b)) + list(set(b) & set(c)) + list(set(a) & set(c))))
# nums2 = [4, 3, 3]
# nums3 = [5]

# nums1 = [1, 1, 3, 2]
# nums2 = [2, 3]
# nums3 = [3]
# print(nums(nums1, nums2, nums3))
# def fa(nums):
#     s = 0
#     nums.sort()
#     for i in range(len(nums)):
#         if nums[i] > nums[0] and nums[i] < nums[-1]:
#             s += 1
#     return s

# def taqiqlanagansoz(p, banned) -> str:
#     p = p.lower()
#     p = p.replace('.', '').replace("'", '')
#     p = p.replace('?', '').replace('!', '').replace(',', '').replace(';', '')
#     d = Counter(p.split())
#
#     for key in banned:
#         if d.get(key):
#             d.pop(key)
#         print(d)
#     return d.most_common(1)[0][0]


# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# paragraph = "a, a, a, a, b,b,b,c, c"
# banned = ["a"]

def palindirom(x):
    if x < 0:
        return False
    else:
        a = str(x)
        if len(a) == 1:
            return True
        for i in a.split():
            if i[::-1] == a:
                return True
            else:
                return False

    # for i in a:
    #     print(i)
    #     if i == x:
    #         return True
    #     else:
    #         return False

    #
    # def sum3(nums2: list[int]):
    #     nums2.sort()
    #     res = []
    #     for i in range(len(nums2)):
    #         if i > 0 and nums2[i] == nums2[i - 1]:
    #             continue
    #         l = i + 1
    #         r = len(nums2) - 1
    #         while l < r:
    #             if nums2[i] + nums2[l] + nums2[r] == 0:
    #                 res.append([nums2[i], nums2[l], nums2[r]])
    #                 l += 1
    #                 while nums2[l] == nums2[l - 1] and l < r:
    #                     l += 1
    #             elif nums2[i] + nums2[l] + nums2[r] > 0:
    #                 r -= 1
    #             else:
    #                 l += 1
    #     return res
    # nums = [-1,0,1,2,-1,-4]
    # print(sum3(nums))
    # def mux(n):
    #     ma = []
    #     mi = []
    #     for i in n:
    #         if i < 0:
    #             mi.append(i)
    #         elif i > 0:
    #             ma.append(i)
    #     return max(len(mi), len(ma))

    # nums = [-2, -1, -1, 1, 2, 3]
    # nums = [-3, -2, -1, 0, 0, 1, 2]
    # nums = [5, 20, 66, 1314]
    # print(mux(nums))

    #
    # data=[]
    #
    #
    # d = {
    #   'f_name': f_name,
    #   'u_name': u_name,
    #   'password': password,
    #   'is_client': is_client,
    #   'id': data[-1]['id']
    # }
    # print(d)
    #
    # d['id'] = d['id'] + 1
    # print('\nYour ID: ' + str(d['id']))
    #
    # data.append(d)
    # with open('register.json', 'w') as file:
    #   json.dump(data, file, indent=3)

    # def top(strs):
    #     res = []
    #     if strs and len(strs) > 0:
    #         strs = sorted(strs)
    #         first, last = strs[0], strs[-1]
    #         for i in range(len(first)):
    #             if len(last) > i and last[i] == first[i]:
    #                 res.append(last[i])
    #             else:
    #                 return "".join(res)
    #     return "".join(res)
    #
    # strs = ["flower", "flow", "flight"]
    # print(top(strs))
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    #
    #
    # class Top():
    #     def mergeTwoLists(self, l1, l2):
    #         l = []
    #         while l1:
    #             l.append(l1.valu)
    #             l1 = l1.next
    #         print(l)
    #         l.sort()
    #         s = t = ListNode()
    #         for i in l:
    #             s.next = ListNode(i)
    #             s = s.next
    #         return t.next
    #
    #
    # list1 = [1, 2, 4]
    # list2 = [1, 3, 4]
    #
    # i = Top()
    # s = i.mergeTwoLists(list1, list2)
    # print(s)
    #
    # def Bool(s: str):
    #     # for i in s.split():
    #     #     if i in '()''[]''{}':
    #     #         return True
    #     #     else:
    #     #         return False
    #     stack = []
    #     for c in s:
    #         if c in ['(', '{', '[']:
    #             stack.append(c)
    #         elif c == ')' and len(stack) != 0 and stack[-1] == '(':
    #             stack.pop()
    #         elif c == '}' and len(stack) != 0 and stack[-1] == '{':
    #             stack.pop()
    #         elif c == ']' and len(stack) != 0 and stack[-1] == '[':
    #             stack.pop()
    #         else:
    #             return False
    #     return stack == []
    #
    # s1 = "()"
    # s2 = "()[]{}"
    # s3 = "(]"
    #
    # print(Bool(s1))


# def removeElement(nums: list[int], val: int) -> int:
#         for i in nums:
#             if i == val:
#                 nums.count(i)
#                 for j in range(nums.count(i)):
#                     nums.remove(i)
#         return len(nums)


# def sort2(n):
#     if len(nums) == 0:
#         return 0
#     i = 0
#     for j in range(1, len(nums)):
#         if nums[j] != nums[i]:
#             i += 1
#             nums[i] = nums[j]
#     return i + 1
#
#
# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# print(sort2(nums))
# def qosh(nums: list[int], target: int):
#     for i in range(len(nums)):
#         if nums[i] == target:
#             return i
#         else:
#             for i in range(len(nums)):
#                 if nums[i] != target:
#                     nums.append(target)
#             a = 0
#             for i, v in enumerate(sorted(list(set(nums)))):
#                 if v == target:
#                     a = i
#             return a


# nums = [1, 3, 5, 6]
# target = 5
# nums = [1, 7, 8, 10]
# target = 10
# print(qosh(nums, target))


# def maxstr(s: str):
#     a = []
#     for i in s.split():
#         a.append(len(i))
#     return max(a)
#
#
# s = "luffy is still joyboy"
# print(maxstr(s))

def nomer(digits: list[int]):
    s = int(''.join(str(e) for e in digits)) + 1
    res = [int(i) for i in str(s)]
    return res


digits = [4, 2, 9]
print(nomer(digits))

s = 'otabek'
