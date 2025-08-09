# application.py


# import code from other directory files -> (package)
from DataStructures.mylist import MyList
from analysis.myanalysis import MyAnalysis


new_list = MyList()

new_list.addElements(23)
new_list.addElements(2)
new_list.addElements(25)
new_list.addElements(27)

new_list.removeElemnt(2)
new_list.printList()


new_analysis = MyAnalysis()
new_analysis.list.append(2)
print(new_analysis.list)
