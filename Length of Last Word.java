class Solution {
    public static void main(String[] args) {
      Solution ins = new Solution();
      System.out.println(ins.lengthOfLastWord("Hello   World") == 5);
      System.out.println(ins.lengthOfLastWord("   fly me   to   the moon  ") == 4);
      System.out.println(ins.lengthOfLastWord("luffy is still joyboy") == 6);
      System.out.println(ins.lengthOfLastWord("good morning") == 7);
      System.out.println(ins.lengthOfLastWord("good afternoon ") == 9);
      System.out.println(ins.lengthOfLastWord("  good evening") == 7);
      System.out.println(ins.lengthOfLastWord("Hello") == 5);
      System.out.println("すべてTrueなら一旦成功");
    }


    public int lengthOfLastWord(String s) {
      // ここにコードを書いてください

      //カウントするための変数
      int count = 0;

      //スペースを代入するための変数
      String space = " ";

      //文字列の前後のスペースを削除するための変数
      String frontAndRearSpacesExcluded = s.strip();

      //文字列全体の文字数をカウントする変数
      int oneSentence = frontAndRearSpacesExcluded.length();

      //次のスペースまでをカウントするための変数
      int countToSpace = 0;

      //ループするたびにカウントに応じたcount番目の文字を代入するための変数
      char charCount = 0;

      //一番最後に出てきた単語の文字数のみを代入するための変数
      int numCharLastWord = 0;
      
      //文字列の文字数分まで繰り返すループ文
      for(int i = 0 ; i<frontAndRearSpacesExcluded.length(); i++){
        charCount = frontAndRearSpacesExcluded.charAt(count);

        //ループするたびにカウントを＋１する
        count += 1;

        //文字(char型)をString型に変更する
        String stringCount = String.valueOf(charCount);

        //stringCountがspaceと同じだった場合はTrue
          if(stringCount.equals(space)){

            //countToSpaceにcountを代入する
            countToSpace = count;
          }
        numCharLastWord = oneSentence - countToSpace;
      }

      //値を引数に返す
      return numCharLastWord;
    }
}