"""Saves an object of type Node as Python code."""

#from node import Node 
def save_node(the_node, counter=[0], lines_of_code=[]):
    """counter keeps track of how many Nodes have been created."""
    if not the_node:
        return
    lefts_name = None
    rights_name = None
    if the_node.has_left():
        lefts_name = save_node(the_node.left, counter, lines_of_code)
    if the_node.has_right():
        rights_name = save_node(the_node.right, counter, lines_of_code)
    var_name = "n"+str(counter[0])
    lines_of_code.append(var_name + " = " + "Node('"+ the_node.val +"')")
    if the_node.has_left():
        lines_of_code.append(var_name + ".insert_left(" + lefts_name +")")
    if the_node.has_right():
        lines_of_code.append(var_name + ".insert_right(" + rights_name +")")
    counter[0]+=1
    return var_name

def to_file(list_of_lines, filename):
    with open(filename, 'w') as f:
        for line in list_of_lines:
            f.write(line+'\n')
        
if __name__ == '__main__':
    AL = Node("Austronesian lang")

    Formosan = Node("Formosan")
    AL.insert_left(Formosan)

    MP = Node("Malayo Polynesian")
    AL.insert_right(MP)

    NorthernF = Node("NorthernF")
    Formosan.insert_left(NorthernF)

    EastF = Node("EasternF")
    Formosan.insert_right(EastF)

    Atayalic = Node("Atayalic")
    NorthernF.insert_left(Atayalic)

    NorthWestF = Node("NorthWestF")
    NorthernF.insert_right(NorthWestF)

    Kavalanic = Node("Kavalanic")
    EastF.insert_left(Kavalanic)

    Ami = Node("Ami")
    EastF.insert_right(Ami)

    WesternMP = Node("WesternMP")
    MP.insert_left(WesternMP)

    CEMP = Node("Central-EasternMP")
    MP.insert_right(CEMP)

    Philippine = Node("Philippine")
    WesternMP.insert_left(Philippine)

    SamBaj = Node("Sama-Bajaw")
    WesternMP.insert_right(SamBaj)

    SuFl = Node("Sumb-Flores")
    CEMP.insert_left(SuFl)

    Oceanic = Node("Oceanic")
    CEMP.insert_right(Oceanic)

    #
    counter = [0]
    lines_of_code = []
    save_node(AL, counter, lines_of_code)
    #print(lines_of_code)
    to_file(lines_of_code, "AU2.py")
    #
