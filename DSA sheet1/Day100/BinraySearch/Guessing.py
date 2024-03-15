"""
Guessing game Where I enter the number then the number is check if it is match or not If not match then i will tell the numbert is
highest or lowest from that number
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
You call a pre-defined API int guess(int num), which returns three possible results:
-1:Your guess is higher than the number I picked (i.e. num > pick).
1:Your guess is lower than the number I picked (i.e. num < pick).
0:your guess is equal to the number I picked (i.e. num == pick).
"""
# this is iterative approach
# class Guess:
#     def game(self, pass_num):
#         picked_num=45
#         while True:
#             result=self.guess(picked_num,pass_num)
#             if result == 1:
#                 print(f"Your guess is {pass_num}. It's less than the picked number.")
#                 pass_num = int(input("Enter a higher number: "))
#             elif result == -1:
#                 print(f"Your guess is {pass_num}. It's greater than the picked number.")
#                 pass_num = int(input("Enter a lower number: "))
#             else:
#                 print(f"Congratulations! {pass_num} is the correct number.")
#                 break
#
#     def guess(self, picked_num,pass_num):
#         if picked_num > pass_num:  # your input number is less than Guess number
#             return 1
#         elif picked_num < pass_num:  # your input number is more than Guess number
#             return -1
#         else:
#             pass
# def user_input():
#     user_picked = int(input("Enter a number between 1 and n: "))
#     guess_game = Guess()
#     guess_game.game(user_picked)
#
#
# if __name__ == "__main__":
#     user_input()
# this is binary approach

# Binary search approach

class Solution:
    def guessNumber(self, n):
        low = 1
        high = n

        while low <= high:
            mid = (low + high) // 2
            result = self.guess(mid)

            if result == 0:
                return mid
            elif result == 1:
                high = mid - 1
            else:
                low = mid + 1

    def guess(self, pick):
        num = 5  # This is the number we are guessing. Replace it with the actual picked number.
        if num < pick:
            return 1
        elif num > pick:
            return -1
        else:
            return 0


if __name__ == "__main__":
    solution = Solution()
    n = 10  # Assuming n is 10 in this case
    result = solution.guessNumber(n)
    print("The number picked is:", result)


