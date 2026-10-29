class Solution {
    public double findMedianSortedArrays(int[] A, int[] B) {
        if (A.length > B.length) {
            int[] t = A;
            A = B;
            B = t;
        }
        int l = 0, r = A.length-1, total = A.length + B.length, half = total/2;

        while (true) {

            int i = l + Math.floorDiv(r-l, 2), j = half-i-2;

            int Aleft = i >= 0 ? A[i] : Integer.MIN_VALUE;
            int Aright = i+1 < A.length ? A[i+1] : Integer.MAX_VALUE;
            int Bleft = j >= 0 ? B[j] : Integer.MIN_VALUE;
            int Bright = j+1 < B.length ? B[j+1] : Integer.MAX_VALUE;

            if (Aleft <= Bright && Bleft <= Aright) {
                if (total % 2 == 0) {
                    return ((double)Math.max(Aleft, Bleft) + Math.min(Aright, Bright))/2;
                } else {
                    return (double)(Math.min(Aright, Bright));
                }
            } else if (Aleft > Bright) {
                r = i-1;
            } else {
                l = i+1;
            }
            
        }
    }
}
