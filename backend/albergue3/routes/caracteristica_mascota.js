const express = require('express');
const router = express.Router();
const carMascotaController = require('../controllers/caracteristica_mascota.js');

router.get('/', carMascotaController.get_car_mascotas);
router.post('/', carMascotaController.get_car_mascota);

module.exports = router;
