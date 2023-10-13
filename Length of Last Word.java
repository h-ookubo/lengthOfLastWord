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
      int test1;
      char test2;
      String test3 = s;
      char test4 = test3.charAt(3);
      int test5 = test3.length();
      for(int i = 0 ; i<10;i++){
      //ループ文のテンプレート
      //System.out.println(test3);
      //System.out.println(test4);
      //System.out.println(test5);
      }
      
      //"abcde".charAt(3);  //"abcde"文字列の3+1文字目を取り出す
      //"abcde".length(); //文字列の長さを取得



      return test5;
    }
}