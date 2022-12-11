# IDSTA-Text-Miners: Hate, Discrimination & Racism in German Rap - A Text Analytics Approach

[![Download Proposal](https://img.shields.io/badge/Download--PDF-Proposal-green)](https://github.com/gsindlinger/IDSTA-Text-Miners/raw/main/Proposal/project-proposal.pdf)

Team Members:
- Gal Lebel (galbalandroid@gmail.com) - Bachelor of Science, Computer Science, Heidelberg University
- Simon Körner - Bachelor of Science, Computer Science, Heidelberg University
- Johannes Gabriel Sindlinger (johannes.sindlinger@stud.uni-heidelberg.de) - Master of Sciencer, Data and Computer Science, Heidelberg University

Previous Team Member:
- Mara-Eliana Popescu

## Milestone update

### Project Information
- Existing Code Fragments: Artist Generation(Collecting artists from which we scrape lyrics), Genius Lyrics Scraper. 
- Utilized libraries: geniuslyrics, spotipy


### Project State
The current state of the project, which is visualized in the graphic below, is that we have successfully fetched a big list of German rap artists using Spotify and have collected the lyrics of 10,500 German rap songs (green color / done). These lyrics will be used for our analysis. At this point, we have not set ElasticSearch to get our data nor we applied any predefined NLP models to our dataset, which are our next steps in the project (yellow color / in progress).

In the upcoming months (not sure if should be more specific than that), we will pipeline our dataset into ElasticSearch so that we can process and analyze it efficiently (yellow color / in progress).

We will use ElasticSearch to apply tokenization, stemming and lemmatization to clean and preprocess our data. Using our preprocessed data, we can now do basic metric analysis and analysis in terms of sentiment analysis using for example HateSonar, NLTK Sentiment Analysis and GermanSentimentBert, in order to extract insights from our data (red color / todo).

Additionally, we might discover new interestings insights and directions for our project through the analysis. We will update our timeline and tasks accordingly, and will incorporate new ideas that might arise through the results our our analysis.

![Current status of the project in december 2022](https://github.com/gsindlinger/IDSTA-Text-Miners/blob/Milestone_December/project_pipeline_december_2022.png)

### Data Analysis

The data sources that we are using in our acquired data collection are as following:
- Spotify Web API: We used the spotipy library to access the Spotify Web API and retrieve a list of German rap artists. We also created a class to work with the API in order to get the list of artists from the official Spotify German rap playlist for the years 1998 to 2023.
- Genius API: We used the lyricsgenius library to communicate with the Genius API and retrieve the lyrics of the songs by the German rap artists we obtained from the Spotify Web API. We also implemented our own method to scrape the lyrics using BeautifulSoup and multi-threaded the process to speed it up.
  - As part of our lyrics scraping process, we've decided to include additional information for each song like date of release, names of other artists participating in the song and information about the album such as album name and cover art in order to provide more context for our analysis and for our front-end platfrom to display the information in a visually appealing way.

Overall, we have collected lyrics for approximately 10,500 German rap songs, along with additional information.

A glimpse into ur collected data, which we will later on put into ElasticSearch.
showing the first 2 songs and their information for the artist 'Kollegah':
```json
{
    '0': {
        'title': '1001 Nacht',
        'album': 'Kollegah',
        'album_cover': 'https://images.genius.com/07e288ab9cef1fc67d4eab53f47737d8.1000x1000x1.jpg',
        'genius_album_id': 11399,
        'release_date': '2008-08-29',
        'featured_artists': [],
        'featured_artists_pics': [],
        'producer_artists': ['Rizbo'],
        'writer_artists': ['Rizbo', 'Kollegah'],
        'primary_artist_picture': 'https://images.genius.com/851cc7ad19da70bb8b380be671ef83d6.1000x1000x1.png',
        'genius_track_id': 52276,
        'song_id': 52276,
        'lyrics': "[Songtext zu „1001 Nacht“]\n[Intro]\nJebiga, Johnny, du bist ein dreckiger Johnny (Hehe)\nRäusper, Räusper, sag' ich mal so ins Blaue hinein\nYeah, yeah, Rene, ey, pass auf\n[Bridge]\nYeah, sieh, wie ich massenweise Zaster schmeiße (Ey)\nFlatternde Scheine regnen herab auf Pflastersteine (Ey)\nHustler-Style, ich ernte neidische Blicke\nDenn 20-Zoll-Felgen sind am Reifen wie Früchte (Ey)\n[Hook]\nUnd ich mach' ein paar Tausend in einer Nacht\n1001 Gramm verkaufen in einer Nacht\n1001 Scherben Schaufensterscheibenglas\nZerspringen in 1001 Nacht\n[Part 1]\nEy, der Boss, er hat schon so manch Ruhmreiches erlebt (Yeah)\nAuf Flugreisen nach Schweden, Dubai und Athen (Ey)\nUnd hat er seinen Schmuck nicht grad wie Zuggleise verlegt\nZieht er mehr Edelmetall an als ein Hufeisenmagnet\nWährend du Kuhweidengras mähst und eine Schreinerlehre machst\nIn deinem 30-Seelen-Kaff, trink' ich Preiselbeerensaft\nAuf einer weißen Segelyacht bei Kreuzfahrtschiffreisen\nWas Charakter? Ich leg' bei Frauen Wert auf Äußerlichkeiten\nWozu heuchlerisch sein? Das ist die männliche Natur\nIch verleih' im Bett kein'n Oscar, doch gebe 'ne glänzende Figur ab\nLehn' am Benz in dem Fuhrpark, Bitch, keiner rappt hier besser (Yeah)\nEy, ich stech' aus der Masse raus wie Weihnachtsplätzchenbäcker\nSieh den Daimler-Benz in pechschwarz und mit Chromleisten veredelt\nNeben großen 3er-BMWs und roten Maybachs steh'n\nUnd im Innern dominier'n die Farben kokosweiß und beige\nWeil da Elfenbein drin ist wie in der Hose einer Fee\n[Hook]\nYeah, ey, das ist 1001 Nacht\n1001 Gramm verkaufen in einer Nacht\n1001 Scherben Schaufensterscheibenglas\nZerspringen in 1001 Nacht (Yeah)\nUnd ich mach' ein paar Tausend in einer Nacht\n1001 Gramm verkaufen in einer Nacht\n1001 Scherben Schaufensterscheibenglas\nZerspringen in 1001 Nacht[Part 2]\nYeah, ey, ich komm' mit der Faust\nUnd weck' dich aus deinem Sommernachtstraum nonchalant auf\nIch bin ein fotogener Player\nDu und G sind zwei paar Schuhe für mich wie meine AirMax und meine Krokoledertreter\nEy, der King, neben dem Knastgrößen Straßenhuren ähneln\nUnd du liegst nach zwei fast tödlichen Magengrubenschlägen (Yeah)\nSchwach stöhnend da im Blumenbeet\nDu bist nicht Straße, ich bin Straße, so wie Ass-König-Dame-Bube-Zehn\nUnd durchfahr' die Hood im BMW, mit Chicks auf dem Beifahrersitz\nBlick auf die Reifen, du Bitch, Chrom blitzt auf im Scheinwerferlicht\nUnd erzähl mir bitte nicht wie viel zigtausend Weiber du fickst\nDu dicksaugender kleiner Wicht kriegst Frau'n nur als Thailandtourist\nNeider seh'n mich mit ungewöhnlich viel Money\nEy, wenn sie seh'n, wie viel Geld mir ungefähr gehört\nDann sagen sie: „Hut ab!“, wie Frisöre zu Rabbis\nNachdem sie kurz stutzen wie ein Bundeswehrfrisör\n[Bridge]\nYeah, sieh, wie ich massenweise Zaster schmeiße\nFlatternde Scheine regnen herab auf Pflastersteine\nHustlerstyle, ich ernte neidische Blicke\nDenn 20-Zoll-Felgen sind am Reifen wie Früchte\n[Hook]\nYeah, ey, das ist 1001 Nacht\n1001 Gramm verkaufen in einer Nacht\n1001 Scherben Schaufensterscheibenglas\nZerspringen in 1001 Nacht (Yeah)\nUnd ich mach' ein paar Tausend in einer Nacht\n1001 Gramm verkaufen in einer Nacht\n1001 Scherben Schaufensterscheibenglas\nZerspringen in 1001 Nacht (Yeah)[Outro]\nBitch, yeah\nKollegah 2008\nRizbo Beat, 1001 Nacht\nYeah, reib die Wunderlampe, ja, Habiba, hehehe\nOkay, Selfmade Records, Biatch"
    }

    ,
    '1': {
        'title': '16 Bars Exclusive',
        'album': '<single>',
        'album_cover': '',
        'genius_album_id': 'none',
        'release_date': '2006-01-01',
        'featured_artists': [],
        'featured_artists_pics': [],
        'producer_artists': ['DJ I-Cut'],
        'writer_artists': ['Kollegah'],
        'primary_artist_picture': 'https://images.genius.com/851cc7ad19da70bb8b380be671ef83d6.1000x1000x1.png',
        'genius_track_id': 382821,
        'song_id': 382821,
        'lyrics': "[Songtext zu „16 Bars Exclusive“]\n[Part]\nEy, komm in meine Wohnung\nUnd du siehst auf der Digitalwaage\nSpitzenschnee wie auf dem Kilimandscharo-Gipfel\nEy, du verkaufst dich billig am Bahnhofsviertel\nTeenager seh'n mich auf der Straße und sagen:\n„Ey Kollegah, könn'n wir noch was kriegen?“\nUnd ich schlage sofort um mich wie ein Tae-Bo-Trainer\nKomm' mit Baseballschläger wie ein Baseballtrainer\nUnd geb' dem Typ ein Brett, als wär er Skateboardräder\nUnd ich muss, wenn ich durch jede x-beliebige Kleinstadt geh'\nLaufend Autogramme geben wie ein Leichtathlet\nKid, für das Hochheben meines Platinarmbands\nBrauchst du Spargeltarzan einen Gabelstapler\nUnd du siehst in dem Laden 'nen Designeranzug hängen und denkst dir: „Unbezahlbar!“\nIch geh' dann demonstrativ in den Laden, kaufe den Anzug und bezahl' bar\nKollegah der Boss, ich vertick' jeden Tag in mehreren Stadtbezirken\nAlles von Coke, Dope, Gras, Guns bis hin zu Flachbildschirmen\nVerbreite Panik wie Geisterbahnen\nKomm' in Karren, die schwarz sind wie Leichenwagen\nMisshandele dich mit dem Butterflymesser, du Bitch\nUnd im Schlafzimmer deiner Mom herrscht ganz schön Getümmel\nDenn sie lutscht für 'ne Handvoll Banknotenbündel Stammkundenpimmel"
    }

    ,
    '2': {
        'title': '180 Grad',
        'album': 'Zuhältertape Volume 3',
        'album_cover': 'https://images.genius.com/a685e3bc53f4008e88891bd0899e71c2.1000x1000x1.jpg',
        'genius_album_id': 12345,
        'release_date': '2009-12-19',
        'featured_artists': [],
        'featured_artists_pics': [],
        'producer_artists': ['B-Case'],
        'writer_artists': ['B-Case', 'Kollegah'],
        'primary_artist_picture': 'https://images.genius.com/851cc7ad19da70bb8b380be671ef83d6.1000x1000x1.png',
        'genius_track_id': 60369,
        'song_id': 60369,
        'lyrics': "[Part 1]\nKilos in der Jackentasche, Kilos in der Aktenmappe\nKollegah mit Kilos in Rio auf 'ner Dachterrasse\nSchlampen gucken angespannt, ich regier' das ganze Land\nUnd klatsche zwecks Promo Ronnie Coleman von der Hantelbank\nDu kommst im Bungalow schlafend am Hungertuch nagend\nÜber dein trostloses Leben im Untergrund klagend\nUnd willst mir dann erzählen, du würdest nicht für 'nen Hunderter blasen?\n(Ja, erzähl das deiner Großmutter)\nEy yo Bitch, während der Kanada-Germane\nhinter Panzerglasfassaden\nSitzt wie Salzwasseraquarienfische, hängst du mit\nComputernerds\n, ich hab im Pool paar Girls am Dick\nDenn ein Fick mit dem King gibt Bitches den Kick wie Uma Thurman\nSieh, ich lade TECs, stapel Cash, fahr' den Lex durch die Straßen\nVercheck Gras und gestrecktes Crack, habe Sex mit deiner Mum in\nIhr'm Bett,\nPlatinumketten am Hals, Kid, ich hör' dir nicht zu\nDoch du laberst weiter, d'rum liegst du Störenfried nun im Emergency Room\n[Hook]\nEy yo, die bad Motherfucker feiern auf Crack ab im Pascha\nBring'n deine Kleine zum Kreischen so wie das Texas Massaker\nIch steh' am Herd, koch' das Crack bei 180 Grad\nGeh' durchs Viertel und G's dreh'n sich um 180 Grad (180 Grad)\nBitch, ich komm' mit ganz großen Bündeln voller Banknoten\nDu mit Computernerds, die sich schwul anhör'n wie Franzosen\nHundesohn, ich koch' das Crack bei 180 Grad\nGeh' durchs Viertel und G's drehn sich um 180 Grad (180 Grad)\n[Part 2]\nIhr seid Cockrider-Bitches (Bitches), ich steppe in den Club (Club)\nMit Teflon vor der Brust (Brust) und Glock an der Hüfte (yeah)\nEs ist der Rauschgiftdealer, breitbeiniger Gang\nDu dagegen hast X-Beine wie Tausendfüßler\nNutte, sieh mich durch die Town fahren,\nquietschend vor dei'm Haus parken\nAn der Zigarre zieh'n und Rauchschwaden ausatmen\nReinkommen, dir dann kurz aufs Maul schlagen\nDeine Frau nageln, deine Kohle greifen und wieder nach Haus fahren\nYeah, mein Freundeskreis besteht leider zum großen\nTeil aus Ganoven wie Freimaurerlogen\nUnd deine Gangmember klappen zusammen wie Campingstühle\nWenn sie den King anrücken sehen wie Engelsflügel\nKomm' in den Club um drei Uhr nachts, du siehst den Gangsterboss\nUmgeben von Cokebitches in engen Tops wie Megan Fox\nIch bin V.I.P\nDich dagegen sieht man nur bei unbekannten Leuten wie beim Klingelstreich spielen[Hook]\nEy yo, die bad Motherfucker feiern auf Crack ab im Pascha\nBring'n deine Kleine zum Kreischen so wie das Texas Massaker\nIch steh' am Herd, koch' das Crack bei 180 Grad\nGeh' durchs Viertel und G's dreh'n sich um 180 Grad (180 Grad)\nBitch, ich komm' mit ganz großen Bündeln voller Banknoten\nDu mit Computernerds, die sich schwul anhör'n wie Franzosen\nHundesohn, ich koch' das Crack bei 180 Grad\nGeh' durchs Viertel und G's drehn sich um 180 Grad (180 Grad)"
    }
```

Although we have yet to preprocess our acquired collected data, we already have few ideas about how we should approach this:
At first we will preprocess our data using ElasticSearch as mentioned above (Tokenization, Lemmatization and so on).
Later on, as we prepare our data to be used for the different NLP models, we may have to exclude songs which have more than a third of the words in a language which isn't German. This will allow easier analysis of our data.


## Project Log

| Date   | Who?                | What?                                                                   | 
|--------|---------------------|-------------------------------------------------------------------------|
| Oct 28 | Johannes Sindlinger | Design pipeline graphics                                                |
| Oct 28 | Johannes Sindlinger | Write motivation, research topic (partly), project description (partly) |
| Oct 30 | Mara-Eliana Popescu | Extend project description                                              |
| Oct 31 | Gal Lebel           | Extend research topic, finish proposal                                  |
| Nov 18 | Johannes Sindlinger | Setup issues for project start                                          |
| Nov 25 | Johannes Sindlinger | Create artist list via Spotify API                                      |
| Dec 10 | Gal Lebel           | Genius Lyrics Scraper                                                   |
| Dec 10 | Gal Lebel           | Milestone Editing                                                              |



## Assignment Log


| Date   | Who?                | What?                      | 
|--------|---------------------|----------------------------|
| Nov 12 | Johannes Sindlinger | Assignment 1 - Exercise 1  |
| Nov 12 | Mara Popescu        | Assignment 1 - Exercise 3  |
| Nov 13 | Simon Körner        | Assignment 1 - Exercise 2  |
| Nov 13 | Gal Lebel           | Assignment 1 - Exercise 2  |
| Dec 09 | Johannes Sindlinger | Assignment 2 - Exercise 2  |
| Dec 10 | Gal Lebel           | Assignment 2 - Exercise 1  |

