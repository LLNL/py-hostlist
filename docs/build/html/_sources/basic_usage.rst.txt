===========
Basic Usage
===========

You can use the command line to process your hostlist strings by using the following command:

``python cla_hostlist.py <method> <args>...``

Here is a list of all of the methods available:

``-h, --help``                   
 Display this message.
``-q, --quiet``
 Quiet output (exit non-zero if empty hostlist)
``-d, --delimiters``
 Set output delimiter (default = ",")
``-c, --count``
 Print the number of hosts
``-s, --size``
 Output at most N hosts (-N for last N hosts)
``-e, --expand``                 
 Expand a compressed hostlist
``-a, --abbreviate``            
 Compress an expanded hostlist
``-t, --tighten``                
 Return a hostlist string
``-m, --minus``                  
 Subtract all HOSTLIST args from first HOSTLIST
``-i, --intersection``           
 Intersection of all HOSTLIST args
``-x, --exclude``
 Exclude all HOSTLIST args from first HOSTLIST
``-X, --xor``
 Symmetric difference of all HOSTLIST args
``-u, --union``                  
 Union of all HOSTLIST arguments
``-n, --nth``                  
 Output the host at index N
``-R, --remove``
 Remove all occurences of NODE from HOSTLIST
``-S, --sort``                   
 Return sorted HOSTLIST 
``-F, --find``              
 Output position of HOST in result HOSTLIST

For example, to execute the expand function displayed above, users can run the following:

``python cla_hostlist.py -e node[1-4]``

This will return ``node1,node2,node3,node4``.