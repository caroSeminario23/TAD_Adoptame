const db = require('../config/db');

const Raza = {
  obtenerTodos: (callback) => {
    db.query('SELECT * FROM raza', callback);
  },
  
  obtenerPorId: (id, callback) => {
    db.query('SELECT * FROM raza WHERE id_raza = ?', [id], callback);
  },
};

module.exports = Raza;
