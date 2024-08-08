---
layout: post
title:  "TCC - Planning"
date:   2024-08-08 12:00:00
categories: blog
---

# Roadmap
~~~
- 🟢 Feito
- 🟡 Na fila
- 🔵 Em progresso
~~~

<details>
    <summary>🟡 Melhorias na base existente</summary>
    <details><summary>🟡 Normalização das Edições/Veículos</summary>
    <p>Atualmente, Edições são apenas registros da ERBD. É necessário criar um Veículo ERBD e ligar cada edição a essa entidade nova. Esta tarefa envolve a criação de uma nova entidade no banco de dados para representar o evento ERBD como um todo, e associar cada edição específica a esta entidade. Isso permitirá uma melhor organização e consulta dos dados, além de facilitar futuras expansões e análises.</p>
    </details>
    <details><summary>🟡 Normalização das Localidades</summary>
    <p>Atualmente dados de localidade só estão presentes nas edições da ERBD. É necessário criar um novo registro para cada diferente cidade onde aconteceu o evento. Esta tarefa envolve a criação de uma entidade para representar as cidades no banco de dados e associar cada edição do evento à cidade correspondente. Isso permitirá uma análise mais detalhada sobre a distribuição geográfica das edições da ERBD.</p>
    </details>
</details>

<details>
 <summary>🔵 Expansão base ERBD</summary>
    <details><summary>🟢 Extração dados ERBD 2021-2024</summary></details>
    <details>
        <summary>🔵 Processamento dados</summary>
        <details><summary>🟢 Normalização do nome dos autores</summary></details>
        <details><summary>🟢 Deduplicação de autores</summary></details>
        <details><summary>🟡 Normalização das Instituições de Ensino</summary>
        <p>É necessário normalizar dados para que, por exemplo, `UFSC` e `Universidade Federal de Santa Catarina` sejam compreendidos como a mesma instituição.</p>
        </details>
    </details>
    <details><summary>🟡 Inserção dados no banco</summary>
    <p>Após o processamento e normalização dos dados, é necessário inserir os novos registros no banco de dados existente. Cuidar para que registros já presentes não sejam duplicados.</p>
    </details>
</details>

<details>
 <summary>🟡 Expansão DBLP</summary>
    <details><summary>🟡 Correspondência dos autores com perfil DBLP</summary>
    <p>Será necessário encontrar o perfil de autor na DBLP a fim de extrair todos seus trabalhos lá indexados. Essa busca contará com uma etapa de validação manual. A tarefa inclui a criação de um algoritmo de correspondência para encontrar os perfis dos autores da ERBD na DBLP e validar manualmente os resultados para garantir precisão.</p>
    </details>
    <details><summary>🟡 Extração dados DBLP</summary>
    <p>A estratégia para extração de dados ainda está em aberto. DBLP fornece um XML com dados de cada autor. Esta tarefa envolve o desenvolvimento de um script para baixar e processar os arquivos XML da DBLP, extrair as informações relevantes e transformá-las para o formato do banco de dados da ERBD.</p>
    </details>
    <details><summary>🟡 Processamento dados</summary>
    <p>Após a extração, os dados devem ser processados para garantir que estejam no formato correto e livres de inconsistências. Isso inclui a normalização de nomes, afiliações e a deduplicação de registros.</p>
    </details>
    <details><summary>🟡 Inserção dados no banco</summary>
    <p>Com os dados processados, a próxima etapa é a inserção no banco de dados. É importante realizar essa etapa com cuidado para evitar conflitos e garantir a integridade dos dados.</p>
    </details>
</details>

<details>
 <summary>🟡 Geração da rede</summary>
    <p>A geração da rede envolve a definição da tecnologia que será utilizada para visualização. Critérios a serem avaliados para a escolha: licensa de uso, formato de importação, visualizações e gráficos gerados.</p>
    <p>Outra etapa necessária será a geração da matriz de adjacência do grafo para uso em demais algoritmos.</p>
</details>

<details>
 <summary>🟡 Identificação de padrões na rede</summary>
    <details><summary>🟡 Calculo de métricas de redes</summary>
        <p>Obtenção das métricas da rede com base no grafo gerado.</p>
    </details>
    <details><summary>🟡 Avaliar k-cliques</summary>
        <p>Esta tarefa envolve a aplicação de algoritmos de detecção de k-cliques para identificar subgrupos densamente conectados dentro da rede de coautoria.</p>
        <details><summary>🟡 Selecionar Top X autores</summary>
        <p>Com base nas análises de k-cliques e outras métricas de rede, selecionar os autores mais influentes na rede de coautoria. Esta seleção deve considerar métricas como centralidade de grau, centralidade de intermediação e número de publicações.</p>
        </details>
    </details>
</details>

<details>
 <summary>🟡 Expansão Lattes</summary>
    <details><summary>🟡 Correspondência dos Top X autores</summary>
    <p>Para os autores mais influentes identificados, será necessário encontrar e validar seus perfis na plataforma Lattes. Esta tarefa pode envolver correspondência manual e automática para garantir a precisão dos dados coletados.</p>
    </details>
    <details><summary>🟡 Extração dados currículo</summary>
    <p>A estratégia para extração de dados ainda está em aberto. Lattes fornece um XML com dados de cada autor. Esta tarefa inclui o desenvolvimento de um script para baixar e processar os arquivos XML da plataforma Lattes, extraindo informações relevantes para o estudo.</p>
    </details>
</details>

<details>
 <summary>🟡 Geração de perfil</summary>
    <p>Com os dados extraídos e processados, é necessário gerar os perfis dos autores. Esta tarefa envolve a integração de dados de diferentes fontes e a definição de um perfil de perfil que compreenda de maneira geral os autores.</p>
</details>

<details>
 <summary>🟡 Plotar gráficos</summary>
    <p>Com base nos dados analisados, gerar gráficos que representem visualmente os resultados do estudo. Esta tarefa inclui a escolha das melhores representações gráficas para diferentes tipos de dados e a utilização de ferramentas de visualização adequadas.</p>
</details>

<details>
 <summary>🟡 Análise de resultados</summary>
    <p>A última etapa envolve a análise detalhada dos resultados obtidos. Esta tarefa inclui a interpretação dos dados e gráficos gerados e a redação de conclusões.</p>
</details>
