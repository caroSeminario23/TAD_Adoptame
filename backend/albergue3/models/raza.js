const db = require('../config/db');

const Raza = {
  obtenerTodos: (callback) => {
    db.query('SELECT * FROM raza', callback);
  },
  
  obtenerPorId: (id_raza, callback) => {
    db.query('SELECT * FROM raza WHERE id_raza = ?', [id_raza], callback);
  },
};

module.exports = Raza;
