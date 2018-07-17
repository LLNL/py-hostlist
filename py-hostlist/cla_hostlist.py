import argparse
import sys
import hostlist as hl 

"""
Command-line arguments for hostlist.py 

Author: Christopher Moussa (moussa1@llnl.gov)
Mentor: Elsa Gonsiorowski (gonsiorowski1@llnl.gov)
Date: June 26, 2018
"""


def msg(name=None):
	return '''
	Description: cla_hostlist processes slurm-style hostlist strings and 
	can return those strings in manipulated fashion. 
	
	Usage: python cla_hostlist.py [OPTION]... [HOSTLIST]...

  	-h, --help                   Display this message.
  	-e, --expand                 Expand a compressed hostlist
  	-a, --abbreviate             Compress an expanded hostlist
  	-t, --tighten                Return a hostlist string
  	-m, --minus                  Subtract second HOSTLIST arg from first HOSTLIST
  	-i, --intersection           Intersection of all HOSTLIST args
  	-u, --union                  Union of all HOSTLIST arguments
  	-n, --nth=N                  Output the host at index N
  	-R, --remove                 Remove all occurences of NODE from HOSTLIST
   	-S, --sort                   Return sorted HOSTLIST 
  	-c, --count                  Print the number of hosts
  	-F, --find=HOST              Output position of HOST in result HOSTLIST
		'''

parser = argparse.ArgumentParser(usage=msg())

parser.add_argument("-e", "--expand", dest="expand")

parser.add_argument("-a", "--abbreviate", dest="compress_range")

parser.add_argument("-t", "--tighten", dest="compress")

parser.add_argument("-m", "--minus", dest="diff", nargs="*")

parser.add_argument("-i", "--intersection", dest="intersection", nargs="*")

parser.add_argument("-u", "--union", dest="union", nargs="*")

parser.add_argument("-n", "--nth=N", dest="nth", nargs="*")

parser.add_argument("-R", "--remove", dest="remove_node", nargs="*")

parser.add_argument("-S", "--sort", dest="sort")

parser.add_argument("-c", "--count", dest="count")

parser.add_argument("-F", "--find", dest="find", nargs="*")

args = parser.parse_args()

if args.expand:
	print hl.expand(args.expand)
if args.compress_range:
	print hl.compress_range(args.compress_range)
if args.compress:
	print hl.compress(args.compress)
if args.diff:
	print hl.diff(*args.diff)
if args.intersection:
	print hl.intersect(*args.intersection)
if args.union:
	print hl.union_nodes(*args.union)
if args.nth:
	print hl.nth(args.nth[0], args.nth[1])
if args.remove_node:
	print hl.remove_node(args.remove_node[1], args.remove_node[0])
if args.sort:
	print hl.sort_nodes(args.sort)
if args.count:
	print hl.count(args.count)
if args.find:
	print hl.find(args.find[0], args.find[1])