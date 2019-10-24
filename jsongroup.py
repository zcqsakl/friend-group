my_group = { 'Jill': { 'age': 26, 
                       'job' : ['biologist'],
                        'relation' : {'Zalika' : ['Friend'],
                                      'John' : ['Partner'],}
                     },
            'Zalika' : { 'age': 28,
                         'job' : ['artist'],
                         'relation' : { 'Jill' :['Friend'],
                                      'Nash' : ['Tenant']}
                       },
            'John' : {'age' : 27,
                      'job' : ['writer'],
                      'relation': {'Jill' : ['Partner'],
                                   'Nash' : ['Cousin']}
                     },
            'Nash' : {'age' : 34,
                      'job' : ['chef'],
                      'relation' : { 'John' : ['Cousin'],
                                    'Zalika' : ['Landlord']}
                     }
           }
                 

import json

with open("group.json", "w") as json_group:
    json_group.write(json.dumps(my_group))

with open('group.json') as json_group_in:
    group = json.load(json_group_in)
    print(group)
