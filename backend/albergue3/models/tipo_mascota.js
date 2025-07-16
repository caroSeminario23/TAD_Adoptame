const db = require('../config/db');

const TipoMascota = {
  obtenerTodos: (callback) => {
    db.query('SELECT * FROM tipo_mascota', callback);
  },
  
  obtenerPorId: (id, callback) => {
    db.query('SELECT * FROM tipo_mascota WHERE id_tipo_mascota = ?', [id], callback);
  },
};

module.exports = TipoMascota;
