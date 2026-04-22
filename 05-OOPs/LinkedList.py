class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class UndoRedoLinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def perform_action(self, data):
        new_node = Node(data)

        # First action
        if self.head is None:
            self.head = new_node
            self.current = new_node
            return

        # Remove redo history
        self.current.next = None

        # Insert new node
        new_node.prev = self.current
        self.current.next = new_node
        self.current = new_node

    def undo(self):
        if self.current is None or self.current.prev is None:
            print("Nothing to undo")
            return

        self.current = self.current.prev

    def redo(self):
        if self.current is None or self.current.next is None:
            print("Nothing to redo")
            return

        self.current = self.current.next

    def show_current(self):
        if self.current:
            print("Current State:", self.current.data)
        else:
            print("No state available")


app = UndoRedoLinkedList()

app.perform_action("Type A")
app.perform_action("Type B")
app.perform_action("Type C")

app.show_current()  # C

app.undo()
app.show_current()  # B

app.undo()
app.show_current()  # A

app.redo()
app.show_current()  # B

app.perform_action("Type D")  # Redo history cleared
app.show_current()

app.redo()  # Nothing to redo
app.show_current()  # D
