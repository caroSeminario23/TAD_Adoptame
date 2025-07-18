const Raza = require('../models/raza.js');

const get_razas = (req, res) => {
    Raza.obtenerTodos((err, resultados) => {
        if (err) {
            return res.status(500).json({ mensaje: 'Error en el servidor', error: err });
        }
        if (resultados.length === 0) {
            return res.status(404).json({ mensaje: 'No se encontraron razas' });
        }
        res.status(200).json(resultados);
    });
};

const get_raza = (req, res) => {
    const { id_raza } = req.body;
    if (!id_raza) {
        return res.status(400).json({ mensaje: 'ID de raza es requerido' });
    }
    
    Raza.obtenerPorId(id_raza, (err, resultado) => {
        if (err) {
            return res.status(500).json({ mensaje: 'Error en el servidor', error: err });
        }
        if (!resultado || resultado.length === 0) {
            return res.status(404).json({ mensaje: 'Raza no encontrada' });
        }
        res.status(200).json(resultado[0]);
    });
}

module.exports = {
    get_razas,
    get_raza
};
