import wx

class Calculadora(wx.Frame):
	"""docstring for Calculadora"""

	def __init__(self):
		wx.Frame.__init__(self, parent=None, title="Minha Calculadora", pos=(30,30))
		self.valor = 0
		self.operacao = ''

		sizerPrincipal = wx.BoxSizer(wx.VERTICAL)

		self.resultado = wx.StaticText(self, size=(-1, 20))

		botao1 = wx.Button(self, label="1")
		botao2 = wx.Button(self, label="2")
		botao3 = wx.Button(self, label="3")
		botao4 = wx.Button(self, label="4")
		botao5 = wx.Button(self, label="5")
		botao6 = wx.Button(self, label="6")
		botao7 = wx.Button(self, label="7")
		botao8 = wx.Button(self, label="8")
		botao9 = wx.Button(self, label="9")

		self.resultado.Bind(wx.EVT_KEY_DOWN, self.numero_digitado)

		botaoMais = wx.Button(self, label="+")
		botaoMenos = wx.Button(self, label="-")
		botaoDividir = wx.Button(self, label="/")
		botaoMultiplicar = wx.Button(self, label="*")

		botaoIgual = wx.Button(self, label="=")

		botaoLimpar = wx.Button(self, label="LIMPAR")

		botoes = [[botao1, botao2, botao3, botaoMais],
			      [botao4, botao5, botao6, botaoMenos],
			      [botao7, botao8, botao9, botaoDividir],
			      [botaoIgual, botaoLimpar, botaoMultiplicar]]


		sizerPrincipal.Add(self.resultado, 1, wx.EXPAND)
		for listaBotoes in botoes:
			linhaBotoes = wx.BoxSizer(wx.HORIZONTAL)
			if botoes.index(listaBotoes) == 3: linhaBotoes.AddStretchSpacer(1)
			for botao in listaBotoes:
				botao.Bind(wx.EVT_BUTTON, self.realizar_funcao)
				linhaBotoes.Add(botao, 1, wx.EXPAND)
			sizerPrincipal.Add(linhaBotoes, 1, wx.EXPAND)

		self.SetSizer(sizerPrincipal)
		sizerPrincipal.Fit(self)
		self.SetAutoLayout(1)
		self.Show()

	def numero_digitado(self, event):
		caractere = event.GetRawKeyCode()
		print(caractere)

	def realizar_funcao(self, event):
		qualBotao = event.GetEventObject().GetLabelText()
		if qualBotao == "LIMPAR":
			self.resultado.SetLabelText('')
			self.operacao = ''
			return

		if qualBotao.isdigit():
			self.operacao += qualBotao
			self.resultado.SetLabelText(self.operacao)
		else:
			if qualBotao == "=":
				try:
					self.resultado.SetLabelText(str(eval(self.operacao)))
				except SyntaxError:
					wx.MessageDialog(self, 'Erro', "Verifique a sua expressão!").ShowModal()
				self.operacao = ''
			else:
				self.operacao += qualBotao
				self.resultado.SetLabelText(self.operacao)


app = wx.App()
Calculadora()
app.MainLoop()