int search(int* A, int N, int x) {
    int low, mid, high;
    low = 0;
    high = N - 1;
    while(low <= high) {
        mid = (low + high) / 2;
        if (A[mid] < x) 
            low = mid + 1;
        
        else if (A[mid] > x) 
            high = mid -1;
        
        else 
            return mid;
             
    }
    return -1;
}