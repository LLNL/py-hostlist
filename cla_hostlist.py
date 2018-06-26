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

parser.add_argument("-e", "--expand", dest="expand", help="Expand a compressed hostlist",
	action="store")

parser.add_argument("-a", "--abbreviate", dest="compress_range", help="Compress an expanded hostlist",
	action="store")

parser.add_argument("-t", "--tighten", dest="compress", help="Return a hostlist string",
	action="store")

parser.add_argument("-m", "--minus", dest="diff", nargs="2", help="Subtract all HOSTLIST args from first HOSTLIST",
	action="store")

parser.add_argument("-i", "--intersection", dest="intersection", nargs="*", help="Intersection of all HOSTLIST args",
	action="store")

parser.add_argument("-u", "--union", dest="union", nargs="*", help="Union of all HOSTLIST arguments",
	action="store")

parser.add_argument("-n", "--nth=N", dest="nth", nargs="*", help="Output the host at index N",
	action="store")

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