import express from "express";
const router = express.Router();
import { engine } from 'express-handlebars';
import rootRouter from './routers/root.js';


const app = express();
const PORT = process.env.PORT || 3000;

// Set Handlebars as the template engine with .html extension

app.engine('html', engine({ extname: '.html' }));
app.set('view engine', 'html');

// Serve static files (CSS, JS, images)
app.use(express.static('assets'));

// routes
app.use('/', rootRouter);
//app.use('blog/', require('./routers/blog'));

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
