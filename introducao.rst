Introdução
============

Solução de gerenciamento para facilitar a disponibilização e o consumo de APIs e promover a interoperabilidade de dados entre Órgãos Públicos Federais.

A ideia do Gerenciador de APIs é facilitar a interoperabilidade de dados para os órgãos Provedores de Dados e o consumo das APIs para os órgãos Recebedores de Dados por meio de várias funcionalidades como a gestão do acesso às APIs, a proteção da infraestrutura, o controle de consumo e disponibilização de um ponto único de acesso à APIs.


Pré-requisitos Técnicos para disponibilizar minha API na Plataforma
-------------------------------------------------------------------------

.. important::
    1. Deve estar disponível na internet através do protocolo https;
    2. Deve ser disponibilizada a documentação do serviço, preferencialmente no formato OpenAPI (ver Referências para Documentação de APIs);
    3. Deve ser disponibilizado ambiente de teste/homologação (não produtivo) para que seja possível testar a integração;
    4. Devem ser disponibilizadas credenciais de acesso, caso necessárias, para os ambientes de teste/homologação e produção;
    5. Deve ser cadastrado o certificado que foi fornecido pelo time do Conecta para que possa ocorrer o consumo do serviço, no caso onde a integração seja através de autenticação mútua;
    6. Deve ser informada a quantidade (capacidade) máxima de requisições por segundo que o serviço suporta;
    7. Deve ser definido o canal de comunicação com o suporte técnico do gestor do dado para que sejam informados possíveis problemas de indisponibilidade e/ou dúvidas durante a integração;
    8. Deve estar catalogada, ou em processo de catalogação, no catálogo do Conecta.


Gerenciador de APIs do Conecta
-------------------------------
.. image:: _imagens/arquitetura_conecta.png
   :scale: 75 %
   :align: center
   :alt: Figura da Arquitetura do Conecta.

O que você tem interesse no Conecta?
************************************

Quero receber Dados de outros órgãos (Acesse o Passo a Passo do Recebedor de Dados)
----------------------------------------------------------------------------------------
.. toctree::
   :maxdepth: 3
   :caption: Acesse o Passo a Passo do Recebedor de Dados

   recebedordados

Quero disponibilizar Dados para outros órgãos (Acesse o Passo a Passo do Provedor de Dados)
-------------------------------------------------------------------------------------------
.. toctree::
  :maxdepth: 3
  :caption: Acesse o Passo a Passo do Provedor de Dados

  provedordedados