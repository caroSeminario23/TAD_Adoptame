const db = require('../config/db');

const CaracteristicaComplementaria = {
  obtenerTodos: (callback) => {
    db.query('SELECT * FROM caracteristica_complementaria', callback);
  },
  
  obtenerPorId: (id, callback) => {
    db.query('SELECT * FROM caracteristica_complementaria WHERE id_caracteristica = ?', [id], callback);
  },
};

module.exports = CaracteristicaComplementaria;
