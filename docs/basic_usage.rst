===========
Basic Usage
===========

You can use the command line to process your hostlist strings by using the following command:

`python cla_hostlist.py <method> <args>...`

Here is a list of all of the methods available:

 -h, --help                   Display this message.
 -e, --expand                 Expand a compressed hostlist
 -a, --abbreviate             Compress an expanded hostlist
 -t, --tighten                Return a hostlist string
 -m, --minus                  Subtract second HOSTLIST arg from first HOSTLIST
 -i, --intersection           Intersection of all HOSTLIST args
 -u, --union                  Union of all HOSTLIST arguments
 -n, --nth=N                  Output the host at index N
 -S, --sort                   Return sorted HOSTLIST 
 -c, --count                  Print the number of hosts
 -F, --find=HOST              Output position of HOST in result HOSTLIST