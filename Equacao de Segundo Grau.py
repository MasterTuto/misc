import Tkinter
import math

janela = Tkinter.Tk()

a = Tkinter.Entry(janela)
a.grid(row=1, column=2)
b = Tkinter.Entry(janela)
b.grid(row=2, column=2)
c = Tkinter.Entry(janela)
c.grid(row=3, column=2)
Tkinter.Label(janela, text='Resultado: ').grid(row=5, column=2)

def somar(a, b, c):
        delta = (b**2) - (4*a*c)
        if delta >= 0:
                resultado1 = ((0-b) + math.sqrt(delta)) / (2*a)
                resultado2 = ((0-b) - math.sqrt(delta)) / (2*a)
                resultado_final = "x' = %s / x'' = %s" % (resultado1, resultado2)
                label_resultado.configure(text=resultado_final)
        else:
                label_resultado.configure(text='Delta eh negativo, sua raiz eh inexistente em R.')
                # delta = delta * -1
                # resultado1 = ((0-b) + str(math.sqrt(delta)) / (2*a)*-1
                # resultado2 = ((0-b) - math.sqrt(delta))) / (2*a)*-1
                # print 'x\' = %si\nx\'\' = %si' % (resultado1, resultado2)


def chamarFuncao():
	a_value = int(a.get())
	b_value = int(b.get())
	c_value = int(c.get())
	somar(a_value, b_value, c_value)

Tkinter.Label(janela, text="A: ").grid(row=1, column=1)
Tkinter.Label(janela, text="B: ").grid(row=2, column=1)
Tkinter.Label(janela, text="C: ").grid(row=3, column=1)
Tkinter.Button(janela, text='Ver resultado', command=chamarFuncao).grid(row=4, column=2)
label_resultado = Tkinter.Label(janela)
label_resultado.grid(row=5, column=3)

janela.mainloop()
