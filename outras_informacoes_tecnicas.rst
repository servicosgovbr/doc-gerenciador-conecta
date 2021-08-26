.. _secao-outras-informacoes-tecnicas:

############################
Outras Informações técnicas
############################
Esta seção destina-se a incluir outras informações técnicas pertinentes para a plataforma.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. Quais as principais etapas técnicas para adaptar uma API já existente para sua inclusão no Gerenciador de APIs?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Em geral, a equipe do Conecta deverá:

    #. Solicitar a implementação de um Adapter para integrar com a API que fornecerá o serviço de forma a atender os seguintes requisitos:

       * Padronizar o serviço disponibilizado como um REST (suportado pelo API Manager);
       * Padronizar códigos de erros conforme demais serviços disponibilizados pelo Conecta;
       * Realizar transformações necessárias para serviços que não tenham o dado com o formato pronto para o consumo;
       * Disponibilizar composição de serviço em um único serviço REST com dados que estejam disponíveis em serviços fornecedores distintos.

    #. Subscrever o Adapter construído no API Manager do Conecta;

    #. Cadastrar o órgão que está fornecendo o serviço como órgão fornecedor no Portal de Gestão;

    #. Criar uma documentação Swagger do serviço disponibilizado para os consumidores terem como referência de uso no padrão Conecta;

    #. Definir o “Rate Limit” de acesso simultâneos para o serviço disponibilizado.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
2. O que é o Gerenciador de APIs?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Um Gerenciador de APIs (Application Programming Interface) é uma ferramenta que implementa uma camada de gestão sobre uma API, permitindo seu gerenciamento. Este gerenciamento envolve, dentre outros, o processo de criação e publicação, de acordo com suas políticas de uso, controlando o acesso, coletando e analisando estatísticas de uso e disponibilizando relatórios de desempenho.

Algumas das funções de um Gerenciador de APIs são:
   * Ponto único de acesso à APIs disponibilizadas, se colocando entre uma API e o serviço público ou sistema que deseja acessar a API.
   * Mecanismos de segurança, que incluem autenticação de usuário e logs de acesso.
   * Controle de acesso baseado em usuário, que permite limitar o acesso do usuário a determinado recurso baseado nas mais diversas premissas, como números de requisições no mês ou nos últimos 10 segundos.
   * Relatórios estatísticos de uso das APIs.
   * Filtragem de dados na entrada, podendo redirecionar o chamado à API para o local correto, baseado nos mais diferentes parâmetros de entrada, e, até mesmo, ignorar a requisição caso seja desejado, sem levar tráfego à sua API.
