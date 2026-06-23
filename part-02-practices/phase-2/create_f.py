def create_user (name, age, city):
    print(name, age, city)

create_user("Atul", 21, "Manikganj")

# keyword double arguments. ei arguments gula ke python bole **kwargs. eta use korle amra function er vitore dictionary er moto data pass korte pari. multiple value pass kora jay ar dictionary hoyei save hobe. 

def create_person(**args): # **kwargs
    print(args)
    # print(type(args))
create_person(name=["Atul", "Ankit"], age=[21, 9], city=["Dhaka", "Manikganj"])

