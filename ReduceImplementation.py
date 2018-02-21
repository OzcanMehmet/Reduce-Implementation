def ReduceImplementation(X,params): #Basic MapImplementation
    params=list(params)
    if len(params)>=2:
        params[1]=params[0]=X(params[0],params[1])
        return ReduceImplementation(X,params[1:])
    else: 
        return params[0]  
ReduceImplementation(lambda x,y:x+y,[1,2,3,5])

functools.reduce(lambda x,y:x+y,[1,2,3])
