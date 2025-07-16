const db = require('../config/db');

const CaracteristicaMascota = {
  obtenerTodos: (callback) => {
    db.query('SELECT * FROM caracteristica_mascota', callback);
  },
  
  obtenerPorId: (idCaracteristica, idMascota, callback) => {
    db.query('SELECT * FROM caracteristica_mascota WHERE id_caracteristica = ? AND id_mascota = ?',
        [idCaracteristica, idMascota], callback);
  },
};

module.exports = CaracteristicaMascota;
