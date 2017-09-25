'Não vou colocar comentários sobre o que é o quê, pois de vc querer aprimorar terá que saber interpretar
Option Explicit
msgbox "MyTeacher - Resolucao de equacao de segundo grau" & vbCrlf & "--------------------------------------------------------" & vbCrlf & "                                          V. 1"
Dim Delta1, Baskhara1, Baskhara2, a, b, c, Resultado, Delta2, Delta3, xa, Bk, Bsk, d, e, f, g, h, i, j
Do
a = inputbox("Digite o valor de a:", "MyTeacher")
Loop Until a <>""
Do
b = inputbox("Digite o valor de b:", "MyTeacher")
Loop Until b <>""
Do
c = inputbox("Digite o valor de c:", "MyTeacher")
Loop Until c <>""
Delta1 =  b^2 
Delta2 = -4*a*c
Delta3 = Delta1 + Delta2
If Delta3 < 0 Then
msgbox "Impossivel encontrar resultado, delta negativo" & vbCrlf & "-------------------------------------------------" & vbCrlf & "                                Delta  = " & Delta3
d = Delta3 * -1
e = 2*a
j = sqr(d)
f = -b / e
g = j / e
h = msgbox("X' = " & f & " + " & g & "i")
i = msgbox("X' = " & f & " - " & g & "i")

Else
Bk = -b + Sqr(Delta3)
Bsk = -b - Sqr(Delta3)
xa = 2*a
Baskhara1 = bk / xa
Baskhara2 = bsk / xa
Resultado =  msgbox("X' = " & Baskhara1 & vbCrlf & "X'' = " & Baskhara2 & vbCrlf & "Delta = " & Delta3)
End If
msgbox "Feito pelo Super23"