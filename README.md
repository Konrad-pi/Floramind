# Floramind - Summer of Code 2023

## 🇩🇪 (DE):
Floramind ist ein innovatives GitHub-Projekt, das die Leistung von Open-Source-Sprachmodellen (LLMs) nutzt, um tägliche Updates aus fremdsprachlichen Umgebungen zu liefern. Als aktiver Teilnehmer an der 2023 Summer of Code Challenge ist es unsere Aufgabe, ein ausgeklügeltes Programm zu entwickeln, das Artikel aus prominenten kolumbianischen Online-Medienquellen extrahiert und zu zusammenhängenden Erzählungen synthetisiert. Das Projekt konzentriert sich in erster Linie darauf, einen umfassenden Überblick über die aktuelle (politische) Landschaft des Landes zu liefern. 

Basierend auf aufschlussreichen Gesprächen mit lokalen Kontakten haben wir eine Reihe angesehener Medien-Websites als Datenquellen ausgewählt:
* El Tiempo
* Semana
* CCN Espanol
* BBC Mundo

### Die Hauptziele von Floramind:
1. Web-Scraping-Infrastruktur: Unter Verwendung der BeautifulSoup (bs4)-Bibliothek bauen wir eine robuste Web-Scraping-Infrastruktur zur systematischen Sammlung von Artikeln aus den ausgewählten kolumbianischen Online-Medienplattformen auf.

2. Inhaltszusammenfassung und Übersetzung: Floramind wird die Leistungsfähigkeit von Open-Source-LLMs nutzen und einen fortschrittlichen Mechanismus zur Inhaltszusammenfassung und Übersetzung implementieren. Diese Technologie wird das Wesentliche eines jeden Artikels kurz und bündig zusammenfassen und so ein effizientes Verständnis ohne Sprachbarrieren ermöglichen.

3. Deutschsprachige Berichterstattung: Ein zentraler Bestandteil des Projekts ist die Erstellung umfassender Berichte in deutscher Sprache. Diese Berichte werden die zusammengefassten Informationen zusammenfassen und eine wertvolle Ressource für deutschsprachige Interessengruppen darstellen, die Einblicke in die kolumbianische Wirtschaft suchen.

### Der Prozess
1. Webscraper mithilfe von bs4: Abgschlossen, 4 Webscraper fertiggestellt, die die top 10 Artikel der folgenden Webseiten in ein csv Dokument Exportieren:
https://cnnespanol.cnn.com/category/zona-andina/colombia/
https://www.bbc.com/mundo/topics/c404v5gz1rkt
https://www.eltiempo.com/colombia
https://www.semana.com/nacion/


2. LLM Implementierung
Das Implementieren des Large Language Models wird getrennt in das Hosting, trainieren und anpassen, und die implementierung der Use cases im code. Auf das selbst gehostete LLM wird mithilfe einer API zugegriffen, da allerdings das Hosting noch nicht erfolgt ist, wird der Code mithilfe der ChatGPT API ausprobiert um ein zwischenergebnis zu haben. 

Die use cases werden folgendermaßen segmentiert: 
    1. Clustering der Artikel nach Thema: Die gescraped artikel werden vom LLM in Themencluster eingeordnet
    2. Die Themencluster werden zusammengefasst
    3. Die zusammenfassung wird von Spanisch auf Deutsch übersetzt


## 🇬🇧 (EN): 
Floramind is an innovative GitHub project that harnesses the power of open source Language Models (LLMs) to provide daily updates from foreign language environments. As an active participant in the 2023 Summer of Code Challenge, our mission is to develop a sophisticated program that extracts and synthesizes articles from prominent Colombian online media sources into cohesive narratives. The project primarily focuses on delivering a comprehensive overview of the current (political) landscape within the nation. 

Based on insightful conversations with local contacts, we have curated a set of reputable media websites for our data sources:
* El Tiempo
* Semana
* CNN Espanol
* BBC Mundo

### Key Objectives of Floramind:
1. Web Scraping Infrastructure: Utilizing the BeautifulSoup (bs4) library, we are constructing a robust web scraping infrastructure for systematic article collection from the chosen Colombian online media platforms.

2. Content Summarization and Translation: Leveraging the power of open source LLMs, Floramind will implement an advanced content summarization and translation mechanism. This technology will succinctly encapsulate the essence of each article, enabling efficient comprehension without language barriers.

3. German Language Reporting: A pivotal component of the project involves generating comprehensive reports in German. These reports will encapsulate the synthesized information, offering a valuable resource for German-speaking stakeholders seeking insights into Colombia's contemporary political landscape.

### The process
1. webscraper using bs4: completed, 4 webscraper completed exporting the top 10 articles to a csv document.
https://cnnespanol.cnn.com/category/zona-andina/colombia/
https://www.bbc.com/mundo/topics/c404v5gz1rkt
https://www.eltiempo.com/colombia
https://www.semana.com/nacion/

2. LLM implementation
The implementation of the Large Language Model is separated into hosting, training and customising, and implementing the use cases in code. The self-hosted LLM will be accessed using an API, but since hosting has not yet been done, the code will be tested using the ChatGPT API to get an intermediate result. 

The use cases are segmented as follows: 
    1. clustering of articles by topic: the scrapped articles are classified into topic clusters by the LLM.
    2. the topic clusters are summarised
    3. the summary is translated from Spanish to German.