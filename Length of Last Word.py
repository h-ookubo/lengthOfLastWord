from typing import *

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        #文字数をカウントする変数
        count = 0
        #スペースを判定するための変数
        space = ' '

        countToSpace = 0

        #sを一文字ずつiに代入して繰り返す
        for i in s :

            #iが英小文字かスペースだったらcountを+1する
            if i == 'a' or 'b' or 'c' or 'd' or 'e' or 'f' or 'g' or 'h' or 'i' or 'j' or 'k' or 'l' or 'm' or 'n' or 'o' or 'p' or 'q' or 'r' or 's' or 't' or 'u' or 'v' or 'w' or 'x' or 'y' or 'z' or ' ' :
                count += 1
                
                #iがスペースだったら"count"を
                #最初のスペースまでをカウントする変数"countToSpace"へ代入する
                if i == space :
                    countToSpace = count
            
            #iがスペースではなかったら"count"を
            #最大文字数をカウントする変数"allCount"に代入する
            allCount = count
            print(count)

        #allCountからcountToSpaceを引いた値を
        #最後の単語の文字数"numCharLastWord"に代入する
        numCharLastWord = allCount - countToSpace

        #numCharLastWordの数値を引数に返す
        return numCharLastWord

print("スタート")
assert Solution().lengthOfLastWord("Hello") == 5
assert Solution().lengthOfLastWord("Hello World") == 5
assert Solution().lengthOfLastWord("   fly me   to   the moon  ") == 4
assert Solution().lengthOfLastWord("luffy is still joyboy") == 6
print("コンプリート!本番テストへ")

"""
from typing import *

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        #文字数をカウントする変数
        count = 0
        #スペースを判定するための変数
        space = ' '

        #sを一文字ずつiに代入して繰り返す
        for i in s :

            #iが英小文字かスペースだったらcountを+1する
            if i == 'a' or 'b' or 'c' or 'd' or 'e' or 'f' or 'g' or 'h' or 'i' or 'j' or 'k' or 'l' or 'm' or 'n' or 'o' or 'p' or 'q' or 'r' or 's' or 't' or 'u' or 'v' or 'w' or 'x' or 'y' or 'z' or ' ' :
                count += 1
                
                #iがスペースだったら"count"を
                #最初のスペースまでをカウントする変数"countToSpace"へ代入する
                if i == space :
                    countToSpace = count
            
            #iがスペースではなかったら"count"を
            #最大文字数をカウントする変数"allCount"に代入する
            allCount = count
            print(count)

        #allCountからcountToSpaceを引いた値を
        #最後の単語の文字数"numCharLastWord"に代入する
        numCharLastWord = allCount - countToSpace

        #numCharLastWordの数値を引数に返す
        return numCharLastWord

print("スタート")
assert Solution().lengthOfLastWord("Hello World") == 5
assert Solution().lengthOfLastWord("   fly me   to   the moon  ") == 4
assert Solution().lengthOfLastWord("luffy is still joyboy") == 6
print("コンプリート!本番テストへ")

"""