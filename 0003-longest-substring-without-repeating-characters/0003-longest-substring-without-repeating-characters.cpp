class Solution {
public:
    int lengthOfLongestSubstring(string s) {
    string word = "";
    word = s[0];
    vector<string> uniqueWords;
    map<char,int> letters;
    int a = 0;
    int b = 1;
    letters[s[a]] = 1;
    while (a < s.size()) {
        char letter  = s[b];
        if (letters[letter] == 1 || b == s.size()) {
            uniqueWords.push_back(word);
            a++;
            word = "";
            word += s[a];
            b = a + 1;
            letters = {};
            letters[s[a]] = 1;
        }
        else {
            letters[letter] = 1;
            word += letter;
            b++;
        }
    }
    int maxLength = 0;
    for (string word: uniqueWords) {
        int len = word.size();
        if (maxLength < len) maxLength = len;
    }
    return maxLength;
}
};