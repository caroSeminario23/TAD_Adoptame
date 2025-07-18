const express = require('express');
const router = express.Router();
const carMascotaController = require('../controllers/caracteristica_mascota.js');

router.get('/get_car_mascotas', carMascotaController.get_car_mascotas);
router.post('/get_car_mascota', carMascotaController.get_car_mascota);

module.exports = router;
