Egzamin NoSQL - Michał Tyczyński

Informacje o komputerze na którym były wykonywane obliczenia:

| Nazwa                 | Wartosć    |
|-----------------------|------------|
| System operacyjny     | Windows 10 |
| Procesor              | i3-3217U |
| Ilość rdzeni          | 2 |
| Pamięć                | 8GB |
| Dysk                  |  SSD 250GB |
| Baza danych           | Reddit Comments|
___________________
Import danych do bazy Mongo ( komenda:)

 ```Measure-Command{ .\mongoimport -d nosql -c reddit3 "C:\Users\Devest\Documents\reddit2.json" }```
_______________

Czas importu danych.


|Time Type                          |  Time value                 |
|---------------------------------|----------------------|
| Minutes                         |  3                  |
| Seconds                         |  2                  |
| Milliseconds                    |  325                |
| Ticks                           |  1823252719         |
| TotalDays                       |  0,0021102462025463 |
| TotalHours                      |  0,0506459088611111 |
| TotalMinutes                    |  3,03875453166667   |
| TotalSeconds                    | 182,3252719        |
| TotalMilliseconds   |                    182325,2719  |

![agr1](https://github.com/mtyczynski/egzaminnosql/raw/master/json.png "Logo Title Text 1")


wazne pola w JSONie:

| pole  | znaczenie pola             |
|--------------|------------------------------------------------------|
| approved_by  |  osoba ktora zaakceptowala komentarz                 |
| author       |  autor komentarza                                    |
| banned_by    |  przez kogo zbanowany                                |
| body         |  tekst komentarza                                    |
| body_html    |  przerobiony komentarz do postaci   html             |
| created      |  czas w sekundach od 00:00:00 1   January 1970       |
| created_utc  |  czas w sekundach od 00:00:00 1   January 1970 (UTC) |
| distingushed |  wyróżniony                                          |
| downs        |  liczba minusów                                      |
| ups          |  liczba plusów                                       |
| edited       |  czy post był edytowany                              |
| id           |  id posta                                            |
| link_title   |  tytul głównego wątku                                |
| num_reports  |  liczba reportow od innych   redditorów              |
| replies      |  liczba odpowiedzi                                   |
| parent_id    |  id do posta nadrzędnego                             |
| subreddit    |  nazwa subreddita na ktorym   napisano post          |
| subreddit_id |  id subreddita                                       |

<BR/>
<BR/>
<BR/>
Informacje wyciągnięte z aggregation pipeline(MongoDB)

| Subreddit            |  Liczba komentarzy |
|--------------------------|----------|
| 'AskReddit'             |  114453 |
| 'funny'                 |  30771  |
| 'AdviceAnimals'         |  27290  |
| 'gaming'                |  26957  |
| 'WTF'                   |  23818  |
| 'pics'                  |  22004  |
| 'leagueoflegends'       |  19019  |
| 'IAmA'                  |  16133  |
| 'worldnews'             |  13556  |
| 'videos'                |  12463  |
| 'todayilearned'         |  1192  |
| 'soccer'                |  8671   |
| 'teenagers'             |  8433   |
| 'politics'              |  8374   |
| 'news'                  |  8264   |
| 'DotA2'                 |  7363   |
| 'Random_Acts_Of_Amazon' |  7316   |
| 'ffxiv'                 |  7144   |
| 'trees'                 |  7082   |
| 'Games'                 |  6846   |
| 'movies'                |  6405   |
| 'nfl'                   |  6204   |
| 'CFB'                   |  5818   |
| 'aww'                   |  5634   |
| 'gonewild'              |  5114   |
| 'hiphopheads'           |  4951   |
| 'cringepics'            |  4869   |
| 'breakingbad'           |  4830   |
| 'explainlikeimfive'     |  4548   |
| 'fantasyfootball'       |  4456   |
| 'nba'                   |  4091   |
| 'AskMen'                |  3974   |
| 'AskWomen'              |  3962   |
| 'technology'            |  3959   |
| 'hearthstone'           |  3751   |
| 'SquaredCircle'         |  3642   |
| 'atheism'               |  3639   |
| 'OkCupid'               |  3630   |
| 'Minecraft'             |  3613   |
| 'malefashionadvice'     |  3605   |
| 'electronic_cigarette'  |  3326   |
| 'pokemon'               |  3266   |
| 'gifs'                  |  3265   |
| 'TumblrInAction'        |  3097   |
| 'Fitness'               |  3085   |
| 'magicTCG'              |  3068   |
| 'books'                 |  3066   |
| 'science'               |  3019   |
| 'buildapc'              |  2878   |
| 'Android'               |  2870   |
| 'MakeupAddiction'       |  2798   |
| 'GrandTheftAutoV'       |  2788   |
| 'MMA'                   |  2738   |
| 'hockey'                |  2697   |
| 'starcraft'             |  2680   |
| 'sex'                   |  2647   |
| 'baseball'              |  2570   |
| 'relationships'         |  2541   |
| 'Music'                 |  2421   |
| 'conspiracy'            |  2284   |
| 'guns'                  |  2273   |
| 'wow'                   |  2178   |
| 'cringe'                |  2164   |
| 'changemyview'          |  2136   |
| 'yugioh'                |  2110   |
| 'australia'             |  2066   |
| 'SteamGameSwap'         |  2007   |
| 'ACTrade'               |  1979   |
| 'Guildwars2'            |  1958   |
| 'canada'                |  1952   |
| 'MLPLounge'             |  1835   |
| 'totalwar'              |  1789   |
| 'motorcycles'           |  1787   |
| 'Smite'                 |  1757   |
| 'Christianity'          |  1753   |
| 'tf2'                   |  1730   |
| 'cars'                  |  1728   |
| 'JusticePorn'           |  1718   |
| 'casualiama'            |  1685   |
| 'Gunners'               |  1637   |
| 'mildlyinteresting'     |  1629   |
| 'SubredditDrama'        |  1587   |
| 'xboxone'               |  1560   |
| 'asoiaf'                |  1555   |
| 'bicycling'             |  1554   |
| 'TwoXChromosomes'       |  1553   |
| 'BabyBumps'             |  1522   |
| 'BigBrother'            |  1514   |
| 'MensRights'            |  1512   |
| 'PS4'                   |  1479   |
| 'Bitcoin'               |  1459   |
| 'PercyJacksonRP'        |  1451   |
| 'photography'           |  1401   |
| 'GlobalOffensive'       |  1394   |
| 'coys'                  |  1387   |
| '3DS'                   |  1383   |
| 'unitedkingdom'         |  1369   |
| 'Civcraft'              |  1364   |
| 'MLS'                   |  1344   |
| 'acturnips'             |  134   |

Czas wykonywana poszczególnych aggregacji.


Agregacja 1:
------------------------------
Time spent in executing function agr1 is: 4.82879003597

![agr1](https://github.com/mtyczynski/egzaminnosql/raw/master/1.png "Logo Title Text 1")

Agregacja 2:
------------------------------
Time spent in executing function agr2 is: 2.57310376325

![agr2](https://github.com/mtyczynski/egzaminnosql/raw/master/2.png "Logo Title Text 1")

Agregacja 3:
------------------------------
Time spent in executing function agr3 is: 1.85864243321

![agr3](https://github.com/mtyczynski/egzaminnosql/raw/master/3.png "Logo Title Text 1")

Agregacja 4:
------------------------------
Time spent in executing function agr4 is: 4.53365750025

![agr4](https://github.com/mtyczynski/egzaminnosql/raw/master/4.png "Logo Title Text 1")


Obserwacje:
RAM oraz dystep do dysku ma duze znaczenie w szybkosci wykonywania aggregacji.