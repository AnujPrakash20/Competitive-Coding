class min_max():
    def __init__(self):
        self.min=0
        self.max=0

    def find(self,array,n):
        if n==1:
            self.min=array[0]
            self.max=array[0]
        if array[0]>array[1]:
                self.min=array[1]
                self.max=array[0]
        else:
                self.min = array[0]
                self.max = array[1]
        for i in range(2,n):
                if array[i] > self.max:
                    self.max=array[i]
                elif array[i] < self.min:
                    self.min=array[i]
        return [self.min,self.max]

if __name__ == '__main__':
    array=[5,6,1,9,3]
    n=5
    a=min_max()
    print(a.find(array,n))


