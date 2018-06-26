import argparse
import sys
import hostlist as hl 

"""
Command-line arguments for hostlist.py 

Author: Christopher Moussa (moussa1@llnl.gov)
Mentor: Elsa Gonsiorowski (gonsiorowski1@llnl.gov)
Date: June 26, 2018
"""


parser = argparse.ArgumentParser()

parser.add_argument("-e", "--expand", dest="expand", help="Expand a compressed hostlist")

parser.add_argument("-a", "--abbreviate", dest="compress_range", help="Compress an expanded hostlist")

parser.add_argument("-t", "--tighten", dest="compress", help="Return a hostlist string")

parser.add_argument("-m", "--minus", dest="diff", nargs="*", help="Subtract all HOSTLIST args from first HOSTLIST")

parser.add_argument("-i", "--intersection", dest="intersection", nargs="*", help="Intersection of all HOSTLIST args")

parser.add_argument("-u", "--union", dest="union", nargs="*", help="Union of all HOSTLIST arguments")

parser.add_argument("-n", "--nth=N", dest="nth", nargs="*", help="Output the host at index N")

parser.add_argument("-s", "--sort", dest="sort", help="Return sorted HOSTLIST")

parser.add_argument("-c", "--count", dest="count", help="Print the number of hosts")

parser.add_argument("-f", "--find", dest="find", nargs="*", help="Output position of HOST in result HOSTLIST")

args = parser.parse_args()

if args.expand:
	hl.expand(args.expand)
if args.compress_range:
	hl.compress_range(args.compress_range)
if args.compress:
	hl.compress(args.compress)
if args.diff:
	hl.diff(args.diff[0], args.diff[1])
if args.intersection:
	hl.intersect(args.intersection[0], args.intersection[1])
if args.union:
	hl.union_nodes(args.union[0], args.union[1])
if args.nth:
	hl.nth(args.nth[0], args.nth[1])
if args.sort:
	hl.sort_nodes(args.sort)
if args.count:
	hl.count(args.count)
if args.find:
	hl.find(args.find[0], args.find[1])