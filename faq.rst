.. _secao-faq:

.. _url-roteiro-geracao-chaves-acesso: https://gov.br/conecta/gerenciador-documentacao/manual_recebedor_dados.html#roteiro-geracao-chaves-acesso

########################
Perguntas frequentes
########################

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. Consigo utilizar uma única chave de acesso para diferentes aplicações?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      Não. Cada concessão de acesso dada gera uma chave diferente independente.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
2. Caso o gestor responsável técnico que gerou as chaves de acesso das aplicações se desligue do órgão, as chaves de acesso deixam de funcionar?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

      Não. Para que não haja interrupção dos sistemas não serão desabilitadas as chaves mas recomenda-se que o órgão solicite a desativação do gestor na plataforma e proceda a substituição das chaves assim que possível.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
3. É a primeira vez que estou adequando meus sistemas ao uso das APIs, por que não está funcionando?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

      Caso seja a primeira integração desenvolvida para acesso a uma API através do Gerenciador do Conecta, é necessário previamente cadastrar os IPs do órgão para que se proceda a criação de regra de firewall no Serpro que libere o acesso à Plataforma.​

.. _faq-erro-autorizacao-ip:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
4. Estou recebendo erro 403 em Produção.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

      Se você está recebendo erro 403 quando tenta acessar alguma API do Conecta em Produção, isso ocorre pois o IP de saída do órgão não está cadastrado no Serpro. Dessa forma, o órgão deverá enviar a faixa de IP de saída para o email: conecta@economia.gov.br, para que se proceda a criação de regra de firewall no Serpro.​
      
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
5. Estou recebendo erro 401
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

      O erro HTTP 401 Unauthorized indica que a solicitação não foi aplicada porque não possui credenciais de autenticação válidas para o recurso de destino.
Você deve verificar se a credencial utilizada é válida para o ambiente (Homologação, Produção) que está fazendo a chamada e para a API acessada.​

.. note:: Para geração das chaves de acesso, consulte :ref:`Roteiro para geração das chaves de acesso <roteiro-geracao-chaves-acesso>`.

