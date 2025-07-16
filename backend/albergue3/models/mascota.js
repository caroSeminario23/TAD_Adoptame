const db = require('../config/db');

const Mascota = {
  obtenerTodos: (callback) => {
    db.query('SELECT * FROM mascota', callback);
  },
  
  obtenerPorId: (id, callback) => {
    db.query('SELECT * FROM mascota WHERE id_mascota = ?', [id], callback);
  },
};

module.exports = Mascota;
