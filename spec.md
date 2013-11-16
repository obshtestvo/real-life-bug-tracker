В описанието е използвана думата `report` е вместо `докладвам` понеже:
 - `докладвам` има ненужно бюрократично звучене. Алтернатива е фразата `съобщи проблем`, която може да се ползва в готовия апп, но за това описание е по-удобно ако е 1 дума
 -  `report` е позната от уеб, точно като дума асоциирана със съобщаване на грешка/проблем


Състои се от app-ове за iphone, android, windows phone и уеб които предоствят само UI, и които комунират със backend услуга на нашия сървър.

Ще имаме google analytics с custom event-и, да виждаме кой къде клика и колко време прекарва на даден екран/страница.

## Функционалност за phone app-a

### Интро екрани
След отваряне потребителя има кратко интро от 2-3 екрана, за да се изясни какво прави app-a

Записки от разговор по темата: `tip workflow , trip.js, https://www.cocoacontrols.com/controls/icetutorial`

### Основен екран
 Потребителят бива посрещнат от екран разделен на 3.
 
 90% от екрана ще е направен, така че да има бутон и да приканва за report-ване на нов проблем. 

 На малка площ от екрана ще са разположени бутони водещи към:

 1. разглеждане на вече report-нати проблеми и 
 1. информация за app-a


### Стъпки за report-ване

#### Избор на източник за снимката 
Камера или галерия на вече съществуваща снимка. Ако се избере  камерата, тогава се пуска "фото" режима на телефона и се взима снимка посредством api-то на дадената мобилна платформа (iphone, android, windows phone) ще имаме 

#### Избор на категория
След като вече доклад има снимка потребителя избира категория за проблема. Тип "опасни сгради", "неправилно паркиране", "озеленяване"...

Избира се само 1 категория. 

#### Избор на локация
Локацията може да се вземе от EXIF данните на снимката, но за да сме по сигурни ще дирекно със достъп до сензора на GPS-a.

Засичането на локацията ще става още на предния екран като задкулисно (background) процес, така че вече на този екран да може да покажем локацията. Потребителя ще вижда адрес и поле за търсене на адрес с дописване (autosuggest) на адреси. 

За момента не е ясно дали ще се показва карта без потребителя да е поискал да види на картата адреса, понеже доста хора могат да са на интернет план с ограничен bandwidth.

От друга страна карта е доста по интуитивна от поле за адрес, и може маркерчето за локацията да се пуска (drop-ва)

Записки от разговор по темата: `custom tursachka na adres s geocoding i reverse geocoding`

#### Проверка на подобни доклади около избраната локация
Ако в радиус от ... 50м? например има report-нати други поблеми се показва екран изреждащ всеки от тях в списък със снимка и кратко инфо. 

За проверката се прави заяква към сървъра с подаден радиус и локация. Може би и категория на проблема и заглавие.

В този момента ако потребителя види същото нещо което е искал да report-не може да има бутон "това имах предвид" или "cancel" за да се върне в началото.

#### Описание на проблема
Ако все пак проблема се окаже нов, потребителя трябва да го опише с няколко изречения.

#### Екран за preview
Екран където може потребителят да направи преглед на проблема преди да го изпрати към сайта.

Екрана е разделен на 3:
 - снимка
 - локация
 - описание

Като потреителя може да scroll-ва или slide-ва и така всяка част ще се уголемява. Същото увеличение е възможно с клик върху някоя от 3те части. За да се уголеми 1 част другите 2 трябва да се смалят до момента в които вместо съдържание се показва просто заглавие какво съдържат.

Бележки от разговр по темата: `scroll tip paralax mai e iskano ne se znae`

#### Екран за удостоверяване/логин
Екран където потребителя може да избере да се логне чрез други сайтове в които има регистрация като Facebook или Twitter. 

Екрана е нужен, за да се предотвратява spam. Когато потребител е удостоверен може да му се зададе лимит от 8 (примерно) report-а на ден. Във бъдещи версии може да изпозлваме репутация за да променим този лимит спрямо нея.

Записки от разговор по темата: `otorozirane chrez OAuth, po ip limitrane sushto obache tova she e po kusno, poneje ne e basic ako shte e dobre napraveno`

#### Екран за повърждение на report-нат проблем
Success.


### Разглеждане на вече report-нати проблеми

Може да се разглеждат в 3 варианта:

 - на карта
 - на thumbnails
 - изредени като текст едно под друго

Преди да разглежда проблемите потребителя .

Може да se разглеждат всички проблеми или само тези на потребителя. Ако потребителя не се е оторизирал/логнал вместо бутон за показване на неговите report-и се появя бутон за логин.

Поради това че много потребители имат ограничен откъм MBs интернет няма да има автоматично refresh-ване на точки през дадени интервали, а ще има копченце за refresh.

Единственото, което си позволяваме да правим, което изхабява доста MBs е пращане на снимка понеже друг вариант няма

Трябва да имаме local strage или url caching за report-ите. Поне за report-ите от даден потребител.


## Бележки


### iPhone бележки:
 - ресурси за добри UI controls:  https://www.cocoacontrols.com/
 - може да има проблеми при избиране на локация, трябва да се проверява timestamp
 - Google Analytics се интегрира лесно с iPhone app-ове.

###  Следващи версии
User proifile екран където се показва репутация и report-и.