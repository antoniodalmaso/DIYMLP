class Vector:
    def __init__(this, N):
        this.__values = [0 for i in range(N)]
        this.__N = N

    def get(this, idx):
        return this.__values[idx]
    
    def set(this, idx, n):
        this.__values[idx] = n

    def size(this):
        return this.__N
    
    def __checkSize(this, v):
        if this.size() != v.size():
            raise Exception("Dot product is not possible between vectors of different sizes")
    
    def plus(this, v):
        this.__checkSize(v)

        res = Vector(this.size())
        for idx in range(this.size()):
            res.set(idx, this.get(idx)+v.get(idx))

        return res
    
    def minus(this, v):
        this.__checkSize(v)

        res = Vector(this.size())
        for idx in range(this.size()):
            res.set(idx, this.get(idx)-v.get(idx))

        return res
    
    def dot(this, v):
        this.__checkSize(v)
        
        res = 0
        for idx in range(this.size()):
            res += this.get(idx)*v.get(idx)

        return res
    
    def norm(this):
        return this.dot(this) ** (1/2)
    
    def hadamard(this, v):
        this.__checkSize(v)
        
        res = Vector(this.size())
        for idx in range(this.size()):
            res.set(idx, this.get(idx)*v.get(idx))

        return res
    
    def applyElementwise(this, f):
        res = Vector(this.size())

        for idx in range(this.size()):
            res.set(idx, f(this.get(idx)))

        return res
    
    def print(this):
        print(this.__values)



class Matrix:
    def __init__(this, N,M):
        this.__values = [[0 for j in range(M)] for i in range(N)]
        this.__N = N
        this.__M = M

    def get(this, i, j):
        return this.__values[i][j]
    
    def set(this, i, j, n):
        this.__values[i][j] = n

    def size(this):
        return this.__N, this.__M
    
    def dotVector(this, v):
        N, M = this.size()

        if M != v.size():
            raise Exception("Dot product is not possible if the number of columns of the matrix is different from the size of the vector")
        
        res = Vector(N)
        for i in range(N):
            aux = 0
            for j in range(M):
                aux += this.get(i,j)*v.get(j)
            res.set(i, aux)

        return res
    
    def print(this):
        print(this.__values)