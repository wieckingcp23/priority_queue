# priorityq.py
#
# Created by: R. Necaise
# Modified by: Peyton Wiecking
# Date: 3/28/19
# CSCI 112 02
#
# Implementation of the unbounded priority queue using an unsorted
# singly linked list.
#

# creates a priority queue type data structure
class PriorityQueue :
  # creates a priority queue
  def __init__(self) :
    self._head = None
    self._tail = None
    self._numItems = 0
   
  # returns the length of the queue 
  def __len__(self) :
    return self._numItems
  
  # returns a boolean to deterimine if the queue is empty or not 
  def isEmpty(self) :
    return self._head is None
  
  # adds an item and its priority to the queue  
  def enqueue(self, item, priority) :
    # create the queue entry
    newNode = PriorityQueueNode(item, priority)
    # establishes the first entry as the head
    if self._head is None:
      self._head = newNode
    # adds the rest of the entries onto the queue and establishes a
    # new tail node
    else:
      self._tail.next = newNode
    self._tail = newNode
    # add the new queue entry to the count
    self._numItems = self._numItems + 1
   
  # removes the element in the list that has the highest priority with 
  # 1 being the highest priority number
  def dequeue(self) :
    assert self._numItems > 0, "Can not remove an element from an empty queue"
    # set up a a way to reference elements in the queue
    predNode = None
    curNode = self._head
    highPred = None
    highest = self._head
    # loop through the queue
    while curNode is not None:
      # determines which priority is the highest priority
      if curNode.priority < highest.priority:
        highest = curNode
        highPred = predNode  
      predNode = curNode
      curNode = curNode.next
    # case for if the head node is the highest priority
    if highest is self._head:
      self._head = highest.next
    # case for everything else
    else:
        highPred.next = highest.next
    # remove the dequeued element from the count     
    self._numItems = self._numItems - 1
    # returns the highest priority and removes it from the queue
    return highest.item 
    
  # allows the user to "peek" 
  def peek(self) :
    assert self._numItems > 0, "Can not peek at an empty queue."
    return self._head.item
    
# given helper: creates what is needed to create a Priority Queue Node    
class PriorityQueueNode :
  def __init__(self, item, priority) :
    self.item = item
    self.priority = priority
    self.next = None