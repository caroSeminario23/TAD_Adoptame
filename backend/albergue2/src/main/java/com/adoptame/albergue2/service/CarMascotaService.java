package com.adoptame.albergue2.service;

import java.util.List;
import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.adoptame.albergue2.model.CaracteristicaMascota;
import com.adoptame.albergue2.model.CaracteristicaMascotaId;
import com.adoptame.albergue2.repository.CarMascotaRepository;

@Service
public class CarMascotaService {
    @Autowired
    private CarMascotaRepository carMascotaRepository;

    public List<CaracteristicaMascota> obtenerTodasLasCaracteristicasMascota() {
        return carMascotaRepository.findAll();
    }

    public Optional<CaracteristicaMascota> obtenerCaracteristicaMascotaPorId(Integer idMascota, Integer idCaracteristica) {
        CaracteristicaMascotaId id = new CaracteristicaMascotaId(idMascota, idCaracteristica);
        return carMascotaRepository.findById(id);
    }
}
