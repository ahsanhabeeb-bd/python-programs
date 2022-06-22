import  random
class math:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.e = 0
        self.f = 0
        self.g = ['+']
        self.h = ['+','-','*','/']
        self.i = ['+','-','*','/']
        self.j = ['+','-','*','/']
        self.k = ['+','-','*','/']
        self.g1 = 0
        self.h1 = 0
        self.ans1 = 0


    def ran_(self):
        self.a = random.randint(1,99)
        self.b = random.randint(1,99)
        self.c = random.randint(1,99)
        self.d = random.randint(1,99)
        self.e = random.randint(1,99)
        self.f = random.randint(1,99)

        return self.a,self.b,self.c,self.d,self.e,self.f

    def mat_(self):
        self.g = random.choice(self.g)
        self.h = random.choice(self.h)
        self.i = random.choice(self.i)
        self.j = random.choice(self.j)
        self.k = random.choice(self.k)

        return self.g,self.h,self.i,self.j,self.k

    def ans_(self):

        if self.g == '+' and self.h == '+' and self.i == '+' and self.j == '+' and self.k == '+':
            self.ans1 = self.a + self.b + self.c + self.d + self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '+' and self.j == '+' and self.k == '-':
            self.ans1 = self.a + self.b + self.c + self.d + self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '+' and self.j == '+' and self.k == '*':
            self.ans1 = self.a + self.b + self.c + self.d + self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '+' and self.j == '+' and self.k == '/':
            self.ans1 = self.a + self.b + self.c + self.d + self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '+' and self.i == '+' and self.j == '-' and self.k == '+':
            self.ans1 = self.a + self.b + self.c + self.d - self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '+' and self.j == '-' and self.k == '-':
            self.ans1 = self.a + self.b + self.c + self.d - self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '+' and self.j == '-' and self.k == '*':
            self.ans1 = self.a + self.b + self.c + self.d - self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '+' and self.j == '-' and self.k == '/':
            self.ans1 = self.a + self.b + self.c + self.d - self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '+' and self.i == '+' and self.j == '*' and self.k == '+':
            self.ans1 = self.a + self.b + self.c + self.d * self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '+' and self.j == '*' and self.k == '-':
            self.ans1 = self.a + self.b + self.c + self.d * self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '+' and self.j == '*' and self.k == '*':
            self.ans1 = self.a + self.b + self.c + self.d * self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '+' and self.j == '*' and self.k == '/':
            self.ans1 = self.a + self.b + self.c + self.d * self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '+' and self.i == '+' and self.j == '/' and self.k == '+':
            self.ans1 = self.a + self.b + self.c + self.d / self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '+' and self.j == '/' and self.k == '-':
            self.ans1 = self.a + self.b + self.c + self.d / self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '+' and self.j == '/' and self.k == '*':
            self.ans1 = self.a + self.b + self.c + self.d / self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '+' and self.j == '/' and self.k == '/':
            self.ans1 = self.a + self.b + self.c + self.d / (self.e / self.f)
            return self.ans1

        elif self.g == '+' and self.h == '+' and self.i == '-' and self.j == '+' and self.k == '+':
            self.ans1 = self.a + self.b + self.c - self.d + self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '-' and self.j == '+' and self.k == '-':
            self.ans1 = self.a + self.b + self.c - self.d + self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '-' and self.j == '+' and self.k == '*':
            self.ans1 = self.a + self.b + self.c - self.d + self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '-' and self.j == '+' and self.k == '/':
            self.ans1 = self.a + self.b + self.c - self.d + self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '+' and self.i == '-' and self.j == '-' and self.k == '+':
            self.ans1 = self.a + self.b + self.c - self.d - self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '-' and self.j == '-' and self.k == '-':
            self.ans1 = self.a + self.b + self.c - self.d - self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '-' and self.j == '-' and self.k == '*':
            self.ans1 = self.a + self.b + self.c - self.d - self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '-' and self.j == '-' and self.k == '/':
            self.ans1 = self.a + self.b + self.c - self.d - self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '+' and self.i == '-' and self.j == '*' and self.k == '+':
            self.ans1 = self.a + self.b + self.c - self.d * self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '-' and self.j == '*' and self.k == '-':
            self.ans1 = self.a + self.b + self.c - self.d * self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '-' and self.j == '*' and self.k == '*':
            self.ans1 = self.a + self.b + self.c - self.d * self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '-' and self.j == '*' and self.k == '/':
            self.ans1 = self.a + self.b + self.c - self.d * self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '+' and self.i == '-' and self.j == '/' and self.k == '+':
            self.ans1 = self.a + self.b + self.c - self.d / self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '-' and self.j == '/' and self.k == '-':
            self.ans1 = self.a + self.b + self.c - self.d / self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '-' and self.j == '/' and self.k == '*':
            self.ans1 = self.a + self.b + self.c - self.d / self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '-' and self.j == '/' and self.k == '/':
            self.ans1 = self.a + self.b + self.c - self.d / (self.e / self.f)
            return self.ans1



        elif self.g == '+' and self.h == '+' and self.i == '*' and self.j == '+' and self.k == '+':
            self.ans1 = self.a + self.b + self.c * self.d + self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '*' and self.j == '+' and self.k == '-':
            self.ans1 = self.a + self.b + self.c * self.d + self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '*' and self.j == '+' and self.k == '*':
            self.ans1 = self.a + self.b + self.c * self.d + self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '*' and self.j == '+' and self.k == '/':
            self.ans1 = self.a + self.b + self.c * self.d + self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '+' and self.i == '*' and self.j == '-' and self.k == '+':
            self.ans1 = self.a + self.b + self.c * self.d - self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '*' and self.j == '-' and self.k == '-':
            self.ans1 = self.a + self.b + self.c * self.d - self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '*' and self.j == '-' and self.k == '*':
            self.ans1 = self.a + self.b + self.c * self.d - self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '*' and self.j == '-' and self.k == '/':
            self.ans1 = self.a + self.b + self.c * self.d - self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '+' and self.i == '*' and self.j == '*' and self.k == '+':
            self.ans1 = self.a + self.b + self.c * self.d * self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '*' and self.j == '*' and self.k == '-':
            self.ans1 = self.a + self.b + self.c * self.d * self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '*' and self.j == '*' and self.k == '*':
            self.ans1 = self.a + self.b + self.c * self.d * self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '*' and self.j == '*' and self.k == '/':
            self.ans1 = self.a + self.b + self.c * self.d * self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '+' and self.i == '*' and self.j == '/' and self.k == '+':
            self.ans1 = self.a + self.b + self.c * self.d / self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '*' and self.j == '/' and self.k == '-':
            self.ans1 = self.a + self.b + self.c * self.d / self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '*' and self.j == '/' and self.k == '*':
            self.ans1 = self.a + self.b + self.c * self.d / self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '*' and self.j == '/' and self.k == '/':
            self.ans1 = self.a + self.b + self.c * self.d / (self.e / self.f)
            return self.ans1

        #01
        elif self.g == '+' and self.h == '+' and self.i == '/' and self.j == '+' and self.k == '+':
            self.ans1 = self.a + self.b + self.c / self.d + self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '/' and self.j == '+' and self.k == '-':
            self.ans1 = self.a + self.b + self.c / self.d + self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '/' and self.j == '+' and self.k == '*':
            self.ans1 = self.a + self.b + self.c / self.d + self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '/' and self.j == '+' and self.k == '/':
            self.ans1 = self.a + self.b + self.c / self.d + self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '+' and self.i == '/' and self.j == '-' and self.k == '+':
            self.ans1 = self.a + self.b + self.c / self.d - self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '/' and self.j == '-' and self.k == '-':
            self.ans1 = self.a + self.b + self.c / self.d - self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '/' and self.j == '-' and self.k == '*':
            self.ans1 = self.a + self.b + self.c / self.d - self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '/' and self.j == '-' and self.k == '/':
            self.ans1 = self.a + self.b + self.c / self.d - self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '+' and self.i == '/' and self.j == '*' and self.k == '+':
            self.ans1 = self.a + self.b + self.c / self.d * self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '/' and self.j == '*' and self.k == '-':
            self.ans1 = self.a + self.b + self.c / self.d * self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '/' and self.j == '*' and self.k == '*':
            self.ans1 = self.a + self.b + self.c / self.d * self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '/' and self.j == '*' and self.k == '/':
            self.ans1 = self.a + self.b + self.c / self.d * self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '+' and self.i == '/' and self.j == '/' and self.k == '+':
            self.ans1 = self.a + self.b + self.c / (self.d / self.e) + self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '/' and self.j == '/' and self.k == '-':
            self.ans1 = self.a + self.b + self.c / (self.d / self.e) - self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '/' and self.j == '/' and self.k == '*':
            self.ans1 = self.a + self.b + self.c / (self.d / self.e) * self.f
            return self.ans1
        elif self.g == '+' and self.h == '+' and self.i == '/' and self.j == '/' and self.k == '/':
            self.ans1 = self.a + self.b + self.c / (self.d / (self.e / self.f))
            return self.ans1

# 0/-
        elif self.g == '+' and self.h == '-' and self.i == '+' and self.j == '+' and self.k == '+':
            self.ans1 = self.a + self.b - self.c + self.d + self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '+' and self.j == '+' and self.k == '-':
            self.ans1 = self.a + self.b - self.c + self.d + self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '+' and self.j == '+' and self.k == '*':
            self.ans1 = self.a + self.b - self.c + self.d + self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '+' and self.j == '+' and self.k == '/':
            self.ans1 = self.a + self.b - self.c + self.d + self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '-' and self.i == '+' and self.j == '-' and self.k == '+':
            self.ans1 = self.a + self.b - self.c + self.d - self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '+' and self.j == '-' and self.k == '-':
            self.ans1 = self.a + self.b - self.c + self.d - self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '+' and self.j == '-' and self.k == '*':
            self.ans1 = self.a + self.b - self.c + self.d - self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '+' and self.j == '-' and self.k == '/':
            self.ans1 = self.a + self.b - self.c + self.d - self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '-' and self.i == '+' and self.j == '*' and self.k == '+':
            self.ans1 = self.a + self.b - self.c + self.d * self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '+' and self.j == '*' and self.k == '-':
            self.ans1 = self.a + self.b - self.c + self.d * self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '+' and self.j == '*' and self.k == '*':
            self.ans1 = self.a + self.b - self.c + self.d * self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '+' and self.j == '*' and self.k == '/':
            self.ans1 = self.a + self.b - self.c + self.d * self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '-' and self.i == '+' and self.j == '/' and self.k == '+':
            self.ans1 = self.a + self.b - self.c + self.d / self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '+' and self.j == '/' and self.k == '-':
            self.ans1 = self.a + self.b - self.c + self.d / self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '+' and self.j == '/' and self.k == '*':
            self.ans1 = self.a + self.b - self.c + self.d / self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '+' and self.j == '/' and self.k == '/':
            self.ans1 = self.a + self.b - self.c + self.d / (self.e / self.f)
            return self.ans1

        elif self.g == '+' and self.h == '_' and self.i == '-' and self.j == '+' and self.k == '+':
            self.ans1 = self.a + self.b - self.c - self.d + self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '_' and self.i == '-' and self.j == '+' and self.k == '-':
            self.ans1 = self.a + self.b - self.c - self.d + self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '_' and self.i == '-' and self.j == '+' and self.k == '*':
            self.ans1 = self.a + self.b - self.c - self.d + self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '_' and self.i == '-' and self.j == '+' and self.k == '/':
            self.ans1 = self.a + self.b - self.c - self.d + self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '-' and self.i == '-' and self.j == '-' and self.k == '+':
            self.ans1 = self.a + self.b - self.c - self.d - self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '-' and self.j == '-' and self.k == '-':
            self.ans1 = self.a + self.b - self.c - self.d - self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '-' and self.j == '-' and self.k == '*':
            self.ans1 = self.a + self.b - self.c - self.d - self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '-' and self.j == '-' and self.k == '/':
            self.ans1 = self.a + self.b - self.c - self.d - self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '-' and self.i == '-' and self.j == '*' and self.k == '+':
            self.ans1 = self.a + self.b - self.c - self.d * self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '-' and self.j == '*' and self.k == '-':
            self.ans1 = self.a + self.b - self.c - self.d * self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '-' and self.j == '*' and self.k == '*':
            self.ans1 = self.a + self.b - self.c - self.d * self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '-' and self.j == '*' and self.k == '/':
            self.ans1 = self.a + self.b - self.c - self.d * self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '-' and self.i == '-' and self.j == '/' and self.k == '+':
            self.ans1 = self.a + self.b - self.c - self.d / self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '-' and self.j == '/' and self.k == '-':
            self.ans1 = self.a + self.b - self.c - self.d / self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '-' and self.j == '/' and self.k == '*':
            self.ans1 = self.a + self.b - self.c - self.d / self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '-' and self.j == '/' and self.k == '/':
            self.ans1 = self.a + self.b - self.c - self.d / (self.e / self.f)
            return self.ans1



        elif self.g == '+' and self.h == '-' and self.i == '*' and self.j == '+' and self.k == '+':
            self.ans1 = self.a + self.b - self.c * self.d + self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '*' and self.j == '+' and self.k == '-':
            self.ans1 = self.a + self.b - self.c * self.d + self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '*' and self.j == '+' and self.k == '*':
            self.ans1 = self.a + self.b - self.c * self.d + self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '*' and self.j == '+' and self.k == '/':
            self.ans1 = self.a + self.b - self.c * self.d + self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '-' and self.i == '*' and self.j == '-' and self.k == '+':
            self.ans1 = self.a + self.b - self.c * self.d - self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '*' and self.j == '-' and self.k == '-':
            self.ans1 = self.a + self.b - self.c * self.d - self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '*' and self.j == '-' and self.k == '*':
            self.ans1 = self.a + self.b - self.c * self.d - self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '*' and self.j == '-' and self.k == '/':
            self.ans1 = self.a + self.b - self.c * self.d - self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '-' and self.i == '*' and self.j == '*' and self.k == '+':
            self.ans1 = self.a + self.b - self.c * self.d * self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '*' and self.j == '*' and self.k == '-':
            self.ans1 = self.a + self.b - self.c * self.d * self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '*' and self.j == '*' and self.k == '*':
            self.ans1 = self.a + self.b - self.c * self.d * self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '*' and self.j == '*' and self.k == '/':
            self.ans1 = self.a + self.b - self.c * self.d * self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '-' and self.i == '*' and self.j == '/' and self.k == '+':
            self.ans1 = self.a + self.b - self.c * self.d / self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '*' and self.j == '/' and self.k == '-':
            self.ans1 = self.a + self.b - self.c * self.d / self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '*' and self.j == '/' and self.k == '*':
            self.ans1 = self.a + self.b - self.c * self.d / self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '*' and self.j == '/' and self.k == '/':
            self.ans1 = self.a + self.b - self.c * self.d / (self.e / self.f)
            return self.ans1

            # 01
        elif self.g == '+' and self.h == '-' and self.i == '/' and self.j == '+' and self.k == '+':
            self.ans1 = self.a + self.b - self.c / self.d + self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '/' and self.j == '+' and self.k == '-':
            self.ans1 = self.a + self.b - self.c / self.d + self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '/' and self.j == '+' and self.k == '*':
            self.ans1 = self.a + self.b - self.c / self.d + self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '/' and self.j == '+' and self.k == '/':
            self.ans1 = self.a + self.b - self.c / self.d + self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '-' and self.i == '/' and self.j == '-' and self.k == '+':
            self.ans1 = self.a + self.b - self.c / self.d - self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '/' and self.j == '-' and self.k == '-':
            self.ans1 = self.a + self.b - self.c / self.d - self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '/' and self.j == '-' and self.k == '*':
            self.ans1 = self.a + self.b - self.c / self.d - self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '/' and self.j == '-' and self.k == '/':
            self.ans1 = self.a + self.b - self.c / self.d - self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '-' and self.i == '/' and self.j == '*' and self.k == '+':
            self.ans1 = self.a + self.b - self.c / self.d * self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '/' and self.j == '*' and self.k == '-':
            self.ans1 = self.a + self.b - self.c / self.d * self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '/' and self.j == '*' and self.k == '*':
            self.ans1 = self.a + self.b - self.c / self.d * self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '/' and self.j == '*' and self.k == '/':
            self.ans1 = self.a + self.b - self.c / self.d * self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '-' and self.i == '/' and self.j == '/' and self.k == '+':
            self.ans1 = self.a + self.b - self.c / (self.d / self.e) + self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '/' and self.j == '/' and self.k == '-':
            self.ans1 = self.a * self.b - self.c / (self.d / self.e) - self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '/' and self.j == '/' and self.k == '*':
            self.ans1 = self.a + self.b - self.c / (self.d / self.e) * self.f
            return self.ans1
        elif self.g == '+' and self.h == '-' and self.i == '/' and self.j == '/' and self.k == '/':
            self.ans1 = self.a * self.b - self.c / (self.d / (self.e / self.f))
            return self.ans1


#***********
        elif self.g == '+' and self.h == '*' and self.i == '+' and self.j == '+' and self.k == '+':
            self.ans1 = self.a + self.b * self.c + self.d + self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '+' and self.j == '+' and self.k == '-':
            self.ans1 = self.a + self.b * self.c + self.d + self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '+' and self.j == '+' and self.k == '*':
            self.ans1 = self.a + self.b * self.c + self.d + self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '+' and self.j == '+' and self.k == '/':
            self.ans1 = self.a + self.b * self.c + self.d + self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '*' and self.i == '+' and self.j == '-' and self.k == '+':
            self.ans1 = self.a + self.b * self.c + self.d - self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '+' and self.j == '-' and self.k == '-':
            self.ans1 = self.a + self.b * self.c + self.d - self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '+' and self.j == '-' and self.k == '*':
            self.ans1 = self.a + self.b * self.c + self.d - self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '+' and self.j == '-' and self.k == '/':
            self.ans1 = self.a + self.b * self.c + self.d - self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '*' and self.i == '+' and self.j == '*' and self.k == '+':
            self.ans1 = self.a + self.b * self.c + self.d * self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '+' and self.j == '*' and self.k == '-':
            self.ans1 = self.a + self.b * self.c + self.d * self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '+' and self.j == '*' and self.k == '*':
            self.ans1 = self.a + self.b * self.c + self.d * self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '+' and self.j == '*' and self.k == '/':
            self.ans1 = self.a + self.b * self.c + self.d * self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '*' and self.i == '+' and self.j == '/' and self.k == '+':
            self.ans1 = self.a + self.b * self.c + self.d / self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '+' and self.j == '/' and self.k == '-':
            self.ans1 = self.a + self.b * self.c + self.d / self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '+' and self.j == '/' and self.k == '*':
            self.ans1 = self.a + self.b * self.c + self.d / self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '+' and self.j == '/' and self.k == '/':
            self.ans1 = self.a + self.b * self.c + self.d / (self.e / self.f)
            return self.ans1

        elif self.g == '+' and self.h == '*' and self.i == '-' and self.j == '+' and self.k == '+':
            self.ans1 = self.a + self.b * self.c - self.d + self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '-' and self.j == '+' and self.k == '-':
            self.ans1 = self.a + self.b * self.c - self.d + self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '-' and self.j == '+' and self.k == '*':
            self.ans1 = self.a + self.b * self.c - self.d + self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '-' and self.j == '+' and self.k == '/':
            self.ans1 = self.a + self.b * self.c - self.d + self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '*' and self.i == '-' and self.j == '-' and self.k == '+':
            self.ans1 = self.a + self.b * self.c - self.d - self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '-' and self.j == '-' and self.k == '-':
            self.ans1 = self.a + self.b * self.c - self.d - self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '-' and self.j == '-' and self.k == '*':
            self.ans1 = self.a + self.b * self.c - self.d - self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '-' and self.j == '-' and self.k == '/':
            self.ans1 = self.a + self.b * self.c - self.d - self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '*' and self.i == '-' and self.j == '*' and self.k == '+':
            self.ans1 = self.a + self.b * self.c - self.d * self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '-' and self.j == '*' and self.k == '-':
            self.ans1 = self.a + self.b * self.c - self.d * self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '-' and self.j == '*' and self.k == '*':
            self.ans1 = self.a + self.b * self.c - self.d * self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '-' and self.j == '*' and self.k == '/':
            self.ans1 = self.a + self.b * self.c - self.d * self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '*' and self.i == '-' and self.j == '/' and self.k == '+':
            self.ans1 = self.a + self.b * self.c - self.d / self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '-' and self.j == '/' and self.k == '-':
            self.ans1 = self.a + self.b * self.c - self.d / self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '-' and self.j == '/' and self.k == '*':
            self.ans1 = self.a + self.b * self.c - self.d / self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '-' and self.j == '/' and self.k == '/':
            self.ans1 = self.a + self.b * self.c - self.d / (self.e / self.f)
            return self.ans1



        elif self.g == '+' and self.h == '*' and self.i == '*' and self.j == '+' and self.k == '+':
            self.ans1 = self.a + self.b * self.c * self.d + self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '*' and self.j == '+' and self.k == '-':
            self.ans1 = self.a + self.b * self.c * self.d + self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '*' and self.j == '+' and self.k == '*':
            self.ans1 = self.a + self.b * self.c * self.d + self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '*' and self.j == '+' and self.k == '/':
            self.ans1 = self.a + self.b * self.c * self.d + self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '*' and self.i == '*' and self.j == '-' and self.k == '+':
            self.ans1 = self.a + self.b * self.c * self.d - self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '*' and self.j == '-' and self.k == '-':
            self.ans1 = self.a + self.b * self.c * self.d - self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '*' and self.j == '-' and self.k == '*':
            self.ans1 = self.a + self.b * self.c * self.d - self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '*' and self.j == '-' and self.k == '/':
            self.ans1 = self.a + self.b * self.c * self.d - self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '*' and self.i == '*' and self.j == '*' and self.k == '+':
            self.ans1 = self.a + self.b * self.c * self.d * self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '*' and self.j == '*' and self.k == '-':
            self.ans1 = self.a + self.b * self.c * self.d * self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '*' and self.j == '*' and self.k == '*':
            self.ans1 = self.a + self.b * self.c * self.d * self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '*' and self.j == '*' and self.k == '/':
            self.ans1 = self.a + self.b * self.c * self.d * self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '*' and self.i == '*' and self.j == '/' and self.k == '+':
            self.ans1 = self.a + self.b * self.c * self.d / self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '*' and self.j == '/' and self.k == '-':
            self.ans1 = self.a + self.b * self.c * self.d / self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '*' and self.j == '/' and self.k == '*':
            self.ans1 = self.a + self.b * self.c * self.d / self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '*' and self.j == '/' and self.k == '/':
            self.ans1 = self.a + self.b * self.c * self.d / (self.e / self.f)
            return self.ans1

            # 01
        elif self.g == '+' and self.h == '*' and self.i == '/' and self.j == '+' and self.k == '+':
            self.ans1 = self.a + self.b * self.c / self.d + self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '/' and self.j == '+' and self.k == '-':
            self.ans1 = self.a + self.b * self.c / self.d + self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '/' and self.j == '+' and self.k == '*':
            self.ans1 = self.a + self.b * self.c / self.d + self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '/' and self.j == '+' and self.k == '/':
            self.ans1 = self.a + self.b * self.c / self.d + self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '*' and self.i == '/' and self.j == '-' and self.k == '+':
            self.ans1 = self.a + self.b * self.c / self.d - self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '/' and self.j == '-' and self.k == '-':
            self.ans1 = self.a + self.b * self.c / self.d - self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '/' and self.j == '-' and self.k == '*':
            self.ans1 = self.a + self.b * self.c / self.d - self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '/' and self.j == '-' and self.k == '/':
            self.ans1 = self.a + self.b * self.c / self.d - self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '*' and self.i == '/' and self.j == '*' and self.k == '+':
            self.ans1 = self.a + self.b * self.c / self.d * self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '/' and self.j == '*' and self.k == '-':
            self.ans1 = self.a + self.b * self.c / self.d * self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '/' and self.j == '*' and self.k == '*':
            self.ans1 = self.a + self.b * self.c / self.d * self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '/' and self.j == '*' and self.k == '/':
            self.ans1 = self.a + self.b * self.c / self.d * self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '*' and self.i == '/' and self.j == '/' and self.k == '+':
            self.ans1 = self.a + self.b * self.c / (self.d / self.e) + self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '/' and self.j == '/' and self.k == '-':
            self.ans1 = self.a + self.b * self.c / (self.d / self.e) - self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '/' and self.j == '/' and self.k == '*':
            self.ans1 = self.a + self.b * self.c / (self.d / self.e) * self.f
            return self.ans1
        elif self.g == '+' and self.h == '*' and self.i == '/' and self.j == '/' and self.k == '/':
            self.ans1 = self.a + self.b * self.c / (self.d / (self.e / self.f))
            return self.ans1

        #/////////

        elif self.g == '+' and self.h == '/' and self.i == '+' and self.j == '+' and self.k == '+':
            self.ans1 = self.a + self.b / self.c + self.d + self.e + self.f
            return self.ans1

        elif self.g == '+' and self.h == '/' and self.i == '+' and self.j == '+' and self.k == '-':
            self.ans1 = self.a + self.b / self.c + self.d + self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '+' and self.j == '+' and self.k == '*':
            self.ans1 = self.a + self.b / self.c + self.d + self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '+' and self.j == '+' and self.k == '/':
            self.ans1 = self.a + self.b / self.c + self.d + self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '/' and self.i == '+' and self.j == '-' and self.k == '+':
            self.ans1 = self.a + self.b / self.c + self.d - self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '+' and self.j == '-' and self.k == '-':
            self.ans1 = self.a + self.b / self.c + self.d - self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '+' and self.j == '-' and self.k == '*':
            self.ans1 = self.a + self.b / self.c + self.d - self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '+' and self.j == '-' and self.k == '/':
            self.ans1 = self.a + self.b / self.c + self.d - self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '/' and self.i == '+' and self.j == '*' and self.k == '+':
            self.ans1 = self.a + self.b / self.c + self.d * self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '+' and self.j == '*' and self.k == '-':
            self.ans1 = self.a + self.b / self.c + self.d * self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '+' and self.j == '*' and self.k == '*':
            self.ans1 = self.a + self.b / self.c + self.d * self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '+' and self.j == '*' and self.k == '/':
            self.ans1 = self.a + self.b / self.c + self.d * self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '/' and self.i == '+' and self.j == '/' and self.k == '+':
            self.ans1 = self.a + self.b / self.c + self.d / self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '+' and self.j == '/' and self.k == '-':
            self.ans1 = self.a + self.b / self.c + self.d / self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '+' and self.j == '/' and self.k == '*':
            self.ans1 = self.a + self.b / self.c + self.d / self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '+' and self.j == '/' and self.k == '/':
            self.ans1 = self.a + self.b / self.c + self.d / (self.e / self.f)
            return self.ans1

        elif self.g == '+' and self.h == '/' and self.i == '-' and self.j == '+' and self.k == '+':
            self.ans1 = self.a + self.b / self.c - self.d + self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '-' and self.j == '+' and self.k == '-':
            self.ans1 = self.a + self.b / self.c - self.d + self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '-' and self.j == '+' and self.k == '*':
            self.ans1 = self.a + self.b / self.c - self.d + self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '-' and self.j == '+' and self.k == '/':
            self.ans1 = self.a + self.b / self.c - self.d + self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '/' and self.i == '-' and self.j == '-' and self.k == '+':
            self.ans1 = self.a + self.b / self.c - self.d - self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '-' and self.j == '-' and self.k == '-':
            self.ans1 = self.a + self.b / self.c - self.d - self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '-' and self.j == '-' and self.k == '*':
            self.ans1 = self.a + self.b / self.c - self.d - self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '-' and self.j == '-' and self.k == '/':
            self.ans1 = self.a + self.b / self.c - self.d - self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '/' and self.i == '-' and self.j == '*' and self.k == '+':
            self.ans1 = self.a + self.b / self.c - self.d * self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '-' and self.j == '*' and self.k == '-':
            self.ans1 = self.a + self.b / self.c - self.d * self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '-' and self.j == '*' and self.k == '*':
            self.ans1 = self.a + self.b / self.c - self.d * self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '-' and self.j == '*' and self.k == '/':
            self.ans1 = self.a + self.b / self.c - self.d * self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '/' and self.i == '-' and self.j == '/' and self.k == '+':
            self.ans1 = self.a + self.b / self.c - self.d / self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '-' and self.j == '/' and self.k == '-':
            self.ans1 = self.a + self.b / self.c - self.d / self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '-' and self.j == '/' and self.k == '*':
            self.ans1 = self.a + self.b / self.c - self.d / self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '-' and self.j == '/' and self.k == '/':
            self.ans1 = self.a + self.b / self.c - self.d / (self.e / self.f)
            return self.ans1



        elif self.g == '+' and self.h == '/' and self.i == '*' and self.j == '+' and self.k == '+':
            self.ans1 = self.a + self.b / self.c * self.d + self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '*' and self.j == '+' and self.k == '-':
            self.ans1 = self.a + self.b / self.c * self.d + self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '*' and self.j == '+' and self.k == '*':
            self.ans1 = self.a + self.b / self.c * self.d + self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '*' and self.j == '+' and self.k == '/':
            self.ans1 = self.a + self.b / self.c * self.d + self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '/' and self.i == '*' and self.j == '-' and self.k == '+':
            self.ans1 = self.a + self.b / self.c * self.d - self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '*' and self.j == '-' and self.k == '-':
            self.ans1 = self.a + self.b / self.c * self.d - self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '*' and self.j == '-' and self.k == '*':
            self.ans1 = self.a + self.b / self.c * self.d - self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '*' and self.j == '-' and self.k == '/':
            self.ans1 = self.a + self.b / self.c * self.d - self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '/' and self.i == '*' and self.j == '*' and self.k == '+':
            self.ans1 = self.a + self.b / self.c * self.d * self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '*' and self.j == '*' and self.k == '-':
            self.ans1 = self.a + self.b / self.c * self.d * self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '*' and self.j == '*' and self.k == '*':
            self.ans1 = self.a + self.b / self.c * self.d * self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '*' and self.j == '*' and self.k == '/':
            self.ans1 = self.a + self.b / self.c * self.d * self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '/' and self.i == '*' and self.j == '/' and self.k == '+':
            self.ans1 = self.a + self.b / self.c * self.d / self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '*' and self.j == '/' and self.k == '-':
            self.ans1 = self.a + self.b / self.c * self.d / self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '*' and self.j == '/' and self.k == '*':
            self.ans1 = self.a + self.b / self.c * self.d / self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '*' and self.j == '/' and self.k == '/':
            self.ans1 = self.a + self.b / self.c * self.d / (self.e / self.f)
            return self.ans1

            # 01
        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '+' and self.k == '+':
            self.ans1 = self.a + (self.b / self.c) / self.d + self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '+' and self.k == '-':
            self.ans1 = self.a + (self.b / self.c) / self.d + self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '+' and self.k == '*':
            self.ans1 = self.a + (self.b / self.c) / self.d + self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '+' and self.k == '/':
            self.ans1 = self.a + (self.b / self.c) / self.d + self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '-' and self.k == '+':
            self.ans1 = self.a + self.b / self.c / self.d - self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '-' and self.k == '-':
            self.ans1 = self.a + self.b / self.c / self.d - self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '-' and self.k == '*':
            self.ans1 = self.a + self.b / self.c / self.d - self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '-' and self.k == '/':
            self.ans1 = self.a + self.b / self.c / self.d - self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '*' and self.k == '+':
            self.ans1 = self.a + self.b / self.c / self.d * self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '*' and self.k == '-':
            self.ans1 = self.a + self.b / self.c / self.d * self.e - self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '*' and self.k == '*':
            self.ans1 = self.a + self.b / self.c / self.d * self.e * self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '*' and self.k == '/':
            self.ans1 = self.a + self.b / self.c / self.d * self.e / self.f
            return self.ans1

        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '/' and self.k == '+':
            self.ans1 = self.a + ((self.b / self.c) / self.d )/ self.e + self.f
            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '/' and self.k == '-':
            self.ans1 = self.a + ((self.b / self.c) / self.d) / self.e - self.f

            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '/' and self.k == '*':
            self.ans1 = self.a + ((self.b / self.c) / self.d) / self.e * self.f

            return self.ans1
        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '/' and self.k == '/':
            self.ans1 = self.a + ((self.b / self.c) / self.d )/ (self.e / self.f)
            return self.ans1


    def prin_(self):
        if self.g == '+' and self.h == '+' and self.i == '+' and self.j == '/' and self.k == '/':
            print(f'{m1.a} {m1.g} {m1.b} {m1.h} {m1.c} {m1.i} {m1.d} {m1.j} ({m1.e} {m1.k} {m1.f})')

        elif self.g == '+' and self.h == '+' and self.i == '-' and self.j == '/' and self.k == '/':
            print(f'{m1.a} {m1.g} {m1.b} {m1.h} {m1.c} {m1.i} {m1.d} {m1.j} ({m1.e} {m1.k} {m1.f})')

        elif self.g == '+' and self.h == '+' and self.i == '*' and self.j == '/' and self.k == '/':
            print(f'{m1.a} {m1.g} {m1.b} {m1.h} {m1.c} {m1.i} {m1.d} {m1.j} ({m1.e} {m1.k} {m1.f})')

        elif self.g == '+' and self.h == '+' and self.i == '/' and self.j == '/' and self.k == '+': #237
            print(f'{m1.a} {m1.g} {m1.b} {m1.h} {m1.c} {m1.i} ({m1.d} {m1.j} {m1.e}) {m1.k} {m1.f}')

        elif self.g == '+' and self.h == '+' and self.i == '/' and self.j == '/' and self.k == '-': #240
            print(f'{m1.a} {m1.g} {m1.b} {m1.h} {m1.c} {m1.i} ({m1.d} {m1.j} {m1.e}) {m1.k} {m1.f}')

        elif self.g == '+' and self.h == '+' and self.i == '/' and self.j == '/' and self.k == '*': #243
            print(f'{m1.a} {m1.g} {m1.b} {m1.h} {m1.c} {m1.i} ({m1.d} {m1.j} {m1.e}) {m1.k} {m1.f}')

        elif self.g == '+' and self.h == '+' and self.i == '/' and self.j == '/' and self.k == '/': #246
            print(m1.a,m1.g,m1.b,m1.h,m1.c,m1.i,'{',m1.d,m1.j,'(',m1.e,m1.k,m1.f,')}')

        elif self.g == '+' and self.h == '-' and self.i == '+' and self.j == '/' and self.k == '/': #299
            print(f'{m1.a} {m1.g} {m1.b} {m1.h} {m1.c} {m1.i} {m1.d} {m1.j} ({m1.e} {m1.k} {m1.f})')

        elif self.g == '+' and self.h == '-' and self.i == '-' and self.j == '/' and self.k == '/': #351
            print(f'{m1.a} {m1.g} {m1.b} {m1.h} {m1.c} {m1.i} {m1.d} {m1.j} ({m1.e} {m1.k} {m1.f})')

        elif self.g == '+' and self.h == '-' and self.i == '*' and self.j == '/' and self.k == '/': #405
            print(f'{m1.a} {m1.g} {m1.b} {m1.h} {m1.c} {m1.i} {m1.d} {m1.j} ({m1.e} {m1.k} {m1.f})')

        elif self.g == '+' and self.h == '-' and self.i == '/' and self.j == '/' and self.k == '+': #449
            print(f'{m1.a} {m1.g} {m1.b} {m1.h} {m1.c} {m1.i} ({m1.d} {m1.j} {m1.e}) {m1.k} {m1.f}')

        elif self.g == '+' and self.h == '-' and self.i == '/' and self.j == '/' and self.k == '-':
            print(f'{m1.a} {m1.g} {m1.b} {m1.h} {m1.c} {m1.i} ({m1.d} {m1.j} {m1.e}) {m1.k} {m1.f}') #452

        elif self.g == '+' and self.h == '-' and self.i == '/' and self.j == '/' and self.k == '*': #455
            print(f'{m1.a} {m1.g} {m1.b} {m1.h} {m1.c} {m1.i} ({m1.d} {m1.j} {m1.e}) {m1.k} {m1.f}')

        elif self.g == '+' and self.h == '-' and self.i == '/' and self.j == '/' and self.k == '/': #458
            print(m1.a,m1.g,m1.b,m1.h,'[',m1.c,m1.i,'{',m1.d,m1.j,'(',m1.e,m1.k,m1.f,')}]')

        elif self.g == '+' and self.h == '*' and self.i == '+' and self.j == '/' and self.k == '/': #512
            print(f'{m1.a} {m1.g} {m1.b} {m1.h} {m1.c} {m1.i} {m1.d} {m1.j} ({m1.e} {m1.k} {m1.f})')

        elif self.g == '+' and self.h == '*' and self.i == '-' and self.j == '/' and self.k == '/': #564
            print(f'{m1.a} {m1.g} {m1.b} {m1.h} {m1.c} {m1.i} {m1.d} {m1.j} ({m1.e} {m1.k} {m1.f})')

        elif self.g == '+' and self.h == '*' and self.i == '*' and self.j == '/' and self.k == '/':#618
            print(f'{m1.a} {m1.g} {m1.b} {m1.h} {m1.c} {m1.i} {m1.d} {m1.j} ({m1.e} {m1.k} {m1.f})')

        elif self.g == '+' and self.h == '*' and self.i == '/' and self.j == '/' and self.k == '+':#662
            print(f'{m1.a} {m1.g} {m1.b} {m1.h} {m1.c} {m1.i} ({m1.d} {m1.j} {m1.e}) {m1.k} {m1.f}')

        elif self.g == '+' and self.h == '*' and self.i == '/' and self.j == '/' and self.k == '-':#665
            print(f'{m1.a} {m1.g} {m1.b} {m1.h} {m1.c} {m1.i} ({m1.d} {m1.j} {m1.e}) {m1.k} {m1.f}')

        elif self.g == '+' and self.h == '*' and self.i == '/' and self.j == '/' and self.k == '*':#668
            print(f'{m1.a} {m1.g} {m1.b} {m1.h} {m1.c} {m1.i} ({m1.d} {m1.j} {m1.e}) {m1.k} {m1.f}')

        elif self.g == '+' and self.h == '*' and self.i == '/' and self.j == '/' and self.k == '/': #671
            print(m1.a,m1.g,m1.b,m1.h,'[',m1.c,m1.i,'{',m1.d,m1.j,'(',m1.e,m1.k,m1.f,')}]')

        elif self.g == '+' and self.h == '/' and self.i == '+' and self.j == '/' and self.k == '/': #725
            print(f'{m1.a} {m1.g} {m1.b} {m1.h} {m1.c} {m1.i} {m1.d} {m1.j} ({m1.e} {m1.k} {m1.f})')

        elif self.g == '+' and self.h == '/' and self.i == '-' and self.j == '/' and self.k == '/':#777
            print(f'{m1.a} {m1.g} {m1.b} {m1.h} {m1.c} {m1.i} {m1.d} {m1.j} ({m1.e} {m1.k} {m1.f})')

        elif self.g == '+' and self.h == '/' and self.i == '*' and self.j == '/' and self.k == '/': #831
            print(f'{m1.a} {m1.g} {m1.b} {m1.h} {m1.c} {m1.i} {m1.d} {m1.j} ({m1.e} {m1.k} {m1.f})')

        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '+' and self.k == '+': #836
            print(f'{m1.a} {m1.g} ({m1.b} {m1.h} {m1.c}) {m1.i} {m1.d} {m1.j} {m1.e} {m1.k} {m1.f}')

        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '+' and self.k == '-': #839
            print(f'{m1.a} {m1.g} ({m1.b} {m1.h} {m1.c}) {m1.i} {m1.d} {m1.j} {m1.e} {m1.k} {m1.f}')

        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '+' and self.k == '*': #842
            print(f'{m1.a} {m1.g} ({m1.b} {m1.h} {m1.c}) {m1.i} {m1.d} {m1.j} {m1.e} {m1.k} {m1.f}')

        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '+' and self.k == '/': #845
            print(f'{m1.a} {m1.g} ({m1.b} {m1.h} {m1.c}) {m1.i} {m1.d} {m1.j} {m1.e} {m1.k} {m1.f}')

        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '-' and self.k == '+': #849
            print(f'{m1.a} {m1.g} ({m1.b} {m1.h} {m1.c}) {m1.i} {m1.d} {m1.j} {m1.e} {m1.k} {m1.f}')

        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '-' and self.k == '-': #852
            print(f'{m1.a} {m1.g} ({m1.b} {m1.h} {m1.c}) {m1.i} {m1.d} {m1.j} {m1.e} {m1.k} {m1.f}')

        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '-' and self.k == '*': #855
            print(f'{m1.a} {m1.g} ({m1.b} {m1.h} {m1.c}) {m1.i} {m1.d} {m1.j} {m1.e} {m1.k} {m1.f}')

        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '-' and self.k == '/': #858
            print(f'{m1.a} {m1.g} ({m1.b} {m1.h} {m1.c}) {m1.i} {m1.d} {m1.j} {m1.e} {m1.k} {m1.f}')

        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '*' and self.k == '+': #862
            print(f'{m1.a} {m1.g} ({m1.b} {m1.h} {m1.c}) {m1.i} {m1.d} {m1.j} {m1.e} {m1.k} {m1.f}')

        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '*' and self.k == '-': #865
            print(f'{m1.a} {m1.g} ({m1.b} {m1.h} {m1.c}) {m1.i} {m1.d} {m1.j} {m1.e} {m1.k} {m1.f}')

        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '*' and self.k == '*': #868
            print(f'{m1.a} {m1.g} ({m1.b} {m1.h} {m1.c}) {m1.i} {m1.d} {m1.j} {m1.e} {m1.k} {m1.f}')

        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '*' and self.k == '/': #872
            print(f'{m1.a} {m1.g} ({m1.b} {m1.h} {m1.c}) {m1.i} {m1.d} {m1.j} {m1.e} {m1.k} {m1.f}')

        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '/' and self.k == '+': #875
            print(m1.a,m1.g,'{(',m1.b,m1.h,m1.c,')',m1.i,m1.d,'}',m1.j,m1.e,m1.k,m1.f)

        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '/' and self.k == '-': #878
            print(m1.a, m1.g, '{(', m1.b, m1.h, m1.c, ')', m1.i, m1.d, '}', m1.j, m1.e, m1.k, m1.f)

        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '/' and self.k == '*': #882
            print(m1.a, m1.g, '{(', m1.b, m1.h, m1.c, ')', m1.i, m1.d, '}', m1.j, m1.e, m1.k, m1.f)

        elif self.g == '+' and self.h == '/' and self.i == '/' and self.j == '/' and self.k == '/': #887
            print(m1.a, m1.g, '{(',m1.b, m1.h, m1.c,')', m1.i, m1.d,'}',  m1.j,'(' ,m1.e, m1.k, m1.f,')')


        else:print(f'{m1.a} {m1.g} {m1.b} {m1.h} {m1.c} {m1.i} {m1.d} {m1.j} {m1.e} {m1.k} {m1.f}')




while True:
    input()
    m1 = math()
    m1.ran_()
    m1.mat_()
    m1.ans_()
    m1.prin_()

    print(m1.g, m1.h, m1.i, m1.j, m1.k)
    print(m1.ans1)








