const express = require('express');
const router = express.Router();
const mascotaController = require('../controllers/mascota.js');

router.get('/get_mascotas', mascotaController.get_mascotas);
router.post('/get_mascota', mascotaController.get_mascota);

module.exports = router;
