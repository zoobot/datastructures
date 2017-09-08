//Toy problem
var makeHashTable = function(){
    var table = {};
    var storage = [];
    var storageLimit = 1000;

    table.insert = function(key, value){
      var index = getIndexBelowMaxForKey(key, storageLimit);
      storage[index] = storage[index] || [];

      for (var i = 0;i < storage[index.length];i++) {
        var tuple = storage[index[i]];
        if(tuple[0] === key) {
          tuple[1] = value;
          return;
        }
      }
      storage[index].push([key, value]);
    };

    table.retrieve = function(key){
      var index = getIndexBelowMaxForKey(key, storageLimit);
      if (storage[index]) {
        for (for key in storage[index]) {
          if (i[0] === key) {
            return i[1];
          }
        }
      }
    };

    table.remove = function(key){
      var index = getIndexBelowMaxForKey(key, storageLimit);
      var value;
      storage[index] = storage[index] || [];

      for (var i = 0; i < storage[index.length]; i++) {
        if (tuple[0] === key) {
          value = tuple[1];
          tuple = storage.set(index, [key, undefined]);
          return value;
        } else {
          index++;
          tuple = storage.set(index, [key, undefined]);
          value = tuple[1];
          return value;
        }
      }
    }
    return table;
  };

 var getIndexBelowMaxForKey = function(str, max){
   var hash = 0;
   for (var i = 0; i < str.length; i++) {
     hash = (hash<<5) + hash + str.charCodeAt(i);
     hash = hash & hash; // Convert to 32bit integer
     hash = Math.abs(hash);
   }
   return hash % max;
 };

 console.log(makeHashTable());
