.. :name: _secao-manual-gestor-conecta

########################################
Manual do Gestor do Conecta
########################################

    -  `O perfil Gestor da Plataforma <#o-perfil-gestor-da-plataforma>`__
    -  `Cadastro de Novo Órgão <#cadastro-de-novo-orgao>`__
    -  `Listar Órgãos <#listar-orgaos>`__
    -  `Adesões <#adesoes>`__
    -  `Cadastro de Gestor <#cadastro-de-gestor>`__
    -  `Listar Gestores <#listar-gestores>`__
    -  `Cadastro de Plano de Consumo <#cadastro-de-plano-de-consumo>`__
    -  `Listar Planos de Consumo <#listar-planos-de-consumo>`__
    -  `Relatório de consumo das APIs <#relatorio-de-consumo-das-apis>`__
    -  `Relatório de disponibilidade das APIs <#relatorio-de-disponibilidade-das-apis>`__
    -  `Relatório Gerencial <#relatorio-gerencial>`__
    -  `Relatório de Auditoria <#relatorio-de-auditoria>`__


------------------------------------------------------------------------------------------------
O perfil Gestor da Plataforma
------------------------------------------------------------------------------------------------
.. :name: o-perfil-gestor-da-plataforma

O gestor da Plataforma é o responsável por viabilizar o acesso dos órgãos às APIS disponibilizadas pelo Conecta.

O gestor da Plataforma têm acesso completo às funcionalidades de cadastro: cadastrar órgão, cadastrar gestor, cadastrar planos de consumo.

Além disso, também tem acesso a todos os relatórios disponíveis na ferramenta. Abaixo, segue a tela com uma visão geral de todos os menus disponíveis para o perfil gestor da plataforma.

|image0|


------------------------------------------------------------------------------------------------
Cadastro de Novo Órgão
------------------------------------------------------------------------------------------------
.. :name: cadastro-de-novo-orgao

A funcionalidade **Cadastro de Novo Órgão** pode ser acessada via menu conforme a tela abaixo: |image1|

Após selecionar a opção **Cadastro de Novo Órgão**, a seguinte tela será exibida para o usuário. |image2|

O gestor da plataforma preenche os campos e aciona o botão **Incluir**. Se tudo estiver de acordo, uma mensagem de sucesso da inclusão será exibida conforme mostra a tela abaixo. A partir da inclusão será possível **Alterar** os dados do Órgão ou gerenciar as **Adesões** do órgão incluído. |image3|

------------------------------------------------------------------------------------------------
Listar Órgãos
------------------------------------------------------------------------------------------------
.. :name: listar-orgaos

A partir da funcionalidade **Listar Órgãos** será possível exibir os órgãos cadastrados, inativar um determinado órgão e/ou alterar seus dados. |image4|

O preenchimento dos campos do filtro de pesquisa é opcional. O resultado da pesquisa será apresentado de forma paginada conforme mostrado abaixo. Em destaque, as opções de ativação/desativação e/ou alteração de um determinado órgão. |image5|

------------------------------------------------------------------------------------------------
Adesões
------------------------------------------------------------------------------------------------
.. :name: adesoes

Após cadastrar um órgão, o usuário poderá cadastrar às adesões (APIs x Planos) para o órgão em questão. Para tal, deverá acionar o botão **Adesões** logo após o cadastro do órgão como indicado anteriormente ou através da funcionalidade **Listar Órgãos** acessar o gerenciamento de adesões de um órgão qualquer como mostrado na figura abaixo: |image6|

. Após isso, a página a seguir será exibida. Se existirem adesões cadastradas, elas serão listadas. Caso contrário, o usuário poderá incluir ao acionar na opção **Incluir**. |image7|

------------------------------------------------------------------------------------------------
Cadastro de Gestor
------------------------------------------------------------------------------------------------
.. :name: cadastro-de-gestor

Para cadastrar um Gestor de Órgão o usuário com perfil Gestor da Plataforma deve selecionar a opção n**Cadastro de Novo Gestor**. |image8|

O gestor da plataforma seleciona o órgão e caso o órgão selecionado seja vinculado ao SIAPE será apresentada a tela abaixo onde é necessário preencher apenas o campo CPF e acionar o botão **Pesquisar Servidor**. |image9|

O sistema faz uma consulta ao Web Service do SIGEPE para recuperar os dados do Servidor. O SIGEPE retorna os dados e o usuário aciona o botão Incluir.

Caso o órgão selecionado **não** seja vinculado ao SIAPE, o cadastro deverá ser preenchido pelo Gestor da Plataforma , que deverá preencher todos os campos do cadastro de acordo com a tela abaixo: |image10|

A partir desse cadastro, o usuário gestor de órgão poderá acessar a Plataforma de Gestão de Acesso do CONECTA para fazer o cadastro da aplicação e geração das chaves de acesso para consumir a API.

**Observação:** se o órgão selecionado pelo usuário possuir alguma API cadastrada, será disponibilizada ao usuário uma lista para selecionar, opcionalmente, essas API’s. O gestor cadastrado será gestor das API’s selecionadas pelo usuário

------------------------------------------------------------------------------------------------
Listar Gestores
------------------------------------------------------------------------------------------------
.. :name: listar-gestores

Para listar os gestores o usuário deverá selecionar a opção **Listar Gestores**. |image11|

Através da funcionalidade **Listar Gestores** será possível fazer a inativação de um Gestor e/ou alterar seus dados. |image12|

------------------------------------------------------------------------------------------------
Cadastro de Plano de Consumo
------------------------------------------------------------------------------------------------
.. :name: cadastro-de-plano-de-consumo

Para cadastrar um novo Plano de Consumo, o usuário deverá selecionar a opção **Cadastro de Novo Plano de Consumo**. |image13|

O gestor da Plataforma preenche os campos e aciona o botão **Incluir**. Deverão ser preenchidos os seguintes campos:

-  **API** (Lista de seleção única das API cadastradas)
-  **Nome** (campo texto de até 50 caracteres)
-  **Limite** (valor inteiro numérico)

|image14|

Se tudo estiver de acordo, uma mensagem de sucesso da inclusão será exibida conforme mostra a tela abaixo. Caso queira fazer uma alteração no plano cadastrado, após a inclusão, basta clicar no botão **Alterar**.

|image15|

------------------------------------------------------------------------------------------------
Listar Planos de Consumo
------------------------------------------------------------------------------------------------
.. :name: listar-planos-de-consumo

Para listar os Plano de Consumo, o usuário deverá selecionar a opção **Listar Planos de Consumo**. A partir dessa funcionalidade será possível exibir os planos de consumo cadastrados, inativar um determinado plano e alterar seus dados. |image16|

O preenchimento dos campos do filtro de pesquisa é opcional. As opções do filtro são apresentadas na tela abaixo: |image17|

O resultado da pesquisa será apresentado de forma paginada conforme mostrado abaixo. Em destaque, as opções de ativação/desativação e/ou alteração de um determinado plano de consumo |image18|

------------------------------------------------------------------------------------------------
Relatório de consumo das APIs
------------------------------------------------------------------------------------------------
.. :name: relatorio-de-consumo-das-apis

A funcionalidade **Relatório de Consumo** pode ser acessada através do menu conforme a figura abaixo:
|image19|

O relatório permite que os dados sejam filtrados de acordo com o **órgão consumidor, api(todas ou uma específica), data inicial, data final**. Se desejar, o usuário poderá visualizar as informações de acordo com o consumo diário (basta marcar o campo **mostrar uso diário**). A base de dados do relatório de consumo é atualizada a cada 15(quinze) minutos. Para gerar um relatório, o usuário deverá preencher os campos do **filtro**\ (nenhum campo é obrigatório) e acionar o botão **Pesquisar** conforme mostrado na tela abaixo.

.. important::
  -  serão exibidas as APIs vinculadas à adesões (ativas ou não).
  -  se o usuário selecionar um órgão consumidor, a  lista será atualizada com as APIs vinculadas a adesões (ativas ou não) do órgão consumidor  selecionado.
  -  serão exibidos os órgãos vinculadas a adesões (ativas ou não).

|image20|

O **Relatório de Consumo** exibe as seguintes informações sobre o consumo de uma determinada API: **órgão, aplicação, api, período(mês/ano), limite do órgão, periodicidade, consumo**. Abaixo, segue um exemplo: |image21|

Após a geração do relatório será possível exportá-lo para os formatos **csv** e/ou **pdf**. Para tal, basta clicar no botão correspondente(**Relatório CSV ou
Relatório PDF**).

------------------------------------------------------------------------------------------------
Relatório de disponibilidade das APIs
------------------------------------------------------------------------------------------------
.. :name: relatorio-de-disponibilidade-das-apis

A funcionalidade **Relatório de Disponibilidade** pode ser acessada através do menu conforme a figura abaixo:
|image22|

O relatório permite que os dados sejam filtrados de acordo com o **api** e o **mês/ano**. Para gerar um relatório, o usuário deverá preencher os campos do **filtro**\ (todos os campos são obrigatórios) e acionar o botão **Pesquisar** conforme mostrado na tela abaixo. |image23|

O **Relatório de Disponibilidade** exibe as seguintes informações sobre a disponibilidade de uma determinada API: **data, api, disponibilidade**. Abaixo, segue um
exemplo: |image24|

Após a geração do relatório será possível exportá-lo para o formato **pdf**. Para tal, basta clicar no botão correspondente(**Relatório PDF**)..

------------------------------------------------------------------------------------------------
Relatório Gerencial
------------------------------------------------------------------------------------------------
.. :name: relatorio-gerencial

A funcionalidade **Relatório Gerencial** pode ser acessada através do menu conforme a figura abaixo:
|image25|

O relatório permite que os dados sejam filtrados de
acordo com o **órgão consumidor, api(todas ou uma
específica), plano de consumo (todos ou um
específico), data inicial, data final**. Para gerar um
relatório, o usuário deverá preencher os campos do
**filtro**\ (somente o campo **api** é obrigatório) e
acionar o botão **Pesquisar** conforme mostrado na
tela abaixo. |image26|

O **Relatório de Gerencial** exibe as seguintes
informações sobre a : **data, api, disponibilidade**.
Abaixo, segue um exemplo: |image27|

Após a geração do relatório será possível exportá-lo
para os formatos **csv** e/ou **pdf**. Para tal, basta
clicar no botão correspondente(**Relatório CSV ou
Relatório PDF**).

------------------------------------------------------------------------------------------------
Relatório de Auditoria
------------------------------------------------------------------------------------------------
.. :name: relatorio-de-auditoria

A funcionalidade **Relatório Auditoria** pode ser
acessada através do menu conforme a figura abaixo:
|image28|

O relatório permite que os dados sejam filtrados de
acordo com o **órgão consumidor, aplicação, api,
período inicial, período final**. O campo
**aplicação** só aparecerá após a seleção do
**órgão**. Para gerar um relatório, o usuário deverá
preencher os campos do **filtro**\ (todos os campos
são obrigatórios) e acionar o botão **Pesquisar**
conforme mostrado na tela abaixo.

.. important::
  -  serão exibidas as APIs vinculadas à adesões (ativas ou não).
  -  se o usuário selecionar um órgão consumidor, a lista será atualizada com as APIs vinculadas a adesões (ativas ou não) do órgão consumidor selecionado.
  -  serão exibidos os órgãos vinculadas a adesões (ativas ou não).

|image29|

O **Relatório de Auditoria** exibe as seguintes
informações sobre a : **órgão, cnpj do órgão,
responsável pela chave, usuário, data e hora do
acesso, endereço IP, aplicação, api**. Abaixo, segue
um exemplo: |image30|

Após a geração do relatório será possível exportá-lo
para os formatos **csv** e/ou **pdf**. Para tal, basta
clicar no botão correspondente(**Relatório CSV ou
Relatório PDF**).

.. |image0| image:: _imagens_portal_antigo/gestorSGD/telaInicialSGD.png
.. |image1| image:: _imagens_portal_antigo/gestorSGD/CadastroDeOrgaoMenu.png
.. |image2| image:: _imagens_portal_antigo/gestorSGD/CadastroDeOrgao1.png
.. |image3| image:: _imagens_portal_antigo/gestorSGD/CadastroDeOrgao2.png
.. |image4| image:: _imagens_portal_antigo/gestorSGD/ListarOrgaos1.png
.. |image5| image:: _imagens_portal_antigo/gestorSGD/ListarOrgaos2.png
.. |image6| image:: _imagens_portal_antigo/gestorSGD/CadastroDeAdesoes1.png
.. |image7| image:: _imagens_portal_antigo/gestorSGD/CadastroDeAdesoes2.png
.. |image8| image:: _imagens_portal_antigo/gestorSGD/CadastroGestorMenu.png
.. |image9| image:: _imagens_portal_antigo/gestorAPI/CadastroGestorAPISiape.png
.. |image10| image:: _imagens_portal_antigo/gestorAPI/CadastroGestorAPINaoSiape.png
.. |image11| image:: _imagens_portal_antigo/gestorSGD/ListarGestoresGestorSGDMenu.png
.. |image12| image:: _imagens_portal_antigo/gestorSGD/ListaDeGestores.png
.. |image13| image:: _imagens_portal_antigo/gestorSGD/CadastroDeUmNovoPlanoMenu.png
.. |image14| image:: _imagens_portal_antigo/gestorSGD/CadastroDeUmNovoPlano2.png
.. |image15| image:: _imagens_portal_antigo/gestorSGD/CadastroDeUmNovoPlano3.png
.. |image16| image:: _imagens_portal_antigo/gestorSGD/ListarPlanosDeConsumo1.png
.. |image17| image:: _imagens_portal_antigo/gestorSGD/ListarPlanosDeConsumo2.png
.. |image18| image:: _imagens_portal_antigo/gestorSGD/ListarPlanosDeConsumo3.png
.. |image19| image:: _imagens_portal_antigo/gestorSGD/RelatorioDeConsumo1.png
.. |image20| image:: _imagens_portal_antigo/gestorSGD/RelatorioDeConsumo2.png
.. |image21| image:: _imagens_portal_antigo/gestorSGD/RelatorioDeConsumo3.png
.. |image22| image:: _imagens_portal_antigo/gestorSGD/RelatorioDeDisponibilidade1.png
.. |image23| image:: _imagens_portal_antigo/gestorSGD/RelatorioDeDisponibilidade2.png
.. |image24| image:: _imagens_portal_antigo/gestorSGD/RelatorioDeDisponibilidade3.png
.. |image25| image:: _imagens_portal_antigo/gestorSGD/RelatorioGerencial1.png
.. |image26| image:: _imagens_portal_antigo/gestorSGD/RelatorioGerencial2.png
.. |image27| image:: _imagens_portal_antigo/gestorSGD/RelatorioGerencial3.png
.. |image28| image:: _imagens_portal_antigo/gestorSGD/RelatorioAuditoria1.png
.. |image29| image:: _imagens_portal_antigo/gestorSGD/RelatorioAuditoria2.png
.. |image30| image:: _imagens_portal_antigo/gestorSGD/RelatorioAuditoria3.png

