const db = require('../config/db');

const Mascota = {
  obtenerTodos: (callback) => {
    db.query('SELECT * FROM mascota', callback);
  },
  
  obtenerPorId: (id_mascota, callback) => {
    db.query('SELECT * FROM mascota WHERE id_mascota = ?', [id_mascota], callback);
  },
};

module.exports = Mascota;
