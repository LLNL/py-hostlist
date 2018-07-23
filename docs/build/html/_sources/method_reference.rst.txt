================
Method Reference
================

This is a high-level overview of the methods that make up py-hostlist.

-------
Methods
-------

``expand(nodelist)``
 **Parameters**: 
  nodelist **(str)** - The hostlist string.

 **Returns**: An expanded hostlist string.  

 **Description**: expand takes in a hostlist string and returns a list of individual hostnames. For example, the input string ``node[1-4]`` will return ``node1,node2,node3,node4``. The expand method will return the suffix string in its final expansion, as well as prepend any leading zeros found in the input string. Multiple ranges can be specified within brackets of a cluster like so:

 ``node[1-4,6-10,19].suffix.com``

 Multiple clusters to be expanded can also be specified in an input string by separating the clusters with a comma followed by a space. An example below:

 ``node1-[1-4], node2-[5-9].suffix.com``

``compress_range(nodelist)``
 **Parameters**: 
  nodelist **(str)** or **(list)** - The expanded hostlist string.

 **Returns**: A compressed hostlist string.

 **Description**: compress_range takes in a hostlist list string and returns an ordered hostlist with a range. For example, the input list ``['node1','node2','node3','node4']`` will return ``node[1-4]``. The compress_range method can also recognize multiple ranges. 

 compress_range can also recognize a string input. Going back to the example above, the following input will also be recognized: ``'node1,node2,node3,node4'``. This will also return ``node[1-4]``.

``compress(nodelist)``
 **Parameters**: 
  nodelist **(str)** - The hostlist string.

 **Returns**: An ordered hostlist string.

 **Description**: compress takes in a hostlist list string and returns an ordered hotlist string. For example, the input string ``['node1','node2','node3','node4']`` will return ``[node1,node2,node3,node4]``.

``diff(nodelist1, nodelist2)``
 **Parameters**: 
  nodelist1 **(str)** or **(list)** - The hostlist string to be subtracted from. 

  following nodelists... **(str)** or **(list)**: The other hostlist strings.

 **Returns**: A remaining hostlist string resulting from subtracting the following nodelists from nodelist1.

 **Description**: diff will subtract elements in all following nodelists from nodelist1 and return a remaining hostlist. It accepts both string and list inputs.

``intersect(*arg)``
 **Parameters**: 
  hostlist strings **(str)** or **(list)** - Any number of nodelists to be intersected.

 **Returns**: An intersecting hostlist string from all hostlist args.

 **Description**: intersect will return a list of intersection nodes given n lists of nodes. It will sort the nodes in ascending order upon returning. 

``union_nodes(*arg)``
 **Parameters**: 
  hostlist strings **(str)** or **(list)** - Any number of nodelists to be combined.

 **Returns**: A union hostlist string from all hostlist args.

 **Description**: union will return the union between n lists of nodes. It will sort the nodes in ascending order upon returning. 
 
``nth(nodelist, n)``
 **Parameters**: 
  nodelist **(str)** or **(list)** - The hostlist string.

  n **(int)** - The index to search.

 **Returns**: The host at the specified index.
 
 **Description**: nth takes in two parameters: a hostlist string (similar to expand()'s parameter) and an index *n*. It will return the *nth* node in that range. 

``find(nodelist, node)``
 **Parameters**:
  nodelist **(str)** or **(list)** - The hostlist string. 

  node **(str)** - The host to be searched inside of the hostlist string.

 **Returns**: The position of the host within the hostlist string.

 **Description**: find will return the position of the node in the input nodelist. 

``count(nodelist)``
 **Parameters**:
  nodelist **(str)** or **(list)** - The hostlist string.

 **Returns**: The number of nodes in the hostlist string.

 **Description**: count will print the number of hosts in the nodelist. The input can accept a hostlist that is already expanded or one that contains ranges. For example, the input ``node[1-5]`` will return ``5``. 

``remove_node(nodelist, node)``
 **Parameters**:
  nodelist **(str)** or **(list)** - The hostlist string.

  node **(str)** - The node to be removed.

 **Returns**: The resulting hostlist upon deletion.

 **Description**: remove_node() will remove all occurences of *node* in the nodelist. The input can accept a hostlist that is already expanded or one that contains ranges.

``delimiter(nodelist, d)``
 **Parameters**:
  nodelist **(str)** or **(list)** - The hostlist string.

  d **(str)** - The custom delimiter.

 **Returns**: The resulting hostlist string with its custom delimiter.

 **Description**: delimiter() will take the hostlist string and output it with the specified delimiter *d*, which can be any string.

``size_hostlist(nodelist, N)``
 **Parameters**:
  nodelist **(str)** or **(list)** - The hostlist string.

  N **(int)** - The number of hosts to print.

 **Returns**: The resulting hostlist string with custom size.

 **Description**: This method will print at most *N* hosts from the hostlist input. If a negative *N* is passed in, the output will consist of the last N hosts from the hostlist input.

``xor(*arg)``
 **Parameters**:
  hostlist strings **(str)** or **(list)** - Any number of nodelists to be combined.

 **Returns**: The resulting xor list.

 **Description**: xor() takes the symmetric difference of an arbitrary number of hostlists passed in.

``exclude(*arg)``
 **Parameters**:
  nodelist **(str)** or **(list)** - The hostlist string.

  node **(str)** - The node to be excluded.

 **Returns**: The resulting hostlist string without the nodes specified.

 **Description**: exclude() will return a hostlist that excludes any nodes specified after the first argument, which is the original hostlist. Each node to be excluded must be passed in one at a time as separate arguments.

``quiet(nodelist=[])``
 **Parameters**:
  nodelist **(str)** or **(list)** - The hostlist string.

 **Returns**: None or non-zero output if an empty hostlist is passed in.

 **Description**: returns quiet output for a hostlist input. It will exit non-zero if there is an empty hostlist passed in.



--------------
Helper Methods
--------------

``append_hostname(machine_name, num_list)``
 **Parameters**: 
  machine_name **(str)** - The name of the cluster.

  num_list **(list)** - The list of nodes to be appended to the cluster name.

 **Returns**: A hostlist string with the hostname and node numbers.  

 **Description**: append_hostname takes in two parameters: the name of the machine and its range of nodes; it is a helper method that will append the machine name (the host) to the node numbers it contains.

``sort_nodes(nodelist)``
 **Parameters**:
  nodelist **(str)** - The hostlist string.

 **Returns**: The hostlist string in ascending order.

 **Description**: sort_nodes takes in a list of nodes; it is a helper method that will return a sorted string of those nodes in ascending order.