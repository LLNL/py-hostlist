import argparse
import hostlist as hl

def expand(args):
	param1 = args.param1
	hl.expand(param1)

def compress_range(args):
	param1 = args.param1
	hl.compress_range(param1)

def compress(args):
	param1 = args.param1
	hl.compress(param1)

def diff(args):
	param1 = args.param1
	param2 = args.param2
	hl.diff(param1, param2)

def inter(args):
	param1 = args.param1
	param2 = args.param2
	hl.intersect(param1, param2)

def union(args):
	param1 = args.param1
	param2 = args.param2
	hl.union_nodes(param1, param2)

def nth(args):
	param1 = args.param1
	param2 = args.param2
	hl.nth(param1, param2)

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

expand_parser = subparsers.add_parser('expand')
expand_parser.add_argument('param1')
expand_parser.set_defaults(func=expand)

compress_range_parser = subparsers.add_parser('compr')
compress_range_parser.add_argument('param1')
compress_range_parser.set_defaults(func=compress_range)

compress_parser = subparsers.add_parser('comp')
compress_parser.add_argument('param1')
compress_parser.set_defaults(func=compress)

diff_parser = subparsers.add_parser('diff')
diff_parser.add_argument('param1')
diff_parser.add_argument('param2')
diff_parser.set_defaults(func=diff)

inter_parser = subparsers.add_parser('inter')
inter_parser.add_argument('param1')
inter_parser.add_argument('param2')
inter_parser.set_defaults(func=inter)

union_parser = subparsers.add_parser('union')
union_parser.add_argument('param1')
union_parser.add_argument('param2')
union_parser.set_defaults(func=union)

nth_parser = subparsers.add_parser('nth')
nth_parser.add_argument('param1')
nth_parser.add_argument('param2')
nth_parser.set_defaults(func=nth)


args = parser.parse_args()
args.func(args)