const TipoMascota = require('../models/tipo_mascota.js');

const get_tipos_mascotas = (req, res) => {
    TipoMascota.obtenerTodos((err, resultados) => {
        if (err) {
            return res.status(500).json({ mensaje: 'Error en el servidor', error: err });
        }
        if (resultados.length === 0) {
            return res.status(404).json({ mensaje: 'No se encontraron tipos de mascota' });
        }
        res.status(200).json(resultados);
    });
};

const get_tipo_mascota = (req, res) => {
    const { id_tmascota } = req.body;
    if (!id_tmascota) {
        return res.status(400).json({ mensaje: 'ID de tipo de mascota es requerido' });
    }
    
    TipoMascota.obtenerPorId(id_tmascota, (err, resultado) => {
        if (err) {
            return res.status(500).json({ mensaje: 'Error en el servidor', error: err });
        }
        if (!resultado || resultado.length === 0) {
            return res.status(404).json({ mensaje: 'Tipo de mascota no encontrado' });
        }
        res.status(200).json(resultado[0]);
    });
}

module.exports = {
    get_tipos_mascotas,
    get_tipo_mascota
};
