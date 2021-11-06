class SLLNode {
    constructor(val) {
        this.value = val;
        this.next = null;
    }
}

class SLL { 
    constructor() {
        this.head = null; 
    }

    // Adds a node to the front
    addFront(value) {
        var newNode = new SLLNode(value);
        newNode.next = this.head;
        this.head = newNode;
        return this.head;
    }

    // Remove a node from the front of the list
    removeFront() {
        if (this.head == null) { // Edge case: If the list is empty, nothing to remove
            return this.head;
        }
        var removedNode = this.head;
        this.head = removedNode.next;
        removedNode.next = null;
        return this.head;
    }

    // Return the value at the front (head) of the list
    front() {
        if (this.head == null) {
            return null;
        } else { 
            return this.head.value;
        }
    }
}
