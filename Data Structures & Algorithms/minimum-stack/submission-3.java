class MinStack {


    // Take example of -2,0,-3 

    Stack<Long> s;
    long min;

    public MinStack() {
        s = new Stack<>();
    }
    
    public void push(int val) {
        if (s.isEmpty()) {
            s.push(0L);
            min = val;
        } else {
            s.push(val-min);
            if (val < min) {
                min = val;
            }
        }
    }
    
    public void pop() {
        if (s.peek() < 0) {
            min = min - s.peek();
        }
        s.pop();
    }
    
    public int top() {
        if (s.peek() < 0) return (int)min;
        return (int)(s.peek() + min);
    }
    
    public int getMin() {
        return (int)min;
    }
}
