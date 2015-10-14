__author__ = 'tianzhang'

# Implement a stack with two queues
import Queue


class stack:
    def __init__(self):
        self.queue1 = Queue.Queue()
        self.queue2 = Queue.Queue()

    def push(self, x):
        if self.queue1.empty():
            self.queue2.put(x, False)
        else:
            self.queue1.put(x, False)

    def pop(self):
        if self.queue1.empty():
            while self.queue2.qsize() > 1:
                self.queue1.put(self.queue2.get(False))
            return self.queue2.get(False)
        else:
            while self.queue1.qsize() > 1:
                self.queue2.put(self.queue1.get(False))
            return self.queue1.get(False)
'''
    def output(self):
        if self.queue1.empty():
            temp = [self.queue2[i] for i in range(self.queue2.qsize())]
        else:
            temp = [self.queue1[i] for i in range(self.queue1.qsize())]
        print temp
'''
if __name__ == '__main__':
    events = [('pu', 0), ('pu', 1), ('po', -1), ('pu', 2), ('po', -1), ('po', -1), ('pu', 3), ('pu', 4), ('po', -1), ('po', -1), ('po', -1), ('pu', 5)]
    test = stack()
    for event in events:
        try:
            if event[0] == 'pu':
                test.push(event[1])
                print 'Push ' + str(event[1])
            else:
                print 'Pop ' + str(test.pop())
        except Queue.Empty as e:
            print "Pop an empty stack!"
            continue