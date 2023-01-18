# Number-recognition

Úloha v rámci přijímacího řízení do DataSentics.

Zadání bylo napsat program pro automatické rozpoznávání čísel.

Problém jsem zjednodušil předpokladem digitálních číslic a jako testovací data jsem použil sérii fotek digitálního teploměru krbu. Úlohu jsem řešil dvěma způsoby.
1) Po vyselektování jednotlivých cifer program kontroluje 'zaplněnost' jednotlivých segmentů a poté páruje s čísly ze slovníku.
2) Po vyselektování jednotlivých cifer byla na hranici čísla použita fourierova transformace a díky tomu získány fourierovy deskriptory.

Poznámka: Jde jen o částečné řešení a nejedná se o plně funkční program
