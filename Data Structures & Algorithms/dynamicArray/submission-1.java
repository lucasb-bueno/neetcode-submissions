class DynamicArray {
    private int[] arr;
    private int currCapacity = 0;
    private int size = 0;

    public DynamicArray(int capacity) {
        arr = new int[capacity];
        currCapacity = capacity;
    }

    public int get(int i) {
        return arr[i];
    }

    public void set(int i, int n) {
        arr[i] = n;
    }

    public void pushback(int n) {
        if (size >= currCapacity) {
            resize();
        }
        arr[size] = n;
        size++;
    }

    public int popback() {
        int prev = arr[size - 1];
        size--;
        return prev;
    }

    private void resize() {
        currCapacity *= 2;
        int[] newArr = new int[currCapacity];
        for (int i = 0; i < size; i++) {
            newArr[i] = arr[i];
        }
        arr = newArr;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return currCapacity;
    }
}
