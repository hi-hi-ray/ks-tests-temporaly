# ks-tests-temporaly
just to show some examples of tests

Rodando API com Docker: `docker build -t flask-library-app .`
Rodando API sem Docker: 
```
cd api
python -m pip install flask bcrypt jwt
python library.py
```
Rodando os testes back:
```
cd api
python -m pip install flask bcrypt jwt
python test_runner.py
```

## Backend & Front-End
### **Unit Tests (Testes de Unidade)**  
Testes automatizados que verificam o funcionamento de unidades individuais do código, como funções ou métodos isolados.  

#### Onde usar:
- Durante o desenvolvimento, para garantir que cada parte do código funcione corretamente.
- Em projetos com alta complexidade de código, onde é necessário isolar e testar pequenas partes.
- Em pipelines de CI/CD para evitar regressões após alterações no código.

#### Plano:
1. Testar cada função/método individualmente com diferentes entradas.
2. Garantir tratamento de exceções.
3. Mockar dependências para isolar a unidade testada.
4. Cobrir casos de borda e valores extremos.
5. Executar frequentemente para evitar regressões.

### **Integration Tests (Testes de Integração)**  
Verificam se diferentes partes do sistema funcionam corretamente juntas.  

#### Onde usar:
- Após o desenvolvimento de módulos ou componentes, para garantir que eles se integram corretamente.
- Em sistemas distribuídos ou com múltiplos serviços.
- Antes de liberar novas funcionalidades para produção.

#### Plano:
1. Testar comunicação entre módulos/componentes.
2. Simular chamadas de API e verificar respostas.
3. Testar interações com banco de dados.
4. Verificar integração com serviços externos.
5. Identificar falhas na troca de dados.

### **Load Tests (Testes de Carga)**  
Avaliam o desempenho do sistema sob carga esperada.  

#### Onde usar:
- Antes de lançamentos para garantir que o sistema suporta o tráfego esperado.
- Em sistemas que precisam lidar com picos de uso (ex.: e-commerce, plataformas de streaming).
- Para identificar gargalos de desempenho.

#### Plano:
1. Simular múltiplos usuários simultâneos.
2. Medir tempos de resposta sob carga.
3. Analisar consumo de recursos.
4. Identificar gargalos.
5. Ajustar parâmetros para otimização.

### **System Tests (Testes de Sistema)**  
Avaliam o sistema como um todo, verificando sua conformidade com os requisitos.  

#### Onde usar:
- Antes da entrega final do produto.
- Para garantir que todas as funcionalidades estão funcionando conforme o esperado.
- Em sistemas complexos com múltiplos módulos.

#### Plano:
1. Testar todas as funcionalidades.
2. Validar requisitos funcionais e não funcionais.
3. Garantir integração correta entre componentes.
4. Simular cenários de uso reais.
5. Certificar que o sistema atende aos critérios de aceitação.

### **Security Tests (Testes de Segurança)**  
Garantem que o sistema esteja protegido contra vulnerabilidades.  

#### Onde usar:
- Em sistemas que lidam com dados sensíveis (ex.: financeiros, saúde).
- Antes de lançamentos para garantir conformidade com padrões de segurança.
- Após alterações no código que possam impactar a segurança.

#### Plano:
1. Testar injeção de SQL e outras vulnerabilidades.
2. Verificar autenticação e autorização.
3. Avaliar proteção contra DDoS.
4. Identificar exposição de dados.
5. Testar segurança de APIs.

### **Compatibility Tests (Testes de Compatibilidade)**  
Verificam se o sistema funciona corretamente em diferentes ambientes.  

#### Onde usar:
- Em aplicações multiplataforma (ex.: web, mobile, desktop).
- Antes de lançamentos para garantir funcionamento em diferentes dispositivos e navegadores.
- Em sistemas que precisam suportar versões antigas de software.

#### Plano:
1. Testar em diferentes navegadores e dispositivos.
2. Validar em diferentes sistemas operacionais.
3. Testar em diferentes resoluções de tela.
4. Garantir funcionamento em diferentes versões.
5. Testar integrações externas.

## Backend 

### **Smoke Tests (Testes de Fumaça)**  
Verificações rápidas para garantir que as funcionalidades principais estão operacionais.  

#### Onde usar:
- Após deploy em ambientes de desenvolvimento, staging ou produção.
- Antes de executar testes mais abrangentes, para garantir que o sistema está estável.
- Em pipelines de CI/CD para validar builds.

#### Plano:
1. Verificar inicialização do sistema.
2. Testar rotas principais da API.
3. Confirmar carregamento da interface do usuário.
4. Validar acesso ao banco de dados.
5. Executar em diferentes ambientes.

### **Stress Tests (Testes de Estresse)**  
Testam o sistema em condições extremas.  

#### Onde usar:
- Para avaliar a resiliência do sistema em cenários de sobrecarga.
- Em sistemas críticos que não podem falhar sob pressão.
- Para identificar pontos de ruptura e melhorar a robustez.

#### Plano:
1. Aumentar carga progressivamente até o sistema falhar.
2. Medir comportamento sob uso intenso.
3. Testar limites de conexões simultâneas.
4. Monitorar tempo de resposta sob sobrecarga.
5. Identificar pontos fracos.

### **Regression Tests (Testes de Regressão)**  
Garantem que novas alterações não quebrem funcionalidades existentes.  

#### Onde usar:
- Após alterações no código, para garantir que funcionalidades antigas continuam funcionando.
- Em projetos com atualizações frequentes.
- Em pipelines de CI/CD para evitar regressões.

#### Plano:
1. Executar testes automatizados em cada nova versão.
2. Verificar funcionalidades antigas.
3. Garantir que correções de bugs não introduzam novos erros.
4. Testar componentes afetados por mudanças recentes.
5. Manter um conjunto robusto de testes.

### **Scalability Tests (Testes de Escalabilidade)**  
Verificam a capacidade do sistema de lidar com aumento de demanda.  

#### Onde usar:
- Em sistemas que precisam escalar horizontal ou verticalmente.
- Antes de lançamentos para garantir que o sistema suporta crescimento.
- Em aplicações com alta demanda de usuários.

#### Plano:
1. Testar escalabilidade horizontal e vertical.
2. Avaliar desempenho com aumento progressivo de carga.
3. Identificar limites de escalabilidade.
4. Simular crescimento de usuários e tráfego.
5. Medir impacto de novas instâncias ou recursos.

### **Performance Tests (Testes de Desempenho)**  
Analisam a velocidade, estabilidade e eficiência do sistema.  

#### Onde usar:
- Em sistemas que precisam atender a requisitos de desempenho rigorosos.
- Para identificar gargalos e otimizar o sistema.
- Antes de lançamentos para garantir que o sistema é rápido e responsivo.

#### Plano:
1. Medir tempos de resposta das requisições.
2. Monitorar consumo de CPU, memória e rede.
3. Testar eficiência do banco de dados.
4. Verificar impacto de otimizações no código.
5. Identificar possíveis gargalos de desempenho.

### **Exploratory Tests (Testes Exploratórios)**  
Testes manuais para explorar o sistema e encontrar comportamentos inesperados.  

#### Onde usar:
- Em fases iniciais de desenvolvimento para identificar falhas não previstas.
- Após alterações no código para garantir que não há regressões.
- Em sistemas complexos onde é difícil prever todos os cenários.

#### Plano:
1. Testar entradas com caracteres especiais.
2. Testar entradas com tamanhos extremos.
3. Testar entradas duplicadas.
4. Testar formatos de dados inválidos ou incomuns.
5. Explorar o sistema fora do fluxo esperado.
6. Tentar "quebrar" o sistema com entradas inesperadas.
7. Documentar e reportar.

## Front-End
### **Usability Tests (Testes de Usabilidade)**  
Avaliam a experiência do usuário ao interagir com o sistema.  

#### Onde usar:
- Durante o design e desenvolvimento de interfaces.
- Antes de lançamentos para garantir que a aplicação seja intuitiva.
- Em projetos com foco em experiência do usuário.

#### Plano:
1. Testar com usuários reais.
2. Medir facilidade de uso.
3. Observar dificuldades encontradas.
4. Coletar feedback.
5. Melhorar o design com base nos resultados.

### **Acceptance Tests (Testes de Aceitação)**  
Garantem que o software atende aos requisitos do usuário.  

#### Onde usar:
- Antes da entrega do produto ao cliente.
- Em colaboração com stakeholders para validar funcionalidades.
- Em projetos ágeis, para garantir que as histórias de usuário foram implementadas corretamente.

#### Plano:
1. Validar funcionalidades principais.
2. Testar experiência do usuário.
3. Garantir conformidade com requisitos.
4. Executar com stakeholders.
5. Validar fluxos completos de uso.