const express = require('express');
const router = express.Router();
import fetch from 'node-fetch';


// Blog API URL
const BLOG_API_URL = process.env.BLOG_API_URL;


// Blog Details Route
router.get('/blog/:id', async (req, res) => {
  const blogId = req.params.id;
  try {
    const response = await fetch(`${BLOG_API_URL}/${blogId}`);
    const blog = await response.json();
    res.render('blog', { blog });
  } catch (error) {
    console.error('Error fetching blog details:', error);
    res.status(500).send('Error fetching blog details');
  }
});


module.exports = router