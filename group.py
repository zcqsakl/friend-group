"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

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
                 
