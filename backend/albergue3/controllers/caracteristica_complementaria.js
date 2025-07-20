const CaracteristicaComplementaria = require('../models/caracteristica_complementaria.js');

const get_car_complementarias = (req, res) => {
    CaracteristicaComplementaria.obtenerTodos((err, resultados) => {
        if (err) {
            return res.status(500).json({ mensaje: 'Error en el servidor', error: err });
        }
        if (resultados.length === 0) {
            return res.status(404).json({ mensaje: 'No se encontraron caracteristicas complementarias' });
        }
        res.status(200).json({
            message: 'Características complementarias encontradas.',
            status: 200,
            data: resultados
        });
    });
};

const get_car_complementaria = (req, res) => {
    const { id_caracteristica } = req.body;
    if (!id_caracteristica) {
        return res.status(400).json({ mensaje: 'ID de caracteristica complementaria es requerido' });
    }
    
    CaracteristicaComplementaria.obtenerPorId(id_caracteristica, (err, resultado) => {
        if (err) {
            return res.status(500).json({ mensaje: 'Error en el servidor', error: err });
        }
        if (!resultado || resultado.length === 0) {
            return res.status(404).json({ mensaje: 'Caracteristica complementaria no encontrada' });
        }
        res.status(200).json({
            message: 'Característica complementaria encontrada.',
            status: 200,
            data: resultado[0]
        });
    });
}

module.exports = {
    get_car_complementarias,
    get_car_complementaria
};
