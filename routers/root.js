import { Router } from "express";
const router = Router()

// Home Route
router.get('/', async (req, res) => {
    try {
      //const response = await fetch(BLOG_API_URL);
      //const blogs = await response.json();
      res.render('index');
    } catch (error) {
      console.error('Error fetching blog data:', error);
      res.status(500).send('Error fetching blog data');
    }
  });


export default router;