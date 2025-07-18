const express = require('express');
const cors = require('cors');
const app = express();

// Middleware
app.use(cors());
app.use(express.json());

// Importar rutas
const tipoMascotaRoutes = require('./routes/tipo_mascota.js');
const razaRoutes = require('./routes/raza.js');
const mascotaRoutes = require('./routes/mascota.js');
const carMascotaRoutes = require('./routes/caracteristica_mascota.js');
const carComplementariaRoutes = require('./routes/caracteristica_complementaria.js');

// Usar rutas
app.use('/tipo_mascota_routes', tipoMascotaRoutes);
app.use('/raza_routes', razaRoutes);
app.use('/mascota_routes', mascotaRoutes);
app.use('/car_mascotas_routes', carMascotaRoutes);
app.use('/car_complementarias_routes', carComplementariaRoutes);

// Ruta por defecto para errores 404
app.use((req, res) => {
  res.status(404).json({ mensaje: 'Ruta no encontrada' });
});

// Puerto de escucha
const DB_PORT = process.env.PORT || 3000;
app.listen(DB_PORT, () => {
  console.log(`Servidor escuchando en el puerto ${PORT}`);
});
