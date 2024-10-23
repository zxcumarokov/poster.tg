## Сперва получим Calendar ID для этого:
1. зайдем на сайт Notion и откроем наш календарь
2. скопируем url
3. выделим из него Calendar_id "https://www.notion.so/"  CALENDAR_ID  "?"
пример: 
  <img width="500" alt="image" src="https://github.com/user-attachments/assets/edc22bd2-f27d-4150-ac76-0afeeec58698">


---



## Далее получим Notion token

для этого переходим по ссылке - https://www.notion.so/profile/integrations


далее откроиться страница и там будет кнопка "New integration"
<img width="500" alt="image" src="https://github.com/user-attachments/assets/44b498b2-cad6-4f65-97b7-6450fc618211">


После нажатия на кнопку нам будет предложено заполнить поля
выбираем из поля **Type** и делаем его **Public**


<img width="500" alt="image" src="https://github.com/user-attachments/assets/3c768208-6bc0-4661-bc38-c7191a04bdc6">


<details>
  <summary>Вот гайд как заполнить все поля </summary>
  


Для того чтобы заполнить поля для создания интеграции в Notion, вот несколько рекомендаций по каждому пункту:

Associated workspace
Выберите рабочее пространство (workspace), с которым будет связана интеграция. Это обычно то пространство, в котором вы будете использовать API. Если у вас только одно рабочее пространство, просто выберите его.

Type
На этом этапе вам нужно выбрать тип интеграции:

**Internal** — внутренняя интеграция для личного использования или использования внутри вашей компании. Это, вероятно, тот выбор, который вам нужен, если вы не планируете публично распространять интеграцию.
**Public** — публичная интеграция, если вы хотите, чтобы она была доступна другим пользователям Notion через OAuth. Выберите Internal на этом этапе, если интеграция только для вас или вашей команды.
**Company name**
Укажите название вашей компании. Если у вас нет компании, вы можете указать своё имя или псевдоним, например:
"zxcumarokov's Bots"

**Website**
Это URL сайта вашей компании или проекта. Если у вас нет веб-сайта, вы можете указать любую публичную страницу проекта, например, ваш репозиторий на GitHub: https://github.com/zxcumarokov/poster.tg

**Tagline**
Краткая фраза, описывающая интеграцию. Например:
"Telegram bot for Notion calendar integration"

**Privacy Policy URL**
Ссылка на политику конфиденциальности вашей интеграции. Если у вас нет такой страницы, вы можете создать её позже или указать любой доступный URL, например шаблон политики конфиденциальности для проектов:
https://www.privacypolicies.com/generator/

**Terms of Use URL**
Ссылка на страницу с условиями использования интеграции. Если у вас её нет, воспользуйтесь генератором условий использования:
https://www.termsfeed.com/

**Email**
Укажите ваш email как разработчика:
ваш.email@пример.com

**Logo**
Вам нужно загрузить логотип. Если у вас пока нет логотипа, можно использовать временный или сделать простой через генератор логотипов:
https://hatchful.shopify.com/

**OAuth domains & URIs (Redirect URIs)**
Укажите URL, куда пользователи будут перенаправлены после аутентификации с помощью OAuth. Это должна быть безопасная (https) ссылка, например на ваш сайт или сервер, обрабатывающий OAuth-токены. Пример: https://example.com/oauth/callback

**Notion URL for optional template**
Это поле можно оставить пустым, если у вас нет шаблона страницы в Notion, которую вы хотите предложить пользователям.

Заполнив все эти поля, вы сможете получить токен для интеграции с Notion API.

</details>

После всех манипуляций мы попадаем на главную страницу нашей интеграции тут нас интересует Authorization URL копируем его и вставляем в поиск 

после перехода на сайт нажимаем на синюю кнопку **Select Pages** и выбираем наш календарь


Далее нас перекидывает на сайт и мы копируем url этого сайта 

затем выбираем из него вот эту часть и сохраняем 


<img width="500" alt="image" src="https://github.com/user-attachments/assets/082ddd7d-cae2-4fde-875d-3b443bae4933">


## Api запрос
Далее необходимо составить API запрос для делать мы это будем с помощью расширения для VS code "Thunder client"
пишем пост запрос на этот url https://api.notion.com/v1/oauth/token

вот все хедеры которые нужно использовать 
HTTP Headers
Content-Type - application/json
Notion-Version - 2022-06-28
Authorization - Basic Y2NjMzBlYjYtN2QyYy00NjM2LTk2ZmYtODM1NWU3NDEyNDc4OnNlY3JldF9kbVJta3BIb0dKZHlZR0Zra0FORGVaanFheHM0ZTAzZG45R1hFNllOUHVH
Accept - */*
для получения Authorization ключа необходимо закодировать в Base64 2 ключа с главной страници интеграции 
<img width="1086" alt="image" src="https://github.com/user-attachments/assets/653b4084-4913-40e1-8998-fef624cdbdf1">
Просим Chat gpt закодировать эти ключи при помощи такого промта 
```
закодируй при помощи BASE64
ccc30eb6-7d2c-4636-96ff-8355e7412478
и 
secret_MInDaghUOOepUsfE74kVslb1Bn7fPbuKFFiqHonFlsW
я должен получить $BASE64_ENCODED_ID_AND_SECRET
```
на выходе получаем ключ для хеддера 
После того как мы собрали все headers составляем body 
оно выглядит так 

```
{
  "grant_type": "authorization_code",
  "code": "03ace596-ede5-452e-ac07-46923809c38a",
  "redirect_uri": "https://poster-tg.com/oauth/callback",
  "external_account": {
    "key": "A83823453409384",
    "name": "Notion - team@makenotion.com"
  }
}
```
в поле code вставляем код 
<img width="910" alt="image" src="https://github.com/user-attachments/assets/082ddd7d-cae2-4fde-875d-3b443bae4933">
После всех манипуляций мы получим access_token 
улыбаемся и машем ребята 
![image](https://github.com/user-attachments/assets/2cdd456b-43e5-400f-970f-dd30ee2dfaa9)
