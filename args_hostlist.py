import argparse
import hostlist as hl

def expand(args):
	param1 = args.param1
	hl.expand(param1)

def compress_range(args):
	param1 = args.param1
	hl.compress_range(param1)

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

expand_parser = subparsers.add_parser('expand')
expand_parser.add_argument('param1')
expand_parser.set_defaults(func=expand)

compress_range_parser = subparsers.add_parser('compr')
compress_range_parser.add_argument('param1')
compress_range_parser.set_defaults(func=compress_range)

args = parser.parse_args()
args.func(args)