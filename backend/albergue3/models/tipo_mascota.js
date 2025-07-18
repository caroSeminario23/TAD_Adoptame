const db = require('../config/db');

const TipoMascota = {
  obtenerTodos: (callback) => {
    db.query('SELECT * FROM tipo_mascota', callback);
  },
  
  obtenerPorId: (id_tmascota, callback) => {
    db.query('SELECT * FROM tipo_mascota WHERE id_tipo_mascota = ?', [id_tmascota], callback);
  },
};

module.exports = TipoMascota;
