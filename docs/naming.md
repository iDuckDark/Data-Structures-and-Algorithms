# Variable Naming Ideas

n_nodes
node_count
size
length

total: cumulative sums
val: element in a contiguous collection
node: element in a graph

length: contiguous elements - e.g. string, array
capacity: refer to allocated space in collection and not number of valid elements in it
size = available slots, count = actual elements. size == count when the collection is full
While Length and Size are nouns, Count is also a verb, thus it could be interpreted as counting at runtime (O(n)) vs lookup a value (O(1))
https://stackoverflow.com/questions/300522/count-vs-length-vs-size-in-a-collection
