import unittest
import hostlist as hl

"""
These are unit tests for hostlist.py. They go through each function
and test its correctness.

Author: Christopher Moussa (moussa1@llnl.gov)
Mentor: Elsa Gonsiorowski (gonsiorowski1@llnl.gov)
Date: June 21, 2018
"""


class TestHostlistMethods(unittest.TestCase):

	# expand() returns correctly when input
	# is just one range of nodes
	def test_expand(self):
		expected = 'quartz4,quartz5,quartz6,quartz7,quartz8'
		test = hl.expand('quartz[4-8]')
		self.assertEqual(test, expected)

	# expand() will also return correctly with
	# multiple sets of ranges
	def test_expand_multi_range(self):
		expected = \
			'node1,node2,node3,node4,node5,node6,node7,node8,' \
			'node9,node10,node11,node12,node13,node14,node15,' \
			'node16,node18,node19,node21,node22'
		test = hl.expand('node[18-19,1-16,21-22]')
		self.assertEqual(test, expected)

	# expand() can also recognize a mix of
	# 	individual and ranges of nodes
	def test_expand_mixed_range(self):
		expected = \
			'node4,node5,node6,node7,node8,node12,node16,node17,' \
			'node18,node19,node20,node22,node24,node25,node26'
		test = hl.expand('node[4-8,12,16-20,22,24-26]')
		self.assertEqual(test, expected)

	# expand() can attach suffixes as well as
	# 	recognize hostnames with numbers and dashes
	def test_expand_prefix_and_suffix(self):
		expected = 'machine2-02vm1,machine2-03vm1,machine2-04vm1'
		test = hl.expand('machine2-[02-4]vm1')
		self.assertEqual(test, expected)

	# expand() can take in comma separated values for different machines
	def test_expand_scr(self):
		expected = \
			'machine2-02vm1,machine2-03vm1,' \
			'machine4-0003.vml2,machine4-0004.vml2,machine4-0005.vml2'
		test = hl.expand("machine2-[02-3]vm1, machine4-[0003-5].vml2")
		self.assertEqual(test, expected)

	# expand() prepends leading zeros if it is in the original input
	def test_expand_leading_zeros(self):
		expected = 'machine2-009vm1,machine2-010vm1,machine2-011vm1'
		test = hl.expand('machine2-[009-11]vm1')
		self.assertEqual(test, expected)

	def test_expand_only_commas(self):
		expected = 'node1,node2,node3'
		test = hl.expand('node[1,2,3]')
		self.assertEqual(test, expected)

	# compress_range() can compress a single range of nodes
	def test_compress_range_simple(self):
		expected = 'node[1-4]'
		test = hl.compress_range(['node1', 'node2', 'node3', 'node4'])
		self.assertEqual(test, expected)

	# compress_range() can take in a string as well
	def test_compress_range_as_string(self):
		expected = 'node[1-4]'
		test = hl.compress_range('node1,node2,node3,node4')
		self.assertEqual(test, expected)

	# compress_range() can compress a mix of ranges
	# and individual nodes
	def test_compress_range_mixed(self):
		expected = 'node[1-5,7-8,10-12]'
		test = hl.compress_range(
			['node1', 'node2', 'node3', 'node4', 'node5',
				'node7', 'node8', 'node10', 'node11', 'node12'])
		self.assertEqual(test, expected)

	# compress_range() will keep the suffix in its result
	def test_compress_range_suffix(self):
		expected = 'node[1-3].suffix.com'
		test = hl.compress_range('node1.suffix.com,node2.suffix.com,node3.suffix.com')
		self.assertEqual(test, expected)

	# compress_range() can recognize machines with hyphens before node numbers
	def test_compress_range_with_hyphen(self):
		expected = 'node1-[1-3].suffix.com'
		test = hl.compress_range('node1-1.suffix.com,node1-2.suffix.com,node1-3.suffix.com')
		self.assertEqual(test, expected)

	# compress() will return an ordered hostlist string
	def test_compress(self):
		expected = '[node1,node2,node3,node4,node5,node7,node8,node10,node11,node12]'
		test = hl.compress(
			['node1', 'node2', 'node3', 'node4', 'node5', 'node7',
				'node8', 'node10', 'node11', 'node12'])
		self.assertEqual(test, expected)

	# compress() can take in a string as well
	def test_compress_as_string(self):
		expected = '[node1,node2,node3,node4]'
		test = hl.compress('node1,node2,node3,node4')
		self.assertEqual(test, expected)

	# diff() will subtract nodelist2 from nodelist1 and return a
	# 	hostlist string of the remainder
	def test_diff(self):
		expected = 'node[1,10]'
		list1 = \
			['node1', 'node2', 'node3', 'node4', 'node5', 'node6', 'node7',
				'node8', 'node9', 'node10']
		list2 = ['node2', 'node3', 'node4', 'node5', 'node6', 'node7', 'node8', 'node9']
		test = hl.diff(list1, list2)
		self.assertEqual(test, expected)

	# diff() can take in a string as well
	def test_diff_as_string(self):
		expected = 'node[1,10]'
		list1 = 'node1,node2,node3,node4,node5,node6,node7,node8,node9,node10'
		list2 = 'node2,node3,node4,node5,node6,node7,node8,node9'
		test = hl.diff(list1, list2)
		self.assertEqual(test, expected)

	# unit test taken fom scr
	def test_diff_scr(self):
		expected = 'machine[2-3]'
		list1 = 'machine1,machine2,machine3'
		list2 = 'machine1,machine4'
		test = hl.diff(list1, list2)
		self.assertEqual(test, expected)

	def test_diff_multiple(self):
		expected = 'node[1,10]'
		list1 = 'node1,node2,node3,node4,node5,node6,node7,node8,node9,node10'
		list2 = 'node2,node3'
		list3 = 'node4,node5'
		list4 = 'node6,node7,node8,node9'
		test = hl.diff(list1, list2, list3, list4)
		self.assertEqual(test, expected)

	def test_diff_with_expand(self):
		expected = 'node[1,4]'
		list1 = 'node[1-4]'
		list2 = 'node[2-3]'
		test = hl.diff(list1, list2)
		self.assertEqual(test, expected)

	# intersect() can return a hostlist string of
	# 	intersecting nodes from two lists
	def test_intersect_simple(self):
		expected = 'node[1,8]'
		list1 = ['node1', 'node2', 'node3', 'node4', 'node8']
		list2 = ['node5', 'node6', 'node7', 'node8', 'node9', 'node1']
		test = hl.intersect(list1, list2)
		self.assertEqual(test, expected)

	def test_intersect_scr(self):
		expected = 'machine[1,3]'
		list1 = 'machine1,machine2,machine3'
		list2 = 'machine1,machine3,machine4'
		test = hl.intersect(list1, list2)
		self.assertEqual(test, expected)

	# intersect() can also return a hostlist string of
	# intersecting nodes from multiple lists
	def test_intersect_multiple(self):
		expected = 'node[1,6,8]'
		list1 = ['node1', 'node2', 'node3', 'node4', 'node8', 'node6']
		list2 = ['node5', 'node6', 'node7', 'node8', 'node9', 'node1']
		list3 = ['node1', 'node6', 'node8', 'node7']
		test = hl.intersect(list1, list2, list3)
		self.assertEqual(test, expected)

	# intersect() can take in a string as well
	def test_instersect_as_string(self):
		expected = 'node[1,8]'
		list1 = 'node1,node2,node3,node4,node8'
		list2 = 'node5,node6,node7,node8,node9,node1'
		test = hl.intersect(list1, list2)
		self.assertEqual(test, expected)

	def test_intersect_with_expand(self):
		expected = 'node[1,8]'
		list1 = 'node[1-4,8]'
		list2 = 'node[1,5-9]'
		test = hl.intersect(list1, list2)
		self.assertEqual(test, expected)

	# union() will return an ordered hostslist of the
	# union of two lists
	def test_union_simple(self):
		expected = 'node[1-12]'
		list1 = \
			['node1', 'node2', 'node3', 'node4', 'node5', 'node7', 'node8',
				'node10', 'node11', 'node12']
		list2 = ['node5', 'node6', 'node7', 'node8', 'node9', 'node1']
		test = hl.union_nodes(list1, list2)
		self.assertEqual(test, expected)

	# union() can also return an ordered hostlist of
	# multiple lists
	def test_union_multiple(self):
		expected = 'node[1-6]'
		list1 = ['node1', 'node2']
		list2 = ['node3', 'node4']
		list3 = ['node6']
		list4 = ['node5']
		test = hl.union_nodes(list1, list2, list3, list4)
		self.assertEqual(test, expected)

	# union() can take in a string as well
	def test_union_as_string(self):
		expected = 'node[1-6]'
		list1 = ['node1', 'node2']
		list2 = 'node3,node4'
		list3 = ['node6']
		list4 = 'node5'
		test = hl.union_nodes(list1, list2, list3, list4)
		self.assertEqual(test, expected)

	def test_union_with_expand(self):
		expected = 'node[1-6]'
		list1 = 'node[1-2]'
		list2 = 'node[3-4]'
		list3 = 'node6'
		list4 = 'node5'
		test = hl.union_nodes(list1, list2, list3, list4)
		self.assertEqual(test, expected)

	# sort_nodes() will return an ordered hostlist
	# of a list of nodes
	def test_sort(self):
		expected = 'node3,node4,node5,node7,node11,node16'
		test = hl.sort_nodes(['node5', 'node4', 'node7', 'node16', 'node11', 'node3'])
		self.assertEqual(test, expected)

	# sort_nodes() can take in a string as well
	def test_sort_as_string(self):
		expected = 'node3,node4,node5,node7,node11,node16'
		test = hl.sort_nodes('[node5,node4,node7,node16,node11,node3]')
		self.assertEqual(test, expected)

	# makes sure that count() returns the correct value
	def test_count(self):
		expected = 5
		test = hl.count('node1,node2,node3,node4,node5')
		self.assertEqual(test, expected)

	def test_count_with_expand(self):
		expected = 5
		test = hl.count('node[1-5]')
		self.assertEqual(test, expected)

	def test_count_as_list(self):
		expected = 5
		test = hl.count(['node1', 'node2', 'node3', 'node4', 'node5'])
		self.assertEqual(test, expected)

	def test_count_multi_ranges(self):
		expected = 10
		test = hl.count('node[1-5,6-10]')
		self.assertEqual(test, expected)

	# nth should return the nth node in a host list
	def test_nth(self):
		expected = 'quartz7'
		test = hl.nth('quartz[4-8]', 4)
		self.assertEqual(test, expected)

	def test_nth_as_str(self):
		expected = 'node2'
		test = hl.nth('node1,node2,node3,node4', 2)
		self.assertEqual(test, expected)

	def test_nth_as_list(self):
		expected = 'node2'
		test = hl.nth(['node1', 'node2', 'node3', 'node4'], 2)
		self.assertEqual(test, expected)

	# nth should just return a simple error message saying that
	# 	the index doesn't exist if it gets a bad index
	def test_nth_doesnt_exist(self):
		expected = 'node does not exist'
		test = hl.nth('quartz[4-8]', 0)
		self.assertEqual(test, expected)

	# find should return the index that the host is at
	def test_find(self):
		expected = 'At position 2'
		test = hl.find('node[1-3]', 'node2')
		self.assertEqual(test, expected)

	# if find cannot find the host, then return a failure
	def test_find_doesnt_exist(self):
		expected = "node does not exist"
		test = hl.find('node[1-3]', 'node0')
		self.assertEqual(test, expected)

	def test_find_as_list(self):
		expected = 'At position 2'
		test = hl.find(['node1', 'node2', 'node3', 'node4'], 'node2')
		self.assertEqual(test, expected)

	def test_find_as_string(self):
		expected = 'At position 2'
		test = hl.find('node1,node2,node3,node4', 'node2')
		self.assertEqual(test, expected)

	def test_remove_node_as_list(self):
		expected = 'node1,node2'
		test = hl.remove_node(['node1', 'node2', 'node3'], 'node3')
		self.assertEqual(test, expected)

	def test_remove_node(self):
		expected = 'node1,node2'
		test = hl.remove_node('node1,node2,node3', 'node3')
		self.assertEqual(test, expected)

	def test_remove_node_with_expand(self):
		expected = 'node1,node2,node3,node4,node6,node7,node8,node9'
		test = hl.remove_node('node[1-5,5-9]', 'node5')
		self.assertEqual(test, expected)

	def test_delimiter_as_list(self):
		expected = 'foo1-foo2-foo3'
		test = hl.delimiter(['foo1', 'foo2', 'foo3'], '-')
		self.assertEqual(test, expected)

	def test_delimiter_with_expand(self):
		expected = 'foo1*foo2*foo3'
		test = hl.delimiter('foo[1-3]', '*')
		self.assertEqual(test, expected)

	def test_delimiter_as_string(self):
		expected = 'foo1-foo2-foo3'
		test = hl.delimiter('foo1,foo2,foo3', '-')
		self.assertEqual(test, expected)

	def test_size_as_list(self):
		expected = 'node[1-3]'
		test = hl.size_hostlist(
			['node1', 'node2', 'node3', 'node4', 'node5', 'node6'], 3)
		self.assertEqual(test, expected)

	def test_size_backwards(self):
		expected = 'node[4-6]'
		test = hl.size_hostlist(
			['node1', 'node2', 'node3', 'node4', 'node5', 'node6'], -3)
		self.assertEqual(test, expected)

	def test_size_with_expand(self):
		expected = 'node[1-5]'
		test = hl.size_hostlist('node[1-10]', 5)
		self.assertEqual(test, expected)

	def test_size_with_expand_backwards(self):
		expected = 'node[6-10]'
		test = hl.size_hostlist('node[1-10]', -5)
		self.assertEqual(test, expected)

	def test_size_as_string(self):
		expected = 'foo[1-2]'
		test = hl.size_hostlist('foo1,foo2,foo3', 2)
		self.assertEqual(test, expected)

	def test_xor_as_list(self):
		expected = 'foo[1-2,4-5]'
		test = hl.xor(['foo1', 'foo2', 'foo3'], ['foo3', 'foo4', 'foo5'])
		self.assertEqual(test, expected)

	def test_xor_with_expand(self):
		expected = 'foo[1-2,6-9]'
		test = hl.xor('foo[1-3]', 'foo[3-5]', 'foo[4-9]')
		self.assertEqual(test, expected)

	def test_xor_as_string(self):
		expected = 'foo[1-2,4-5]'
		test = hl.xor('foo1,foo2,foo3', 'foo3,foo4,foo5')
		self.assertEqual(test, expected)

	def test_exclude_as_list(self):
		expected = 'foo[1-2]'
		test = hl.exclude(['foo1', 'foo2', 'foo3'], 'foo3')
		self.assertEqual(test, expected)

	def test_exclude_with_expand(self):
		expected = 'foo[1-2]'
		test = hl.exclude('foo[1-3]', 'foo3')
		self.assertEqual(test, expected)

	def test_exclude_as_string(self):
		expected = 'foo[1-2]'
		test = hl.exclude('foo1,foo2,foo3', 'foo3')
		self.assertEqual(test, expected)

	def test_quiet(self):
		expected = None
		test = hl.quiet('node1,node2,node3')
		self.assertEqual(test, expected)

	def test_quiet_empty(self):
		expected = "hostlist empty"
		test = hl.quiet()
		self.assertEqual(test, expected)

	def test_quiet_with_expand(self):
		expected = None
		test = hl.quiet("node[1-5]")
		self.assertEqual(test, expected)

	def test_quiet_as_list(self):
		expected = None
		test = hl.quiet(['node1', 'node2', 'node3', 'node4'])
		self.assertEqual(test, expected)

if __name__ == '__main__':
	unittest.main()

# unittest.main()
