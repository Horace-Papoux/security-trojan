# Sécurité - Écriture d'un Troyen - Aubert & Vuilliomenet

## Contexte

Dans le cadre du cours de sécurité informatique, nous nous sommes intéressés aux logiciels malveillants et plus particulièrement aux Troyens. Les Troyens sont des programmes dissimulés dans d'autres programmes que l'on pense sains et bienveillants. Cependant, après avoir installé ce logiciel "façade", le programme malveillant commencera à agir discrètement.

Son nom ne vient évidemment pas de nulle part, il est tiré de l'histoire du cheval de Troie qui avait été offert en guise de félicitations aux vainqueurs alors qu'à l'intérieur se cachaient des guerriers prêts à tuer leurs adversaires une fois qu'ils ne s'y attendraient plus.

<figure>
    <img src="trojan_horse.jpg"/>
    <figcaption>Figure 1 : Cheval de Troie</figcaption>
</figure>

Le même principe est appliqué dans un cheval de Troie informatique. L'attaquant va tenter de dissimuler au mieux son programme malveillant dans un logiciel utile qui semble provenir d'une source fiable ou du moins pas trop douteuse. On retrouve régulièrement cette stratégie dans des logiciels craqués que l'on peut gratuitement télécharger sur internet.

Notre travail sera d'élaborer un Troyen qui soit assez crédible pour persuader nos cibles que notre logiciel façade est digne de confiance pour qu'ils l'installent.

Nous avons vu qu'il existait un grand nombre de bonnes pratiques en sécurité informatique pour éviter toute intrusion dans ses systèmes, mais nous savons aussi que le maillon le plus vulnérable est toujours l'être humain. La mise en place d'un Troyen n'est pas l'attaque informatique la plus technique, mais elle demande plutôt une certaine part de social engineering.

Par contre, nous avons appris qu'une bonne gestion des logs permettait de repérer très rapidement les comportements anormaux et les intrusions dans un système informatique. C'est pourquoi nous devrons aussi porter une attention particulière à rendre notre programme malveillant discret et non trop actif.

## État de l'art

Un cheval de Troie n'est pas forcément un grand logiciel comme un antivirus qui possède aussi un programme malveillant, ça peut aussi être une image ou un pdf qui est en réalité un exécutable.
Cette méthode d'intrusion dans un système est largement utilisée par les Ethical hackers qui tentent d'exploiter les failles humaines.

Un cheval de Troie peut être écrit dans n'importe quel language de programmation mais il est plus facile de le faire en C/C++ afin de bypasser les permissions.

Voici quelques exemples de cheval de Troie :

### Troyen dans un fichier jpg ou autre fichier

Il semble très facile de mettre en place un Troyen dans un fichier jpg d'après le post de *Gourav Dhar* sur le site *InfoSec Write-ups*. Il explique aussi que sa marche à suivre fonctionne pour les pdf ou d'autres extensions de fichiers.

Lien sur son post : https://infosecwriteups.com/how-i-created-a-trojan-malware-ethical-hacking-82239a6b64c6

### Troyen dans un 

## Mise en place concrète

Nous avons commencé par établir un but, un certain type de données que nous voudrions récupérer. Nous avons choisi les mots de passes car c'est généralement des données difficiles à obtenir et donc intéréssant à implémenter. Nous avons eu vent de la possibilité de récupérer les mots de passes en clair de personnes possédant des mots de passe enregistré sur google chrome. Cette informations nous vient du lien suivant : https://techbrowser.co/browser/google-chrome/where-are-google-chrome-passwords-stored/.

Par la suite, nous avons creusé dans cette direction en nous renseignant par le biais de diverses sources citées plus bas dans les références.

## Résultats

Notre troyen est dissumulé dans un jeu de plateau informatisé qui s'appelle othello. Lorsque le jeu démarre sur la machine de notre cible, s'il possède des mots de passe dans google chrome, nous parvenons à les récupérer et les envoyer à une api pour concentrer les mots de passes récupéré à un unique endroit. 

Notre troyen n'est pour l'instant pas particulièrement discret. 

## Références

### Sites internet

 - **Wikipédia**, Cheval de Troie, https://fr.wikipedia.org/wiki/Cheval_de_Troie
 - **Wikipédia**, Cheval de Troie (informatique), https://fr.wikipedia.org/wiki/Cheval_de_Troie_(informatique)
 - **InfoSec Write-ups**, How I created a Trojan malware - Ethical Hacking, https://infosecwriteups.com/how-i-created-a-trojan-malware-ethical-hacking-82239a6b64c6
 - **techbrowser**, Where are Google Chrome passwords stored? Guide to find it, https://techbrowser.co/browser/google-chrome/where-are-google-chrome-passwords-stored/.
 - **GitHub**, decrypt-chrome-passwords, https://github.com/ohyicong/decrypt-chrome-passwords/blob/main/decrypt_chrome_password.py
 - **Medium**, How to crack Chrome password with Python?, https://ohyicong.medium.com/how-to-hack-chrome-password-with-python-1bedc167be3d
 - **StackOverlow**, Trying to decrypt password win32crypt.CryptUnprotectedData, https://stackoverflow.com/questions/44709034/trying-to-decrypt-password-win32crypt-cryptunprotecteddata
 - **StackOverflow**, DPAPI password encryption in C# and saving into database.Then Decrypting it using a key, https://stackoverflow.com/questions/34194223/dpapi-password-encryption-in-c-sharp-and-saving-into-database-then-decrypting-it

### Illustrations

 - Figure 1 : http://www.droits-justice-et-securites.fr/intrusion/un-cheval-de-troie-dans-ma-messagerie/
