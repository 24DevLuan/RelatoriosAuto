from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import date
from funcoes import *
touch = canvas.Canvas("Relatorio.pdf")

mes = date.today().month 
ano = date.today().year
mesanterior = mes - 1
taxanext = 15

nome = input("Insira o nome do cliente: ")
indice = buscaindice(nome)
aplicacao = indice[0]
dia = indice[1]

#Porcentagem, rendimento
porcentagem = int(input("Insira a porcentagem que será aplicada:"))

#Cálculo da porcentagem
rendimentobruto = rendimento(aplicacao,porcentagem)
#Taxa de consultoria
taxaconsultoria = taxanxt(rendimentobruto,taxanext)

#Aplicação incial + lucro liquido antes da retirada
carteiraantesdaretirada = afterretirada(aplicacao, rendimentobruto, taxaconsultoria)

#Retirada
retirada= int(input("O cliente quer retirar alguma quantia, se sim qual?"))
#Saldo Final
saldofinal = beforeretirada(carteiraantesdaretirada, retirada)

rendimentobruto = '%.2f' %rendimentobruto

#----------------------------------------

# Converter a medida de pontos flutuantes para centímetros.
def mm_to_cm(cm):
    return cm / 0.352777 * 10

#Adicionando Imagens

#Next Logo
touch.drawImage("logo.png", mm_to_cm(2) ,mm_to_cm(27), mask='auto', width=200, height=60)
#Linha Horizontal Preta
touch.drawImage("black.png", mm_to_cm(0) ,mm_to_cm(26), mask='auto', width=600, height=1)
#Linha Vertical Preta
touch.drawImage("black2.png", mm_to_cm(0) ,mm_to_cm(0), mask='auto', width=20, height=900)
#Template Tabela
touch.drawImage("tab1.png", mm_to_cm(5) ,mm_to_cm(17), mask='auto', width=330, height=55)
#Assinatura
touch.drawImage("ass.png", mm_to_cm(6) ,mm_to_cm(2), mask='auto', width=250, height=160)
#Informações do cabeçalho

touch.setFont('Helvetica-Oblique', 12)
touch.drawString(mm_to_cm(15) , mm_to_cm(28.3) ,'Avenida Ário Barnabé, 1149')
touch.drawString(mm_to_cm(15) , mm_to_cm(27.9) ,'Indaiatuba, São Paulo.')
touch.drawString(mm_to_cm(15) , mm_to_cm(27.2) ,'(19)99881-7857')

#Título de descrição do relatório

touch.setFont('Helvetica-Bold', 22)
touch.drawString(mm_to_cm(2) , mm_to_cm(24.5) ,'Relatório mensal do resultado das aplicações:')

#Cliente

touch.setFont('Helvetica', 14)
touch.drawString(mm_to_cm(2) , mm_to_cm(23.9) ,'Cliente:')
touch.setFont('Helvetica-Oblique', 14)
touch.drawString(mm_to_cm(3.8) , mm_to_cm(23.9) ,nome)

#Data

touch.setFont('Helvetica-Bold', 18)
touch.drawString(mm_to_cm(7.5) , mm_to_cm(21) ,'De 0'+str(dia)+'/0'+str(mesanterior)+ '/24 a 0'+str(dia)+'/0'+str(mes)+'/24')

#-------------------------------------------------------------------------------
#Tab1

#Título
touch.setFont('Helvetica', 15)
touch.drawString(mm_to_cm(5) , mm_to_cm(19.2) ,'Balanço mensal:')

#Linha 1

#Célula 1 
touch.setFont('Helvetica-Bold', 16)
touch.drawString(mm_to_cm(5.6) , mm_to_cm(18.3) ,'Aplicação')
#Célula 2
touch.setFont('Helvetica', 14)
touch.drawString(mm_to_cm(5.9) , mm_to_cm(17.3) , 'R$' + str(aplicacao))

#Linha 2

#Célula 1
touch.setFont('Helvetica-Bold', 16)
touch.drawString(mm_to_cm(9.3) , mm_to_cm(18.3) ,'Rendimento')
#Célula 2
touch.setFont('Helvetica', 14)
touch.drawString(mm_to_cm(9.35) , mm_to_cm(17.3) ,'BNB-US -' + str(porcentagem) + '%')

#Linha 3

#Célula 1
touch.setFont('Helvetica-Bold', 16)
touch.drawString(mm_to_cm(13.3) , mm_to_cm(18.3) ,'Resultado')
#Célula 2
touch.setFont('Helvetica', 14)
touch.drawString(mm_to_cm(13.5) , mm_to_cm(17.3) ,'R$' + str(rendimentobruto))

#-------------------------------------------------------------------------------

#Tab2---------------------------------------------------------------------------

#Título
touch.setFont('Helvetica', 15)
touch.drawString(mm_to_cm(5) , mm_to_cm(15.5) ,'Taxa da consultoria financeira:')

#Tabela
touch.drawImage("tab2.png", mm_to_cm(5) ,mm_to_cm(13.3), mask='auto', width=330, height=55)
touch.setFont('Helvetica-Bold', 16)
touch.drawString(mm_to_cm(13.3) , mm_to_cm(18.3) ,'Resultado')

#Linha1

#Célula1
touch.setFont('Helvetica-Bold', 14)
touch.drawString(mm_to_cm(5.3) , mm_to_cm(14.6) ,'Rendimento bruto')

#Célula2
touch.setFont('Helvetica', 14)
touch.drawString(mm_to_cm(6.6) , mm_to_cm(13.6) , str(rendimentobruto))

#Linha2

#Célula1
touch.setFont('Helvetica-Bold', 14)
touch.drawString(mm_to_cm(10.5) , mm_to_cm(14.6) ,'-15% Consultoria Next')

#Célula2
touch.setFont('Helvetica', 14)
touch.drawString(mm_to_cm(12.5) , mm_to_cm(13.6) , 'R$%.2f' %(taxaconsultoria))

#--------------------------------------------------------

#Tab2.1
touch.drawImage("tab3.png", mm_to_cm(7.5) ,mm_to_cm(12.5), mask='auto', width=170, height=25)

#Contéudo
touch.setFont('Helvetica-Bold', 14)
touch.drawString(mm_to_cm(7.9) , mm_to_cm(12.8) ,'Novo saldo:')
touch.setFont('Helvetica', 12.6)
touch.drawString(mm_to_cm(11) , mm_to_cm(12.8) ,'R$%.2f' %carteiraantesdaretirada)

#-------------------------------------------------------------------------
#Título
touch.setFont("Helvetica",15)
touch.drawString(mm_to_cm(5) , mm_to_cm(10.8) ,'Situação atual:')

#Layout
touch.drawImage("tab4.png", mm_to_cm(5) ,mm_to_cm(8), mask='auto', width=330, height=70)

#Linha 1

#Célula1
touch.setFont('Helvetica-Bold', 15)
touch.drawString(mm_to_cm(7.5) , mm_to_cm(9.8) ,'Saldo')
#Célula2
touch.setFont('Helvetica-Bold', 15)
touch.drawString(mm_to_cm(7.2) , mm_to_cm(9) ,'Retirada')
#Carteira
touch.setFont('Helvetica-Bold', 15)
touch.drawString(mm_to_cm(7.2) , mm_to_cm(8.2) ,'Carteira')

#Linha2
#Célula1
touch.setFont('Helvetica', 15)
touch.drawString(mm_to_cm(13) , mm_to_cm(9.8) ,'R$%.2f' %carteiraantesdaretirada)
#Célula2
touch.setFont('Helvetica', 15)
touch.drawString(mm_to_cm(12.7) , mm_to_cm(9) ,'-')
touch.setFont('Helvetica', 15)
touch.drawString(mm_to_cm(13) , mm_to_cm(9) ,'R$%.2f' %retirada)
#Carteira
touch.setFont('Helvetica', 15)
touch.drawString(mm_to_cm(13) , mm_to_cm(8.2) ,'R$%.2f' %saldofinal)

#------------------------------------------------------------------------------
#Assinatura

touch.save()
