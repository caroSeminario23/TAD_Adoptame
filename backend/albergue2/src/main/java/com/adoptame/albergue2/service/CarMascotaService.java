package com.adoptame.albergue2.service;

import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.adoptame.albergue2.dto.CaracteristicaMascotaDTO;
import com.adoptame.albergue2.model.CaracteristicaMascota;
import com.adoptame.albergue2.model.CaracteristicaMascotaId;
import com.adoptame.albergue2.repository.CarMascotaRepository;

@Service
public class CarMascotaService {
    @Autowired
    private CarMascotaRepository carMascotaRepository;

    // Método para convertir una entidad a DTO
    private CaracteristicaMascotaDTO convertirADTO(CaracteristicaMascota entidad) {
        return new CaracteristicaMascotaDTO(
            entidad.getMascota().getIdMascota(),
            entidad.getCaracteristica().getIdCaracteristica(),
            entidad.getValor()
        );
    }

    // Devolver todas las características como DTO
    public List<CaracteristicaMascotaDTO> obtenerTodasLasCaracteristicasMascota() {
        return carMascotaRepository.findAll()
                .stream()
                .map(this::convertirADTO)
                .collect(Collectors.toList());
    }

    // Buscar por ID y devolver DTO si existe
    public Optional<CaracteristicaMascotaDTO> obtenerCaracteristicaMascotaPorId(Integer idMascota, Integer idCaracteristica) {
        CaracteristicaMascotaId id = new CaracteristicaMascotaId(idMascota, idCaracteristica);
        return carMascotaRepository.findById(id).map(this::convertirADTO);
    }
}
