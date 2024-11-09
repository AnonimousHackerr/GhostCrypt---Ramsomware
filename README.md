**GhostCrypt: Ransomware - Descrição do Arquivo**

GhostCrypt é um ransomware altamente agressivo que criptografa arquivos vitais do sistema alvo, bloqueando o acesso dos usuários e sem nenhum resgate, ou seja, voce nunca vai recuperar os seus dados criptografados, literalmente. Ele usa técnicas de criptografia avançadas e exibe uma interface de bloqueio personalizada, com uma animação visual perturbadora, com o objetivo de criptografar todos os arquivos sem nenhum resgate.
### Funcionalidades Principais:

1. **Criptografia de Arquivos:**
   GhostCrypt criptografa arquivos de sistemas inteiros, incluindo diretórios vitais do sistema e arquivos de programas, tornando-os inacessíveis para o usuário. O ransomware ignora o próprio arquivo de script para evitar a criptografia de seu próprio código e garantir a continuidade do ataque.

2. **Geração e Armazenamento de Chave de Criptografia:**
   O ransomware gera uma chave de criptografia única (utilizando o algoritmo **Fernet**), que é armazenada em um arquivo oculto para ser usada posteriormente na descriptografia. Se o arquivo de chave não existir, o ransomware o gera automaticamente.

3. **Tela de Bloqueio Visual:**
   Após a criptografia de arquivos, o ransomware exibe uma tela de bloqueio em **fullscreen** com uma arte ASCII de uma caveira. A tela bloqueia interações do teclado e mouse, tornando impossível para o usuário interagir com o sistema. A tela de bloqueio pisca alternando entre cores verde e preta, criando uma experiência visualmente perturbadora para a vítima.

4. **Instruções de Resgate:**
   Embora não explicitamente incluído no código, normalmente este tipo de ransomware incluiria instruções dentro da tela de bloqueio, solicitando que a vítima pague um resgate (em criptomoeda, geralmente) para receber a chave de descriptografia e recuperar os arquivos criptografados.

5. **Caminho de Criptografia Abrangente:**
   O GhostCrypt criptografa arquivos em diretórios essenciais do sistema (como o diretório **C:\Windows\System32**, **Program Files**, **/bin**, **/usr**, etc.), aumentando a probabilidade de danos significativos e forçando as vítimas a pagar pelo resgate.

6. **Mecanismo Anti-Sandbox:**
   Embora o código original não contenha uma verificação explícita para ambientes virtuais, a criptografia de arquivos críticos, juntamente com os métodos de ofuscação simples e o comportamento aleatório (como delays entre as criptografias), são táticas que tornam a análise em um ambiente de pesquisa mais difícil.

---

**Aviso Legal:**

GhostCrypt é uma ferramenta de **ransomware** e, portanto, é **ilegal**. A utilização de ransomware para extorsão e dano a terceiros é um crime em muitas jurisdições ao redor do mundo. Este código **não deve ser usado** para qualquer propósito criminoso. Ele é fornecido para fins educacionais ou de pesquisa em ambientes controlados e nunca deve ser distribuído ou usado para causar dano a indivíduos ou sistemas de qualquer natureza.

