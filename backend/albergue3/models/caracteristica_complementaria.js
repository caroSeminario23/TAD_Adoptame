const db = require('../config/db');

const CaracteristicaComplementaria = {
  obtenerTodos: (callback) => {
    db.query('SELECT * FROM caracteristica_complementaria', callback);
  },
  
  obtenerPorId: (id_caracteristica, callback) => {
    db.query('SELECT * FROM caracteristica_complementaria WHERE id_caracteristica = ?', [id_caracteristica], callback);
  },
};

module.exports = CaracteristicaComplementaria;
