// A binary heap is a heap data structure that takes the form of a binary tree. Binary heaps are a common way of implementing priority queues. The binary heap was introduced by J. W. J. Williams in 1964, as a data structure for the heapsort.

BinaryHeap.prototype.insert = function(node) {
  this._heap.push(node);
  var index = this._heap.length - 1;
  var parentIndex = Math.floor((index - 1) / 2);
  while (index > 0 && this._compare(this._heap[index], this._heap[parentIndex])) {
    swapNodesAt(index, parentIndex, this);
    index = parentIndex;
    parentIndex = Math.floor((index - 1) /2);
  }
}

BinaryHeap.prototype.removeRoot = function() {
  swapNodesAt(this._heap.length - 1, 0, this);
  var originalRoot = this._heap.pop();
  var temporaryRootIndex = 0;
  var lesserChildIndex = getLesserChildIndex(temporaryRootIndex, this);

  while (lesserChildIndex && this._compare(this._heap[lesserChildIndex], this._heap[temporaryRootIndex])) {
    swapNodesAt(lesserChildIndex, temporaryRootIndex, this);
    temporaryRootIndex = lesserChildIndex;
    lesserChildIndex = getLesserChildIndex(temporaryRootIndex, this);
  }
  return originalRoot;
}

function swapNodesAt(index, parentIndex, BinaryHeap) {
  var heap = BinaryHeap._heap;
  var temp = heap[index];
  heap[index] = heap[parentIndex];
  heap[parentIndex] = temp;
}

function getLesserChildIndex (parentIndex, BinaryHeap) {
  var childIndices = [parentIndex * 2 + 1, parentIndex * 2 + 2]. filter(function(index) {
    return index < binaryHeap._heap.length;
  });

  if (BinaryHeap._compare(binaryHeap._heap[childIndices[1]], binaryHeap._heap[childIndices[0]])) {
    return childIndices[1];
  } else {
    return childIndices[0];
  }
}