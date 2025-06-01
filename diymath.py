class Vector:
    def __init__(this, N):
        this.__values = [0]*N
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