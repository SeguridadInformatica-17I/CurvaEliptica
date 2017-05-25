#!/usr/bin/env python3

import collections
import random

EllipticCurve = collections.namedtuple('EllipticCurve', 'name p a b g n h')

curve = EllipticCurve(
    'secp256k1',

    p=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f,

    a=0,
    b=7,

    g=(0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
       0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8),

    n=0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141,

    h=1,
)




def inverse_mod(k, p):

    if k == 0:
        raise ZeroDivisionError('division by zero')

    if k < 0:

        return p - inverse_mod(-k, p)


    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = p, k

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    gcd, x, y = old_r, old_s, old_t

    assert gcd == 1
    assert (k * x) % p == 1

    return x % p




def is_on_curve(point):

    if point is None:

        return True

    x, y = point

    return (y * y - x * x * x - curve.a * x - curve.b) % curve.p == 0


def point_neg(point):

    assert is_on_curve(point)

    if point is None:

        return None

    x, y = point
    result = (x, -y % curve.p)

    assert is_on_curve(result)

    return result


def point_add(point1, point2):

    assert is_on_curve(point1)
    assert is_on_curve(point2)

    if point1 is None:

        return point2
    if point2 is None:

        return point1

    x1, y1 = point1
    x2, y2 = point2

    if x1 == x2 and y1 != y2:

        return None

    if x1 == x2:

        m = (3 * x1 * x1 + curve.a) * inverse_mod(2 * y1, curve.p)
    else:

        m = (y1 - y2) * inverse_mod(x1 - x2, curve.p)

    x3 = m * m - x1 - x2
    y3 = y1 + m * (x3 - x1)
    result = (x3 % curve.p,
              -y3 % curve.p)

    assert is_on_curve(result)

    return result


def scalar_mult(k, point):

    assert is_on_curve(point)

    if k % curve.n == 0 or point is None:
        return None

    if k < 0:

        return scalar_mult(-k, point_neg(point))

    result = None
    addend = point

    while k:
        if k & 1:
            result = point_add(result, addend)

        addend = point_add(addend, addend)

        k >>= 1

    assert is_on_curve(result)

    return result




def make_keypair():

    private_key = random.randrange(1, curve.n)
    public_key = scalar_mult(private_key, curve.g)

    return private_key, public_key


print('Curve:', curve.name)


alice_private_key, alice_public_key = make_keypair()
print("Alice private key:", hex(alice_private_key))
print("Alice public key: (0x{:x}, 0x{:x})".format(*alice_public_key))

a_private = hex(alice_private_key)
a_public = hex(alice_public_key[0])

bob_private_key, bob_public_key = make_keypair()
print("Bob private key:", hex(bob_private_key))
print("Bob public key: (0x{:x}, 0x{:x})".format(*bob_public_key))


s1 = scalar_mult(alice_private_key, bob_public_key)
s2 = scalar_mult(bob_private_key, alice_public_key)
assert s1 == s2

b_private = hex(bob_private_key)
b_public = hex(bob_public_key[0])
print('Clae: (0x{:x}, 0x{:x})'.format(*s1))

k = hex(s1[0])
k = k[2:]
mensaje = 'Mama ooh Didnt mean to make you cry If Im not back again this time tomorrow Carry on carry on as if nothing really matters'

encriptado = ''
desencriptado = ''
for i in range(len(mensaje)):
    u = ord(mensaje[i]) ^ int(k[i%len(k)],16)
    u = hex(u)[2:] if(u > 15) else '0' + hex(u)[2:]
    encriptado = encriptado + u
print(encriptado)

for i in range(len(mensaje)):
    u = int(encriptado[2*i:2*(i+1)],16)^int(k[i%len(k)],16)
    desencriptado = desencriptado + chr(u)
print(desencriptado)
## Desencriptar






from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E,Text
from tkinter.font import Font
class Calculator:

    def __init__(self, master):
        self.men = ''
        self.encriptado = ''
        self.desencriptado = ''
        self.master = master
        master.title("Criptografia eliptica")
        self.myFont = Font(family="Times New Roman", size=14)


        self.total = 0
        self.entered_number = 0

        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)

        # self.label = Label(master, text="Total:")

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.add_button = Button(master, text="Encriptar", command=lambda: self.update("encriptar"))
        self.subtract_button = Button(master, text="Desencriptar", command=lambda: self.update("desencriptar"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

        self.t = Text(root, height=4, width=50)
        self.t2 = Text(root, height=4, width=50)
        self.t.configure(font=self.myFont)
        self.t2.configure(font=self.myFont)
        # LAYOUT

        self.add_button.grid(row=2, column=0)
        self.subtract_button.grid(row=2, column=1)
        self.reset_button.grid(row=2, column=2, sticky=W+E)
        self.t.grid(row=4,columnspan=10)
        self.t2.grid(row=5,columnspan=10)

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "encriptar":
            self.encriptado = ''
            self.men = self.t.get("1.0",END)
            self.men = self.men[:122]
            print(len(self.men))
            for i in range(len(self.men)):
                u = ord(self.men[i]) ^ int(k[i%len(k)],16)
                u = hex(u)[2:] if(u > 15) else '0' + hex(u)[2:]
                self.encriptado = self.encriptado + u
            print(self.encriptado) 
            self.t2.delete(1.0,END)
            self.t2.insert(END,self.encriptado)          
        elif method == "desencriptar":
            self.desencriptado = ''
            self.encriptado = self.t2.get("1.0",END)
            print('----------------------------')
            print(self.encriptado)
            self.men = self.t.get("1.0",END)
            for i in range(len(self.men)):
                u = int(self.encriptado[2*i:2*(i+1)],16)^int(k[i%len(k)],16)
                self.desencriptado = self.desencriptado + chr(u)
            print(self.desencriptado)
            self.t2.delete(1.0,END)
            self.t2.insert(END,self.desencriptado)
        else: # reset
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, END)

root = Tk()
my_gui = Calculator(root)
root.geometry("520x300")

root.mainloop()
