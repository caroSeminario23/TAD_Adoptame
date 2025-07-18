const Mascota = require('../models/mascota.js');

const get_mascotas = (req, res) => {
    Mascota.obtenerTodos((err, resultados) => {
        if (err) {
            return res.status(500).json({ mensaje: 'Error en el servidor', error: err });
        }
        if (resultados.length === 0) {
            return res.status(404).json({ mensaje: 'No se encontraron mascotas' });
        }
        res.status(200).json(resultados);
    });
};

const get_mascota = (req, res) => {
    const { id_mascota } = req.body;
    if (!id_mascota) {
        return res.status(400).json({ mensaje: 'ID de mascota es requerido' });
    }
    
    Mascota.obtenerPorId(id_mascota, (err, resultado) => {
        if (err) {
            return res.status(500).json({ mensaje: 'Error en el servidor', error: err });
        }
        if (!resultado || resultado.length === 0) {
            return res.status(404).json({ mensaje: 'Mascota no encontrada' });
        }
        res.status(200).json(resultado[0]);
    });
}

module.exports = {
    get_mascotas,
    get_mascota
};
