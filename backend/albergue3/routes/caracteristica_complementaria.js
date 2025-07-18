const express = require('express');
const router = express.Router();
const carComplementariaController = require('../controllers/caracteristica_complementaria.js');

router.get('/get_car_complementarias', carComplementariaController.get_car_complementarias);
router.post('/get_car_complementaria', carComplementariaController.get_car_complementaria);

module.exports = router;
