class MinStack {


    // Take example of -2,0,-3

    Stack<Integer> s;
    Stack<Integer> minS;

    public MinStack() {
        s = new Stack<>();
        minS = new Stack<>();
    }
    
    public void push(int val) {
        if (s.isEmpty()) {
            minS.push(val);
        } else {
            if (val < minS.peek()) minS.push(val);
            else minS.push(minS.peek());
        }
        s.push(val);
    }
    
    public void pop() {
        if (s.isEmpty()) return;
        s.pop();
        minS.pop();
    }
    
    public int top() {
        return s.peek();
    }
    
    public int getMin() {
        return minS.peek();
    }
}
