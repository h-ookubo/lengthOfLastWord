from typing import *

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        #末尾のスペースを削除
        removeLastSpace = s.rstrip()

        #スペースを基準にする
        space = ' '
        basedOnSpace = removeLastSpace.split(space)

        #最後のスペースの後にある単語のみを代入する
        lastWord = basedOnSpace[-1]
        #print(lastWord)

        #文字列の長さを取得する
        num_char_end = len(lastWord)

        #数値を引数に返す
        return num_char_end

print("スタート")
assert Solution().lengthOfLastWord("Hello World") == 5
assert Solution().lengthOfLastWord("   fly me   to   the moon  ") == 4
assert Solution().lengthOfLastWord("luffy is still joyboy") == 6
print("コンプリート!本番テストへ")
