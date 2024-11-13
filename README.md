# projeto_calculadora
 O repositório armazena o arquivo .py da calculadora e o script .sh para executar a calculadora.

Instruções:

PREPARAÇÃO DO AMBIENTE
- Para o uso adequado da calculadora, recomenda-se em um primeiro momento que o usuário execute o arquivo shell_script.sh no terminal Ubuntu (ou qualquer distribuição baseada em Linux), com o comando ./shell_script.sh.

EXECUÇÃO DO SHELL SCRIPT (shell_script.sh)

- Para as duas próximas instruções, o script utiliza o comando "sudo", que concede maior nível de permissão ao usuário;
- O shell script irá verificar a relação de pacotes que podem ser atualizados;
- Em seguida irá instalar o Python3, caso o usuário não possua o Python3 instalado no computador, ou irá atualizá-lo, caso o Python3 já esteja presente no ambiente;
- Uma mensagem será exibida ao usuário informando que a calculadora está sendo inicializada;
- Neste ponto, o código .py é executado pelo shell script. 

EXECUÇÃO DO CÓDIGO PYTHON (projetocalculadora.py)

- A calculadora solicita um primeiro número e na sequência um segundo número;
- Na sequência é exibido um menu de opções contendo as quatro principais operações (soma, subtração, divisão e multiplicação);
- Cada operação possui um número correspondente de atalho, e o usuário deve informar qual o número correspondente à operação que deseja realizar;
- No fim, aparece a opção de continuar realizando cálculos ou encerrar o uso da calculadora.

- Se o usuário optar por encerrar a atividade da calculadora uma mensagem será exibida informando sobre o encerramento da calculadora. Esta mensagem está configurada no shell script após a execução do código python.

