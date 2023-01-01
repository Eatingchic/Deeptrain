# Zh Website

![GitHub forks](https://img.shields.io/github/forks/zmh-program/Zh-Website)
![GitHub Repo stars](https://img.shields.io/github/stars/zmh-program/Zh-Website)
![GitHub repo size](https://img.shields.io/github/repo-size/zmh-program/Zh-Website)
![GitHub repo file count](https://img.shields.io/github/directory-file-count/zmh-program/Zh-Website)
![GitHub](https://img.shields.io/github/license/zmh-program/Zh-Website)
[![star](https://gitee.com/zmh-program/Zh-Website/badge/star.svg?theme=dark)](https://gitee.com/zmh-program/Zh-Website/stargazers)
[![fork](https://gitee.com/zmh-program/Zh-Website/badge/fork.svg?theme=dark)](https://gitee.com/zmh-program/Zh-Website/members)

![Lines of code](https://img.shields.io/tokei/lines/github/zmh-program/Zh-Website)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/zmh-program/Zh-Website)
&nbsp;
![GitHub language count](https://img.shields.io/github/languages/count/zmh-program/Zh-Website)
![GitHub top language](https://img.shields.io/github/languages/top/zmh-program/Zh-Website)

> 🔥 Zh-Website, An Open Source Deep Reinforcement Learning training platform

<div align="center">

![system: linux/unix](https://img.shields.io/badge/system-Linux%2FUnix-important)
&nbsp;
![python: 3.7+](https://img.shields.io/badge/python-3.7%2B-success)
&nbsp;
![django: 3.2](https://img.shields.io/badge/Django-3.2-informational)
</div>
<hr>

## 🌊 Website Features

1. [x]  🍹  **User**
2. [x]  🥁  **Files**
3. [x]  🧃  **Websocket protocol & Instant Message**
4. [x]  🍵  **Website Management**
5. [x]  ☕  **Database & Cache**
6. [x]  🍷  **Embedding Applications**
7. [x]  👋  **OAuth** *(Open Authorization)*
     - `Github`
     - `Gitee`
8. [ ]  📚  **Blog**
9. [ ]  🌏  **i18n** *(Internationalization)*

<br>

> **🌎 Website Online 🌏**
> <br>&nbsp;&nbsp;![Website](https://img.shields.io/website?url=https%3A%2F%2Fzmh-program.site)
>
> 1. **[zmh-program.site](https://zmh-program.site) - tencent cloud**
> 2. *[zh-website.zmh-program.repl.co](https://zh-website.zmh-program.repl.co) - replit (container)*
> 3. *[zh-website.vercel.app](https://zh-website.vercel.app) - vercel (redirect)*

## 🚀️ ScreenShot

![screenshot](/screenshot/screenshot.png)

## 🏠 Embedding Applications Structure

![application](/screenshot/application.jpg)

## 🍉 QuickStart Production

1. initialize
   *(there is no need to make migrations)*

   ```commandline
   cd Zh-Website
   pip install -r requirements.txt
   python manage.py migrate
   ```
2. run

   ```commandline
     python manage.py
   ```

## 🌏 Deploy

1. initialize
   ```commandline
    cd Zh-Website
    pip install -r requirements.txt

    python manage.py migrate
    python manage.py collectstatic
   ```
2. run
   ```commandline
   gunicorn -c gunicorn.conf.py DjangoWebsite:wsgi:application
   ```
3. Nginx Example Configuration
   ```nginx configuration
   server
   {
       listen 80;
       server_name localhost;

       location ~ ^/(\.user.ini|\.htaccess|\.git|\.svn|\.project|LICENSE|README.md)
       {
           return 404;
       }

       location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
       }

         location /static {
           alias /static/;
       }
       location /media {
           alias /media/;
       }

       location ~ .*\.(gif|jpg|jpeg|png|bmp|swf)$
       {
           expires      10h;
           error_log /dev/null;
           access_log /dev/null;
       }

       location ~ .*\.(js|css)?$
       {
           expires      1h;
           error_log /dev/null;
           access_log /dev/null;
       }
   }
   ```

## Deploy Config
https://github.com/zmh-program/Zh-Website/blob/7a44e9597a40d7407e1fe8c9c995663c266eecc8/config.json#L1-L18

## 📕 Settings

*⚠ initialize then!*

https://github.com/zmh-program/Zh-Website/blob/aac95dbd5a1ae9a0b64a245063538e4567f07d72/DjangoWebsite/settings.py#L114

rewrite to
```python
IS_CONTAINER = False
```

- `MySQL` 
  
  https://github.com/zmh-program/Zh-Website/blob/aac95dbd5a1ae9a0b64a245063538e4567f07d72/DjangoWebsite/settings.py#L133-L143
  > ```sql
  > create DATABASE `django-database`;
  > ```
  >
- `Redis`
  
  https://github.com/zmh-program/Zh-Website/blob/aac95dbd5a1ae9a0b64a245063538e4567f07d72/DjangoWebsite/settings.py#L145-L154


## 📜 Change Log

### version `1.x.x`

- 🥎 `Release 1.0`

1. Basic User Features (login, logout, register, cookies validate)

- 🌿 `Pre 1.1`
  1. Prepare to migrate `channels` to `dwebsocket` (websocket protocol)
- 🎍 `Pre 1.2`
  1. Update Static Files

### version `2.x.x`

- 🍒 `Release 2.0.0`
  1. 🎉 Emoji Support 🎉
  2. 📕 iframe Support ( home page)📘
  3. ✈ beautify login / register page ✈
  4. 🔥 Websocket: Channels -> dwebsocket 🔥
  5. 🚀 Application Config 🚀
- 🍎 `Release 2.1.3`
  1. **putting on `ICP record`, deploy website**
  2. Use Django-form
  3. Add `django-simple-captcha` validation
  4. Add Embedding Application Repository Information(`shields.io`)
  5. Add `Gunicorn` Support
  6. Add `Websocket Security`(wss) Support
- 🍋 `Release(s) 2.2.4.1`
  - File Features
    1. validation, limits (including `permission`, `file size`, `file name length`)
    2. download
    3. upload (client `ajax` upload, server `uuid` file handle)
    4. cache
    5. pagination
- `Pre 2.3.0 to 2.3.1`
  - GeoIP Monitor (User country, request region analysis) v2.3.0-2.3.1
- `Pre 2.3.2-alpha to 2.3.2-beta.2`
  - Instant Message (Websocket Protocol)
- 🌍 `Pre 2.4.0 to 2.4.1`
  - `django-simple-captcha` -> `hCaptcha` verify
- ✈ `Pre 2.5.0 to 2.5.0.2`
  - Improve the performance of code & database
  - User Django-auth
- 🌲 `Pre 2.6.0 to 2.6.0.3`
  - Replit and Vercel deployment
- 🔥 `Pre 2.7.0 to 2.7.2.3`
  - Admin Analysis Pages
    - Users & Requests Region Distribution
    - Server & Website Monitor
- 🌱 `Pre 2.7.3 to 2.7.12`
  - Change Password Page
  - **Intelligent verification**
    - change password page
    - login page
    - register page
  - User Avatars
  - update Profile Page (`gitee`, `github`, `codepen` info)
- 🎇 `Release 2.7`
- 🍀 `Pre 2.8.0 to 2.8.4.2`
  - dockerfile
  - update `Embedding Applications` structure
  - `SiteApplication` construction
- 📕 `Pre 2.9.0 to 2.9.1`
  - Reduce Photo size (per < 0.6MiB)
- 🚀 `Release 2.10.0 to 2.10.3`
  - `hCaptcha` -> `Cloudflare Turnstile` verify
  - Network attack and defense TEST (php) **Thanks to @APGPerson**
    - fixed file download bug
- 📚 `Pre 2.11.0 to 2.11.6`
  - Update README style
- 🙌 `Pre 2.12.0 to 2.12.6.2`
  - update models
  - update im
  - Use Verify using `Turnstile` and `hCaptcha` dual components
    - `Turnstile`: file-upload, login, change-password pages
    - `hCaptcha`: register page
  - Fixed the failure of multiple verification codes submitted by the deployment environment
    - call `(hcaptcha or turnstile).refresh()`
- 🧃 `Release 2.13.0 to 2.13.3`
  - **OAuth** *(Open Authorization)*
    - OAuth Login
    - OAuth Bind *(Support `Github`, `Gitee`)*
    - OAuth Config

## Thanks

<div align="center">

[<img height="32px" src="https://www.tencentcloud.com/favicon.ico" alt="tencent cloud">](https://www.tencentcloud.com/)&nbsp;
[<img height="32px" src="https://www.kaggle.com/static/images/favicon.ico" alt="kaggle">](https://kaggle.com/)&nbsp;
[<img height="32px" src="https://docs.replit.com/image/logo.svg" alt="replit">](https://replit.com/)&nbsp;
<br>
[<img height="32px" src="https://cdn-icons-png.flaticon.com/128/5968/5968866.png" alt="github">](https://github.com/)&nbsp;
[<img height="32px" src="https://gitee.com/favicon.ico" alt="gitee">](https://gitee.com/)&nbsp;
[<img height="32px" src="https://cdn-icons-png.flaticon.com/128/1377/1377243.png" alt="codepen">](https://codepen.io/)&nbsp;
[<img height="32px" src="https://cdn-icons-png.flaticon.com/128/5969/5969044.png" alt="cloudflare">](https://cloudflare.com/)&nbsp;
<br>
[<img height="32px" src="https://code.visualstudio.com/favicon.ico" alt="vscode">](https://code.visualstudio.com/)&nbsp;
[<img height="32px" src="https://account.jetbrains.com/static/favicon.ico" alt="jetbrains">](https://www.jetbrains.com/)&nbsp;
<br>
[<img height="32px" src="https://media.flaticon.com/dist/min/img/logo/flaticon_negative.svg" alt="favicon">](https://www.flaticon.com/)&nbsp;
[<img height="32px" src="https://wallhaven.cc/images/layout/logo.png" alt="wallhaven">](https://wallhaven.cc/)&nbsp;
<br>

[`Jetbrains OSS` <br>`(Open Source Development Community Support)`](https://www.jetbrains.com/community/opensource/#support)

</div>
