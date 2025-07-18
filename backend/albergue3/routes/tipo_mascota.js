const express = require('express');
const router = express.Router();
const tipoMascotaController = require('../controllers/tipo_mascota.js');

router.get('/', tipoMascotaController.get_tipos_mascotas);
router.post('/', tipoMascotaController.get_tipo_mascota);

module.exports = router;
