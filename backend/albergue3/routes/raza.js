const express = require('express');
const router = express.Router();
const razaController = require('../controllers/raza.js');

router.get('/get_razas', razaController.get_razas);
router.post('/get_raza', razaController.get_raza);

module.exports = router;
