class Solution {
public:
    bool closure(char a, char b){
        return (a == '(' && b == ')') || (a == '{' && b == '}') || (a == '[' && b == ']');
    }
    bool starter(char a){
        return a == '(' || a == '{' || a == '[' ;
    }
    bool ending(char b){
        return b == ')' || b == '}' || b == ']' ;
    }

bool isValid(string s) {
    int len = s.length();
    vector<int> starters;
    
    for(int i=0;i<len;i++){
        if (starter(s[i])){
            starters.push_back(s[i]);
        }
        else{
            if (!(starters.empty())){
                if (closure(starters.back(),s[i])){
                    starters.pop_back();
                } 
                else return false;
            }
            else{
                return false;
            }

        }
    }
    return starters.empty();
}
};