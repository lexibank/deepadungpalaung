#from node import Node 
def XML_node(the_node, depth=0):
    """counter keeps track of how many Nodes have been created."""
    XML_data = ''
    if depth == 0:
        XML_data += "<root>"
    if not the_node:
        return
    lefts_name = None
    rights_name = None
    if the_node.has_left():
        lefts_name = XML_node(the_node.left, depth+1)
    if the_node.has_right():
        rights_name = XML_node(the_node.right, depth+1)
    #var_name = "n"+str(counter[0])
    XML_data += the_node.val.replace("&", '')
    if the_node.has_left():
        XML_data+= "\n"+"\t"*depth+"<left>"+ lefts_name +"</left>" 
    if the_node.has_right():
        XML_data+= "\n"+"\t"*depth+"<right>" + rights_name +"</right>"
    if depth == 0:
        XML_data += "</root>"
    return XML_data



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

    XML_data = ''
    print(XML_node(AL))
