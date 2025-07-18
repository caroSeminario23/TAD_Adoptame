const express = require('express');
const router = express.Router();
const tipoMascotaController = require('../controllers/tipo_mascota.js');

router.get('/get_tipos_mascotas', tipoMascotaController.get_tipos_mascotas);
router.post('/get_tipo_mascota', tipoMascotaController.get_tipo_mascota);

module.exports = router;
