import { Header } from "./components/Header.js"
import { footer } from "./components/Footer.js"
import { post, news } from "./components/Post.js"

let header  =  document.querySelector('#header')
let footerEl = document.querySelector('footer')
let head = document.querySelector('head')
let newsEl = document.querySelector('#main-news')
let postEl = document.querySelector('#posts')


header.insertAdjacentHTML("afterbegin", Header())
footerEl.insertAdjacentHTML("afterbegin", footer())
newsEl.insertAdjacentHTML('afterbegin', news())
postEl.insertAdjacentHTML('afterbegin', post())


head.insertAdjacentHTML('afterbegin', `
    <meta charset="utf-8">
    <meta name="description" content="Transforming Ideas into Immersive Experiences through Innovative Programming">
    <meta name="keywords" content="pixtinifinty, pixet, pixt, infinity">
    <meta name="author" content="pixtinifinty">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="icon" href="assets/images/favicon.ico">
    <title>PIXTINFINITY</title>
    <link href="https://fonts.googleapis.com/css?family=Montserrat:400,600&display=swap" rel="stylesheet"> 

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/fontawesome.min.css" integrity="sha512-siarrzI1u3pCqFG2LEzi87McrBmq6Tp7juVsdmGY1Dr8Saw+ZBAzDzrGwX3vgxX1NkioYNCFOVC0GpDPss10zQ==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.10.0/css/all.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/brands.min.css" integrity="sha512-W/zrbCncQnky/EzL+/AYwTtosvrM+YG/V6piQLSe2HuKS6cmbw89kjYkp3tWFn1dkWV7L1ruvJyKbLz73Vlgfg==" crossorigin="anonymous" referrerpolicy="no-referrer" />

    <link href="assets/css/theme.css" rel="stylesheet">

    <link href="assets/css/style.css" rel="stylesheet">
    <link href="assets/css/main.css" rel="stylesheet">
`)