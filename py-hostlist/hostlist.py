"""
.. module:: hostlist
   :platform: Unix, MacOS
   :synopsis: A slurm-style hostlist processor.

.. moduleauthor:: Christopher Moussa <moussa1@llnl.gov>


"""

import re

# ========== HELPER METHODS ========== #


def append_hostname(machine_name, num_list):
    """append_hostname is a helper method to append the hostname to node numbers.

    Args:
        machine_name (str): The name of the cluster.
        num_list (list):    The list of nodes to be appended to the cluster name.

    Returns:
        hostlist (str): A hostlist string with the hostname and node numbers.

    """

    hostlist = []
    for elem in num_list:
        hostlist.append(machine_name + str(elem))

    return '%s' % ','.join(map(str, hostlist))



def sort_nodes(nodelist):
    """sort_nodes is a helper method that sorts the nodes in ascending order.

    Args:
        nodelist (str): The hostlist string.

    Returns:
        hostlist (str): The hostlist string in ascending order.

    """

    list_of_nodes = nodelist

    if type(list_of_nodes) == str:
        left_br = list_of_nodes.replace("[","")
        right_br = left_br.replace("]","")
        nodelist = right_br.split(',')

    count = 0
    num_list = []
    for node in nodelist:
        iter_node = nodelist[count]
        nodelist_match = r"([a-z]+)(\d+)"
        machine_name = re.search(nodelist_match, iter_node)
        num_list.append(int(machine_name.group(2)))
        count = count+1
    num_list.sort()
    
    hostlist = append_hostname(machine_name.group(1), num_list)

    print('[%s]' % ''.join(map(str, hostlist)))
    return '[%s]' % ''.join(map(str, hostlist))


# ========== END OF HELPER METHODS =========== # 



def expand(nodelist):
    """expand takes in a compressed hostlist string and returns all hosts listed.

    Args:
        nodelist (str): The hostlist string.

    Returns: 
        final_hostlist (str): The expanded hostlist string.
    """

    nodelist_match = r"(\w+-?)\[((,?[0-9]+,?-?[0-9]+-?){0,})\](.*)?"
    if re.search(nodelist_match, nodelist):
        match = re.search(nodelist_match, nodelist) 

        # holds the ranges of nodes as a string
        # now we can manipulate the string and cast it to a list of numbers
        oldstr = str(match.group(2))
        left_br = oldstr.replace("[","")
        right_br = left_br.replace("]","")
        num_list = right_br.split(',')


        final_list = []
        lead_zeros = 0
        lead_zeros_str = ''
        for elem in num_list:
            # if it is a range of numbers, break it by the hyphen and create a list
            # will then be merged with final list
            if '-' in elem:
                tmp_list = elem.replace("-", ",").split(",")

                for digit in tmp_list[0]:
                    if digit == '0':
                        lead_zeros = lead_zeros + 1
                        lead_zeros_str = lead_zeros_str + '0'

                rng_list = range(int(tmp_list[0]), int(tmp_list[1]) + 1)
                final_list.extend(rng_list)
            else:
                final_list.append(int(elem))

        # put final list in ascending order and append cluster name to each node number
        final_list.sort()

        # prepend leading zeros to numbers required
        hostlist_tmp = []
        for elem in final_list:
            if ((lead_zeros > 0) and (len(str(elem)) <= len(lead_zeros_str))):
                hostlist_tmp.append(str(elem).zfill(lead_zeros + 1))
            else:
                hostlist_tmp.append(str(elem))

        # append hostname to the node numbers
        hostlist_no_suffix = []
        for elem in hostlist_tmp:
            hostlist_no_suffix.append(match.group(1) + elem)

        # append suffix to hostlist if there is one
        final_hostlist = []
        for elem in hostlist_no_suffix:
            final_hostlist.append(elem + match.group(4))

        print('%s' % ','.join(map(str, final_hostlist)))
        return '%s' % ','.join(map(str, final_hostlist)) 



def compress_range(nodelist):
    """compress_range will return a compressed hostlist string given a list of hostnames.
    
    Args:
        nodelist (str): The expanded hostlist string.

    Returns:
        final_list (str): The compressed hostlist string.
    """

    list_of_nodes = nodelist

    if type(list_of_nodes) == str:
        left_br = list_of_nodes.replace("[","")
        right_br = left_br.replace("]","")
        list_of_nodes = right_br.split(',')

    # get machine name and numbers for nodes
    # append the numbers of the nodes to num_list for compression
    count = 0
    num_list = []

    # check if node is in the following format: <node1-2,node1-3,node1-4>
    if "-" in list_of_nodes[0]:
        for node in list_of_nodes:
            iter_node = list_of_nodes[count]
            nodelist_match = r"(\w+-?)(\d+)(.*)"
            machine_name = re.search(nodelist_match, iter_node)
            num_list.append(int(machine_name.group(2)))
            count = count+1
    else:
        for node in list_of_nodes:
            iter_node = list_of_nodes[count]
            nodelist_match = r"([a-zA-Z]+)(\d+)(.*)"
            machine_name = re.search(nodelist_match, iter_node)
            num_list.append(int(machine_name.group(2)))
            count = count+1
    
    # build the ranges
    final_list = []
    num_list.sort()
    low = num_list[0]
    last = low
    i = 1
    for i in range(1, len(num_list)):
        high = num_list[i]
        if (high == last+1):
            last = high
            continue            
        if (last > low):
            final_list.append(str(low) + "-" + str(last))
        else:
            final_list.append(str(low))
        low = high
        last = low
    if (len(num_list) > 0):
        if (last > low):
            final_list.append(str(low)+"-"+str(last))
        else:
            final_list.append(low)

    result_str = machine_name.group(1) + '[%s]' % ','.join(map(str, final_list))
    print(result_str + machine_name.group(3))
    return result_str + machine_name.group(3)



def compress(nodelist):
    """compress will return a hostlist string given a list of hostnames.
    
    Args:
        nodelist (str): The hostlist string.

    Returns:
        nodelist (str): The hostlist string. 
    
    """

    if type(nodelist) == str:
        left_br = nodelist.replace("[","")
        right_br = left_br.replace("]","")
        nodelist = right_br.split(',') 

    print('[%s]' % ','.join(map(str, nodelist)))
    return '[%s]' % ','.join(map(str, nodelist))



def diff(nodelist1, nodelist2):
    """diff will subtract elements in list 2 from list 1 and return remainder.

    Args:
        nodelist1 (str): The hostlist string to be subtracted from. 
        nodelist2 (str): The other hostlist string.

    Returns:
        diff_list (str): The remainding list from subtracting the two original lists.
    """

    list_of_nodes1 = nodelist1
    list_of_nodes2 = nodelist2

    if type(list_of_nodes1) == str:
        left_br = list_of_nodes1.replace("[","")
        right_br = left_br.replace("]","")
        list_of_nodes1 = right_br.split(',') 

    if type(list_of_nodes2) == str:
        left_br = list_of_nodes2.replace("[","")
        right_br = left_br.replace("]","")
        list_of_nodes2 = right_br.split(',')  

    # use python's set features to get difference between two lists
    diff_list = set(list_of_nodes1).difference(set(list_of_nodes2))

    print('[%s]' % ','.join(map(str, diff_list)))
    return '[%s]' % ','.join(map(str, diff_list))



def intersect(*arg):
    """Given references to n lists, intersect return a list of intersecting nodes.

    Args:
        nodelist (str): Any number of nodelists to be intersected.

    Returns:
        first_list (str): The resulting intersected list.
    """
    
    num_of_lists = len(arg)

    # will hold a list of the lists passed in
    conv_lists = []
    for lst in arg:
        # check to see if the list passed in is a string; if it is, convert to list
        if type(lst) == str:
            left_br = lst.replace("[","")
            right_br = left_br.replace("]","")
            lst = right_br.split(',')
            
        conv_lists.append(lst)

    first_list = conv_lists[0]

    # use Boolean logic to find intersecting nodes between passed in lists
    for i in range(1, len(conv_lists)):
        first_list = list(set(first_list) & set(conv_lists[i]))

    return sort_nodes(first_list)



def union_nodes(*arg):
    """union_nodes returns the union between n lists of nodes.

    Args:
        nodelist (str): Any number of nodelists to be combined.

    Returns:
        union_list (str): The resulting unioned list.
    """

    num_of_lists = len(arg)

    # will hold a list of the lists passed in
    conv_lists = []
    for lst in arg:
        # check to see if the list passed in is a string; if it is, convert to list
        if type(lst) == str:
            left_br = lst.replace("[","")
            right_br = left_br.replace("]","")
            lst = right_br.split(',')
            
        conv_lists.append(lst)

    first_list = conv_lists[0]

    for i in range(1, len(conv_lists)):
        first_list = first_list + conv_lists[i]

    union_list = list(set(first_list))

    return sort_nodes(union_list)



def nth(nodelist, n):
    """nth returns the nth node from a list of nodes.

    Args:
        nodelist (str): The hostlist string.
        n (int): The index desired.

    Returns:
        hostlist_indexed[int(n)-1] (int): The host at the specified index.

    .. note::

        The index specified is one-base indexed, not zero-based.
    """

    nodelist_match = r"([a-z]+[A-Z0-9]?)-?\[((,?[0-9]+,?-?[0-9]+-?){0,})\](.*)?"
    if re.search(nodelist_match, nodelist):
        match = re.search(nodelist_match, nodelist)

        # holds the ranges of nodes as a string
        # now we can manipulate the string and cast it to a list of numbers
        oldstr = str(match.group(2))
        left_br = oldstr.replace("[","")
        right_br = left_br.replace("]","")
        num_list = right_br.split(',')

        final_list = []
        for elem in num_list:
            # if it is a range of numbers, break it by the hyphen and create a list
            # will then be merged with final list
            if '-' in elem:
                tmp_list = elem.replace("-", ",").split(",")
                rng_list = range(int(tmp_list[0]), int(tmp_list[1]) + 1)
                final_list.extend(rng_list)
            else:
                final_list.append(int(elem))

        # put final list in ascending order and append cluster name to each node number
        final_list.sort()
        hostlist = append_hostname(match.group(1), final_list)

        # put sorted hostlist into a list, use comma as delimiter so it can be accessed by an index
        hostlist_indexed = hostlist.split(",")

        if (int(n) not in range(1, len(hostlist_indexed)+1)):
            print("node does not exist")
            return "node does not exist"
        else:
            print(hostlist_indexed[int(n)-1])
            return hostlist_indexed[int(n)-1]



def find(nodelist, node):
    """find outputs the position of the node in the nodelist passed in.

    Args:
        nodelist (str): The hostlist string.
        node (str): The host to be searched inside of the hostlist string.

    Returns:
        nodelist.index(node) (int): The position of the host within the hostlist string.

    .. note::

        The index specified is one-base indexed, not zero-based.
    """

    if type(nodelist) == list:
        if node in nodelist:
            print("At position " + str(nodelist.index(node) + 1))
            return "At position " + str(nodelist.index(node) + 1)
        else:
            print("node does not exist")
            return "node does not exist"
    elif "[" in nodelist:
        list_of_nodes = expand(nodelist)
        left_br = list_of_nodes.replace("[","")
        right_br = left_br.replace("]","")
        nodelist = right_br.split(',')
        if node in nodelist:
            print("At position " + str(nodelist.index(node) + 1))
            return "At position " + str(nodelist.index(node) + 1)
        else:
            print("node does not exist")
            return "node does not exist"
    else:
        list_of_nodes = nodelist
        left_br = list_of_nodes.replace("[","")
        right_br = left_br.replace("]","")
        nodelist = right_br.split(',') 
        if node in nodelist:
            print("At position " + str(nodelist.index(node) + 1))
            return "At position " + str(nodelist.index(node) + 1)
        else:
            print("node does not exist")
            return "node does not exist"       



def count(nodelist):
    """count returns the number of hosts.

    Args:
        nodelist (str): The hostlist string.

    Returns:
        len(nodelist) (int): The host at the specified index.

    """

    if type(nodelist) == list:
        print(len(nodelist))
        return len(nodelist)
    elif "[" in nodelist: 
        list_of_nodes = expand(nodelist)
        left_br = list_of_nodes.replace("[","")
        right_br = left_br.replace("]","")
        nodelist = right_br.split(',') 
        print(len(nodelist))
        return len(nodelist)         
    else:
        list_of_nodes = nodelist
        left_br = list_of_nodes.replace("[","")
        right_br = left_br.replace("]","")
        nodelist = right_br.split(',') 
        print(len(nodelist))
        return len(nodelist)        


