class MinStack {
    int[] list;
    int len;
    int idx;
    public MinStack() {
        list = new int[2];
        len = list.length;
        idx = 0;
    }

    public void push(int val) {
        if (idx == len){
            int[] bigList = new int[2*len];
            for(int i=0;i<len;i++){
                bigList[i]=list[i];
            }
            len *= 2;
            bigList[idx] = val;
            list = bigList;
        }
        else list[idx] = val;
        idx++;
    }

    public void pop() {
        if (len > 0){
            list[idx-1] = 0;
            idx--;
        }
    }

    public int top() {
        return list[idx-1];
    }

    public int getMin() {
        int min = list[0];
        for(int i=1;i<idx;i++){
            if (list[i] < min) min = list[i];
        }
        return min;
    }
}
