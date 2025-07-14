package com.adoptame.albergue2.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

import com.adoptame.albergue2.dto.TipoMascotaDTO;
import com.adoptame.albergue2.model.TipoMascota;
import com.adoptame.albergue2.repository.TipoMascotaRepository;

@Service
public class TipoMascotaService {
    @Autowired
    private TipoMascotaRepository tipoMascotaRepository;

    // Método para convertir una entidad a DTO
    private TipoMascotaDTO convertirADTO(TipoMascota entidad) {
        return new TipoMascotaDTO(
            entidad.getIdTipoMascota(),
            entidad.getNombre()
        );
    }

    // Devolver todas las características como DTO
    public List<TipoMascotaDTO> obtenerTodosLosTiposMascota() {
        return tipoMascotaRepository.findAll()
                .stream()
                .map(this::convertirADTO)
                .collect(Collectors.toList());
    }

    // Buscar por ID y devolver DTO si existe
    public Optional<TipoMascotaDTO> obtenerTipoMascotaPorId(Integer id) {
        return tipoMascotaRepository.findById(id).map(this::convertirADTO);
    }
}
