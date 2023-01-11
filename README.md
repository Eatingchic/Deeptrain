# Zh Website

<div align="center">

![GitHub forks](https://img.shields.io/github/forks/zmh-program/Zh-Website)
![GitHub Repo stars](https://img.shields.io/github/stars/zmh-program/Zh-Website)
![GitHub repo size](https://img.shields.io/github/repo-size/zmh-program/Zh-Website)
![GitHub repo file count](https://img.shields.io/github/directory-file-count/zmh-program/Zh-Website)
![GitHub](https://img.shields.io/github/license/zmh-program/Zh-Website)
[![star](https://gitee.com/zmh-program/Zh-Website/badge/star.svg?theme=dark)](https://gitee.com/zmh-program/Zh-Website/stargazers)
[![fork](https://gitee.com/zmh-program/Zh-Website/badge/fork.svg?theme=dark)](https://gitee.com/zmh-program/Zh-Website/members)

</div>

<div align="center">

![Lines of code](https://img.shields.io/tokei/lines/github/zmh-program/Zh-Website)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/zmh-program/Zh-Website)
&nbsp;
![GitHub language count](https://img.shields.io/github/languages/count/zmh-program/Zh-Website)
![GitHub top language](https://img.shields.io/github/languages/top/zmh-program/Zh-Website)

</div>

> 🔥 Zh-Website, An Open Source Deep Reinforcement Learning training platform

<div align="center">

![system: linux/unix](https://img.shields.io/badge/system-Linux%2FUnix-important)
&nbsp;
![python: 3.9+](https://img.shields.io/badge/python-3.9%2B-success)
&nbsp;
![django: 4.1](https://img.shields.io/badge/Django-4.1-informational)

</div>

---

> **🌎 Website Online 🌏**
> <br>&nbsp;&nbsp;![Website](https://img.shields.io/website?url=https%3A%2F%2Fzmh-program.site)
>
> 1. **[zmh-program.site](https://zmh-program.site) - tencent cloud**
> 2. *[zh-website.zmh-program.repl.co](https://zh-website.zmh-program.repl.co) - replit (container)*
> 3. *[zh-website.vercel.app](https://zh-website.vercel.app) - vercel (redirect)*

## 🚀️ ScreenShot 🎋

![screenshot](/docs/screenshot/screenshot.png)

## 🌊 Website Features 🔮

1. [X]  🍹  **User**
2. [X]  🥁  **Files**
3. [X]  🧃  **Websocket protocol & Instant Message**
4. [X]  🍵  **Website Management (GeoIP, Monitor)**
5. [X]  ☕  **Database & Cache**
6. [X]  🍷  **Embedding Applications**
7. [X]  👋  **OAuth** *(Open Authorization)*
8. [X]  📚  **Blog & Text Audit**
9. [X]  🔍  **IP Verify**
10. [ ] 🌀  **Front-end and Back-end Separation**
11. [ ] 🌏  **i18n** *(Internationalization)*
12. [ ] 📫  **Email Validation**

## ✨ Open Authorization Support 🎈

<div align="center">

[<img height="56px" src="https://cdn-icons-png.flaticon.com/128/919/919847.png" alt="github">](https://github.com/)&nbsp;
[<img height="56px" src="https://gitee.com/favicon.ico" alt="gitee">](https://gitee.com/)&nbsp;

</div>
<br>

## 🏠 Embedding Applications Structure 🎫

![application](/docs/screenshot/application.jpg)

### [👉 Production & Deployment 👈](/docs/RUN.md)

## 📜 Change Log 📰

### version `1.x.x`

- 🥎 `Release 1.0`

1. Basic User Features (login, logout, register, cookies validate)

- 🌿 `Pre 1.1`
  1. Prepare to migrate `channels` to `dwebsocket` (websocket protocol)
<br><br>
- 🎍 `Pre 1.2`
  1. Update Static Files

### version `2.x.x`

- 🍒 `Release 2.0.0`
  1. 🎉 Emoji Support 🎉
  2. 📕 iframe Support ( home page)📘
  3. ✈ beautify login / register page ✈
  4. 🔥 Websocket: Channels -> dwebsocket 🔥
  5. 🚀 Application Config 🚀
<br><br>
- 🍎 `Release 2.1.0 to 2.1.3`
  1. **putting on `ICP record`, deploy website**
  2. Use Django-form
  3. Add `django-simple-captcha` validation
  4. Add Embedding Application Repository Information(`shields.io`)
  5. Add `Gunicorn` Support
  6. Add `Websocket Security`(wss) Support
<br><br>
- 🍋 `Release 2.2.0 to 2.2.4.1`
  - File Features
    1. validation, limits (including `permission`, `file size`, `file name length`)
    2. download
    3. upload (client `ajax` upload, server `uuid` file handle)
    4. cache
    5. pagination
<br><br>
- 🎁 `Pre 2.3.0 to 2.3.1`
  - GeoIP Monitor (User country, request region analysis) v2.3.0-2.3.1
<br><br>
- 🎯 `Pre 2.3.2-alpha to 2.3.2-beta.2`
  - Instant Message (Websocket Protocol)
<br><br>
- 🌍 `Pre 2.4.0 to 2.4.1`
  - `django-simple-captcha` -> `hCaptcha` verify
<br><br>
- ✈ `Pre 2.5.0 to 2.5.0.2`
  - Improve the performance of code & database
  - User Django-auth
<br><br>
- 🌲 `Pre 2.6.0 to 2.6.0.3`
  - Replit and Vercel deployment
<br><br>
- 🔥 `Pre 2.7.0 to 2.7.2.3`
  - Admin Analysis Pages
    - Users & Requests Region Distribution
    - Server & Website Monitor
<br><br>
- 🎇 `Release 2.7.3 to 2.7.12`
  - Change Password Page
  - **Intelligent verification**
    - change password page
    - login page
    - register page
  - User Avatars
  - update Profile Page (`gitee`, `github`, `codepen` info)
<br><br>
- 🍀 `Pre 2.8.0 to 2.8.4.2`
  - dockerfile
  - update `Embedding Applications` structure
  - `SiteApplication` construction
<br><br>
- 📕 `Pre 2.9.0 to 2.9.1`
  - Reduce Photo size (per < 0.6MiB)
<br><br>
- 🚀 `Release 2.10.0 to 2.10.3`
  - `hCaptcha` -> `Cloudflare Turnstile` verify
  - Network attack and defense TEST (php) **Thanks to @APGPerson**
    - fixed file download bug
<br><br>
- 📕 `Pre 2.11.0 to 2.11.6`
  - Update README style
<br><br>
- 🙌 `Pre 2.12.0 to 2.12.6.2`
  - update models
  - update im
  - Use Verify using `Turnstile` and `hCaptcha` dual components
    - `Turnstile`: file-upload, login, change-password pages
    - `hCaptcha`: register page
  - Fixed the failure of multiple verification codes submitted by the deployment environment
    - call `(hcaptcha or turnstile).refresh()`
<br><br>
- 🧃 `Release 2.13.0 to 2.13.3`
  - **OAuth** *(Open Authorization)*
    - OAuth Login
    - OAuth Bind *(Support `Github`, `Gitee`)*
    - OAuth Config
<br><br>
- 📚 `Release 2.14.0-alpha to 2.14.7.1`
  - **Markdown Blog System** (`haystack` & `whoosh` & `jieba` & `mptt` & `layui`)
    - Articles
    - Comments (two-level)
    - Tags
    - Likes
    - Search & Highlight (haystack)
<br><br>
- ⛳ `Pre 2.15.0 to 2.15.5`
  - change code & frontend structure
  - django commands
  - operation throttle
<br><br>
- 🔍 `Pre 2.16.0 to 2.16.4.4`
  - Text Audit (paddlehub dataset & model)
  - Docker-compose
<br><br>
- 👆 `Release 2.17 to 2.17.0.1`
  - python 3.7 -> 3.9
  - django 3.2 -> 4.1
<br><br>

## Thanks

<div align="center">

[<img height="32px" src="https://www.tencentcloud.com/favicon.ico" alt="tencent cloud">](https://www.tencentcloud.com/)&nbsp;
[<img height="32px" src="https://www.kaggle.com/static/images/favicon.ico" alt="kaggle">](https://kaggle.com/)&nbsp;
[<img height="32px" src="https://docs.replit.com/image/logo.svg" alt="replit">](https://replit.com/)&nbsp;
[<img height="32px" src="https://cdn-icons-png.flaticon.com/128/5969/5969044.png" alt="cloudflare">](https://cloudflare.com/)&nbsp;
<br>
[<img height="32px" src="https://code.visualstudio.com/favicon.ico" alt="vscode">](https://code.visualstudio.com/)&nbsp;
[<img height="32px" src="https://cdn-icons-png.flaticon.com/128/1377/1377243.png" alt="codepen">](https://codepen.io/)&nbsp;
[<img height="32px" src="https://account.jetbrains.com/static/favicon.ico" alt="jetbrains">](https://www.jetbrains.com/)&nbsp;
<br>
[<img height="32px" src="https://media.flaticon.com/dist/min/img/logo/flaticon_negative.svg" alt="favicon">](https://www.flaticon.com/)&nbsp;
[<img height="32px" src="https://wallhaven.cc/images/layout/logo.png" alt="wallhaven">](https://wallhaven.cc/)&nbsp;
<br>

[`Jetbrains OSS` <br>`(Open Source Development Community Support)`](https://www.jetbrains.com/community/opensource/#support)

</div>
