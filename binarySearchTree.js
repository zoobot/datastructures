var BinarySearchTree = value => {
  //prototypal datastructure
  // generate object
  var bTree = Object.create(bTreeMethods)
  // assign properties
  bTree.value = value
  bTree.left = null
  bTree.right = null
  //return object
  return bTree
}

var bTreeMethods = {}

bTreeMethods.prototype.insert = val => {
  var node = BinarySearchTree(val)
  function bTree(root) {
    if (node.value < root.value) {
      if (root.left === null) {
        root.left = node
      } else {
        bTree(root.left)
      }
    } else if (node.value > root.value) {
      if (root.right === null) {
        root.right = node
      } else {
        bTree(root.right)
      }

    }
  }
  bTree(this)
}

bTreeMethods.prototype.contains = target => {
  var setBool = false
  function bTree
}