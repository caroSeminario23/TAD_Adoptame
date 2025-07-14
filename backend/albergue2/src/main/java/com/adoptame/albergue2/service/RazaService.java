package com.adoptame.albergue2.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

import com.adoptame.albergue2.dto.RazaDTO;
import com.adoptame.albergue2.model.Raza;
import com.adoptame.albergue2.repository.RazaRepository;

@Service
public class RazaService {
    @Autowired
    private RazaRepository razaRepository;

    // Método para convertir una entidad a DTO
    private RazaDTO convertirADTO(Raza entidad) {
        return new RazaDTO(
            entidad.getIdRaza(),
            entidad.getNombre()
        );
    }

    // Devolver todas las razas como DTO
    public List<RazaDTO> obtenerTodasLasRazas() {
        return razaRepository.findAll()
                .stream()
                .map(this::convertirADTO)
                .collect(Collectors.toList());
    }

    // Buscar por ID y devolver DTO si existe
    public Optional<RazaDTO> obtenerRazaPorId(Integer id) {
        return razaRepository.findById(id).map(this::convertirADTO);
    }
}
