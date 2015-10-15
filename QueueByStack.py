__author__ = 'tianzhang'

# Implement a queue with two stacks


class queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        if len(self.stack1) == 0:
            while len(self.stack2) > 0:
                self.stack1.append(self.stack2.pop())
        self.stack1.append(x)

    def dequeue(self):
        if len(self.stack2) == 0:
            while len(self.stack1) > 1:
                self.stack2.append(self.stack1.pop())
            return self.stack1.pop()
        else:
            return self.stack2.pop()
'''
    def output(self):
        if len(self.stack1) > 0:
            print self.stack1
        else:
            print self.stack2[::-1]
'''

if __name__ == '__main__':
    events = [('e', 0), ('d', -1), ('e', 1), ('e', 2), ('e', 3), ('d', -1), ('e', 4), ('d', -1), ('d', -1), ('d', -1), ('d', -1), ('e', 5)]
    test = queue()
    for event in events:
        try:
            if event[0] == 'e':
                test.enqueue(event[1])
                print 'Enqueue ' + str(event[1])
                #test.output()
            else:
                print 'Dequeue ' + str(test.dequeue())
                #test.output()
        except IndexError:
            print 'Dequeue an empty queue!'
            continue
