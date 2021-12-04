# Fórmula de Bháskara

## Um pouco de história

Bháskara foi o mais famoso Geômetra da Índia, considerado em seu tempo por todos um importante sábio que sabia todos os segredos dos astros e estudava os mistérios dos céus. Bhaskara nasceu em Bidon, na Provincia de Deca em 1145 d.C. Sua primeira e pricipal obra *Bija-ganita* (*Bija* quer dizer *semente*, e *ganita* quer dizer *contar, avaliar, medir* ou seja *A Arte de Contar Sementes*) que continha doze capítulos e foi o primeiro a apresentar um método de cálculo de duas raízes quadradas para um número positivo.

E você deve estar pensando: *Isso quer dizer que esse é o cara que criou a **Fórmula de Bháskara**, certo?*

E lamento lhe informar que não!

Na verdade, a fórmula é apenas conhecida com esse nome no Brasil. A maior parte do mudno conhece essa fórmula como **equação quadrática** e a mesma foi descoberta aproximadamente 4000 anos antes de Bháskara nascer, na Babilônia e foi amplamente empregada na forma geométrica pelos Gregos milhares de anos antes de Bháskara. Porém, na Europa o trabalho de Bháskara em *A Arte de Contar Sementes* tornou-se famosa, a mesma continha um método de resolução desses problemas que na verdade havia sido criado por outro matemático indiano chamado Sridhara que viveu duzentos anos antes de Bháskara, mas graças ao livro no mundo acadêmico europeu onde é normal associar pesquisadores da matemática ao conteúdo de suas obras Bháskara tornou-se conhecido por essa fórmula em sua obra de resolução de equações quadráticas.

E agpra sim você deve estar pensando: *Ah! Agora entendi! Então foi esse tal de **Sridhara** quem criou essa fórmula que me traz memórias de guerra do ensino médio!*

E lamento lhe informar novamente que não!

Eita! De novo? Pois é, a fórmula que estava presente em *A Arte de Contar Sementes* na verdade não é a mesma que utilizamos para resolver equações quadráticas no Ensino Médio, nessa obra o que é mostrado é um passo-a-passo (lembra disso?) de como encontrar as raízes de uma equação quadrádica, mas mesmo Bháskar ou Sridara não entendiam como isso funcionava ou tinham uma fórmula para isso, na verdade essa fórmula foi criada por um matemático francês chamado François Viète no Séc. XVII que a criou como uma formula geral para a resolução de equações de segundo grau.

*Trè bien, allons-y*! 

## Vamos a Matemática!

A "Fórmula de Bháskara" (entre aspas, chame de **equação quadrádica** se preferir) é uma fórmula que usamos para calcular o valor de **x** em uma equação de 2º grau que basicamente é uma equação que é representada por:

<p align="center">
    <strong>ax² + bx + c = 0</strong>
</p>

Normalmente quando temos uma equação de segundo grau temos os valores de **a**, **b** e **c**, por exemplo: *x² - 2x + 1 = 0*, nesse caso **a** vale 1 pois temos 1x² mas omitimos o valor 1 a frente, **b** vale -2 e **c** vale 1.

> Quando trabalhamos com equações de segundo grau, os valore b e c podem ser 0. Por exemplo, 2x² + 5 = 0 é uma equação com valores a = 2, b = 0 e c = 5. Porém, o valor de a nunca pode ser 0, pois nesse caso não seria mais uma equação de segundo grau.

A fórmula é essa:
<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=$x=\frac{-b\pm\sqrt{\Delta}}{2a}$" width="250">
</p>

O valor representado por Δ (letra grega delta) é chamado de **discriminante**:
<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=$\Delta = b^2-4ac$" width="250">
</p>
Seu valor vai nos dizer quantas raízes nossa equação vai ter:

- Se o delta for maior que zero, a equação terá dois valores reais e distintos. 
- Se o delta for igual a zero, a equação terá somente um valor real ou dois resultados iguais. 
- Se o delta for menor que zero, a equação não possuirá valores reais.

### Primeiro Exemplo
Vamos então resolver a equação que tínhamos usado de exemplo:

<p align="center">
    <strong>x² - 2x + 1 = 0</strong>
</p>

Vamos começar nossa fórmula pelo cálculo do discriminante, substituindo os valores de *a, b e c* pelos valores de nossa equação, nesse caso **a** vale 1, **b** vale -2 e **c** vale 1: 

<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=$\Delta = b^2-4ac$" width="150">
</p>
<br>
<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=$\Delta = (-2)^2-4.(1).(1)$" width="190">
</p>
<br>
<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=$\Delta = 4-4$" width="100">
</p>
<br>
<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=$\Delta = 0$" width="60">
</p>


E então substituimos os valores de Δ, a e b em nossa bháskara:

<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=$x=\frac{2\pm\sqrt{0}}{2}$" width="150">
</p>

Nosso **discriminante** é 0, então temos 1 raíz:

<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=$x=\frac{2}{2}$" width="75">
</p>
<br>
<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=$x=1$" width="75">
</p>

### Segundo Exemplo

Vamos então resolver mais uma equação de segundo grau:

<p align="center">
    <strong>4x² + 2x -6 = 0</strong>
</p>

Vamos começar nossa fórmula pelo cálculo do discriminante, substituindo os valores de *a, b e c* pelos valores de nossa equação, nesse caso **a** vale 4, **b** vale 2 e **c** vale -6: 

<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=$\Delta = b^2-4ac$" width="150">
</p>
<br>
<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=$\Delta = (2)^2-4.(4).(-6)$" width="190">
</p>
<br>
<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=$\Delta = 4 %2B 96$" width="100">
</p>
<br>
<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=$\Delta = 100$" width="80">
</p>


E então substituimos os valores de Δ , a e b em nossa bháskara:

<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=$x=\frac{-2\pm\sqrt{100}}{2.4}$" width="150">
</p>

Nosso **discriminante** é maior que 0, então temos 2 raízes:

<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=$x=\frac{-2\pm\10}{8}$" width="150">
</p>

Então podemos simplificar essa conta dividindo os valores por 2, uma vez em que é um fator comum entre numerador e denominador:

<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=$x=\frac{-1\pm\5}{4}$" width="120">
</p>

E agora podemos determinar as raízes.

Sendo a **primeira**:

<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=$x=\frac{-1 %2B 5}{4}$" width="120">
</p>
<br>
<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=$x=\frac{4}{4}$" width="70">
</p>
<br>
<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=$x=1$" width="70">
</p>

E a **segunda**:

<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=$x=\frac{-1 %2d 5}{4}$" width="120">
</p>
<br>
<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=$x=\frac{-6}{4}$" width="75">
</p>

Que póde ser simplificado para:

<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=$x=\frac{-3}{2}$" width="75">
</p>

Logo, as raízes dessa equação são 1 e -3/2.

## Programação

Ok, agora que relembramos como calcular equações de segundo grau vamos para nosso exercício de programação: 
``` 
Você deve desenvolver um algoritmo em Python que calcule o resultado de uma equação quadrática.

Entradas:
- Valor number de a
- Valor number de b
- Valor number de c

Saída:
- Se o valor de delta for maior que zero, o retorno deve ser dois valores reais e distintos. 
- Se o delta for igual a zero, o retorno terá somente um valor real ou dois resultados iguais. 
- Se o delta for menor que zero, deverá ser escrito no console que essa equação não possuí raízes reais.
``` 
