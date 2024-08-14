from typing import Dict, Union, Optional
import pprint             # pprint is used to show data more beautifully

Key = Union[int,str]
Value = Union[int,str,list, dict, tuple,set]

data : Dict[Key,Value] = {"fname" : "Muhammad Qasim",
                        "name" : "Abu Bakr",
                         "Education" :"Engineering",
                         1: ["Majid Ali", 5, 6, True],
                         'abc' : (1,2,5,8),
                         'cde' : {'a': "Majid", 'b':"Sajid"},
                         'dge' : {1,3,5,5,5,5}
                         }


print(data['cde']['b'])