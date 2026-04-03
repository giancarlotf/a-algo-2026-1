# Cálculo de complexidade para:
## 1) Algoritmo de ordenação Merge Sort:

O algoritmo de ordenação *Merge Sort* baseia-se na lógica dividir para conquistar. Ele atua da seguinte maneira: a lista de valores é dividida repetidamente pela metade até que cada sublista contenha apenas um elemento. Em seguida, o algoritmo combina essas sublistas, comparando e ordenando os elementos, formando listas crescentes, que correspondem ao tamanho das etapas anteriores, até que a lista original seja reconstruída, mas agora completamente ordenada.

Na etapa de divisão da lista, o algoritmo gera duas sublistas de tamanho $n/2$, resultando no termo recursivo $2T(\frac{n}{2})$. Para combinar as sublistas ordenadas, o algoritmo percorre todos os elementos, tendo um custo O(n). Portanto a recorrência que descreve o algoritmo é:
$$
T(n)=2T\Big(\frac{n}{2}\Big)+n.
$$
A análise de complexidade pode ser feita por meio do Teorema Mestre:
$$
n^{log_{b}a}=n^{log_{2}2}=n\\
f(n)=n
$$
Este é Caso 2 do Teorema Mestre, logo:
$$
T(n)=\Theta(n\cdot log_{2}(n))\\
T(n)=\Theta(n\cdot log(n)).
$$

## 2) Multiplicação de matrizes:

Dadas duas matrizes $\,A\in\mathbb{R}^{am\times an}\,$ e $\,B\in\mathbb{R}^{bm\times bn}$, sua multiplicação $\,C=A\cdot B\,$ só é definida se o número de colunas de $A$ for igual ao de número de linhas de $B$, ou seja, se $an=bm$. Caso essa condição seja satisfeita, o resultado será a matriz $\,C\in\mathbb{R}^{am\times bn}$.

A multiplicação ocorre da seguinte maneira:
$$
C_{i,j}=\sum_{k=1}^{an} A_{i,k}\cdot B_{k,j}
$$
Para cada elemento $\,C_{i,j}$ há $an$ multiplicações, e existem $am\cdot bn$ elementos na matriz resultante. Portanto, pode-se deduzir que o número total de operações é $am\cdot an\cdot bn$, e consequentemente sua complexidade é:
$$
T(am,an,bn)=O(am\cdot an\cdot bn)
$$
De forma geral:
$$
T(n_1,n_2,n_3)=O(n_1\cdot n_2\cdot n_3).
$$

## 3) Recorrências:

A análise de complexidade das recorrências foi realizada por meio do Teorema Mestre, visto que todas seguem o padrão:

$$
T(n)=aT([n/b])+f(n),\quad a\in\mathbb{N},\; a\geq 1,\; b\in\mathbb{N},\; b>1
$$

---
a) $T(n)=2T(\frac{n}{4})+\sqrt{n}$

&nbsp;&nbsp;&nbsp;&nbsp;$n^{log_{b}(a)}=n^{log_{4}(2)}=n^\frac{1}{2}=\sqrt{n}$

&nbsp;&nbsp;&nbsp;&nbsp;$f(n)=\sqrt{n}$

Este é Caso 2 do Teorema Mestre, logo:

&nbsp;&nbsp;&nbsp;&nbsp;$T(n)=\Theta(\sqrt{n}\cdot log_{4}(n))$

&nbsp;&nbsp;&nbsp;&nbsp;$T(n)=\Theta(\sqrt{n}\cdot log(n))$

---
b) $T(n)=2T(\frac{n}{4})+n$

&nbsp;&nbsp;&nbsp;&nbsp;$n^{log_{b}(a)}=n^{log_{4}(2)}=n^\frac{1}{2}=\sqrt{n}$

&nbsp;&nbsp;&nbsp;&nbsp;$f(n)>\sqrt{n}$

Este é Caso 3 do Teorema Mestre, logo:

&nbsp;&nbsp;&nbsp;&nbsp;$T(n)=\Theta(n)$

---
c) $T(n)=16T(\frac{n}{4})+n^2$

&nbsp;&nbsp;&nbsp;&nbsp;$n^{log_{b}(a)}=n^{log_{4}(16)}=n^2$

&nbsp;&nbsp;&nbsp;&nbsp;$f(n)=n^2$

Este é Caso 2 do Teorema Mestre, logo:

&nbsp;&nbsp;&nbsp;&nbsp;$T(n)=\Theta(n^2\cdot log_{4}(n))$

&nbsp;&nbsp;&nbsp;&nbsp;$T(n)=\Theta(n^2\cdot log(n))$
