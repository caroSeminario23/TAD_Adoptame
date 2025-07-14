package com.adoptame.albergue2.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

import com.adoptame.albergue2.dto.CarateristicaComplementariaDTO;
import com.adoptame.albergue2.model.CaracteristicaComplementaria;
import com.adoptame.albergue2.repository.CarComplementariaRepository;

@Service
public class CarComplementariaService {
    @Autowired
    private CarComplementariaRepository carComplementariaRepository;

    // Método para convertir una entidad a DTO
    private CarateristicaComplementariaDTO convertirADTO(CaracteristicaComplementaria entidad) {
        return new CarateristicaComplementariaDTO(
            entidad.getIdCaracteristica(),
            entidad.getNombre(),
            entidad.getUnidadMedida()
        );
    }

    // Devolver todas las características como DTO
    public List<CarateristicaComplementariaDTO> obtenerTodasLasCaracteristicasComplementarias() {
        return carComplementariaRepository.findAll()
                .stream()
                .map(this::convertirADTO)
                .collect(Collectors.toList());
    }

    // Devolver todas las características como entidades
    public Optional<CarateristicaComplementariaDTO> obtenerCaracteristicaComplementariaPorId(Integer id) {
        return carComplementariaRepository.findById(id).map(this::convertirADTO);
    }
}
