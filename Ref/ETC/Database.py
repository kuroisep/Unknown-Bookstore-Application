import pandas

#['USER', 'PASSWORD', 'NAME', 'LNAME', 'EMAIL']
df = pandas.read_csv('login.csv')
data = df.set_index('USER').T.to_dict('list')

def verify(user,password):
    if data.get(user) != None:
        if data.get(user)[0] == password:
            print('success')
        else:
            print('incorrect pass')
    else:
        print('Not Found')

verify('ddd',1243)