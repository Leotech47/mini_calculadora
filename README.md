# Mini-Calculadora Interativa em Python

Este projeto é uma **mini-calculadora interativa** desenvolvida em Python. O programa permite ao usuário realizar várias operações matemáticas básicas e avançadas, incluindo soma, subtração, multiplicação, divisão, potência, módulo e raiz quadrada. A calculadora funciona em loop, permitindo múltiplas operações até que o usuário escolha encerrar o programa.

---

## Funcionalidades

A calculadora suporta as seguintes operações:

| Operação | Símbolo | Descrição |
|----------|---------|-----------|
| Soma | `+` | Adição de dois números |
| Subtração | `-` | Subtração de dois números |
| Multiplicação | `*` | Multiplicação de dois números |
| Divisão | `/` | Divisão de dois números (verifica divisão por zero) |
| Potência | `^` | Elevar o primeiro número ao segundo |
| Módulo | `%` | Calcula o resto da divisão entre dois números |
| Raiz quadrada | `r` | Calcula a raiz quadrada de um número (não permite números negativos) |
| Encerrar | `sair` | Sai do programa |

---

## Como o código foi criado

1. **Importação de bibliotecas:**  
   A biblioteca `math` foi importada para permitir o cálculo da raiz quadrada.

   ```python
   import math

2. **Loop principal:**
   O programa roda dentro de um `while True`, permitindo operações contínuas até que o usuário escolha sair digitando `"sair"`.

3. **Exibição das operações disponíveis:**
   Um menu é exibido no terminal para que o usuário visualize rapidamente as opções.

4. **Entrada do usuário:**

   * Para operações que envolvem dois números (`+`, `-`, `*`, `/`, `^`, `%`), o programa solicita dois valores numéricos.
   * Para raiz quadrada (`r`), apenas um número é solicitado.

5. **Cálculo das operações:**

   * Condições `if/elif` verificam qual operação foi escolhida e realizam o cálculo correspondente.
   * Tratamento de erros foi incluído: divisão por zero e raiz de número negativo.

6. **Exibição do resultado:**

   * O resultado da operação é exibido no terminal.
   * Um separador visual (`"-" * 40`) é usado para facilitar a leitura entre operações consecutivas.

---

## Como executar

1. Certifique-se de ter o **Python 3** instalado na sua máquina.
   Você pode verificar executando no terminal:

   ```bash
   python --version
   ```

2. Salve o código Python em um arquivo chamado, por exemplo, `calculadora.py`.

3. Abra o terminal ou prompt de comando e navegue até o diretório onde o arquivo está salvo.

4. Execute o programa com o seguinte comando:

   ```bash
   python calculadora.py
   ```

5. Siga as instruções exibidas no terminal:

   * Escolha a operação desejada digitando o símbolo correspondente (`+`, `-`, `*`, `/`, `^`, `%`, `r`).
   * Digite os números solicitados.
   * Veja o resultado.
   * Para encerrar, digite `sair`.

---

## Exemplo de execução

```
Operações disponíveis:
 + : Soma
 - : Subtração
 * : Multiplicação
 / : Divisão
 ^ : Potência
 % : Módulo
 r : Raiz quadrada
 sair : Encerrar a calculadora

Escolha a operação: *
Digite o primeiro número: 5
Digite o segundo número: 3
Resultado: 15.0
----------------------------------------
Escolha a operação: r
Digite o número para calcular a raiz quadrada: 16
Resultado: 4.0
----------------------------------------
Escolha a operação: sair
Encerrando a calculadora. Até mais!
```

---

## Observações

* O programa trata erros comuns, como **divisão por zero** e **raiz de número negativo**.
* É possível adicionar novas operações facilmente seguindo a estrutura de `if/elif`.
* Ideal para aprendizado e prática de programação básica em Python.

---

Feito para quem deseja uma **calculadora simples, interativa e extensível** em Python.
