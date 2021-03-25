from tools.node import Node
from tools.save_XML import XML_node
from time import process_time
import csv

"""Unweighted Pair Group Method with Arithmetic mean"""
"""Sokal & Michener 1958"""

def UPGMA(matrix, names=None):
    if not names:
        names = [str(i) for i in range(len(matrix))]
    """ Contructs the phylogenetic tree determined by UPGMA
    from the pairwise-distance matrix matrix."""
    if len(matrix)!=len(names):
        print("ERROR: in UPGMA(), matrix and names should be of the same length")
        return None
    nodelist = [Node(item) for item in names]
    nodeqties = [1 for item in names] #9/2/20
    while len(nodelist)>1:
        print("Calculating for",len(nodelist),"nodes...")
        mnt = min_nondiag_triple(matrix)
        i = min(mnt[0], mnt[1])
        j = max(mnt[0], mnt[1])
        reduced_matrix = red_matrix(matrix, i, j, nodeqties) #9/2/20
        new_node = Node(str(round(mnt[2],4)))
        nodelist.append(new_node)
        new_node.insert_left(nodelist[i])
        new_node.insert_right(nodelist[j])
        nodelist.pop(j)
        nodelist.pop(i)
        nodeqties.append(nodeqties[i]+nodeqties[j]) #9/2/20
        nodeqties.pop(j)
        nodeqties.pop(i)
        matrix = reduced_matrix
    return nodelist[0]

def min_nondiag_triple(matrix):
    """Returns a triple consisting of a row #, col #, and value
    of a minimal non-diagonal entry of matrix."""
    if (not len(matrix) > 1) or (not len(matrix[0]) > 1):
        print("ERROR in min_nondiag_triple: matrix too small")
        return
    minval = matrix[0][1]
    mini = 0
    minj = 1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i != j and matrix[i][j] < minval:
                mini, minj, minval = i, j, matrix[i][j]
    return mini, minj, minval

def red_matrix(matrix,i,j,nodeqties):
    """The function that returns the matrix with average distance.
    Updated 9/2/20 to consider node quantities."""
    Mmatrix = []
    wti = nodeqties[i]
    wtj = nodeqties[j]
    for q in range(len(matrix)):
        Mmatrix.append(matrix[q].copy()) #9/2/20: added .copy()
        avg = (matrix[q][i] * wti + matrix[q][j] * wtj)/(wti + wtj)
        Mmatrix[q].pop(j)
        Mmatrix[q].pop(i)
        if q in [i,j]:
            Mmatrix[q].append(0)
        else:
            Mmatrix[q].append(avg)
    NewM = average_of_lists(Mmatrix[i], Mmatrix[j], wti, wtj)
    NewM[-1] = 0 #New addition, 9/2/20
    Mmatrix.pop(j)
    Mmatrix.pop(i)
    Mmatrix.append(NewM)
    return Mmatrix

def average_of_lists(list1, list2, wti, wtj):
    list3 = []
    for a in range(len(list1)):
        summ = (list1[a]* wti + list2[a]* wtj)/(wti + wtj)
        list3.append(summ)
    return list3

root_node = None
if __name__=="__main__":
    method = input('method: ')
    filename = '../output/distmat_'+method+'.csv'
    with open(filename, encoding="utf-8") as infile:
        reader = csv.reader(infile)
        lang_names = []
        dist_matrix = []
        header_row = next(reader) 
        for row in reader:
            lang_names.append(row[0])
            dist_matrix.append([float(x) for x in row[1:]])
        root_node = UPGMA(dist_matrix, lang_names)
        root_XML = XML_node(root_node)
        with open("../output/tree_"+method+'.xml', 'w', encoding='utf-8') as outfile:
            outfile.write(root_XML)
