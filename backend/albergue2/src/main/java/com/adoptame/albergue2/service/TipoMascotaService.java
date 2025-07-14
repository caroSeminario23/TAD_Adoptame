package com.adoptame.albergue2.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.Optional;

import com.adoptame.albergue2.model.TipoMascota;
import com.adoptame.albergue2.repository.TipoMascotaRepository;

@Service
public class TipoMascotaService {
    @Autowired
    private TipoMascotaRepository tipoMascotaRepository;
    
    public List<TipoMascota> obtenerTodosLosTiposMascota() {
        return tipoMascotaRepository.findAll();
    }

    public Optional<TipoMascota> obtenerTipoMascotaPorId(Integer id) {
        return tipoMascotaRepository.findById(id);
    }
}
