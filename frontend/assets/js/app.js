import { Header } from "./components/Header.js"
import { footer } from "./components/Footer.js"

let header  =  document.querySelector('#header')
let footerEl = document.querySelector('footer')

header.insertAdjacentHTML("afterbegin", Header())
footerEl.insertAdjacentHTML("afterbegin", footer())

