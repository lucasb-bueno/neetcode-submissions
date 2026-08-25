class Node {
    public int val;
    public Node next;

    public Node(int val) {
        this.val = val;
        this.next = null;
    }
}

class LinkedList {
    private Node head;
    private Node tail;
    private int size = 0;

    public LinkedList() {
        head = null;
        tail = null;
        size = 0;
    }

    public int get(int index) {
        if (index >= size) {
            return -1;
        }
        Node curr = head;
        int count = 0;

        while (curr != null) {
            if (count == index) {
                return curr.val;
            }
            curr = curr.next;
            count++;
        }
        return -1;
    }

    public void insertHead(int val) {
        Node newNode = new Node(val);
        if (head == null) {
            head = newNode;
            tail = head;
        } else {
            newNode.next = head;
            head = newNode;
        }
        size++;
    }

    public void insertTail(int val) {
        Node newNode = new Node(val);
        if (tail == null) {
            head = newNode;
            tail = newNode;
        } else {
            tail.next = newNode;
            tail = newNode;
        }
        size++;
    }

    public boolean remove(int index) {
        if (index >= size || index < 0) {
            return false;
        }
        if (head == null) {
            tail = null;
            return true;
        }
        Node curr = head;
        Node prev = null;
        int count = 0;
        while (curr != null) {
            if (count == index) {
                if (index == 0) {
                    head = head.next;
                    if (head == null) {
                        tail = null;
                    }
                    size--;
                    return true;
                } else {
                    if (curr.next == null) {
                        tail = prev;
                    }
                    prev.next = curr.next;
                    size--;
                    return true;
                }
            }
            prev = curr;
            curr = curr.next;
            count++;
        }
        return false;
    }

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> arr = new ArrayList();
        Node curr = head;
        while (curr != null) {
            arr.add(curr.val);
            curr = curr.next;
        }
        return arr;
    }
}
