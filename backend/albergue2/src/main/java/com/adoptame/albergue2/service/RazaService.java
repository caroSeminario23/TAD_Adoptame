package com.adoptame.albergue2.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.Optional;

import com.adoptame.albergue2.model.Raza;
import com.adoptame.albergue2.repository.RazaRepository;

@Service
public class RazaService {

    @Autowired
    private RazaRepository razaRepository;

    public List<Raza> obtenerTodasLasRazas() {
        return razaRepository.findAll();
    }

    public Optional<Raza> obtenerRazaPorId(Integer id) {
        return razaRepository.findById(id);
    }
}
