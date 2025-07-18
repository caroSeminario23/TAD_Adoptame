const express = require('express');
const router = express.Router();
const mascotaController = require('../controllers/mascota.js');

router.get('/', mascotaController.get_mascotas);
router.post('/', mascotaController.get_mascota);

module.exports = router;
