# Code: Max Priority Queue
# Send Feedback
# Implement the class for Max Priority Queue which includes following functions -
# 1. getSize -
# Return the size of priority queue i.e. number of elements present in the priority queue.
# 2. isEmpty -
# Check if priority queue is empty or not. Return true or false accordingly.
# 3. insert -
# Given an element, insert that element in the priority queue at the correct position.
# 4. getMax -
# Return the maximum element present in the priority queue without deleting. Return - Infinity if priority queue is empty.
# 5. removeMax -
# Delete and return the maximum element present in the priority queue. Return - Infinity if priority queue is empty.
# Note: main function is given for your reference which we are using internally to test the class.
class PriorityQueuenode:
    def __init__(self, ele, priority):
        self.ele = ele
        self.priority = priority


class PriorityQueue:

    def __init__(self):
        self.pq = []

    def isEmpty(self):
        #Implement the isEmpty() function here
        return self.getSize() == 0

    def getSize(self):
        #Implement the getSize() function here
        return len(self.pq)

    def getMax(self):
        #Implement the getMax() function here
        if self.isEmpty() is True:
            return float('inf')

        return self.pq[0].ele

    def __percolateup(self):
        childindex = self.getSize()-1
        while childindex > 0:
            parentindex = (childindex-1)//2
            if self.pq[childindex].priority > self.pq[parentindex].priority:
                self.pq[childindex], self.pq[parentindex] = self.pq[parentindex], self.pq[childindex]
                childindex = parentindex
            else:
                break

    def insert(self, ele, priority):
        #Implement the insert() function here
        pqnode = PriorityQueuenode(ele, priority)
        self.pq.append(pqnode)
        self.__percolateup()

    def __percolatedown(self):
        parentIndex = 0
        leftchildIndex = 2*parentIndex+1
        rightchildIndex = 2*parentIndex+2
        while leftchildIndex < self.getSize():
            maxindex = parentIndex

            if self.pq[maxindex].priority < self.pq[leftchildIndex].priority:
                maxindex = leftchildIndex

            if rightchildIndex < self.getSize() and self.pq[maxindex].priority < self.pq[rightchildIndex].priority:
                maxindex = rightchildIndex

            if maxindex == parentIndex:
                break
            self.pq[parentIndex], self.pq[maxindex] = self.pq[maxindex], self.pq[parentIndex]
            parentindex = maxindex
            leftchildIndex = 2*(parentIndex)+1
            rightchildIndex = 2*(parentIndex)+2

    def removeMax(self):
        #Implement the removeMax() function here
        if self.isEmpty():
            return None
        element = self.pq[0].ele
        self.pq[0] = self.pq[self.getSize()-1]
        self.pq.pop()
        self.__percolatedown()
        return element


myPq = PriorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i = 1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i += 1
        myPq.insert(element, element)
    elif choice == 2:
        print(myPq.getMax())
    elif choice == 3:
        print(myPq.removeMax())
    elif choice == 4:
        print(myPq.getSize())
    elif choice == 5:
        if myPq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i += 1
