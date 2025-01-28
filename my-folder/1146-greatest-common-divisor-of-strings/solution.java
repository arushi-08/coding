class Solution {
    public String gcdOfStrings(String str1, String str2) {
        
        if (str2.length() < str1.length()){
            String temp = str2;
            str2 = str1;
            str1 = temp;
        }
        for (int i=str1.length();i>=0;i--){
            if (canDivide(str1.substring(0,i), str1, str2)){
                return str1.substring(0,i);
            }
        }
        return "";
    }

    public boolean canDivide(String t, String str1, String str2){
        if (t == ""){
            return false;
        }
        return t.repeat(str1.length()/t.length()).equals(str1) && t.repeat(str2.length()/t.length()).equals(str2);
    }
}
