import re

"""
This package processes slurm-style hostlist strings.

expand(nodelist)
    returns a list of individual hostnames given a hostlist string

compress_range(nodelist)
    returns an ordered hostlist string given a list of hostnames with a range

compress(nodelist)
    returns an ordered hostlist string given a list of hostnames

diff(nodelist1, nodelist2)
    subtract elements in list 2 from list 1 and return a remainding hostlist
  
sort_nodes(nodelist)
    sort will return a sorted hostlist in ascending order

append_hostname(machine_name, num_list)
    helper method to append hostname to node numbers 

intersect(*arg)
    return list of intersection nodes given n lists of nodes

union(*arg)
    returns the union between n lists of nodes

   
Author: Christopher Moussa (moussa1@llnl.gov)
Mentor: Elsa Gonsiorowski (gonsiorowski1@llnl.gov)
Date: June 15, 2018
"""

# ========== HELPER METHODS ========== #


# helper method to append hostname to node numbers
def append_hostname(machine_name, num_list):
    hostlist = []
    for elem in num_list:
        hostlist.append(machine_name + str(elem))

    return '%s' % ','.join(map(str, hostlist))



# sort_nodes will sort the nodes in ascending order
def sort_nodes(nodelist):

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

    print '[%s]' % ''.join(map(str, hostlist))
    return '[%s]' % ''.join(map(str, hostlist))


# ========== END OF HELPER METHODS =========== # 



"""
expand will match an arbitrary number of ranges
    ex. quartz[7,9,10-12] will return a hostlist string 
    quartz7,quartz9,quartz10,quartz11,quartz12
nodelist_match will put the expression into three control groups:
    (0) the full expression
    (1) the cluster name
    (2) the ranges of nodes
"""
def expand(nodelist):
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

#        print final_list

#        for i in range(len(final_list)):
#            final_list[i] = str(final_list[i])
#            if (int(final_list[i]) < 10):
#                final_list[i] = "{:02}".format(int(final_list[i]))

#       print final_list                

        hostlist = append_hostname(match.group(1), final_list)


        print '%s' % ''.join(map(str, hostlist))
        return '%s' % ''.join(map(str, hostlist))

    else:
        print("No match")





"""
compress_range will return a hostlist string compressed string given a list of hostnames
compress_range('cab1','cab2','cab3','cab4','cab6') will return cab[1-4,6]
"""
def compress_range(nodelist):

    list_of_nodes = nodelist
    # get machine name and numbers for nodes
    # append the numbers of the nodes to num_list for compression
    count = 0
    num_list = []
    for node in nodelist:
        iter_node = nodelist[count]
        nodelist_match = r"([a-z]+)(\d+)"
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

    print machine_name.group(1) + '[%s]' % ','.join(map(str, final_list))
    return machine_name.group(1) + '[%s]' % ','.join(map(str, final_list))



"""
# compress will return a hostlist string given a list of hostnames
# compress('cab1','cab2','cab3','cab4','cab6') will return [cab1,cab2,cab3,cab4,cab6]
"""
def compress(nodelist):

    list_of_nodes = nodelist

    print '[%s]' % ','.join(map(str, nodelist))
    return '[%s]' % ','.join(map(str, nodelist))


"""
diff will subtract elements in list 2 from list 1 and return remainder
"""
def diff(nodelist1, nodelist2):

    list_of_nodes1 = set(nodelist1)
    list_of_nodes2 = set(nodelist2)

    # use python's set features to get difference between two lists
    diff_list = list_of_nodes1.difference(list_of_nodes2)

    print '[%s]' % ','.join(map(str, diff_list))
    return '[%s]' % ','.join(map(str, diff_list))

    
"""
given references to n lists, return list of intersecting nodes
"""
def intersect(*arg):
    num_of_lists = len(arg)
    first_list = arg[0]

    for i in range(1, len(arg)):
        first_list = list(set(first_list) & set(arg[i]))

    return sort_nodes(first_list)


"""
returns the union between n lists of nodes
"""
def union_nodes(*arg):
    num_of_lists = len(arg)
    first_list = arg[0]

    for i in range(1, len(arg)):
        first_list = first_list + arg[i]

    union_list = list(set(first_list))

    return sort_nodes(union_list)


