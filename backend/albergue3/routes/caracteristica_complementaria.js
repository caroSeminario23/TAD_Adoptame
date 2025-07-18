const express = require('express');
const router = express.Router();
const carComplementariaController = require('../controllers/caracteristica_complementaria.js');

router.get('/', carComplementariaController.get_car_complementarias);
router.post('/', carComplementariaController.get_car_complementaria);

module.exports = router;
