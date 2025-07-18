const express = require('express');
const router = express.Router();
const razaController = require('../controllers/raza.js');

router.get('/', razaController.get_razas);
router.post('/', razaController.get_raza);

module.exports = router;
