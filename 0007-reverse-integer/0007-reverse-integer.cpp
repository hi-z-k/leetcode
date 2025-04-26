#import <vector>

class Solution {
public:
    bool isInt(double x){
        return !(x <= -2147483649 || x >= 2147483648);
    }
    int reverse(int x) {
        if (!(isInt(x))) return 0;
        bool isNeg = (x<0);
        if(isNeg && !(isInt(-1*(double)x))) return 0;
        x = (x>0)?x:-1*x;
        vector<int> digits;
        int power = 0;
        while(true){
            digits.push_back(x%10);
            if (x%10==x) break;
            x /= 10;
            power++;
        }
        double reverse = 0;
        for(int d: digits){
            reverse += d*pow(10,(power));
            if (!(isInt(reverse))) return 0;
            power--;
        }
        int rev = (int)reverse;
        return (isNeg)?-1*rev:rev;
    }
};

