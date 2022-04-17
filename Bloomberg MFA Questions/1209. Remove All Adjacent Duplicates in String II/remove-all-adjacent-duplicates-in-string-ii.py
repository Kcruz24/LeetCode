class Solution:
    # O(N) time ? | O(1) space
    def removeDuplicates(self, s: str, k: int) -> str:
        if len(s) < k or len(s) == 1:
            return len(s)

        prev_ptr = 0
        curr_ptr = 1
        counter = 1

        while curr_ptr < len(s):
            prev_char = s[prev_ptr]
            curr_char = s[curr_ptr]

            if prev_char != curr_char:
                prev_ptr += 1
                curr_ptr += 1
            else:
                curr_ptr += 1
                counter += 1

            if counter == k:
                s = s[:prev_ptr] + s[curr_ptr:]
                prev_ptr = 0
                curr_ptr = 1
                counter = 1

        return s


class Solution2:
    # O(N) time | O(N) space
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] #[character, count]

        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])

            if stack and stack[-1][1] == k:
                stack.pop()
                
        print('stack', stack)
        print('Comprehensive', [char * count for char, count in stack])
        return "".join([char * count for char, count in stack])




if __name__ == '__main__':
    sol = Solution2()

    s = 'deeedbbcccbdaa'
    s2 = 'abcd'
    s3 = 'aabb'

    print('solution')
    print(sol.removeDuplicates(s, 3))
    print(sol.removeDuplicates(s2, 2))
    print(sol.removeDuplicates(s3, 2))

# print()

# sample = 'deeedbbcccbdaa'
# print(sample)
# sample = sample[0:1] + sample[4:]

# print(sample)
