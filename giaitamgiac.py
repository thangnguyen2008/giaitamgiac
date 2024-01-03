print("Cạnh Cạnh Cạnh = 1")
print("Cạnh Góc Cạnh = 2")
print("Cạnh Góc Cạnh đối diện góc = 3")
print("Góc cạnh góc = 4")
print("Góc Cạnh Góc đối diện cạnh = 5")
q = int(input("Nhập cách giải tam giác theo: "))
while q <= 0 or q > 5:
    print("Lỗi")
    q = int(input("Nhập lại"))
    if q > 0 and q < 6:
        break
if q == 1:
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))
    while a <= 0 or b <= 0 or c <= 0 or a >= b + c or b >= a + c or c >= a + b:
        print("Lỗi")
        a = float(input("Nhập lại a: "))
        b = float(input("Nhập lại b: "))
        c = float(input("Nhập lại c: "))
        if a <= 0 and b <= 0 and c <= 0 and a <= b + c and b <= a + c and c <= a + b:
            break
    from math import *
    A = acos((b**2+c**2-a**2)/(2*b*c))
    B = acos((a**2+c**2-b**2)/(2*a*c))
    A = A/pi*180
    B = B/pi*180
    C = 180 - A - B
    print("3 góc của tam giác lần lượt là:",round(A,2),round(B,2),round(C,2))
if q == 2:
    print("A=1")
    print("B=2")
    print("C=3")
    w = int(input("Nhập góc xen giữa 2 cạnh: "))
    while w <= 0 or w > 3:
        print("Lỗi")
        w = int(input("Nhập lại: "))
        if w > 0 and w <= 3:
            break
    if w == 1:
        A = float(input("Nhập góc A: "))
        while A <= 0 or A >= 180:
            print("Lỗi")
            A = float(input("Nhập lại: "))
            if A > 0 and A < 180:
                break
        b = float(input("Nhập cạnh b: "))
        while b <= 0:
            print("Lỗi")
            b = float(input("Nhập lại: "))
            if b > 0:
                break
        c = float(input("Nhập cạnh c: "))
        while c <= 0:
            print("Lỗi")
            c = float(input("Nhập lại: "))
            if c > 0:
                break
        from math import *
        a = sqrt(b**2+c**2-2*b*c*cos(A/180*pi))
        B = asin(b*sin(A/180*pi)/a)
        B = B/pi*180
        C = 180 - A -B
        print("Cạnh a là:",round(a,2))
        print("Góc B là: ",round(B,2))
        print("Góc C là: ",round(C,2))
    if w == 2:
        B = float(input("Nhập góc B: "))
        while B <= 0 or B >= 180:
            print("Lỗi")
            B = float(input("Nhập lại: "))
            if B > 0 and B < 180:
                break
        a = float(input("Nhập cạnh a: "))
        while a <= 0:
            print("Lỗi")
            a = float(input("Nhập lại: "))
            if a > 0:
                break
        c = float(input("Nhập cạnh c: "))
        while c <= 0:
            print("Lỗi")
            c = float(input("Nhập lại: "))
            if c > 0:
                break
        from math import *
        b = sqrt(a**2+c**2-2*a*c*cos(B/180*pi))
        A = asin(a*sin(B/180*pi)/b)
        A = A/pi*180
        C = 180 - A - B
        print("Cạnh b là:",round(b,2))
        print("Góc A là:",round(A,2))
        print("Góc C là:",round(C,2))
    if w == 3:
        C = float(input("Nhập góc C: "))
        while C <= 0 or C >= 180:
            print("Lỗi")
            C = float(input("Nhập lại: "))
            if C > 0 and C < 180:
                break
        a = float(input("Nhập cạnh a: "))
        while a <= 0:
            print("Lỗi")
            a = float(input("Nhập lại: "))
            if a > 0:
                break
        b = float(input("Nhập cạnh c: "))
        while b <= 0:
            print("Lỗi")
            b = float(input("Nhập lại: "))
            if b > 0:
                break
        from math import *
        c = sqrt(a**2+b**2-2*a*b*cos(C/180*pi))
        A = asin(a*sin(C/180*pi)/c)
        A = A/pi*180
        B = 180 - A - C
        print("Cạnh c là:",round(c,2))
        print("Góc A là:",round(A,2))
        print("Góc B là:",round(B,2))
if q == 3:
    print("A=1")
    print("B=2")
    print("C=3")
    e = int(input("Nhập góc cho trước: "))
    while e <= 0 or e > 3:
        print("Lỗi")
        e = int(input("Nhập lại: "))
        if e > 0 and e <= 3:
            break
    if e == 1:
        print("Cạnh a c = 1")
        print("Cạnh a b = 2")
        r = int(input("Giải theo hai cạnh: "))
        while r <= 0 or r > 2:
            print("Lỗi")
            r = int("Nhập lại: ")
            if r > 0 and r <= 2:
                break
        if r == 1:
            A = float(input("Nhập góc A: "))
            while A <= 0 or A >= 180:
                print("Lỗi")
                A = float(input("Nhập lại: "))
                if A > 0 and A < 180:
                    break
            a = float(input("Nhập cạnh a: "))
            while a <= 0:
                print("Lỗi")
                a = float(input("Nhập lại: "))
                if a > 0:
                    break
            c = float(input("Nhập cạnh c: "))
            while c <= 0 or c >= 180:
                print("Lỗi")
                A = float(input("Nhập lại: "))
                if c > 0 and c < 180:
                    break
            from math import *
            C = asin(c*sin(A/180*pi)/a)
            C = C/pi*180
            B = 180 - A - C
            b = sqrt(a**2+c**2-2*a*c*cos(B/180*pi))
            print("Góc C là:",round(C,2))
            print("Góc B là:",round(B,2))
            print("Cạnh b là:",round(b,2))
        if r == 2:
            A = float(input("Nhập góc A: "))
            while A <= 0 or A >= 180:
                print("Lỗi")
                A = float(input("Nhập lại: "))
                if A > 0 and A < 180:
                    break
            a = float(input("Nhập cạnh a: "))
            while a <= 0:
                print("Lỗi")
                a = float(input("Nhập lại: "))
                if a > 0:
                    break
            b = float(input("Nhập cạnh c: "))
            while b <= 0:
                print("Lỗi")
                b = float(input("Nhập lại: "))
                if b > 0:
                    break
            from math import *
            B = asin(b*sin(A/180*pi)/a)
            B = B/pi*180
            C = 180 - A - B
            c = sqrt(a**2+b**2-2*a*b*cos(C/180*pi))
            print("Góc B là:",round(B,2))
            print("Góc C là:",round(C,2))
            print("Cạnh c là:",round(c,2))
    if e == 2:
        print("Cạnh a b = 1")
        print("Cạnh c b = 2")
        t = int(input("Giải theo hai cạnh: "))
        while t <= 0 or t > 2:
            print("Lỗi")
            t = int("Nhập lại: ")
            if t > 0 and t <= 2:
                break
        if t == 1:
            B = float(input("Nhập góc B: "))
            while B <= 0 or B >= 180:
                print("Lỗi")
                B = float(input("Nhập lại: "))
                if B > 0 and B < 180:
                    break
            a = float(input("Nhập cạnh a: "))
            while a <= 0:
                print("Lỗi")
                a = float(input("Nhập lại: "))
                if a > 0:
                    break
            b = float(input("Nhập cạnh b: "))
            while b <= 0 or b >= 180:
                print("Lỗi")
                b = float(input("Nhập lại: "))
                if b > 0 and b < 180:
                    break
            from math import *
            A = asin(a*sin(B/180*pi)/b)
            A = A/pi*180
            C = 180 - A - B
            c = sqrt(a**2+b**2-2*a*b*cos(C/180*pi))
            print("Góc A là:",round(A,2))
            print("Góc C là:",round(C,2))
            print("Cạnh c là:",round(c,2))
        if t == 2:
            B = float(input("Nhập góc B: "))
            while B <= 0 or B >= 180:
                print("Lỗi")
                B = float(input("Nhập lại: "))
                if B > 0 and B < 180:
                    break
            c = float(input("Nhập cạnh c: "))
            while c <= 0:
                print("Lỗi")
                c = float(input("Nhập lại: "))
                if c > 0:
                    break
            b = float(input("Nhập cạnh b: "))
            while b <= 0:
                print("Lỗi")
                b = float(input("Nhập lại: "))
                if b > 0:
                    break
            from math import *
            C = asin(c*sin(B/180*pi)/b)
            C = C/pi*180
            A = 180 - C - B
            a = sqrt(b**2+c**2-2*b*c*cos(B/180*pi))
            print("Góc C là:",round(C,2))
            print("Góc A là:",round(A,2))
            print("Cạnh b là:",round(a,2))
    if e == 3:
        print("Cạnh b c = 1")
        print("Cạnh a c = 2")
        y = int(input("Giải theo hai cạnh: "))
        while y <= 0 or y > 2:
            print("Lỗi")
            y = int(input("Nhập lại: "))
            if y > 0 and y <= 2:
                break
        if y == 1:
            C = float(input("Nhập góc C: "))
            while C <= 0 or C >= 180:
                print("Lỗi")
                C = float(input("Nhập lại: "))
                if C > 0 and C < 180:
                    break
            b = float(input("Nhập cạnh b: "))
            while b <= 0:
                print("Lỗi")
                b = float(input("Nhập lại: "))
                if b > 0:
                    break
            c = float(input("Nhập cạnh c: "))
            while c <= 0:
                print("Lỗi")
                c = float(input("Nhập lại: "))
                if c > 0:
                    break
            from math import *
            B = asin(b*sin(C/180*pi)/c)
            B = B/pi*180
            A = 180 - C - B
            a = sqrt(c**2+b**2-2*c*b*cos(A/180*pi))
            print("Góc B là:",round(B,2))
            print("Góc A là:",round(A,2))
            print("Cạnh a là:",round(a,2))
        if y == 2:
            C = float(input("Nhập góc C: "))
            while C <= 0 or C >= 180:
                print("Lỗi")
                C = float(input("Nhập lại: "))
                if C > 0 and C < 180:
                    break
            a = float(input("Nhập cạnh a: "))
            while a <= 0:
                print("Lỗi")
                a = float(input("Nhập lại: "))
                if a > 0:
                    break
            c = float(input("Nhập cạnh c: "))
            while c <= 0:
                print("Lỗi")
                c = float(input("Nhập lại: "))
                if c > 0:
                    break
            from math import *
            A = asin(a*sin(C/180*pi)/c)
            A = A/pi*180
            B = 180 - C - A
            b = sqrt(a**2+c**2-2*a*c*cos(B/180*pi))
            print("Góc A là:",round(A,2))
            print("Góc B là:",round(B,2))
            print("Cạnh a là:",round(a,2))
if q == 4:
    print("a=1")
    print("b=2")
    print("c=3")
    u = int(input("Nhập cạnh xen giữa hai góc: "))
    while u < 1 or u > 3:
        print("Lỗi")
        u = int(input("Nhập lại: "))
        if u > 0 and u < 4:
            break
    if u == 1:
        a = float(input("Nhập cạnh a: "))
        while a <= 0:
            print("Lỗi")
            a = float(input("Nhập lại: "))
            if a > 0:
                break
        B = float(input("Nhập góc B: "))
        while B <= 0 or B > 180:
            print("Lỗi")
            B = float(input("Nhập lại: "))
            if B > 0 and B < 180:
                break
        C = float(input("Nhập góc C: "))
        while C <= 0 or C > 180:
            print("Lỗi")
            C = float(input("Nhập lại: "))
            if C > 0 and C < 180:
                break
        A = 180 - B - C
        from math import *
        b = a*sin(B/180*pi)/sin(A/180*pi)
        c = a*sin(C/180*pi)/sin(A/180*pi)
        print("Góc A là: ",round(A,2))
        print("Góc b là: ",round(b,2))
        print("Góc c là: ",round(c,2))
    if u == 2:
        b = float(input("Nhập cạnh b: "))
        while b <= 0:
            print("Lỗi")
            b = float(input("Nhập lại: "))
            if b > 0:
                break
        A = float(input("Nhập góc A: "))
        while A <= 0 or A > 180:
            print("Lỗi")
            A = float(input("Nhập lại: "))
            if A > 0 and A < 180:
                break
        C = float(input("Nhập góc C: "))
        while C <= 0 or C > 180:
            print("Lỗi")
            C = float(input("Nhập lại: "))
            if C > 0 and C < 180:
                break
        B = 180 - A - C
        from math import *
        a = b*sin(A/180*pi)/sin(B/180*pi)
        c = b*sin(C/180*pi)/sin(B/180*pi)
        print("Góc B là:",round(B,2))
        print("Góc a là:",round(a,2))
        print("Góc c là:",round(c,2))
    if u == 3:
        c = float(input("Nhập cạnh c: "))
        while c <= 0:
            print("Lỗi")
            c = float(input("Nhập lại: "))
            if c > 0:
                break
        A = float(input("Nhập góc A: "))
        while A <= 0 or A > 180:
            print("Lỗi")
            A = float(input("Nhập lại: "))
            if A > 0 and A < 180:
                break
        B = float(input("Nhập góc B: "))
        while B <= 0 or B > 180:
            print("Lỗi")
            B = float(input("Nhập lại: "))
            if B > 0 and B < 180:
                break
        C = 180 - A - B
        from math import *
        a = c*sin(A/180*pi)/sin(C/180*pi)
        b = c*sin(B/180*pi)/sin(C/180*pi)
        print("Góc C là:",round(C,2))
        print("Góc a là:",round(a,2))
        print("Góc b là:",round(b,2))
if q ==5:
    print("a=1")
    print("b=2")
    print("b=3")
    i = int(input("Nhập kiểu cạnh cho trước: "))
    while i < 1 or i > 3:
        print("Lỗi")
        i = int(input("Nhập lại: "))
        if i > 0 and i < 4:
            break
    if i == 1:
        print("Góc A,B = 1")
        print("Góc A,C = 2")
        o = int(input("NHập hai góc nho trước: "))
        while o < 1 or o > 2:
            print("Lỗi")
            o = int(input("Nhập lại: "))
            if o > 0 or o < 3:
                break
        if o == 1:
            a = float(input("Nhập cạnh a: "))
            while a <= 0:
                print("Lôi")
                a = float(input("Nhập lại:"))
                if a > 0:
                    break
            A = float(input("Nhập góc A: "))
            while A <= 0 or A >= 180:
                print("Lỗi")
                A = float(input("Nhập lại: "))
                if A > 0 or A < 180:
                    break
            B = float(input("Nhập góc B: "))
            while B <= 0 or B >= 180:
                print("Lỗi")
                B = float(input("Nhập lại: "))
                if B > 0 or B < 180:
                    break
            C = 180 - A - B
            from math import *
            b = a*sin(B/180*pi)/sin(A/180*pi)
            c = a*sin(C/180*pi)/sin(A/180*pi)
            print("Góc C là:",round(C,2))
            print("Cạnh b là:",round(b,2))
            print("Cạnh C là:",round(c,2))
        if o == 2:
            a = float(input("Nhập cạnh a: "))
            while a <= 0:
                print("Lôi")
                a = float(input("Nhập lại:"))
                if a > 0:
                    break
            A = float(input("Nhập góc A: "))
            while A <= 0 or A >= 180:
                print("Lỗi")
                A = float(input("Nhập lại: "))
                if A > 0 or A < 180:
                    break
            C = float(input("Nhập góc B: "))
            while C <= 0 or C >= 180:
                print("Lỗi")
                C = float(input("Nhập lại: "))
                if C > 0 or C < 180:
                    break
            B = 180 - A - C
            from math import *
            c = a*sin(C/180*pi)/sin(A/180*pi)
            b = a*sin(B/180*pi)/sin(A/180*pi)
            print("Góc B là:",round(B,2))
            print("Cạnh c là:",round(c,2))
            print("Cạnh b là:",round(b,2))
    if i == 2:
        print("Góc A,B = 1")
        print("Góc B,C = 2")
        o = int(input("NHập hai góc nho trước: "))
        while o < 1 or o > 2:
            print("Lỗi")
            o = int(input("Nhập lại: "))
            if o > 0 or o < 3:
                break
        if o == 1:
            b = float(input("Nhập cạnh b: "))
            while b <= 0:
                print("Lôi")
                b = float(input("Nhập lại:"))
                if b > 0:
                    break
            A = float(input("Nhập góc A: "))
            while A <= 0 or A >= 180:
                print("Lỗi")
                A = float(input("Nhập lại: "))
                if A > 0 or A < 180:
                    break
            B = float(input("Nhập góc B: "))
            while B <= 0 or B >= 180:
                print("Lỗi")
                B = float(input("Nhập lại: "))
                if B > 0 or B < 180:
                    break
            C = 180 - A - B
            from math import *
            a = b*sin(A/180*pi)/sin(B/180*pi)
            c = a*sin(C/180*pi)/sin(B/180*pi)
            print("Góc C là:",round(C,2))
            print("Cạnh a là:",round(a,2))
            print("Cạnh C là:",round(c,2))
        if o == 2:
            b = float(input("Nhập cạnh b: "))
            while b <= 0:
                print("Lôi")
                b = float(input("Nhập lại:"))
                if b > 0:
                    break
            B = float(input("Nhập góc B: "))
            while B <= 0 or B >= 180:
                print("Lỗi")
                B = float(input("Nhập lại: "))
                if B > 0 or B < 180:
                    break
            C = float(input("Nhập góc B: "))
            while C <= 0 or C >= 180:
                print("Lỗi")
                C = float(input("Nhập lại: "))
                if C > 0 or C < 180:
                    break
            A = 180 - B - C
            from math import *
            a = b*sin(A/180*pi)/sin(B/180*pi)
            c = b*sin(C/180*pi)/sin(B/180*pi)
            print("Góc A là:",round(A,2))
            print("Cạnh a là:",round(a,2))
            print("Cạnh c là:",round(c,2))
    if i == 3:
        print("Góc A,C = 1")
        print("Góc B,C = 2")
        p = int(input("NHập hai góc nho trước: "))
        while p < 1 or p > 2:
            print("Lỗi")
            p = int(input("Nhập lại: "))
            if p > 0 or p < 3:
                break
        if p == 1:
            c = float(input("Nhập cạnh c: "))
            while c <= 0:
                print("Lôi")
                c = float(input("Nhập lại:"))
                if c > 0:
                    break
            A = float(input("Nhập góc A: "))
            while A <= 0 or A >= 180:
                print("Lỗi")
                A = float(input("Nhập lại: "))
                if A > 0 or A < 180:
                    break
            C = float(input("Nhập góc C: "))
            while C <= 0 or C >= 180:
                print("Lỗi")
                C = float(input("Nhập lại: "))
                if C > 0 or C < 180:
                    break
            B = 180 - A - C
            from math import *
            a = c*sin(A/180*pi)/sin(C/180*pi)
            b = c*sin(B/180*pi)/sin(C/180*pi)
            print("Góc B là:",round(B,2))
            print("Cạnh a là:",round(a,2))
            print("Cạnh b là:",round(b,2))
        if p == 2:
            c = float(input("Nhập cạnh c: "))
            while c <= 0:
                print("Lôi")
                c = float(input("Nhập lại:"))
                if c > 0:
                    break
            B = float(input("Nhập góc B: "))
            while B <= 0 or B >= 180:
                print("Lỗi")
                B = float(input("Nhập lại: "))
                if B > 0 or B < 180:
                    break
            C = float(input("Nhập góc C: "))
            while C <= 0 or C >= 180:
                print("Lỗi")
                C = float(input("Nhập lại: "))
                if C > 0 or C < 180:
                    break
            A = 180 - B - C
            from math import *
            a = c*sin(A/180*pi)/sin(C/180*pi)
            b = c*sin(B/180*pi)/sin(C/180*pi)
            print("Góc A là:",round(A,2))
            print("Cạnh a là:",round(a,2))
            print("Cạnh b là:",round(b,2))