from typing import *

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

##################################################

        #文字数をカウントする変数
        count = 0
        #スペースを判定するための変数
        space = ' '
        #一文全体のスペースをカウントする変数
        spaceCount = 0
        #次のスペースまでをカウントする変数
        countToSpace = 0
        #次のスペースが終わるまで文字数から、スペースの数を引いた数値を代入する変数
        numCharMinCountSpace = 0
        #前回のnumCharMinCountSpaceを代入する変数
        previousNCMCS = 0
        #今回の値(numCharMinCountSpace)から前回の値(previousNCMCS)を引いた数を代入する変数
        subtractCNCMCSfromPNCMCS = 0
        #一番最後に出てきた単語の文字数のみを代入する変数
        numCharLastWord = 0
        #スペースが入る手前までの文字数をカウントする変数
        numCharWord = 0

        #sを一文字ずつiに代入して繰り返す
        for i in s :
            #iが文字列だった場合、もしくはスペースだった場合はtrue
            if i == '' or ' ' :
                count += 1
                previousNCMCS = numCharMinCountSpace
                #iがspaceと同じだった場合はtrue
                #それ以外はfalse、(1)へ
                if i == space:
                    countToSpace = count
                    spaceCount += 1
                    numCharMinCountSpace = countToSpace - spaceCount
                    #numCharMinCountSpaceがpreviousNCMCSと同じでなかった場合はtrue
                    if numCharMinCountSpace != previousNCMCS:
                        subtractCNCMCSfromPNCMCS = numCharMinCountSpace - previousNCMCS
                        numCharLastWord = subtractCNCMCSfromPNCMCS                        
                #(1)
                else:
                    numCharWord = count
                    numCharLastWord = numCharWord - countToSpace
        #値を引数に返す
        return numCharLastWord

##################################################

print("スタート")
print(Solution().lengthOfLastWord("ab "),"←2のはず")
print(Solution().lengthOfLastWord("a "),"←1のはず")
print(Solution().lengthOfLastWord("   fly me   to   the moon "),"←4のはず")
assert Solution().lengthOfLastWord("   fly me   to   the moon  ") == 4
assert Solution().lengthOfLastWord("Hello   World") == 5
assert Solution().lengthOfLastWord("good morning") == 7
assert Solution().lengthOfLastWord("good afternoon ") == 9
assert Solution().lengthOfLastWord("  good evening") == 7
assert Solution().lengthOfLastWord("luffy is still joyboy") == 6
assert Solution().lengthOfLastWord("Hello") == 5
print("コンプリート!本番テストへ")

"""
        #文字数をカウントする変数
        count = 0
        #スペースを判定するための変数
        space = ' '
        #次のスペースまでをカウントする変数
        countToSpace = 0
        #一番最後に出てきた単語の文字数のみを代入する変数
        numCharLastWord = 0
        #スペースが入る手前までの文字数をカウントする変数
        numCharWord = 0

        #sを一文字ずつiに代入して繰り返す
        for i in s :
            count += 1
            #iがspaceと同じだった場合はtrue
            #それ以外はfalse、(1)へ
            if i == space:
                countToSpace = count
            #(1)
            else:
                numCharWord = count
                numCharLastWord = numCharWord - countToSpace
        #値を引数に返す
        return numCharLastWord
"""