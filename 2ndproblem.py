class validate:
    def validate_triangle(self,a,b,c):
        if a+b>=c and b+c>=a and c+a>=b:
            return "valid Triangle"
        else:
            return "Invalid Triangle"
    def validate_rectangle(self,a,b,c,d):
        if (a==b and c==d) or (a==c and b==d) or (a==d and b==c):
            return "valid rectangle"
        else:
            return "Invalid rectangle"
obj=validate()
print(obj.validate_triangle(4,1,9))
print(obj.validate_rectangle(1,2,1,2))