.. _secao-outras-informacoes-tecnicas:

.. _roteiro-geracao-chaves-acesso:

############################
Outras Informações técnicas
############################
Esta seção destina-se a incluir outras informações técnicas pertinentes para a plataforma.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. Como acessar os dados das APIs solicitadas?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  O Conecta gov.br tem como base o protocolo de autorização OAuth 2. Logo o usuário deve seguir os seguintes passos para acessar os dados das APIs solicitadas:
  
    #. O usuário deve gerar as chaves de acesso (Chave e senha) conforme orientado no item `Roteiro para geração das chaves de acesso <https://gerenciador-conecta.readthedocs.io/manual_recebedor_dados.html#roteiro-geracao-chaves-acesso>`_ deste manual. Para a obtenção da chave de acesso do ambiente de homologação para o desenvolvimento da integração, os responsáveis técnicos do órgão, deverão seguir as informações técnicas que serão enviadas automaticamente pela Plataforma Conecta gov.br no momento do deferimento de acesso aos dados solicitados.
    
    #. O usuário deve realizar a chamada no endpoint de geração de tokens da Plataforma de Interoperabilidade Conecta gov.br. 
    
        * Endpoint Access Token URL de Produção: https://apigateway.conectagov.estaleiro.serpro.gov.br/oauth2/jwt-token
        * Endpoint Access Token URL de Homologação: https://h-apigateway.conectagov.estaleiro.serpro.gov.br/oauth2/jwt-token
      
    #. Após seguir as orientações do passo 1 e 2, o usuário receberá um retorno do Endpoint Access Token. Este resultado será o token de acesso para os dados da API que deseja utilizar. (Cada token gerado tem um prazo de validade de duas horas. Após este tempo, será necessário a geração de um novo token).
   
    #. O usuário deve fazer a chamada ao endpoint da API (Exemplo: https://apigateway.conectagov.estaleiro.serpro.gov.br/api-cep/v1/consulta/cep/ ) que deseja fazer o acesso e utilizar o token Bearer gerado no passo 3 como parâmetro de acesso!
    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1.1 Qual o limite de requisições em ambiente de homologação?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
O ambiente de homologação do Conecta gov.br é limitado a 1000 chamadas de teste por API. Caso seja necessário mais de 1000 requisições, é necessário que o órgão faça uma solicitação de aumento das solicitações com a devida justificativa. A solicitação deve ser enviada para conecta@economia.gov.br.

No momento o Conecta não tem ambiente específico para testes de carga.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
2. Quais as principais etapas técnicas para adaptar uma API já existente para sua inclusão no Gerenciador de APIs?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Em geral, a equipe do Conecta deverá:

    #. Solicitar a implementação de um Adapter para integrar com a API que fornecerá o serviço de forma a atender os seguintes requisitos:

       * Padronizar o serviço disponibilizado como um REST (suportado pelo API Manager);
       * Padronizar códigos de erros conforme demais serviços disponibilizados pelo Conecta;
       * Realizar transformações necessárias para serviços que não tenham o dado com o formato pronto para o consumo;
       * Disponibilizar composição de serviço em um único serviço REST com dados que estejam disponíveis em serviços fornecedores distintos.

    #. Subscrever o Adapter construído no API Manager do Conecta;

    #. Cadastrar o órgão que está fornecendo o serviço como órgão fornecedor no Portal de Gestão;

    #. Criar uma documentação Swagger do serviço disponibilizado para os recebedores terem como referência de uso no padrão Conecta;

    #. Definir o “Rate Limit” de acesso simultâneos para o serviço disponibilizado.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
3. O que é o Gerenciador de APIs?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Um Gerenciador de APIs (Application Programming Interface) é uma ferramenta que implementa uma camada de gestão sobre uma API, permitindo seu gerenciamento. Este gerenciamento envolve, dentre outros, o processo de criação e publicação, de acordo com suas políticas de uso, controlando o acesso, coletando e analisando estatísticas de uso e disponibilizando relatórios de desempenho.

Algumas das funções de um Gerenciador de APIs são:
   * Ponto único de acesso à APIs disponibilizadas, se colocando entre uma API e o serviço público ou sistema que deseja acessar a API.
   * Mecanismos de segurança, que incluem autenticação de usuário e logs de acesso.
   * Controle de acesso baseado em usuário, que permite limitar o acesso do usuário a determinado recurso baseado nas mais diversas premissas, como números de requisições no mês ou nos últimos 10 segundos.
   * Relatórios estatísticos de uso das APIs.
   * Filtragem de dados na entrada, podendo redirecionar o chamado à API para o local correto, baseado nos mais diferentes parâmetros de entrada, e, até mesmo, ignorar a requisição caso seja desejado, sem levar tráfego à sua API.
   





