O tkinter.ttkmódulo fornece acesso ao conjunto de widgets temáticos Tk, introduzido no Tk 8.5.
A ideia básica tkinter.ttké separar, na medida do possível, o código que implementa o comportamento de um widget do código que implementa sua aparência.

Desenvolvimento de uma máquina dotada de dispositivos tecnológicos e computacional realizando cálculos matemáticos.
Para começar a usar o Ttk, importe os seguintes módulos.

from tkinter import *
from tkinter.ttk import *

Esse código faz com que vários tkinter.ttkwidgets ( Button, Checkbutton, Entry, Frame, Label, LabelFrame, Menubutton, PanedWindow, Radiobuttone ) substituam automaticamente os widgets Tk Scale.Scrollbar
Tendo o benefício direto de usar os novos widgtes, proporcionando uma aparência mais amigável
em todas as plataformas. Nas linhas 12 e 18 gero a minha janela,cursor e as suas dimensões.
Consequentemente, entre 20 e 23 aplicamos o nossos frames de corpo e tela.

O nosso botão_valores recebe uma variável global acabando funcionando efetivamente dentro de um escopo global, tendo acesso e persistindo as funções limpar_tela(),
entrada_valores() 'nossos valores de entrada da calculadora' e calculo 'para somar, diminuir e etc dentro da calculadora', tendo um importante papel dentro do nosso script
Apliquei as seguintes variáveis para seleção de cores entre a linha 5 e 10, para deixar mais
organizado o design enquanto realizava e personalizava o código.
A função entrada_valores() é quem define nossa entrada lógica dos valores de calculo com o botao_valores, dando entrada
no frame tela após definir um valor pelo mouse.

Além disso, dentre as linhas 49 até 53 criamos a função config() do cursor enter & leave do botão igual.
Entretanto, nas linhas 55 até 96 gero meus botões e configuro, lembrando de gerar nosso método frame_corpo e o comando calculo
para realizar as operações matemáticas. No entanto, na linha 95 e 96 especificamente estará uma função de retorno de chamada para alterar a cor de fundo e o texto de um botão, através do cursor.

Concluo realizando um loop para o software ficar rodando e quando o usuário fechar o programa, ele realiza o seu encerramento.