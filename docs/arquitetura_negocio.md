# Sumário

* [1. Estrutura da governança de dados](#1-estrutura-da-governança-de-dados)
    * [1.1 Importância da LGPD](#11-importância-da-lgpd)
        * [1.1.1 Introdução à LGPD](#111-introdução-à-lgpd)
        * [1.1.2 Objetivos da LGPD](#112-objetivos-da-lgpd)
        * [1.1.3 Impacto nos negócios](#113-impacto-nos-negócios)
        * [1.1.4 Conclusão](#114-conclusão)
    * [1.2 Acesso aos dados](#12-acesso-aos-dados)
        * [1.2.1 Definição de papéis e responsabilidades](#121-definição-de-papéis-e-responsabilidades)
        * [1.2.2 Critérios para acesso](#122-critérios-para-acesso)
        * [1.2.3 Conclusão](#123-conclusão)
    * [1.3 Políticas de segurança](#13-políticas-de-segurança)
        * [1.3.1 Medidas de segurança implementadas](#131-medidas-de-segurança-implementadas)
        * [1.3.2 Gestão de incidentes](#132-gestão-de-incidentes)
        * [1.3.3 Treinamento e conscientização dos funcionários](#133-treinamento-e-conscientização-dos-funcionários)
        * [1.3.4 Conclusão](#134-conclusão)
    * [1.4 Outros aspectos da governança de dados](#14-outros-aspectos-da-governança-de-dados)
    * [1.5 Conclusão geral](#15-conclusão-geral)

* [2. Políticas de Uso dos Dados](#2-políticas-de-uso-dos-dados)
    * [2.1 Propósito da Política](#21-propósito-da-política)
    * [2.2 Escopo, amplitude e alcance da Política](#22-escopo-amplitude-e-alcance-da-política)
    * [2.3 Termos e Definições](#23-termos-e-definições)
    * [2.4 Classificação e Gestão de Dados](#24-classificação-e-gestão-de-dados)
        * [2.4.1 Políticas de Classificação](#241-políticas-de-classificação)
        * [2.4.2 Gestão de Dados](#242-gestão-de-dados)
        * [2.4.3 Criação de novos dados](#243-criação-de-novos-dados)
    * [2.5 Políticas de Retenção e Descarte de Dados](#25-políticas-de-retenção-e-descarte-de-dados)
    * [2.6 Política de uso dos dados disponibilizados](#26-política-de-uso-dos-dados-disponibilizados)
        * [2.6.1 Conteúdo dos registros](#261-conteúdo-dos-registros)
        * [2.6.2 Uso Permitido](#262-uso-permitido)
        * [2.6.3 Dados Sensíveis e Uso Restrito](#263-dados-sensíveis-e-uso-restrito)
        * [2.6.4 Tratamento das informações](#264-tratamento-das-informações)
    * [2.7 Coleta de Dados e geração de novos](#27-coleta-de-dados-e-geração-de-novos)
        * [2.7.1 Tipos de Dados Coletados e gerados](#271-tipos-de-dados-coletados-e-gerados)
        * [2.7.2 Método de coleta e geração](#272-método-de-coleta-e-geraçao)
        * [2.7.3 Finalidade da Coleta e da geração dos novos dados](#273-finalidade-da-coleta-e-da-geraçao-dos-novos-dados)
    * [2.8 Bases Legais](#28-bases-legais)
    * [2.9 Atualizações da Política](#29-atualizações-da-política)

* [3. Medição da Qualidade dos Dados](#3-medição-da-qualidade-dos-dados)
    * [3.1 Introdução](#31-introdução)
    * [3.2 Objetivos da Medição da Qualidade dos Dados](#32-objetivos-da-medição-da-qualidade-dos-dados)
    * [3.3 Critérios de Qualidade dos Dados](#33-critérios-de-qualidade-dos-dados)
    * [3.4 Processos de Medição e Garantia de Qualidade](#34-processos-de-medição-e-garantia-de-qualidade)
        * [3.4.1 Auditoria de Dados](#341-auditoria-de-dados)
        * [3.4.2 Monitoramento Contínuo](#342-monitoramento-contínuo)
        * [3.4.3 Governança de Dados](#343-governança-de-dados)
    * [3.5 Análise dos Resultados](#35-análise-dos-resultados)
        * [3.5.1 Melhoria Contínua](#351-melhoria-contínua)
    * [3.6 Conclusão](#36-conclusão)


# 1. Estrutura da governança de dados

## 1.1 Importância da LGPD

### 1.1.1 Introdução à LGPD

Todo indivíduo brasileiro tem os direitos de liberdade, privacidade e livre formação de personalidade, e a Lei Geral de Proteção de Dados (LGPD) foi criada com o intuito de proteger tais direitos.

Sua maior abordagem é relatar como deve ser feito o tratamento de dados pessoais, ou seja, dados que possibilitam a identificação, direta ou indireta da pessoa (nome e sobrenome, data e local de nascimento, RG, CPF, retrato em fotografia, endereço, e-mail, telefone, renda, número do cartão, etc.)  

Considerando isso, a LGPD é fundamental para a proteção de dados pessoais no Brasil, pois garante que as empresas sejam obrigadas a relatar aos usuários como os seus dados estão sendo tratados, cabendo aos mesmos aceitar ou não as condições impostas.

### 1.1.2 Objetivos da LGPD

O principal objetivo da Lei Geral de Proteção de Dados é garantir que as instituições, além de esclarecer ao usuário como seus dados pessoais serão utilizados, realmente apliquem na prática as regras impostas pela lei.

Segundo um artigo do governo sobre a LGPD [(link para o artigo)](https://www.gov.br/mds/pt-br/acesso-a-informacao/privacidade-e-protecao-de-dados/lgpd), o tratamento de dados "diz respeito a qualquer atividade que utiliza um dado pessoal na execução da sua operação, como, por exemplo: coleta, produção, recepção, classificação, utilização, acesso, reprodução, transmissão, distribuição, processamento, arquivamento, armazenamento, eliminação, avaliação ou controle da informação, modificação, comunicação, transferência, difusão ou extração."

Isso significa que antes de realizar qualquer tipo de tratamento, a instituição deve ter certeza de que a finalidade da operação está registrada e foi informada ao titular dos dados de forma clara e transparente. Isso ajuda a promover a segurança da informação, pois incentiva o uso de técnicas que minimizem riscos de violações, como a criptografia e a anonimização dos dados.

### 1.2.3 Impacto nos negócios

Depois de realmente colocada em prática, a LGPD causou uma mudança significativa na forma como os dados devem ser gerenciados pelas empresas, sendo necessária a alocação de especialistas para definir as políticas de tratamento dos dados, e constante revisão das mesmas. 

Por outro lado, o lado positivo de se adotar a lei é que instituições que têm compromisso com a proteção de dados, ganham a confiança de seus clientes e parceiros, o que é um diferencial competitivo.

### 1.2.4 Conclusão

De forma geral, a LGPD é extremamente importante para a privacidade, liberdade e segurança dos brasileiros, uma vez que impõe que as organizações estabeleçam políticas de como os dados pessoais dos indivíduos serão tratados e para qual finalidade, além de transparecer todos esses tópicos aos usuários.

## 1.2 Acesso aos dados

A governança de dados é um conjunto de práticas e políticas que visa garantir o uso adequado, seguro e eficiente dos dados dentro de uma organização. Um de seus aspectos é o controle de acesso aos dados, que é baseado em uma hierarquia e nas responsabilidades de cada um dentro da empresa.

### 1.2.1 Definição de papéis e responsabilidades

O objetivo de definir papéis e responsabilidades específicos aos indivíduos de uma organização é garantir que cada um acesse os dados que realmente precisa, evitando o acesso desnecessário ou não autorizado a informações sensíveis. 

Considerando que a governança de dados trabalha com uma hierarquia, quem tem mais poder dentro da organização acaba tendo um acesso maior. De acordo com as informações fornecidas pelo parceiro sobre a empresa CosmeticCo, existem 3 cargos principais: vendedor, gerente e diretor, e por isso, os seguintes papéis são recomendados:
- **Administrador:** tem controle total sobre os dados, podendo modificar acessos e configurações em todos os níveis;
- **Supervisor:**  tem acesso parcial aos dados, apenas aqueles necessários para tarefas específicas, e não pode modificar dados sensíveis;
- **Operador:** possui acesso bem restrito, podendo visualizar relatórios e outras análises, mas o acesso direto a dados brutos ou sensíveis em si não costuma ser permitido.

Tendo os papéis bem definidos, é possível compreender como será a divisão dos níveis de acesso, que costuma seguir o que foi definido nos papéis. Para este projeto, é recomendado os seguintes níveis:
- **Nível administrativo:** é o nível mais alto de acesso, tendo permissão para acessar todos os dados, e costuma envolver administradores de dados, gerentes de TI ou profissionais da área de segurança da informação. No caso da CosmeticCo, é recomendado que apenas a diretoria tenha acesso administrativo;
- **Nível gerencial:** pessoas com esse acesso podem visualizar conjuntos de dados relevantes para a área que gerenciam, incluindo relatórios, estatísticas de desempenho, informações financeiras etc. Por outro lado, o acesso a dados sensíveis costuma ser restrito. No caso deste projeto, é recomendado que cada gerente de uma loja tenha permissões do nível gerencial no sistema;
- **Nível operacional:** costuma ser o nível mais baixo de acesso, e é voltado para funcionários que realizam operações diárias como vendas, atendimento ao cliente ou processos administrativos. Além disso, eles não costumam ter permissão para visualizar dados de outros usuários, como ocorre nos níveis acima, por exemplo. No caso da CosmeticCo, é recomendado que o acesso de nível operacional seja concedido aos vendedores das lojas;

Há ainda um quarto nível, que lida com informações altamente sensíveis e que por isso precisam de mais atenção. Neste caso, apenas pessoas selecionadas pela instituição possuem acesso.

### 1.2.2 Critérios para acesso

Os critérios de acesso se baseiam em como e porque cada funcionário irá utilizar certo dado. A governança de dados permite explorar alguns caminhos, que estão descritos a seguir:
- **Necessidade de saber:** o acesso é concedido de acordo com as tarefas que cada funcionário precisa executar naquele momento, o que permite que ninguém tenha acesso a dados desnecessários, o que evita a exposição dos mesmos;
- **Função desempenhada:** o acesso aos dados é definido de acordo com o cargo ou função que o funcionário desempenha, ou seja, já existe um conjunto pré-definido de permissões de acesso a diferentes tipos de dados, de acordo com as responsabilidades de cada cargo;
- **Sensibilidade dos dados:** quanto mais sensíveis ficam os dados, mais restritos são seus acessos, e por isso costumam ser limitados a profissionais com credenciais e treinamento específicos para lidar com esse tipo de informação;

A CosmeticCo pode utilizar essas três técnicas principais (que são complementares ao que foi recomendado no nível de acesso) para definir os critérios de permissão para cada funcionário.

### 1.2.3 Conclusão

De forma geral, a governança de dados fornece um conjunto de políticas e regras que auxilia a organização no momento de decidir os níveis e critérios de acesso a um sistema de forma hierarquizada.

Ela é de extrema importância, pois serve como guia em um processo difícil como este, já que a má definição e execução dos papéis e critérios geram falhas de segurança.

## 1.3 Políticas de segurança 

As políticas de segurança, quando aplicadas, ajudam a garantir a proteção dos dados sob a responsabilidade da empresa conforme a LGDP. Elas relatam o que fazer para mitigar riscos, prevenir incidentes e tratar os dados da maneira correta.

### 1.3.1 Medidas de segurança implementadas

Existem 3 principais formas que ajudam a garantir um alto nível de segurança no sistema, e portanto, nos dados, sendo elas:
- **Criptografia:** existem vários tipos de criptografia, sendo que cada uma foca em proteger algo diferente, porém, é essencial que por trás ela utilize a criptografia assíncrona. Isso se dá porque esse tipo de criptografia emprega duas chaves, uma pública e uma privada, o que garante mais segurança aos dados do sistema. Além disso, existe uma criptografia específica para dados, que se chama AES, e deve ser levada em consideração;
- **Autenticação:** o ideal é que a autenticação seja multifatorial (MFA), pois esta adiciona uma camada extra de proteção, já que obriga o usuário a comprovar sua identidade duas ou mais vezes;
- **Monitoramento contínuo:** fazer o uso de ferramentas de monitoração automatizadas a todo momento, pois quando elas detectam comportamentos estranhos como tentativa de invasão, acesso não autorizado, SQL injection entre outros, já enviam um alerta para os profissionais de segurança, que irão lidar com o incidente;

É recomendado que a CosmeticCo aplique essas medidas de segurança para que os seus dados estejam seguros. Ainda assim, não significa que só isso é suficiente, outras medidas além dessas devem ser consideradas também.

### 1.3.2 Gestão de incidentes

Além das medidas de segurança, é necessário que a empresa estabeleça um plano de resposta aos incidentes, para que o sistema não sofra nenhum prejuízo. Normalmente, esse processo é dividido em 4 partes:
- **Detecção de incidentes:** as ferramentas automatizadas de monitoração ou os próprios analistas detectam comportamentos estranhos no sistema, o que cria alertas de incidente;
- **Resposta rápida:** ao receber esse alerta, a equipe de segurança se dedica para investigar a origem do ataque, entender o que ocorreu, conter a ameaça e mitigar os danos;
- **Notificação do incidente:** seguindo as normas da LGPD, a empresa deve notificar os titulares dos dados afetados e as autoridades competentes dentro do prazo regulamentar, garantindo transparência;
- **Mitigação e recuperação:** após a contenção do incidente, é importante que a empresa realize modificações no sistema para que o ataque não ocorra novamente;

Seguindo esses 4 passos, a CosmeticCo já irá conseguir lidar de forma completa e ética com um possível incidente que ocorra no sistema, trazendo mais confiança aos seus clientes.

### 1.3.3 Treinamento e conscientização dos funcionários

A maior brecha de segurança de uma empresa são os próprios colaboradores, e por isso é extremamente fundamental que eles sejam treinados sobre as formas de ataques que podem os atingir.

Um treinamento muito realizado no mundo corporativo é o de phishing, que é quando o atacante utiliza da engenharia social para fazer com que o funcionário clique em um link malicioso, por exemplo.

Conscientizar os colaboradores da empresa deixará seus dados menos expostos e ainda vai garantir a segurança tanto corporativa, como individual. Por isso, é imprescindível que a CosmeticCo realize treinamentos com seus funcionários.

### 1.3.4 Conclusão

Acima foram citadas diversas formas de compor a política de segurança de uma corporação, e é importante que elas sejam seguidas, mas apenas isto não basta. A cada dia os atacantes estão com tecnologias mais novas e descobrem novos jeitos de hackear os sistemas, por isso, é importante que a CosmeticCo esteja sempre atualizada de quais tecnologias e políticas novas pode implementar para constantemente evoluir a segurança da sua empresa.

## 1.4 Outros aspectos da governança de dados

Além de todas as práticas que foram citadas até agora, existem alguns outros aspectos da governança de dados que também são importantes e recomenda-se que sejam considerados pela empresa parceira.
- **Qualidade dos dados:** é importante que os dados mantenham sua integridade, ou seja, precisam ser precisos, completos, tratados e atualizados conforme necessidade;
- **Ciclo de vida dos dados:** com a grande quantidade de dados gerada hoje, é comum que depois de um tempo eles necessitem serem descartados. Por isso, a empresa precisa definir como irá gerenciar o ciclo de vida dos mesmos, desde a coleta até o descarte, garantindo que todo o processo ocorra de forma segura;
- **Metadados:** é ideal que existam profissionais para interpretar os dados para as diferentes linguagens da empresa, e permitir que diretores ou colaboradores com cargos mais altos compreendam o que eles querem transparecer;

Ainda assim, é recomendado que a CosmeticsCo explore outros aspectos da governança de dados além dos citados acima, para obter documentações e processos mais completos.

## 1.5 Conclusão geral

Em resumo, a implementação de uma estrutura sólida de governança de dados, alinhada às exigências da LGPD, é essencial para garantir a segurança, privacidade e integridade das informações na CosmeticCo. Além disso, as práticas relatadas nesta sessão fortalecem a confiança e o posicionamento competitivo da empresa no mercado, o que atrai mais clientes.

# 2. Políticas de Uso dos Dados

A Política de Proteção de Dados Pessoais é um normativo institucional que tem o papel de estabelecer regras e diretrizes para gestão e controle de dados pessoais dentro do nosso projeto. Estipular papéis e responsabilidades claras e objetivas, definir diretrizes de tratamento e estabelecer meios de monitoramento do cumprimento da política são processos muito importantes para garantir a privacidade e a proteção de dados pessoais custodiados pela organização.

A presente política de uso de dados, visa auxiliar na elaboração da Política de Proteção de Dados em atendimento ao previsto na Lei Geral de Proteção de Dados Pessoais (LGPD). Ela determina que ao prestar diversos serviços que tratam dados pessoais à sociedade, deve, no âmbito de suas competências, formular regras de boas práticas e de governança que estabeleçam as condições de organização, o regime de funcionamento, os procedimentos, incluindo reclamações e petições de titulares, as normas de segurança, os padrões técnicos, as obrigações específicas para os diversos envolvidos no tratamento, as ações educativas, os mecanismos internos de supervisão e de mitigação de riscos e outros aspectos relacionados ao tratamento de dados pessoais. Adicionalmente, essa elaboração da Política de uso de Dados Pessoais visa a atender, além da LGPD, a outros normativos vigentes sobre o tema de privacidade e proteção de dados.

Essa política tem como referência fundamental o Programa De Privacidade 
e Segurança da Informação (PPSI), um modelo de Política de Proteção de Dados Pessoais baseado em diversas publicações e documentos técnicos já existentes que são utilizados amplamente por profissionais da área de privacidade e segurança da informação. Destacam-se as publicações do Center for Internet Security (CIS), da International Organization for Standardization (ISO) e do National Institute of Standards and Technology (NIST).

## 2.1 Propósito da Política

O objetivo desta política de uso de dados é garantir que todos os dados coletados, processados e analisados no âmbito do projeto "Assistente de Vendas Hiper Personalizado" do Inteli sejam utilizados de forma ética, segura e eficiente. A política visa proteger a privacidade e a confidencialidade dos dados dos colaboradores, gerentes e vendedores das lojas, bem como garantir o uso responsável de dados operacionais e financeiros, ao mesmo tempo em que maximiza o valor desses dados para melhorar a performance e o engajamento dos vendedores. Especificamente, esta política estabelece diretrizes claras sobre como os dados, incluindo dados de transações, informações de produtos, estoques, metas de vendas e outros dados relevantes, serão utilizados, processados e protegidos. Ela também define quais dados serão excluídos ou anonimizados, em conformidade com as melhores práticas de governança de dados e a legislação vigente, para maximizar o valor desses dados no aumento da performance e engajamento dos vendedores.

## 2.2 Escopo, amplitude e alcance da Política

Esta política se aplica a todas as etapas do módulo estrutura e governança para análise de dados para o assistente de Vendas Hiper Personalizado, abrangendo o ciclo completo de vida dos dados, desde a coleta e armazenamento até o processamento, análise e visualização final. O escopo da política inclui todas as tabelas de dados fornecidas, como as que contêm informações sobre vendas, estoque, produtos, categorias, status de SKUs, custos, preços, metas de vendas, e transações, além dos dados pessoais de colaboradores das lojas.

A política cobre também o uso de ferramentas e técnicas de análise de dados, incluindo métodos de anonimização e proteção de dados sensíveis e pessoais, garantindo que as práticas de uso de dados estejam alinhadas com os objetivos estratégicos do projeto e os requisitos acadêmicos.

No contexto de um projeto acadêmico do Instituto de Tecnologia e Liderança (Inteli), o alcance desta política é restrito às atividades necessárias para o desenvolvimento, teste e avaliação da solução proposta, englobando tanto dados pessoais quanto operacionais e financeiros. Qualquer uso dos dados fora do escopo do projeto acadêmico ou para fins comerciais está estritamente proibido, salvo indicação contrária e mediante autorização apropriada.

## 2.3 Termos e Definições

- **Dado pessoal:** informação relacionada a pessoa natural identificada ou identificável; 
 
- **Dado pessoal sensível:** dado pessoal sobre origem racial ou étnica, convicção religiosa, opinião política, filiação a sindicato ou a organização de caráter religioso, filosófico ou político, dado referente à saúde ou à vida sexual, dado genético ou biométrico, quando vinculado a uma pessoa natural;

- **Dados Confidenciais:** Informação restrita, que exige medidas de proteção específicas para prevenir acesso não autorizado ou divulgação indevida. Estes dados podem incluir, mas não se limitam a, informações comerciais sensíveis, segredos industriais, dados pessoais sensíveis (como definidos anteriormente), e quaisquer outras informações que possam comprometer a privacidade, segurança ou interesses comerciais e pessoais se reveladas inadequadamente.

- **Dados Públicos:** Informação que está disponível para acesso por qualquer pessoa, sem restrições ou necessidade de autorização prévia. Estes dados incluem, mas não se limitam a, registros de domínio público, dados estatísticos abertos, e quaisquer outros dados que sejam acessíveis ao público em geral, seja por meio de publicações oficiais, plataformas digitais ou outros meios de comunicação amplamente acessíveis.

- **Tratamento:** toda operação realizada com dados, como as que se referem a coleta, produção, recepção, classificação, utilização, acesso, reprodução, transmissão, distribuição, processamento, arquivamento, armazenamento, eliminação, avaliação ou controle da informação, modificação, comunicação, transferência, difusão ou extração.
 
- **Uso compartilhado de dados:** comunicação, difusão, transferência internacional, interconexão de dados pessoais ou tratamento compartilhado de bancos de dados pessoais por órgãos e entidades públicos no cumprimento de suas competências legais, ou entre esses e entes privados, reciprocamente, com autorização específica, para uma ou mais modalidades de tratamento permitidas por esses entes públicos, ou entre entes privados.

## 2.4 Classificação e Gestão de Dados

### 2.4.1 Políticas de Classificação

Os dados serão classificados de acordo com sua sensibilidade e importância para a organização, utilizando as seguintes categorias:

- **Dados Sensíveis:** Incluem informações pessoais identificáveis (PII) de colaboradores, dados de remuneração e transações financeiras. Estes dados terão o mais alto nível de proteção e serão acessíveis apenas por indivíduos autorizados.

- **Dados Confidenciais:** Incluem informações de desempenho de vendas, metas e estratégias de vendas. Estes dados serão protegidos com controles de acesso rigorosos, mas estarão disponíveis para análise por gerentes e diretores.

- **Dados Públicos:** Incluem informações sobre produtos, estoques e preços que são compartilhadas publicamente. Estes dados, embora protegidos, terão um nível de acesso mais aberto.

### 2.4.2 Gestão de Dados

A gestão dos dados é crucial para garantir que diferentes tipos de dados sejam tratados de acordo com sua sensibilidade e importância. Este item deve descrever como os dados fornecidos (como informações de transações, estoque e colaboradores) serão geridos para maximizar sua utilidade e minimizar riscos, como a perda de dados ou violações de privacidade.

- **Catalogação:** Todos os conjuntos de dados disponibilizados serão catalogados e descritos em um repositório de dados centralizado. Este catálogo incluirá a origem, proprietário, e regras de acesso para cada conjunto de dados, além da documentação neste mesmo documento.

- **Ciclo de Vida:** Os dados serão geridos ao longo de todo o seu ciclo de vida, desde a criação/coleta até o arquivamento. Políticas específicas serão estabelecidas para cada fase do ciclo de vida dos dados.

- **Geração de novas informações e variáveis:** Para atender e resolver o problema identificado pelo nosso parceiro, iremos gerar novas informações como parte do processo de tratamento e análise das informações. Essas novas variáveis serão cruciais não apenas para fornecer insights valiosos que orientem nossa solução, mas também para enriquecer a experiência dos usuários finais da aplicação.

A criação dessas novas informações da CosmeticCo permitirá uma personalização ainda maior das informações já apresentadas, garantindo que os vendedores e gerentes recebam recomendações e análises sob medida para suas necessidades específicas. Além disso, esses dados servirão como uma base robusta para a tomada de decisões estratégicas do parceiro.

## 2.5 Políticas de Retenção e Descarte de Dados

Esta política estabelece as diretrizes para a retenção e o descarte dos dados utilizados no projeto. O objetivo é garantir que os dados sejam mantidos apenas pelo período necessário para cumprir os objetivos comerciais e legais, minimizando os riscos associados ao armazenamento excessivo de informações.

Essa retenção é focada exclusivamente no banco de dados do warehouse com o ClickHouse, pois armazenar grandes volumes de dados não analisados ou utilizados pode gerar custos desnecessários. Em contrapartida, os dados raw em nosso datalake terão um período de retenção indefinido, visto que o custo de manter os buckets é significativamente baixo e não representa um risco financeiro relevante.

- **sku_store_stock:** Retenção por 24 meses a partir do final do ano correspondente para análises históricas de estoque e tendências de demanda.

- **sku_category, sku, sku_status:** Retenção indefinida, enquanto os produtos estiverem ativos, com revisão anual para descontinuação.

- **sku_cost, sku_price:** Retenção por 36 meses, permitindo a análise de margens de lucro e variações de preço ao longo do tempo.

- **employee:** Dados de colaboradores ativos são mantidos enquanto estiverem empregados; dados de ex-colaboradores são retidos por 12 meses após a saída para fins de auditoria.

- **store:** Retenção indefinida enquanto a loja estiver ativa, com revisão bianual.

- **targets:** Retenção por 12 meses após o término do período de avaliação, permitindo análises de desempenho e projeções de remuneração.

- **transactions:** Retenção por 60 meses para cumprir exigências legais e permitir análises de longo prazo.

Os dados que atingirem o fim de seu período de retenção serão descartados de forma segura e irreversível. Isso inclui a exclusão dos registros no Warehouse e backups para evitar a recuperação dos dados.

A política de retenção está alinhada com as exigências da LGPD e outras regulamentações aplicáveis, garantindo que os dados pessoais sejam mantidos apenas pelo tempo necessário para cumprir suas finalidades originais.

## 2.6 Política de uso dos dados disponibilizados

Esta seção define as diretrizes para o uso adequado dos dados fornecidos para o projeto. O objetivo é garantir que todos os dados sejam utilizados de maneira responsável, alinhada aos objetivos do projeto e em conformidade com as regulamentações de proteção de dados.

### 2.6.1 Descrição dos registros

- **sku:** Informações sobre cada SKU, incluindo identificadores, descrições e atributos específicos.

- **sku_status:** Status dos SKUs, que identifica se o produto ainda está em vendas nas lojas.

- **sku_cost:** Detalhes sobre os custos de aquisição de cada SKU, utilizados para cálculo de margem.

- **sku_price:** Preços de venda de cada SKU, atualizados conforme necessário para as análises.

- **employee:** Dados dos colaboradores, incluindo nome, cargo, status, loja e atributos específicos.

- **store:** Informações sobre as lojas, como região, identificadores e diretoria.

- **targets:** Metas de vendas atribuídas a cada vendedor, incluindo os mês e ano de comparação.

- **transactions:** Registros de transações de vendas, detalhando o SKU, a quantidade vendida, o valor e a data da transação.


### 2.6.2 Uso Permitido

O uso dos dados disponibilizados é permitido exclusivamente para fins acadêmicos e atende mas não se limita as seguintes finalidades:

- **sku:** Categorização de produtos, segmentação de mercado e suporte à personalização de ofertas.

- **sku_status:** Monitoramento do ciclo de vida dos produtos e ajustes na estratégia de vendas.

- **sku_cost, sku_price:** Cálculo de margens de lucro, análises de rentabilidade e ajuste de preços de venda.

- **employee:** Projeções de remuneração, com foco na melhoria do desempenho individual.

- **store:** Análise comparativa entre lojas, identificação de oportunidades de melhoria e planejamento estratégico.

- **targets:** Avaliação do desempenho dos vendedores, projeção de bônus e alinhamento das metas corporativas.

- **transactions:** Análise de comportamento de compra, identificação de padrões de venda e suporte a campanhas de marketing.

### 2.6.3 Dados Sensíveis e Uso Restrito

Alguns dos dados fornecidos são considerados sensíveis e devem ser tratados com cuidados adicionais e todos eles estão contidos na tabela de employee:

Informações pessoais, como nome e cargo, serão acessíveis apenas para fins de personalização de relatórios e projeções de remuneração e meta. Os dados de cargo, data de entrada na empresa e data de saída serão tratados como informações confidenciais e acessíveis apenas a indivíduos com permissões adequadas. Os outros dados pessoais sensíveis somente serão visíveis ao parceiro e aos integrantes do grupo do projeto. Os dados de status, cargo e regionais poderão ser utilizados de forma não individualizada para fins estritamente estatísticos.

### 2.6.4 Tratamento das informações

As informações fornecidas pelo parceiro são registradas e armazenadas em nossos bancos de dados Warehouses e Datalakes, observados os necessários padrões de segurança, confidencialidade e integridade, e somente serão utilizadas para as finalidades próprias do projeto.

As informações de caráter pessoal ou confidencial são tratadas de acordo com a legislação vigente. O acesso a estas informações só poderá ser efetuado pelo oficial responsável pela tutoria da CosmeticCo, pelo parceiro do projeto fornecedor ou pelos próprios integrantes do grupo em relação as informações que lhe auxiliem a análise de dados.

O compartilhamento, cessão ou divulgação, onerosa ou gratuita, de tais informações a terceiros ou a sua utilização para finalidades diversas daquelas para as quais foram coletadas, não poderá ocorrer em virtude de nenhuma razão.

## 2.7 Coleta de Dados

### 2.7.1 Tipos de Dados Coletados

Os dados coletados incluem registros operacionais da CosmeticCo como estoque, transações, e dados de colaboradores. Novas informações e variáveis gerados vão incluir métricas de desempenho, projeções de vendas, e perfis de comportamento de compra, eles serão especificados no tópico 2.7.1.

## 2.8 Finalidade da Coleta e da geração dos novos dados

### 2.8.1 Uso dos Dados

Os dados coletados e gerados são utilizados para as seguintes finalidades:

- **Personalização de Recomendações:** Ajustar as sugestões de vendas e estratégias de acordo com o perfil de cada vendedor, loja e produtos.

- **Projeções de Desempenho:** Estimar e fazer uma projeção do desempenho futuro dos vendedores com base em tendências históricas e metas estabelecidas.

- **Simulações de Remuneração:** Permitir que vendedores projetem seus ganhos futuros com base em diferentes cenários de sazonalidade de vendas.

- **Análise Comparativa:** Facilitar a comparação de desempenho entre diferentes vendedores e lojas, incentivando a melhoria contínua.

- **Acompanhamento de Metas:** Monitorar o progresso dos vendedores e gerentes em relação às metas estabelecidas, permitindo ajustes estratégicos em tempo real.

- **Visualização Gráfica de Remuneração:** Representar graficamente os diferentes componentes da remuneração, como comissões e bonificações, para facilitar a compreensão e otimização dos ganhos.

- **Recomendações de Produtos Substitutos:** Oferecer sugestões de produtos alternativos quando um item desejado não estiver disponível, ajudando a manter as vendas e a satisfação do cliente.

- **Ranking de Desempenho:** Exibir um ranking de vendas para vendedores, promovendo uma competição saudável e o engajamento.

- **Gestão de Estoque:** Permitir consultas em tempo real na base de estoque, auxiliando no controle e na reposição de produtos, para evitar rupturas e maximizar as vendas.

- **Margem de Lucro Otimizada:** Destacar produtos com maior margem de lucro, orientando os vendedores a focarem em itens que aumentem a rentabilidade da empresa.

### 2.8.2 Bases Legais

O tratamento dos dados neste projeto está fundamentado nas seguintes bases legais, conforme a LGPD:

- **Legítimo Interesse:** O uso de dados para melhorar o desempenho das vendas e o engajamento dos colaboradores está alinhado ao legítimo interesse da CosmeticCo em maximizar suas operações.

- **Consentimento:** Como os dados foram fornecidos pelo parceiro que mantém contato direto com a CosmeticCo, entende-se que o consentimento explícito dos colaboradores foi obtido para o uso de seus dados em análises personalizadas.

## 2.9 Atualizações da Política

A política de uso de dados será revisada periodicamente para garantir a relevância e conformidade com as mudanças legais e operacionais que acontecem nesse período de desenvolvimento. Alterações significativas nos objetivos do projeto, nos dados, na legislação de proteção de dados ou nos processos de tratamento de dados poderão motivar revisões adicionais fora do cronograma a cada duas semanas. Todas essas atualizações serão documentadas e comunicadas aos parceiros e orientadores para garantir a transparência e a adesão contínua às diretrizes aqui estabelecidas estabelecidas.

# 3. Medição da Qualidade dos Dados

## 3.1 Introdução
A qualidade dos dados é essencial para garantir que as análises realizadas e os insights extraídos sejam precisos e confiáveis. No contexto do projeto "Assistente de Vendas Hiper Personalizado" para a empresa de cosméticos, este documento detalha os processos e métricas aplicados para medir e assegurar a qualidade dos dados fornecidos. Nosso objetivo é garantir que os dados sejam consistentes, completos, precisos, atualizados e relevantes para a tomada de decisões estratégicas.

## 3.2 Objetivos da Medição da Qualidade dos Dados

* **Assegurar a Confiabilidade dos Dados:** Garantir que os dados utilizados nas análises estejam livres de erros, inconsistências ou desatualizações. Isso inclui práticas como a eliminação de outliers, normalização de dados númericos e o tratamento de dados faltantes, que são fundamentais para evitar vieses e assegurar que as análises e algoritmos de aprendizado de máquina baseiem-se em informações precisas.

* **Estabelecer Governança de Dados:** Implementar processos contínuos e automatizados de governança que monitorem e aprimorem a qualidade dos dados ao longo do tempo. Esses processos garantem a preparação adequada dos dados para uso em decisões empresariais, minimizando retrabalhos e assegurando que cada camada de dados (bronze, prata e ouro) seja mantida com alta qualidade. Dessa forma, O uso de 'jobs' automáticos que coletam e revalidam os dados poderia ser aplicado para assegurar que os dados sejam periodicamente verificados e corrigidos antes de avançarem para camadas de análise e visualização.

* **Identificar e Corrigir Anomalias:** Detectar e corrigir proativamente anomalias, como valores ausentes ou duplicados,de modo a manter a integridade dos dados e a confiabilidade das previsões dos algoritmos de aprendizado de máquina. Para reforçar esse processo, os 'jobs' automáticos atuam como uma camada adicional de segurança, identificando anomalias que possam ter escapado ao tratamento inicial e garantindo que os dados sejam continuamente revisados e corrigidos em conformidade com os padrões de qualidade estabelecidos.

## 3.3 Critérios de Qualidade dos Dados

Os dados fornecidos serão avaliados com base nos seguintes critérios:

* **Completude:** Avaliar se todos os dados necessários estão presentes, especialmente nas colunas críticas como `sku_id`, `cod_produto`, `cod_transacao`, `cod_vendedor`, `cod_loja`, `data`, `quantidade`, `preco` e `target`. Essas são colunas consideradas críticas pois fazem parte do processo de transação de vendas e acompanhamento de métrica, ponto principal de observação do projeto
* **Consistência:** Garantir que os dados sejam consistentes entre diferentes fontes e ao longo do tempo. Por exemplo, o mesmo `sku_id` deve ter uma descrição consistente em todas as bases, embora em algumas tabelas ele apareça com o nome de `cod_prod`.
* **Atualização:** Certificar-se de que os dados estão atualizados e refletem o estado atual, com especial atenção às colunas que registram a passagem do tempo, como `initial_date` e `end_date`, e aquelas que indicam o status, como `status`.
* **Relevância:** Assegurar que os dados armazenados são relevantes para as análises e decisões necessárias. Colunas como `descricao_produto`, embora sejam importantes para entendimentos dos dados, não agregam valor a uma medição quantitativa voltada para negócios.

## 3.4 Processos de Medição e Garantia de Qualidade

Implementação de procedimentos sistemáticos para avaliar a precisão e a consistência dos dados ou produtos ao longo do ciclo de vida do projeto. Esses processos garantem que os padrões de qualidade sejam mantidos, detectando e corrigindo possíveis desvios antes que afetem os resultados finais, promovendo a confiança nos dados e nas decisões tomadas com base neles.

### 3.4.1 Auditoria de Dados

A auditoria de dados será realizada em três fases:
* **Fase Inicial:** Verificação básica de completude e presença de dados ausentes.
    * <u>Métrica:</u> Percentual de valores ausentes por coluna.
    * <u>Ferramentas:</u> Uso de scripts em R ou Python para identificar valores NA ou nulos.
* **Fase Intermediária:** Análise de consistência entre bases e detecção de duplicatas.
    * <u>Métrica:</u> Taxa de duplicação de registros e consistência de chaves primárias (ex. sku_id e store_id).
    * <u>Ferramentas:</u> Queries SQL e scripts de validação cruzada.
* **Fase Final:** Assegurar que os dados presentes na base são precisos, relevantes e alinhados com informações verificáveis do mundo real, garantindo a integridade das análises e decisões baseadas nesses dados. Uma forma de aplicação dessa prática seria validar se os dados de transações salvos no banco de dados estão de acordo com as análises de auditoria fiscal da empresa, de modo a garantir que não hajam conflitos entre essas fontes de informação.
    * <u>Métricas:</u>
        * Taxa de Conformidade com Fontes Externas: Percentual de registros que coincidem exatamente com as informações fornecidas por fontes externas confiáveis, como empresas de auditoria.
        * Índice de Correção de Dados: Percentual de registros corrigidos após validação manual ou automatizada com fontes oficiais.
    * <u>Ferramentas:</u>
        * Machine Learning para Detecção de Anomalias: Scripts automatizados de observabilidade serão integrados ao Prometheus e Grafana para monitorar mudanças nos dados e notificar sobre anomalias em tempo real. Essa abordagem garante uma visualização contínua do fluxo de dados e a rápida identificação de inconsistências, promovendo uma resposta proativa e garantindo a qualidade e integridade dos dados.
        * Amostragem Estatística: Utilização de software estatístico para selecionar amostras representativas dos dados para revisão manual

### 3.4.2 Monitoramento Contínuo

Um sistema de monitoramento contínuo, como o Grafana, será implementado para assegurar a manutenção da qualidade dos dados ao longo do tempo e proporcionar maior observabilidade dos processos na esteira de tratamento de dados. Isso permitirá a identificação proativa de problemas e a análise em tempo real dos indicadores de qualidade, garantindo maior confiabilidade e eficiência nas operações.
* <u>Métrica:</u> Relatórios semanais de qualidade dos dados, com foco em alterações inesperadas.
* <u>Ferramentas:</u> Ferramentas de BI e scripts automatizados de observalidade integrados com  que monitoram mudanças nos dados e notificam sobre anomalias.

### 3.4.3 Governança de Dados

Será estabelecido um comitê de governança de dados que se reunirá regularmente para revisar a qualidade dos dados, discutir possíveis problemas e implementar melhorias contínuas.
* <u>Métrica:</u> Frequência de reuniões do comitê e número de ações corretivas implementadas.
* <u>Ferramentas:</u> Documentação de governança e plano de ações.

### 3.5 Análise dos Resultados

Os resultados da medição de qualidade dos dados serão documentados e apresentados aos stakeholders em relatórios mensais. O foco será em áreas que necessitam de melhorias e em como as ações corretivas implementadas estão impactando a qualidade geral dos dados.

### 3.5.1 Melhoria Contínua

Com base nos resultados das auditorias e do monitoramento contínuo, serão identificadas áreas de melhoria. A cada ciclo de revisão, o processo de qualidade dos dados será ajustado para abordar novas ameaças à integridade e relevância dos dados.

### 3.6 Conclusão

A implementação de um processo robusto de medição da qualidade dos dados é essencial para o sucesso do projeto "Assistente de Vendas Hiper Personalizado". Ao garantir a qualidade dos dados, asseguramos que as análises e insights gerados serão precisos e confiáveis, promovendo o sucesso das operações e o alcance das metas estratégicas da empresa em questão.

<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://embed.figma.com/design/SVRRy0tBmJXB38MrwAyDII/DataLoom?embed-host=share" allowfullscreen></iframe>