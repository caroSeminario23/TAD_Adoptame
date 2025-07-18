const CaracteristicaMascota = require('../models/caracteristica_mascota.model');

const get_car_mascotas = (req, res) => {
    CaracteristicaMascota.obtenerTodos((err, resultados) => {
        if (err) {
            return res.status(500).json({ mensaje: 'Error en el servidor', error: err });
        }
        if (resultados.length === 0) {
            return res.status(404).json({ mensaje: 'No se encontraron características de mascotas' });
        }
        res.status(200).json(resultados);
    });
};

const get_car_mascota = (req, res) => {
    const { id_caracteristica } = req.body;
    const { id_mascota } = req.body;

    if (!id_caracteristica || !id_mascota) {
        return res.status(400).json({ mensaje: 'ID de característica y ID de mascota son requeridos' });
    }
    
    CaracteristicaMascota.obtenerPorId(id_caracteristica, id_mascota, (err, resultado) => {
        if (err) {
            return res.status(500).json({ mensaje: 'Error en el servidor', error: err });
        }
        if (!resultado || resultado.length === 0) {
            return res.status(404).json({ mensaje: 'Característica de mascota no encontrada' });
        }
        res.status(200).json(resultado[0]);
    });
}

module.exports = {
    get_car_mascotas,
    get_car_mascota
};
